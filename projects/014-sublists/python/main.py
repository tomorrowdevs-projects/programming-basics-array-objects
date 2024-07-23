'''
A sublist is a list that is part of a larger list. A sublist may be a list containing a single element, multiple elements, or even no elements at all. For example, [1], [2], [3] and [4] are all sublists of [1, 2, 3, 4].
The list [2, 3] is also a sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of any list.
As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself, meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].

In this exercise you will create a function, isSublist, that determines whether or not one list is a sublist of another. Your function should take two lists, larger and smaller, as its only parameters.
It should return True if and only if smaller is a sublist of larger. Write a main program that demonstrates your function.
'''

def isSublist(larger, smaller):
    if not smaller:
        return True

    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    
    return False

def main():
    larger_list = [1, 2, 3, 4]
    smaller_list1 = [2, 3]
    smaller_list2 = [2, 4]
    smaller_list3 = []
    smaller_list4 = [1, 2, 3, 4]
    smaller_list5 = [1, 2, 3, 4, 5]
    
    print(isSublist(larger_list, smaller_list1))
    print(isSublist(larger_list, smaller_list2))
    print(isSublist(larger_list, smaller_list3))
    print(isSublist(larger_list, smaller_list4))
    print(isSublist(larger_list, smaller_list5))

main()