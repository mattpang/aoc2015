import re
import codecs

d1 = open("inputs/8a.txt", "r").read()
d = open("inputs/8.txt", "r").read()


def escape(x: str) -> int:
    y = x[1:-1]
    pos = 0
    #   tell the difference between \x True and \\x False and \\\x True and \\\\x FALSE
    tally = ""
    if len(re.findall(r"(?<!\\)(?:\\\\)*(\\x)", y)) == 0:
        tally = y
    else:
        for m in re.finditer(r"(?<!\\)(?:\\\\)*(\\x)", y):
            p1, p2 = m.span(1)

            tally += y[pos:p1]

            h = chr(int(y[p2 : p2 + 2], 16))
            tally += h

            pos = p2 + 2
        if pos<len(y):
            tally += y[pos:]

    tally = tally.replace(r"\"", '"').replace(r"\\", "\\")
    return len(tally)


def processed(inputs, expand=False) -> int:
    str_tokens = 0
    char_tokens = 0
    ex_tokens = 0 
    for line in inputs.splitlines():
        str_tokens += len(line)
        char_tokens += escape(line)
        expanded = '"'+line.replace('\\','\\\\').replace(r'"',r'\"')+'"'
        ex_tokens += len(expanded)
        
        # print(line,len(line),escape(line),expanded, len(expanded))
    
    if expand:
        return ex_tokens - str_tokens
    else:
        return str_tokens - char_tokens


assert processed(d1) == 23 - 11
print(processed(d))
assert processed(d1,True) == 42 - 23
print(processed(d,True))
