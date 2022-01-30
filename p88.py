#lex_auth_0127136216235950081185
'''Problem Statement
A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, the next list in the sequence is formed by taking the absolute differences of neighboring integers in the previous list.

Start List: [0,653,1854,4063]

Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]

Assumption: The Ducci sequence ends with a list containing 0s and the starting list contains four elements.

Write a python function that takes a starting list of integers and a number ‘n’ as input, and returns the nth element of the Ducci sequence.

Sample Input

Expected Output

test_list=[0,653,1854,4063]
n = 1

[548,1008,1854,3410]

'''


def ducci_sequence(test_list,n):
    #start writing your code here
    final_list = []
    for i in range(0,n+1):
        x = test_list[0]
        test_list[0] = test_list[0] - test_list[1]
        test_list[1] = test_list[1] - test_list[2]
        test_list[2] = test_list[2] - test_list[3]
        test_list[3] = test_list[3] - x
        if test_list[0] < 0:
            test_list[0] = -(test_list[0])
        if test_list[1] < 0:
            test_list[1] = -(test_list[1])
        if test_list[2] < 0:
            test_list[2] = -(test_list[2])
        if test_list[3] < 0:
            test_list[3] = -(test_list[3])
        final_list.append(test_list)
    return final_list[n]

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 1)
print(ducci_element)