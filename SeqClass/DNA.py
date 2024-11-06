#!/usr/bin/env python
from SeqClass.sequences import Sequence
from SeqMod.seqIO import *
from SeqClass.GenomicConst import *

class DNA(Sequence):
    def get_reverse_complement(self):
        if "seqs" not in dir(self):
            self.get_seqs
        # self.reve= Reverse(self.Seqs)
        # self.reve_comp= complement(self.reve)
        # return self.reve_comp
        return Reverse_Complement(self.Seqs)
    
    def dna_translate(seqs):
        trans_Dict= GenomicConst.TripleCodonTableDNA
        aa=""
        for i in range(0,len(seqs), 3):
            codon = seqs[i:i+3]
            if len(codon)==3:
                aa+=trans_Dict[codon]
        return aa
    

    def traslate(self):
        self.aa_seq={}

        if "seqs" not in dir(self):
            self.get_seqs()
            for header, seq in self.Seqs.items():
                self.aa_seq[header] = DNA.dna_translate(seq)
        return self.aa_seq
