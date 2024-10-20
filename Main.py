#!/usr/bin/env python
FastaFile= "exampledata/seqmultiline.fasta"
# SeqFileObject= open(FastaFile, "r")
# print("first print")
# print(SeqFileObject.read())
# print("second print")
# print(SeqFileObject.read())
# SeqFileObject.close()

def Read_Fasta(fastaFile):
    Seqs = {}  #Key: Header, Value: Sequence
    with open(FastaFile,"r") as f:
        header=None
        for line in f:
            #removing whitespaces
            line = line.strip() 
            #skip empty lines
            if len(line)==0: 
                continue
            #Check for Heaer
            if line.startswith(">"):
                header=line
                # remove ">" and extract only the first value
                header=header[1:].split()[0]
                Seqs[header]=""
            #Check for Sequence
            else:
                Seqs[header] +=line
    return Seqs