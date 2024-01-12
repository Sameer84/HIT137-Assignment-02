global_variable = 100 #global_variable is set to 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # my_dic is initialized with some key-values

def process_numbers(numbers): #function process_numbers take parameter of numbers
    global global_variable 
    local_variable = 5
    numbers = [1, 2, 3, 4, 5] #local variable numbers is initialized to [,2,3,4,5]

    while local_variable > 0: #while loop is used to iterate local varible is greater than 0
        if local_variable % 2 == 0: #if it is even numbers
            numbers.remove(local_variable) #removes number from list
        local_variable -= 1
    return numbers #returns modified numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #my_set is inialized
result = process_numbers(numbers=my_set)

def modify_dict(local_variable ): # function modify_dict takes parameter local_variable
    my_dict['key4'] = local_variable #Adds a new key to my_dict whith the value of local_variable

modify_dict(10) 

def upbate_global():
    global global_variable
    global_variable += 10 #increaments by 10

for i in range(5):#Iterates over the range 0 to 4
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable) #print value of global_variable
print(my_dict)#print value of my_dict
print(my_set)#print value of my_set