import itertools, heapq, contextlib

inputs = ['t1.txt', 't2.txt', 't3.txt']


def kayMapping(s):
    t = s.split()
    if len(t) < 1:
        return ""
    return s.split()[0]

def dedup(file):
    return [line for line, group in itertools.groupby(file)]

with contextlib.ExitStack() as stack:
    files = []
    for file in inputs:
        files.append(stack.enter_context(open(file)))
    with open('output.txt', 'w') as f:
        temp = dedup(heapq.merge(*files, key=kayMapping))
        f.writelines(temp)




