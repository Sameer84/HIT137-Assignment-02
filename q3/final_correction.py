global_variable = 100
my_dict = {'key1': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # Corrected: Removed unnecessary argument from process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict()  # Corrected: Removed unnecessary argument from modify_dict()

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    # Corrected: Changed variable I to lowercase i in loop
    # Removed unnecessary I += 1 line

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")

if 5 not in my_dict: # Corrected: Changed my_set to my_dict in conditional. Since checking if 5 is in dictionary, not set
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
