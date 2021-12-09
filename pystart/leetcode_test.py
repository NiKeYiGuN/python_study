from collections import defaultdict
from typing import DefaultDict


if __name__ == "__main__":
    s = "ab"
    t = "a"
    dic: DefaultDict[str, int] = defaultdict(int)
    for letter in s:
        dic[letter] += 1
    for letter in t:
        dic[letter] -= 1
        if dic[letter] < 0:
            print(False)
    print(True)
