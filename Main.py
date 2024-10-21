#!/usr/bin/env python
from SeqMod.seqIO import Read_Fasta, get_sequence_lenght
from SeqClass import

FastaFile= "exampledata/seqmultiline.fasta"



mySeqs=Sequence(FastaFile)
print(mySeqs)

# mySeqs= Read_Fasta(FastaFile)
# seqLenght=get_sequence_lenght(mySeqs)
# print(seqLenght)
#print(mySeqs)