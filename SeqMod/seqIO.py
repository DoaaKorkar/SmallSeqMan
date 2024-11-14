#!/usr/bin/env python
import os   # module provides a way to interact with the operating system
import sys  # It gives you control over things like input and output like exit() and path()
import re   # module provides support for working with regular expressions
            # This is useful for searching, replacing, and manipulating strings based on specific patterns.

############# OLD #################
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
                #sys.exit(0) typically signals a successful termination.
                 #sys.exit(1) or any non-zero number indicates an error or abnormal termination.
                if len(header)< 1:
                    print("Error empty Header")
                    sys.exit(1)   #exit the program due to an error.
                # remove ">" and extract only the first value
                header=header.split()[0]
                Seqs[header]=""
            #append Sequence(value) to header(key)
            else:
                Seqs[header] +=line.upper()
    return Seqs

# calculate sequence length
def sequence_lenght(Seqs):
    Seq_len={}
    for header, seq in Seqs.items():
        #items() --> outputs a list of tuples
        Seq_len[header]=len(seq)
    return Seq_len
def RNA(Seqs):
    rnaDict={}
    for header, seq in Seqs.items():
        rnaDict[header]= seq.replace("T","U")
        return rnaDict


def GC_content(Seqs):
    gc_content={}
    for header, seq in Seqs.items():
        gc_content[header]= round((seq.count("G"))+(seq.count("C"))/len(seq),2)
    return gc_content


def AT_content(Seqs):
    at_content={}
    for header, seq in Seqs.items():
        at_content[header]=round((seq.count("A"))+(seq.count("T"))/len(seq),2)
    return at_content


def Check_nonDNA(Seqs):
    for head, seq in Seqs.items():
        for nuc in seq:
            if nuc not in "ATGC":
                print(f"Error {head} has non DNA base {nuc}")
                return True
    return False

def Reverse(Seqs):
    """
    this function takes Dictionary.
    """
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


def Find_ORFs(Seq):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs_List = []
    sequence_length = len(Seq)
        
    for frame in range(3):
        pos = frame
        while pos + 2 < sequence_length:
            codon = Seq[pos:pos + 3]
            print(type(codon))
            if codon == start_codon:
                # Start new ORF
                orf_start = pos
                for i in range(pos, sequence_length, 3):
                    stop_codon = Seq[i:i + 3]
                    if stop_codon in stop_codons:
                        # Stop the ORF
                        orfs_List.append((orf_start, i + 3, Seq[orf_start:i + 3]))
                        break
            pos += 3
    return orfs_List
    
def find_all_orfs(sequences_dict):
    all_orfs = {}

    for header, sequence in sequences_dict.items():
        forward_orfs = Find_ORFs(sequence)
        reverse_sequence = Reverse_Complement(sequence)
        reverse_orfs = Find_ORFs(reverse_sequence)

        # Store ORFs for this sequence under its header
        all_orfs[header] = {
            'forward_strand': forward_orfs,
            'reverse_strand': reverse_orfs
        }
                    
    return all_orfs