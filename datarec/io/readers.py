from typing import Union


class RawData:
    def __init__(self, data=None, header=False):
        self.data = data
        self.header = header
        if data is None:
            self.data = []
            self.header = header
        self.path = None

    def append(self, new_data):
        self.data.append(new_data)

    def __repr__(self):
        return repr(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __add__(self, other):
        return RawData(self.data + other.data)

    def __iter__(self):
        return iter(self.data)


def read_tabular(filepath: str, sep, header: Union[bool, int] = False):

    result = RawData()
    result.path = filepath

    if header is True:
        header = 0

    with open(filepath, 'r') as file:
        if header is False:
            for line in file:
                elems = line.replace('\n', '').split(sep)
                result.append(elems)
        elif isinstance(header, int):
            for idx, line in enumerate(file):
                elems = line.replace('\n', '').split(sep)
                if idx == header:
                    result.header = elems
                else:
                    result.append(elems)
    return result
