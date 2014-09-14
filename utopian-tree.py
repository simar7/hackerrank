# Enter your code here. Read input from STDIN. Print output to STDOUT

# first line = T = # of test cases
# T lines after 1st = N = # of cycles for that test case.

'''
    Cycles      ||      Length (origLength = 1)		||		output
    0                   (origLength)							1
    1                   (origLength*2)							2
    2                   (origLength*2 + 1)						3
    3                   (((origLength*2)+1)*2)					6
    4					((((origLength*2)+1)*2)+1)				7
'''
import sys

origLength = 1
growthLength = 1
limiter = 0

# This method returns growth.
def eval_height(cyclecount, growthLength):
	
    global limiter 
    limiter = limiter + 1

    if int(cyclecount) == 0:
       return int(growthLength)

    elif limiter & 0x1 == True: # Odd
	   return eval_height(int(cyclecount) - 1, growthLength * 2)
	
    elif limiter & 0x1 == False: # Even
	   return eval_height(int(cyclecount) - 1, growthLength + 1)


def main():
	    
 input_array = []
    
 for line in sys.stdin:
 	input_array.append(line)

 num_of_test_cases = input_array[0]

 for tree_cycle_count in input_array[1:]:
 	print (int(eval_height(tree_cycle_count, origLength)))

 

if __name__ == '__main__':
    main()