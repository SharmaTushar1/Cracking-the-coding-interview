# pretty simple the only thing to keep in mind is to use a list as strings (in python and java) are immutable. In java we can use stringbuilders but python we will require a list

from typing import List

def stringCompression(s: str):
    if len(s) <= 2:
        return s
    lst: List(str) = []
    output: str = ''
    count: int = 1
    for i in range(0, len(s)):
        if i == len(s) - 1:
            lst.append(s[i])
            lst.append(str(count))
            count = 1
            continue
        if s[i] == s[i+1]:
            count += 1
        else:
            lst.append(s[i])
            lst.append(str(count))
            count = 1
    output: str =  ''.join(lst)
    return output if len(output) < len(s) else s
