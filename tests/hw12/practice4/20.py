def linear_search(search_list, target):

    def binary_search(search_list, target):
        left_index = 0
        right_index = (search_list) - 1
        while left_index <= right_index:
            middle_index = (right_index + left_index)
            middle_value = search_list[middle_index]
            if middle_value == target:
                return middle_index
            elif middle_value < target:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
            return -1
# recursion
def print_repeat(s, n):
# Print Hi Calls itself again
    if n == 0:
        return
    else:
        print(s)
        print_repeat(s, n - 1)
l = [1,2,3,4]
#1 + sum ([2, 1]) + 2 + sum([2]) + 3 + sum([0]) <== sum of 0 is 0, Base Case!
def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_list(l[1:])

def sum_list_tail(l, t):
    if len(l) == 0:
        return t
    else:
        t += l[0]
        return sum_list_tail(l[1:], t)

if __name__ == '__main__':
    print_repeat('hi', 3)
    s = sum_list([1, 2, 3, 4])
    print(s)
    t = sum_list_tail([1,2,3,4,5], 0)
    print(t)
# on exam
# what is the big o for best case and worst case
# binary and linear search

#Recursion
# Base Case in function, 1 to many
# stopping function in Base Case
# multiple conditions
#