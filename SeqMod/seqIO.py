#!/usr/bin/env python
# SeqFileObject= open(FastaFile, "r")
# print("first print")
# print(SeqFileObject.read())
# print("second print")
# print(SeqFileObject.read())
# SeqFileObject.close()

def Read_Fasta(fastaFile):
    Seqs = {}  #Key: Header, Value: Sequence
    with open(fastaFile,"r") as f:
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



