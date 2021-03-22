""" 1.) Understand the problem
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
and write a program that prints out all the elements of the list that are less than 5. """

a = [1, 1, 11, 2, 33, 4, 5, 3, 2, 3, 22, 22, 33, 55]
for item in a:
    if item < 5:
        print(item)
