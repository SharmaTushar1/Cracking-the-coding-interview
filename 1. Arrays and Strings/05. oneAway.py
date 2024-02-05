# aa, a => return False always!!!
# ab, a
# abbb, abad
# size difference should always be less than or equals to 1
# Insertion and deletion will happen only when the size diff is one
# Replacement will be done when the size is same

# Insert: abc, ab => abc => True
# Delete: abc => ab, ab => True
# Replace: abc, abv => abc => True

# abcdf, abcddf        diff = 1
#      '       '

from typing import List

def oneWay(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1: return False
    if len(s1) == len(s2): return replaceCharacterCheck(s1, s2)
    else: return insertOrRemoveCharacterCheck(s1, s2)

def insertOrRemoveCharacterCheck(s1: str, s2: str) -> bool:
    if len(s1) == 0 or len(s2) == 0: return True
    differCount = 0
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if len(s1) > len(s2):
                i += 1
            else:
                j += 1
            differCount += 1
            if differCount > 1: return False
    return True
    
    
def replaceCharacterCheck(s1: str, s2: str) -> bool:
    differCount = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            differCount += 1
            if differCount > 1:
                return False
    return True
    
# for insert and remove: find the character which is not present
# remove it from the string it is present and check if the strings are equal or not if yes return true else false

    
print(oneWay('ab', 'ab'))
print(oneWay('aaa', 'aab'))
print(oneWay('aDb', 'adb'))
print(oneWay('pale', 'ple'))
print(oneWay('ple', 'pale'))
print(oneWay('adb', 'aDb'))
print(oneWay('pales', 'pale'))
print(oneWay('pale', 'bae'))
print(oneWay('aDd', 'adD'))
print(oneWay('aDd', 'add'))
