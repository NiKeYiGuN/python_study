"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.
Say the initial state is an array:
[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.
And the final state is
[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.
Edit:
Now also prints the sequence of changes in states.
Output of this example :-
initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence :
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""

from typing import List
from multiprocessing import Process


def garage(initial: List[int], final: List[int]) -> None:
    steps = 0
    i = 0

    while not initial == final:
        i %= len(initial)
        if not initial[i] == final[i]:
            temp, index = initial[i], initial.index(0)
            initial[index], initial[i] = temp, 0
            print(initial)
            steps += 1

        i += 1

    print(final, "\n", steps)


if __name__ == "__main__":
    init = [1, 2, 3, 0, 4]
    fi = [0, 3, 2, 1, 4]
    l1 = [1, 2, 3, 4, 5, 0]
    l2 = [1, 2, 3, 5, 4, 0]

    # garage(init, fi)
    # garage(l1, l2)

    p1 = Process(target=garage, args=(init, fi))
    p2 = Process(target=garage, args=(l1, l2))

    p1.start()
    p2.start()

