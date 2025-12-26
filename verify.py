#!/usr/bin/env python3
# Verify the certificates for m between 7 and 432.
# It checks that: 
# (i) m is present,
# (ii) the denominators are distinct,
# (iii) there are at most 39 denominators,
# (iv) the sum 1/n_1 + .. + 1/n_t is equal to 1/6, so that 1 = 1/2 + 1/3 + 1/n_1 + .. + 1/n_t

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
