# -*- coding: utf-8 -*-
"""700740428_ICP_Assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h0SzCEylQc2bjsEirUp_vKf7y7G3PHKH
"""

'''
Machine Learning (CS 5710)
Assignment - 2
Vinay Kumr Camarushi (700740428)
'''

"""Question - 1)
Use a python code to display the following star pattern using the for loop
"""

# Use a python code to display the following star pattern using the for loop
rows = 5 # taking the maximum number (mid row) of stars in the pattern as input
# Intializing the upper part of the star 
for i in range(0, rows): # Running a for loop to run over the number of the rows in the upper part of the pattern
    for j in range(0, i + 1): # Running a nested for loop to run over the number of elemenets in each row in the upper part of the pattern
        print("*", end=' ') # Printing stars in each row
    print("\r") #printing carriage return

# Intializing the lower part of the pattern
for i in range(rows, 0, -1): #Running a for loop to run over the number of the rows in the lower part of the pattern
    for j in range(0, i - 1): # Running a nested for loop to run over the number of elemenets in each row in the lower part of the pattern
        print("*", end=' ') # Printing stars in each row
    print("\r") # printing carriage return

"""Question - 2) 
. Use looping to output the elements from a provided list present at odd indexes.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # input list of the numbers
output_list = [] # creating an empty list to store the output
for i in range(0,len(my_list)): # Running a for loop to iterate over the list of elements
  if i%2 == 1: # Checking if the index of the list is odd or not
    output_list.append(my_list[i]) # Appending the elements of my_list to the outpit list if the index is odd
print(output_list) # printing the output list

"""Question - 3)
Write a code that appends the type of elements from a given list.
Input
 x = [23, ???Python???, 23.98]
 Expected output
 [23, 'Python', 23.98]
 [<class 'int'>, <class 'str'>, <class 'float'>]
"""

x = [23, 'Python', 23.98] # Input list of elements
type_x = [] # Creating an empty list to store the type of the element of the list
for i in range(0,len(x)): # Running a for loop to append the type of the elements of the list into type_x list
  type_x.append(type(x[i])) # Appending the type of the list x to the list type_x

print(type_x) # Printing the output list

"""Question - 4)
Write a function that takes a list and returns a new list with unique items of the first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]
"""

def unique_list(input): # A defintion to take a list as an input and return the unique elements of the list as an output
  return (list(set(input))) #returning the list which is converted into set to eliminate the duplicate values 

input_list = [1,2,3,3,3,3,4,5] # taking input list

output_list = unique_list(input_list) # Calling the function and storing the returned output to output_list variable

print(output_list) # printing the output list

"""Question - 5)
Write a function that accepts a string and calculate the number of upper-case letters and lower-case
letters.
Input String: 'The quick Brow Fox'
Expected Output:
No. of Upper-case characters: 3
No. of Lower-case Characters: 12
"""

def char_counter(s): # Defining a function to take the string as an input and which returns the no. of uppercase and lowercase characters
  upper = 0 # Initializing a variable to store the no. of uppercase characters
  lower = 0 # Initializing a variable to store the no. of lowercase characters
  for i in s: # Running a for loop to iterate over the given string
    if i.islower(): # checking if the character is lowercase
      lower+= 1 # If the checked character is lowercase then the lower variba;e will be incremented by 1
    elif i.isupper():# checking if the character is uppercase
      upper+= 1  # If the checked character is uppercase then the lower variba;e will be incremented by 1


  print("No. of Upper-case characters:{} \nNo. of Lower-case Characters:{}".format(upper,lower)) # Printing the output as per given format

input_string = 'The quick Brow Fox' # Taking the string output

char_counter(input_string) # Calling the function to get the output as per given format