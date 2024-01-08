# 1-1 Extract file
# Extract the ‘text’ in all the CSV files
# and store them into a single ‘.txt file’.

try:
    # put csv file names to list
    csv_files = ['./q1/CSV1.csv', './q1/CSV2.csv', './q1/CSV3.csv', './q1/CSV4.csv']
    with open('./q1/merged_csv.txt', 'w') as f_out:
        # open each csv
        for file in csv_files:
            with open(file, 'r') as f_in:
                content = f_in.read()
                f_out.write(content)
    print('proccess done.')
except IOError as e:
    # if any csv file is missing
    print('IOError : ', e.errno, e)
finally:
    print('clean up...')
    f_in.close()
    f_out.close()
