#!/usr/bin/env python3

def MadMax(N, Tele):

    Tele.sort()
    slice_idx = int((len(Tele) - 1) / 2)
    first_slice = Tele[:slice_idx]
    second_slice = Tele[slice_idx:] 
    second_slice.reverse()
    result_arr = first_slice + second_slice

    return result_arr
