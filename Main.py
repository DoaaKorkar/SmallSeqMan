#!/usr/bin/env python
# from SeqMod.seqIO import Read_Fasta, get_sequence_lenght
from SeqClass.Classes import Sequence

FastaFile= "exampledata/seqmultiline.fasta"



mySeqs=Sequence(FastaFile)

print(mySeqs.get_seqs())
print(mySeqs.get_seqs_length())
print(mySeqs.get_GC_content())
print(mySeqs.get_at_content())
# print(mySeqs)
# print(type(mySeqs))


# mySeqs= Read_Fasta(FastaFile)
# seqLenght=get_sequence_lenght(mySeqs)
# print(seqLenght)
#print(mySeqs)