"""
Sometimes you need to limit array result to use. Such as you only need the
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value
If array, Min, Max value was given, it returns array that contains values of
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.
ex) limit([1,2,3,4,5], None, 3) = [1,2,3]
Complexity = O(n)
"""


def limit(array, *, min_num, max_num):
    return list(filter(lambda x: (min_num <= x <= max_num), array))


if __name__ == '__main__':
    print(limit([1, 2, 3, 4, 5], min_num=0, max_num=3))
