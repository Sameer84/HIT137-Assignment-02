# Import random module
import random 

# Initialize variables
total_sum = 100
my_dict= {'key11': 'value1', 'key12': 'value2', 'key13': 'value3'}

def process_numbers():
  total = total_sum
  number = 5
  numbers = [1, 2, 3, 4, 5]
  
  while number > 0:
    if number % 2 == 0:
      numbers.remove(number)
    number -= 1
  
  return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
result = process_numbers(numbers=my_set)

def test_dict():
  number = 10
  my_dict['key14'] = number
  test_dict(5)

def update_total():
  global total_sum 
  total_sum += 10
  
  for i in range(5):
    print(i)
    i += 1
    
  if my_set is not None and my_dict['key14'] == 10:
    print("Condition met!")
    
  if 5 not in my_dict:
    print("5 not found in the dictionary!")
  
  print(total_sum)
  print(my_dict)
  print(my_set)

