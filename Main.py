#!/usr/bin/env python
FastaFile= "exampledata/seqmultiline.fasta"
from SeqMod.seqIO import Read_Fasta
mySeqs= Read_Fasta(FastaFile)
print(mySeqs)