from dataclasses import dataclass, field
from typing import List
import string


content: str = """If you can keep your head when all about you   
    Are losing theirs and blaming it on you,
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;
If you can wait and not be tired by waiting,
    Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
    And yet don’t look too good, nor talk too wise:

If you can dream — and not make dreams your master;   
    If you can think — and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth you’ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build ’em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: ‘Hold on!’

If you can talk with crowds and keep your virtue,   
    Or walk with Kings — nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty seconds’ worth of distance run,   
Yours is the Earth and everything that’s in it,   
    And — which is more — you’ll be a Man, my son!"""

mapping = dict(zip(list(string.ascii_lowercase), list(range(26))))  # type: ignore


@dataclass(frozen=True)
class Word:
    detail: str = ""
    weight: int = field(init=False)

    def __post_init__(self):
        weight: int = 0
        detail: str = ""

        for item in self.detail.lower():
            if mapping.get(item):
                weight += mapping.get(item, 0)
                detail += item

        object.__setattr__(self, "detail", detail)
        object.__setattr__(self, "weight", weight)

    def __lt__(self, __o: object) -> bool:
        return self.weight < __o.weight  # type: ignore

    def __gt__(self, __o: object) -> bool:
        return self.weight > __o.weight  # type: ignore

    def __le__(self, __o: object) -> bool:
        return self.weight <= __o.weight  # type: ignore

    def __ge__(self, __o: object) -> bool:
        return self.weight >= __o.weight  # type: ignore

    def __ne__(self, __o: object) -> bool:
        return self.weight != __o.weight  # type: ignore

    def __eq__(self, __o: object) -> bool:

        return self.detail is __o.detail  # type: ignore


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# class Word:
#     def __init__(self, detail: str) -> None:
#         self.detail = detail
#         self.weight = sum([mapping.get(item, 0) for item in self.detail.lower()])

#     def __repr__(self) -> str:
#         return f"({self.detail.strip()},{self.weight})"


def calculate_top_3_heaviest_words(*, content: str) -> List[Word]:
    words: List[Word] = list()

    for detail in content.split(" "):
        word = Word(detail)
        if is_prime(word.weight):
            words.append(word)

    words.sort(key=lambda x: x.weight, reverse=True)

    return words[:3]


if __name__ == "__main__":
    print(calculate_top_3_heaviest_words(content=content))
