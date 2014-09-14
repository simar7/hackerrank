# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import array
import ctypes

global_elem_count = array.array('i', (0 for i in range(0, 26)))

def elem_counter(elem):
    #print elem
    #print type(elem)
    global_elem_count[(ord(elem)-97)] = global_elem_count[(ord(elem)-97)] + 1
    
def check_for_elems(rock):
    for elem in ''.join(set(rock[:len(rock)-1])): # Purposely for whitesp.
        #print elem
        elem_counter(elem)
        
def main():
    gems = 0
    input_array = []
    
    for line in sys.stdin:
        input_array.append(line)
       
    number_of_rocks = input_array[0]
    
    for rock in input_array[1:]:
        #print rock
        check_for_elems(rock)
        
    for elem in global_elem_count:
        #print elem
        #print global_elem_count
        if (int(elem) == int(number_of_rocks)):
            gems = gems + 1
    
    #print "Gems are %s" % gems
    #print "Number of rocks are %s" % number_of_rocks
    print gems
        
if __name__ == '__main__':
    main()