# In_Class_Programming_Assignment_2
ML_Assignment_2


Name: Vinay Kumar Camarush (CRN :22002)
700740428  

GitHub Link: https://github.com/VXC04280/In_Class_Programming_Assignment_2


Question – 1)
Use a python code to display the following star pattern using the for loop

Solution :
1)Here we used to nested for loops to print the given star pattern.
2)The first nested loop is used to print the upper part of the star pattern and the lower for 
loop is used to print the lower part of the string.
3)The first for loop in both the parts are used to loop over the number of rows in the pattern.
4)The Second for loop is used to loop over the number of elements of the rows based on the 
iterable of the first for loop.



Question – 2)
Use looping to output the elements from a provided list present at odd indexes. 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

1) Here the input list is stored in my_list
2) Created an empty list for storing the output
3) We ran a for loop to check if the index is even or odd.
4) If the index is odd, we appended the list elements to the output_list
5) At last we printed the output_list

Question – 3)
Write a code that appends the type of elements from a given list.
Input x = [23, ‘Python’, 23.98] 
Expected output [23, 'Python', 23.98] [class<’int’>,class<’str’> ,class<’int’> ] 

1) Here the input list is stored in x
2) Created an empty list for storing the output
3) We ran a for loop to iterate over the loop to get the type of the index.
4) We appended the type of the list elements to the output_list.
5) At last we printed the output_list


Question – 4)
Write a function that takes a list and returns a new list with unique items of the first list. Sample List: 
[1,2,3,3,3,3,4,5] Unique List: [1, 2, 3, 4, 5]

Solution : 
1) Here the input list is stored in input_list
2) Created a function to get the unique elements of the list.
3)In the method, we convert the input list to a set and then type cast the set as a list again.
4) We return the list from the given method.
5) When the function is called the output is stored in the variable output_list
6) Output_list is printed


Question – 5)
Write a function that accepts a string and calculate the number of upper-case letters and lowercase letters. 
Input String: 'The quick Brow Fox' 
Expected Output:
No. of Upper-case characters: 3 
No. of Lower-case Characters: 12


1) Here the input string is stored in input_string and pass it to the definition to get the output.
2) Created a function to get the no. of uppercase and lowercase letters.
3) In the method, we iterate over the string and check if the character is lowercase or 
uppercase.
4) If the character is uppercase, then the upper counter will be incremented.
5) If the character is lowercase, then the lower counter will be incremented.
6) We print the statements as per the given question.