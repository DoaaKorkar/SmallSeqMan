#!/usr/bin/env python
FastaFile= "exampledata/seqmultiline.fasta"

class Sequence():
    def __init__(self, fileName):
        self.fileName= fileName

mySeqs=Sequence(FastaFile)
print(mySeqs)
# from SeqMod.seqIO import Read_Fasta, get_sequence_lenght
# mySeqs= Read_Fasta(FastaFile)
# seqLenght=get_sequence_lenght(mySeqs)
# print(seqLenght)
#print(mySeqs)