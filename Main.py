#!/usr/bin/env python
FastaFile= "exampledata/seqmultiline.fasta"



from SeqMod.seqIO import Read_Fasta, get_sequence_lenght
mySeqs= Read_Fasta(FastaFile)
seqLenght=get_sequence_lenght(mySeqs)
print(seqLenght)
#print(mySeqs)