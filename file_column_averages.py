def get_file_column_averages(filename):
    #opens file to get averages from
    myfile = open(filename, 'r')
    rows = myfile.readlines()
    row_list = []
    count = 0

    for row in rows:
        strip = row.strip('\n')
        split = strip.split(',')
        split.pop(len(rows))
        row_list.append(split)
        count += 1

    averages = []

    for i in range(len(row_list)):  #adds up total in columns
        sum = 0
        for line in row_list:
            sum += float(line[i])

        i_average = sum / count
        averages.append(i_average) #gets average in columns

    return(averages)

if __name__ == "__main__":
    print(get_file_column_averages('optimizedBubbleSort'))