#!/usr/bin/env python
from SeqMod.seqIO import *
from SeqClass.sequences import Sequence
from SeqClass.DNA import DNA
FastaFile= "exampledata/seqmultiline.fasta"



# mySeqs=Sequence(FastaFile)

# print(mySeqs.get_seqs())
# print(mySeqs.get_seqs_length())
# print(mySeqs.get_GC_content())
# print(mySeqs.get_AT_content())
# print(mySeqs.get_Reverse())
# print(mySeqs.get_Complement())

mine=Read_Fasta(FastaFile)
print(Reverse_Complement(mine))

###print(mySeqs.get_seq_info())
# print(mySeqs)
# print(type(mySeqs))


# mySeqs= Read_Fasta(FastaFile)
# seqLenght=get_sequence_lenght(mySeqs)
# print(seqLenght)
#print(mySeqs)