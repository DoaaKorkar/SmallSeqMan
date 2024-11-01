#!/usr/bin/env python
import os
import sys


# SeqFileObject= open(FastaFile, "r")
# print("first print")
# print(SeqFileObject.read())
# print("second print")
# print(SeqFileObject.read())
# SeqFileObject.close()

def Read_Fasta(fastaFile):
    if not os.path.exists(fastaFile):
        print(f"Error: {fastaFile} does not exist")
        return 
    Seqs = {}  #Key: Header, Value: Sequence
    with open(fastaFile) as f:   #removed "r" mode --> the function defult mode to read
        header=None
        for line in f:
            #removing whitespaces
            line = line.strip() 
            #skip empty lines
            if len(line)==0: 
                continue
            #Check for Heaer
            if line.startswith(">"):
                header=line[1:]
                #Check the header
                if len(header)< 1:
                    print("Error empty Header")
                    sys.exit(1)
                # remove ">" and extract only the first value
                header=header.split()[0]
                Seqs[header]=""
            #append Sequence(value) to header(key)
            else:
                Seqs[header] +=line.upper()
    return Seqs

# calculate sequence length
def get_sequence_lenght(Seqs):
    Seq_len={}
    for header, seq in Seqs.items():
        Seq_len[header]=len(seq)
    return Seq_len


def get_GC_content(Seqs):
    gc_content={}
    for header, seq in Seqs.items():
        gc_content[header]= (seq.count("G"))+(seq.count("C"))/len(seq)
    return gc_content


def get_at_content(Seqs):
    at_content={}
    for header, seq in Seqs.items():
        at_content[header]=(seq.count("A"))+(seq.count("T"))/len(seq)
    return at_content


def Check_nonDNA(Seqs):
    for head, seq in Seqs.items():
        for nuc in seq:
            if nuc not in "ATGC":
                print(f"Error {head} has non DNA base {nuc}")
                return True
    return False

def Reverse(Seqs):
    SeqDict={}
    for header, seq in Seqs.items():
        SeqDict[header]=seq[::-1]
    return SeqDict

def complement(Seqs):
    SeqDict={}
    for head,seq in Seqs.items():
        SeqTab=str.maketrans("ATGC","TACG")
        seq=seq.translate(SeqTab)
        SeqDict[head]=seq
    return SeqDict

def Reverse_Complement(Seqs):
    #encapsulation
    return complement(Reverse(Seqs))
