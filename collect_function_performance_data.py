import random
import counting_quad_sorts

def test_function(fn, max_n, num_tests):
    #gets function name for file name
    file_name = fn.__name__
    file = open(file_name + '.csv', 'w+')

    for i in range(num_tests):
        rand_list = [random.random() for x in range(max_n)]  #Generates list of 100 random floats
        row = []  # Creates a row for every test

        for n in range(max_n):
            row.append(fn(rand_list[:n]))
        for x in row:
            file.write(str(x) + ',') #Writes to files
        file.write("\n") #Goes to next line
    file.close()

if __name__ == "__main__":
    test_function(counting_quad_sorts.bubbleSort, 100, 100)
    # the above line builds the csv file and fills it with count of iterationss