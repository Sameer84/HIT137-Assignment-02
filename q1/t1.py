# 1-1 Extract file
# Extract the ‘text’ in all the CSV files
# and store them into a single ‘.txt file’.

csv_files = ['./q1/CSV1.csv', './q1/CSV2.csv', './q1/CSV3.csv', './q1/CSV4.csv']
with open('./q1/merged_csv.txt', 'w') as f_out:
    for file in csv_files:
        with open(file, 'r') as f_in:
            content = f_in.read()
            f_out.write(content)

f_in.close()
f_out.close()
