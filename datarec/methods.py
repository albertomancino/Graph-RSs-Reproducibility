from .io import readers
from typing import Union


def read_tsv(filepath, header: Union[int, bool] = False, *args, **kwargs):
    return readers.read_tabular(filepath, sep='\t', header=header)


def read_txt(filepath, header: Union[int, bool] = False, *args, **kwargs):
    return readers.read_tabular(filepath, sep=' ', header=header)
