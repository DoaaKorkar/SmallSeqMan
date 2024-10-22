#!/usr/bin/env python
from SeqMod.seqIO import *
class Sequence():
    def __init__(self, fileName):
        self.fileName= fileName
    
    def get_seqs(self):
        self.Seqs= Read_Fasta(self.fileName)
        return self.Seqs
    
    def get_seqs_length(self):
        if self.Seqs is None:
            self.get_seqs()
        self.Seq_len= get_sequence_lenght(self.Seqs)
        return self.Seq_len
    
    def get_GC_content(self):
        if self.Seqs is None:
            self.get_seqs()
        self.gc_content= get_GC_content(self.Seqs)
        return self.gc_content
    
    def get_at_content(self):
        if self.Seqs is None:
            self.get_seqs
        self.at_content= get_at_content(self.Seqs)
        return self.at_content