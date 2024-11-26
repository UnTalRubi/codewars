'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''

def unique_in_order(sequence):
    list_sequence = list(sequence)
    
    position = 1
    while position < len(list_sequence):
        if list_sequence[position] == list_sequence[position - 1]:
            list_sequence.pop(position)
        else:
            position += 1
        
    return list_sequence