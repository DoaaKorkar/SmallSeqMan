#!/usr/bin/env python
import re
from SeqMod.seqIO import *
class Sequence():
    def __init__(self, fileName):
        self.fileName= fileName
    
    def get_seqs(self):
        self.Seqs= Read_Fasta(self.fileName)
        return self.Seqs
    
    # def get_seq_info(self):
    #     if "Seqs" not in dir(self):
    #         self.get_seqs
    #     info={}
    #     info["length"]=get_sequence_lenght(self.Seqs)
    #     info["GC_content"]= get_GC_content(self.Seqs)
    #     info["AT_content"]=get_at_content(self.Seqs)
    #     return info
    
    def get_seqs_length(self):
        if "Seqs" not in dir(self):
            self.get_seqs()
        self.Seq_len= sequence_lenght(self.Seqs)
        return self.Seq_len
    
    def get_GC_content(self):
        if "Seqs" not in dir(self):
            self.get_seqs()
        self.gc_content= GC_content(self.Seqs)
        return self.gc_content
    
    def get_AT_content(self):
        if "Seqs" not in dir(self):
            self.get_seqs
        self.at_content= AT_content(self.Seqs)
        return self.at_content
    
    def get_Reverse(self):
        if "Seqs" not in dir(self):
            self.get_seqs
        self.Revesre= Reverse(self.Seqs)
        return self.Revesre
    
    def get_Complement(self):
        if "Seqs" not in dir(self):
            self.get_seqs
        self.Complement= complement(self.Seqs)
        return self.Complement
 
    def get_RNA(self):
        if "Seqs" not in dir(self):
            self.get_seqs
        self.RNA= RNA(self.Seqs)
        return self.RNA