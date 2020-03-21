#!/usr/bin/env python

import json
import argparse
import datetime

# Number of days from epoch to 1.1.2020
daycnt2020 = (datetime.datetime(2020,1,1) - datetime.datetime(1970,1,1)).days

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True,
                        help="input file")
    parser.add_argument("-c", "--country", type=str, required=True,
                        help="country")
    args = parser.parse_args()
    return args.input, args.country

def fill(dbda, key, count, day_from, day_to=None):
    if day_to is None:
        day_to = 365
    for idx in range(day_from, day_to):
        dbda[key][idx] += count

def compute_X(date):
    return (datetime.datetime.fromtimestamp(date) \
            - datetime.datetime(1970,1,1)).days - daycnt2020
        
def handle_one(dbda, X, dead):
    fill(dbda, 'imun', dead, X + 1)
    fill(dbda, 'icu', dead * 2, X - 10, X)
    fill(dbda, 'hospital', dead * 6, X - 11, X + 3)
    fill(dbda, 'imun', dead * 6, X + 4)
    fill(dbda, 'sick', dead * 177.7777778, X - 15, X - 6)
    fill(dbda, 'infectious', dead * 177.7777778, X - 17, X - 7)
    fill(dbda, 'imun', dead * 177.7777778, X - 6)

def compute_data_based_on_deaths(jdata, country):
    # Day by Day array - starts beginnig of 2020 with 0
    # 0: 2020-01-01
    dbda = {
        'imun': [0] * 366,
        'icu': [0] * 366,
        'hospital': [0] * 366,
        'sick': [0] * 366,
        'infectious': [0] * 366,
        'reported_infected': [0] * 366
    }

    # print(dbda['imun'])

    for jd in jdata:
        if jd['adm'][1] != country:
            continue
        if jd['dead'] == '':
            continue
        
        dead = int(jd['dead'])
        
        if dead == 0:
            continue

        X = compute_X(jd['date'])
        
        handle_one(dbda, X, dead)
        dbda['reported_infected'][X] += int(jd['infected'])
    print(dbda)

def main():
    input_filename, country = parse_args()
    with open(input_filename, "r") as fd:
        jdata = json.load(fd)
    #print(json.dumps(jdata))
    compute_data_based_on_deaths(jdata, country)

if __name__ == '__main__':
    main()
