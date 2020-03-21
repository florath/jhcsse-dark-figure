Try to predict dark figure for COVID-19
+++++++++++++++++++++++++++++++++++++++

Description
===========

The problem with the current data sets is, that the dark figure of
infected people is unknown and might be very high.  The number of
known infections depends on many influences, especially on the number
of tests.

Trying to match the numbers from John Hopkins CSSE with the result of
the paper [1] the number of the infected is *much* too low.

Idea
====

Throw aways the 'infected' numbers of the available statistics and
compute them based on the results of [1] **only** based on the death
rate.  Compare them with the reported numbers, try to find a
correlation between these and try to extrapolate for the future.

Computation
===========

Based on figure 1 (page 4) of [1] from one person's death at day X the
following can be concluded:

* 1 person: day X: healed from intensive care unit
* 1 person: day X + 1, ...: this person is imun
* 2 persons: day X - 10, ..., X: intensive care unit
* 6 persons: day X - 11, ..., X + 3: (normal) hospital
* 6 persons: day X + 4, ...: these persons are imun
* 177.778 persons: day X - 15, ..., X - 6: sick (no hospital)
* 177.778 persons: day X - 17, ..., X - 7: infectious
* 177.778 persons: day X - 6, ...: imun

[1] Modellierung von Beispielszenarien der SARS-CoV-2-Epidemie 2020 in
Deutschland https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Modellierung_Deutschland.pdf?__blob=publicationFile
