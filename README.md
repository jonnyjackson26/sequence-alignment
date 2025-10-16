# sequence-alignment (Needleman-Wunsch)
This is project 5 for Analysis of Algorithms with Brian Knaeble. This uses *dynamic programming*

From the website for the textbook complete Programming Problem 17.8: Sequence Alignment along with the reconstruction algorithm to print out your solution showing the optimally aligned sequences.


https://www.algorithmsilluminated.org/
Programming Problem 17.8: Sequence Alignment
This file describes an instance of the sequence alignment problem. The format of the file is:
1st line: length of X and length of Y
2nd line: gap cost and mismatch cost (the latter is the same for every pair of distinct symbols)
3rd line: X sequence
4th line: Y sequence
(Answer: the NW score is 224.)

148 123 (length of X and length of Y)
4 5 (gap cost and mismatch cost)
ACACATGCATCATGACTATGCATGCATGACTGACTGCATGCATGCATCCATCATGCATGCATCGATGCATGCATGACCACCTGTGTGACACATGCATGCGTGTGACATGCGAGACTCACTAGCGATGCATGCATGCATGCATGCATGC (X)
ATGATCATGCATGCATGCATCACACTGTGCATCAGAGAGAGCTCTCAGCAGACCACACACACGTGTGCAGAGAGCATGCATGCATGCATGCATGCATGGTAGCTGCATGCTATGAGCATGCAG (Y)

### In my program, I:
1. **read in the data (x and y sequences, the gap cost and mismatch cost)**
 - the length is also in that file but I choose to not use it. 

2. **Generate a matrix**
 - I set the top row equal to '0,  -<gap_cost> -<gap_cost>*2, -<gap_cost>*3, ...' and the first column the same.
 - For each cell in the matrix, going top->bottom left-> right, I check what the score were to be if you were to have a gap in the x sequence there, have a gap in the y sequence there, or if you have a match/mismatch. Whichever option gives the best score, i set as that cells value.

3. **Reconstruct**
 - I start at the bottom right and check if it's best for me to go up/down/diagnoal until I get to the top left corner. As I do, I sum my total alignment score and construct the X and Y sequences while adding either dashes or characters.


# Example:
for:
gap cost: 4 and mismatch cost: 5 with sequences X and Y:
```
ACACATGCATCATGACTATGCATGCATGACTGACTGCATGCATGCATCCATCATGCATGCATCGATGCATGCATGACCACCTGTGTGACACATGCATGCGTGTGACATGCGAGACTCACTAGCGATGCATGCATGCATGCATGCATGC
ATGATCATGCATGCATGCATCACACTGTGCATCAGAGAGAGCTCTCAGCAGACCACACACACGTGTGCAGAGAGCATGCATGCATGCATGCATGCATGGTAGCTGCATGCTATGAGCATGCAG
```

We get the following Optimal Alignment:

```
ACACATGCATCATGACTATGCATGCATGACTGACTGCATGCATGCATCCATCATGCATGCATCGATGCATG--CATGAC-CACCTGTG-TGACA-CATGCATGCGTGTGACATGCGA-GAC-TCACTAGCGATGCATGC-ATGCATGCATGCATGC
----ATG-ATCATG-C-ATGCATGCATCAC--ACTG--TGCAT-CAGAGA-GA-GC-T-C-TC-A-GCA-GACCA-CACACACGTGTGCAGAGAGCATGCATGC--ATG-CATGC-ATG-CAT-GGTAGC--TGCATGCTATG-A-GCATGCA-G-
```

with score 224. 