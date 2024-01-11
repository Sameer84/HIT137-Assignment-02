def divide_and_seperate(a):
    number_string = ''
    letter_string = ''

    for char in a:
        if char.isdigit():
            number_string += char
        elif char.isalpha():
            letter_string += char

    #ASCII values of characters if digit is even
    even_numbers_ascii = [str(ord(char)) for char in number_string if int(char) % 2 == 0]
    #contain the ASCII values of the uppercase letters 
    upper_case_ascii = [str(ord(char)) for char in letter_string if char.isupper()]

    return number_string, letter_string, even_numbers_ascii, upper_case_ascii

#example from question
input_question_string = '56aAw1984sktr235270aYmn145ss785fsq3100'
#calling divide_and_seperate function
result = divide_and_seperate(input_question_string)

number_string, letter_string, even_numbers_ascii, upper_case_ascii = result

print(f'Seperate Number String: {number_string}')
print(f'Seperate Letter String: {letter_string}')
print(f'Even Numbers to ASCII Code: {", ".join(even_numbers_ascii)}')
print(f'Upper-case Letters to ASCII Code: {", ".join(upper_case_ascii)}')