# Smallest-missing-denominator-data
Data for the paper 'The smallest denominator not contained in a unit fraction decomposition of 1 with fixed length' that was jointly written by Quanyu Tang and me.

For all integers m between 2 and 432 (inclusive) we need distinct positive integers n_1, .., n_t with t ≤ 41 such that 1/n_1 + .. + 1/n_t = 1 and m occurs as one of the n_i. For m smaller than or equal to 7 one can use either 1 = 1/2 + 1/3 + 1/6 or 1 = 1/2 + 1/4 + 1/5 + 1/20, so we may assume that m ≥ 7. For all these m we then actually write 1 = 1/2 + 1/3 + 1/n_1 + .. + 1/n_t with the n_i chosen in a greedy manner such that one of the n_i is equal to m (and with t ≤ 39). The denominators we then obtain can be found in the other document. Each line in that list has the format

m=<integer> : n1 n2 ... nt

and represents the claim that m is one of the n_i, that all the n_i are pairwise distinct, and that 1/2 + 1/3 + 1/n_1 + .. + 1/n_t = 1.  One may verify all lines using exact rational arithmetic.

For completeness, we include a short Python3 script below; it parses the list and checks, for every m between 7 and 432, that the corresponding list satisfies the above conditions.

#!/usr/bin/env python3
# Verify the listed certificates.
# It checks that: 
# (i) m is present 
# (ii) the denominators are distinct
# (iii) we do not use more than 39 denominators
# (iv) the equality 1/n_1 + .. + 1/n_t = 1/6 holds (so that 1/2 + 1/3 + 1/n_1 + .. + 1/n_t = 1).

import sys
import re
from fractions import Fraction
import os

LINE_RE = re.compile(r"^m=(\d+)\s*:\s*(.*)$")

def parse_lines(lines):
    cert = {}
    for raw in lines:
        raw = raw.strip()
        if not raw or raw.startswith("%"):
            continue
        m_str, rest = LINE_RE.match(raw).groups()
        m = int(m_str)
        denoms = [int(x) for x in rest.split()]
        cert[m] = denoms
    return cert

def verify(cert):
    for m in range(7, 433):
        if m not in cert:
            raise ValueError(f"Missing certificate for m={m}")
        denoms = cert[m]
        if m not in denoms:
            raise ValueError(f"Certificate for m={m} does not contain m")
        if len(set(denoms)) != len(denoms):
            raise ValueError(f"Certificate for m={m} has repeated denominators")
        if len(denoms) > 39:
            raise ValueError(f"Certificate for m={m} has too many denominators")        
        s = sum(Fraction(1, d) for d in denoms)
        if s != Fraction(1, 6):
            raise ValueError(f"Certificate for m={m} has sum {s}, expected 1/6")
    return True

def main():
    path = os.path.join(os.path.dirname(__file__), "cert.txt")
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        cert = parse_lines(f.readlines())
    verify(cert)
    print("All certificates verified for 7<=m<=432.")

if __name__ == "__main__":
    main()
\end{lstlisting}

To run the verifier on the list in this appendix, first copy the lines 'm=7 : ...' through 'm=432 : ...' into a plain text file named cert.txt. Each certificate for a fixed m must appear on a single line in the input file. In particular, long integers should not be broken across lines; otherwise the parser will fail. Then place cert.txt in the same directory as verify.py and execute python3 verify.py.
