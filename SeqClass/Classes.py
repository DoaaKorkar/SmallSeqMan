#!/usr/bin/env python
from SeqMod.seqIO import Read_Fasta, get_sequence_lenght
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
        return self.get_seqs_length