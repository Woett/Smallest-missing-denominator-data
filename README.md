# Smallest-missing-denominator-data
Data for the paper 'The smallest denominator not contained in a unit fraction decomposition of 1 with fixed length' that was jointly written by Quanyu Tang and me.

For all integers m between 2 and 432 (inclusive) we need distinct positive integers n_1, .., n_t with t ≤ 41 such that 1/n_1 + .. + 1/n_t = 1 and m occurs as one of the n_i. For 2 ≤ m ≤ 6 one can use either 1 = 1/2 + 1/3 + 1/6 or 1 = 1/2 + 1/4 + 1/5 + 1/20, so we may assume that m ≥ 7. For all these m we then actually write 1 = 1/2 + 1/3 + 1/n_1 + .. + 1/n_t with the n_i chosen in a greedy manner such that one of the n_i is equal to m. The denominators we then obtain can be found in the document cert.txt. Each line in that list has the format

m='integer' : n1 n2 ... nt

and represents the claim that m is one of the n_i, that all the n_i are pairwise distinct, that t ≤ 39, and that 1/2 + 1/3 + 1/n_1 + .. + 1/n_t = 1.  One may verify all lines using exact rational arithmetic.

For completeness, we included a short Python3 script vrify.py; it parses the list and checks, for every m between 7 and 432, that the corresponding list satisfies the required conditions.
