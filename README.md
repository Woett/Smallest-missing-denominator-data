# Smallest missing denominator data

In this repository one can find certificates for certain unit fraction decompositions of $1$, and Python code to verify these decompositions.

More precisely, for every integer $2 \leq m \leq 432$ we exhibit pairwise distinct positive integers $n_1,\dots,n_t$ with $t \leq 41$ such that $1=\frac1{n_1}+\cdots+\frac1{n_t}$, and where $m$ occurs as one of the denominators.

For $2 \leq m \leq 6$ one may use either $1=\frac12+\frac13+\frac16$ or $1=\frac12+\frac14+\frac15+\frac1{20}$, so it suffices to treat $m \geq 7$. For these $m$ we write $1=\frac12+\frac13+\frac1{n_1}+\cdots+\frac1{n_t}$, where the $n_i$ are pairwise distinct, one of them equals $m$, and $t \le 39$ (so that the total number of terms is at most $41$). 

The certificates are listed in cert.txt. Each line has the format

m=<integer> : n1 n2 ... nt

such that $m$ is one of the $n_i$, the $n_i$ are all distinct, $t \le 39$, and $\frac1{n_1}+\cdots+\frac1{n_t}=\frac16$ (so that $\frac12+\frac13+\frac1{n_1}+\cdots+\frac1{n_t} = 1$).

For completeness, we include a short Python 3 script verify.py which parses cert.txt and checks, for every $7 \leq m \leq 432$, that the corresponding line satisfies the required conditions using exact rational arithmetic.
