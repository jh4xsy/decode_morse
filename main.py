from morse import ALPHABET
from itertools import groupby

num_tags = len(ALPHABET)

# 0: blank label
tag_to_idx = {c: i + 1 for i, c in enumerate(ALPHABET)}
idx_to_tag = {i + 1: c for i, c in enumerate(ALPHABET)}


def prediction_to_str(seq):
    if not isinstance(seq, list):
        seq = seq.tolist()

    # remove duplicates
    seq = [i[0] for i in groupby(seq)]

    # remove blanks
    seq = [s for s in seq if s != 0]

    # convert to string
    seq = "".join(idx_to_tag[c] for c in seq)

    return seq

