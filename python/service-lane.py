'''
Sample Input
The first line of input contains two integers - N & T, where N is the length
of the freeway, and T is the number of test cases. The next line has N space 
separated integers which represents the width array.

T test cases follow. Each test case contains two integers - i & j, where i is 
the index of segment through which Calvin enters the service lane and j is the 
index of the lane segment where he exits

	8 5
	2 3 1 2 3 2 3 3
	0 3
	4 6
	6 7
	3 5
	0 7
'''

'''
Sample Output
	1
	2
	3
	2
	1
'''

'''
Reasoning
   |HIGHWAY|Lane|    ->    Width

0: |       |--|            2
1: |       |---|           3
2: |       |-|             1
3: |       |--|            2
4: |       |---|           3
5: |       |--|            2
6: |       |---|           3
7: |       |---|           3
'''
'''
Constraints
	2 <= N <= 100000 
	1 <= T <= 1000 
	0 <= i < j < N 
	2 <= j-i+1 <= min(N,1000) 
	1 <= width[k] <= 3, where 0 <= k < N
'''

import sys
counter = 0

def main():

    input_array = []
    seg_array = []
    test_array = []
    entry_array = []
    exit_array = []

    # (N, T), (0, 1, 2, ... N), N*(i, j)    
    for line in sys.stdin:
     	input_array.append(line)

    # Bad hax but whatever.
    freeway_len = input_array[0].split(' ')[0] # N
    num_of_tests = input_array[0].split(' ')[1] # T
    

    # Input hax still continues...
    for seg_width in input_array[1]:
    	if seg_width != ' ' and seg_width != '\n':
    		seg_array.append(seg_width)


   	for test in xrange(2, num_of_tests):
   		if test != ' ' and test != '\n':
   			test_array.append(input_array[test].strip())


   	for each_test in test_array:
   		entry_array.append(int(each_test[0]))
   		exit_array.append(int(each_test[1]))

   	print test_array
   	print entry array
   	print exit_array


if __name__ == '__main__':
	main()