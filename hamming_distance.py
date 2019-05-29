#!/usr/bin/python
import itertools

def hamming_distance(str1, str2):
    try:
        assert (len(str1)==len(str2))
        return sum(c1 != c2 for c1,c2 in zip(str1, str2))
    except AssertionError as e:
        return sum(c1 != c2 for c1,c2 in itertools.zip_longest(str1, str2, fillvalue='x'))

dist = hamming_distance("sanjay", "sanjay")
print (dist)
