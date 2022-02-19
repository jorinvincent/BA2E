In this assignment you will have to implement a greedy motif search algorithm, as described in the book as algorithm 2E.  You will submit the code through Gradescope as assignment: https://www.gradescope.com/courses/358896/assignments/1822203 .

Your code will expect a file named "input" that contains multiple lines in the following format:

3 5
ACGATTGCCTGCACTG
GCCCAGTATCGACAAC
GTTTGACAGATATTTCC
CTAGAGGGACTAGAGA
AGAGATTTAGATAGTA
The first line contains two integers, representing the values for k (k-mer size, or motif "width") and t (number of strings).  This line is followed by exactly t lines containing the t DNA sequences within which you are searching for motifs.  Note that the sequences do not have to have the same exact length, though each sequence will be entirely contained within one line (no need to deal with wrapping here).

Your code must produce a file called "output" that contains exactly t lines, each of which contains a string of length k. These represent the motif found by the greedy motif search algorithm.  For example, for the sequences above, your code should output:

GAT
TAT
GAT
GAG
GAT
This problem is equivalent to the Rosalind problem BA2E: http://rosalind.info/problems/ba2e/ .

IMPORTANT: note that the greedy motif search appears twice in the book, first prior to describing Laplace's rule (2D) and the second time afterwards (2E).  You must implement the second approach, however the algorithm is outlined in the book only under 2D.

HINT: To be successful in this assignment, it is best if you create a couple of helper functions. Some examples include:

build profile from motifs
compute profile-most probable k-mer given a profile and a string
compute the score of a motif
