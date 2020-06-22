from collect_function_performance_data import *
from counting_quad_sorts import *
from file_chooser import *
from file_column_averages import *
from menu import *
from plotter import *
max_n = 100
num_tests = 100

def main():
    list = ["Generate Sort Times","Plot Average Sort Times"]
    choice = do_menu("Main Menu",list)
    # This function lets user choose between different sorting algorithms to generate random data for
    if choice == 1:
        list = ["Bubble Sort", "Insertion Sort", "Optimized Bubble Sort", "Selection Sort"]
        choice = do_menu("Select a Sort", list)
        if choice == 1:
            test_function(counting_quad_sorts.bubbleSort, max_n, num_tests)
            print("Bubble sort data generated")
        if choice == 2:
            test_function(counting_quad_sorts.insertionSort, max_n, num_tests)
            print("Insertion sort data generated")
        if choice == 3:
            test_function(counting_quad_sorts.optimizedBubble, max_n, num_tests)
            print("Optimized bubble sort data generated")
        if choice == 4:
            test_function(counting_quad_sorts.selectionSort, max_n, num_tests)
            print("Selection sort data generated")
        if choice == "x" or choice == "X":
            return
    elif choice == 2:
        filename = get_file_path_and_name(pattern='*.csv')  #Gets path and file name
        averages = get_file_column_averages(filename[1])  #Gets column averages
        plot_1 = plot(title=f'{filename[1]} Plot', scale_x=6,  #Creates canvas
                      scale_y=0.11, bg='lime green', origin_x=28, origin_y=21)
        plot_1['draw_axes'](tick_interval_y=100, tick_length=1)

        for i in range(len(averages)):  #loop plots points
            plot_1['plot_point'](i, averages[i], 7, 'deep sky blue')
        plot_1['block']()

main()