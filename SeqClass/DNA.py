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
        return Reverse_Complement(self.get_seqs)

    
