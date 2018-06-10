# @File  : util.py
# @Author: TianWen
# @Date  : 2018/6/10  13:26
# @Desc  : 工具类


def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []