#!/usr/bin/python

# Find the most frequent k-mers in a string.
# Given: A DNA string 'Text' and an integer 'k'.
# Return: All most frequent k-mers in 'Text' (in any order).

Text = 'TCTTGATGATCTTGATGAGCGAATGAACTATGATGGGGCGAATGAACTATGATGGGGGGGTGGACTAGCAGTAACGCGAATGAAGGGGTGGACTCTTGATGACTATGATGGGGCGAATGAATCTTGATGACTATGATGGGTCTTGATGAGGGGTGGACGCGAATGAAGCGAATGAAGGGGTGGACGCGAATGAACTATGATGGGCTATGATGGGGCGAATGAAGCGAATGAACTATGATGGGGGGGTGGACTAGCAGTAACGCGAATGAAGGGGTGGACGCGAATGAACTATGATGGGTAGCAGTAACTCTTGATGATCTTGATGACTATGATGGGTAGCAGTAACCTATGATGGGGCGAATGAATCTTGATGAGGGGTGGACGCGAATGAACTATGATGGGTAGCAGTAACGCGAATGAAGCGAATGAACTATGATGGGTAGCAGTAACGCGAATGAACTATGATGGGTAGCAGTAACCTATGATGGGGCGAATGAATCTTGATGATCTTGATGATCTTGATGATCTTGATGAGCGAATGAACTATGATGGGTCTTGATGACTATGATGGGTCTTGATGATCTTGATGATCTTGATGAGGGGTGGACGCGAATGAATCTTGATGATAGCAGTAACCTATGATGGGTCTTGATGACTATGATGGGTCTTGATGATAGCAGTAACGCGAATGAACTATGATGGGCTATGATGGGGGGGTGGACTCTTGATGATAGCAGTAACTCTTGATGAGCGAATGAATCTTGATGACTATGATGGGGCGAATGAAGCGAATGAATAGCAGTAACCTATGATGGGTAGCAGTAACTCTTGATGACTATGATGGGGCGAATGAACTATGATGGGTCTTGATGAGGGGTGGACTAGCAGTAACTAGCAGTAACTCTTGATGACTATGATGGGGCGAATGAATCTTGATGAGCGAATGAAGCGAATGAAGGGGTGGACTCTTGATGACTATGATGGG'
k = 14

# Make a dictionary of all k-mers and the number of occurances of each
kmers = {}
for x in range(len(Text)-k-1):
        mer = Text[x:x+k]
        kmers[mer] = 1
        for y in range(len(Text)-k-1):
                if Text[y:y+k] == mer:
                        kmers[mer] += 1

# Find the max number of occurances and the corresponding k-mer(s)
max_count = max(kmers.values())
answer = [key for key, val in kmers.items() if val == max_count]
for a in answer: print a
