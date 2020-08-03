#!/usr/bin/env python
# coding: utf-8

# # control_sctructures_exercises

# ## conditional basics

# In[579]:


# prompt the user for a day of the week, print out whether the day is Monday or not

day = input("Enter a day of the week: ")

if day.lower() == 'monday':
    print('You input monday')
else: 
    print('You did not input monday')


# In[2]:


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']
day = input("Enter a day of the week: ")

if day.lower() in weekdays:
    print(f'{day} is a weekday')
    
elif day.lower() in weekend:
    print(f'{day} is a weekend day')
    
else: 
    print(f'{day} is not a day of the week')


# In[547]:


""" 
create variables and make up values for:
1) the number of hours worked in one week
2) the hourly rate
3) how much the week's paycheck will be
THEN write the python code that calculates the weekly paycheck. 
You get paid time and a half if you work more than 40 hours 
"""

hours = 45
rate = 10.25
ot = (hours - 40) * (rate * 1.5)
reg_paycheck = rate * hours
ot_paycheck = ot + (rate * 40)

if hours > 40:
    print (round(ot_paycheck, 2))
else:
    print (round(reg_paycheck, 2))


# ## loop basics

# In[4]:


"""
Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
"""

i = 5
while i <= 15:
    print(i)
    i += 1


# In[5]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2


# In[9]:


# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5


# In[18]:


# Create a while loop that starts at 2, and displays the number squared on each 
#line while the number is less than 1,000,000. 

i = 2
while i <= 1000000:
    print(i)
    i = i**2


# In[19]:


# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# ## For Loops

# In[305]:


# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

number = (input('please input a number: '))
print()

if number.isdigit():
    for x in range(1, 11):
        print(f'{x} * {number} = {x * int(number)}')
else:
    print('you did not input a number. please input a number.')
        


# In[138]:


# Create a for loop that uses print to create the output shown below.

for x in range(1,10):
    print(str(x) * x)


# In[638]:


"""
Prompt the user for an odd number between 1 and 50. 
Use a loop and a break statement to continue prompting the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
except for the number the user entered.
"""

number = input('please input an odd number between 1 and 50: ')

for x in range(1,51,2):
    while number.isdigit() == False or int(number) < 1 or int(number) > 50 or int(number) % 2 == 0:
        print('\nYou must enter an odd number between 1 and 50. Try again.\n')
        number = input('please input an odd number between 1 and 50: ')
        if number.isdigit() == True and int(number) >= 1 and int(number) < 50 and int(number) % 2 == 1:
            print('\n', number, 'is the number to skip\n')
            break
            
    if x == int(number):
        print('Yikes! Skipping number:', x)
        continue
       
        
    print('Here is an odd number:', x)
    


# In[634]:


"""
The input function can be used to prompt for input and use that input in your python code. 
Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
(Hints: first make sure that the value the user entered is a valid number, 
 also note that the input function returns a string, so youll need to convert this to a numeric type.)
"""

number = input('please input a positive number: ')


while number.isdigit() == False or int(number) < 0:
    number = input('that is not a positive number. please input a positive number: ')
    if number.isdigit() == True and int(number) > 0:
        break
        
print('\n',list(x for x in range(0,int(number)+1)))


# In[647]:


# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

number = input('please input a positive integer: ')

while number.isdigit() == False or int(number) < 0:
    number = input('please input a positive integer: ')
    if number.isdigit() == True and int(number) > 0:
        break

print('\n',list(x for x in range(int(number), 0, -1)))


# In[432]:


"""
Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)


# In[687]:


"""
Display a table of powers.
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
"""

user_check = 'y'
while(user_check.lower() == 'y'):
    x = (input('what number would you like to go up to? '))
    while x.isdigit() == False:
        x = (input('that was not a number. please input a number: '))
        if x.isdigit() == True:
            break

    print('\nHere is your table!\n')
    print('number | squared | cubed')
    print('------------------------')
    for x in range(1,int(x)+1):
        print("{:^7}|{:^9}|{:^7}".format(x,x**2,x**3))
    
    user_check = input("\nWould you like to continue? (y/n): ")


# In[542]:


"""
Convert given number grades into letter grades.
Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
"""

usercon = 'y'
while usercon.lower() == 'y':
    grade = int(input('Please enter a grade: '))
    if grade >= 99 and grade <= 100:
        print('\n',f'{grade} is an A+!','\n')
    elif grade >= 90:
        print('\n',f'{grade} is an A!','\n')
    elif grade >= 88:
        print('\n',f'{grade} is an A-!','\n')
    elif grade >= 86:
        print('\n',f'{grade} is a B+!','\n')
    elif grade >= 82:
        print('\n',f'{grade} is a B!','\n')
    elif grade >= 80:
        print('\n',f'{grade} is a B-!','\n')
    elif grade >= 78:
        print('\n',f'{grade} is a C+!','\n')
    elif grade >= 69:
        print('\n',f'{grade} is a C!','\n')
    elif grade >= 67:
        print('\n',f'{grade} is a C-!','\n')
    elif grade >= 65:
        print('\n',f'{grade} is a D+!','\n')
    elif grade >= 62:
        print('\n',f'{grade} is a D!','\n')
    elif grade >= 60:
        print('\n',f'{grade} is a D-!','\n')
    elif grade <= 59:
        print('\n',f'{grade} is an F!','\n')
    else:
        print('you did not enter a grade between 1-100')
    usercon = input('Would you like to continue? "y" for yes. "n" for no ')


# In[553]:


"""
Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. 
Loop through the list and print out information about each book.
"""
books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "fiction",
    },
    {
        "title": "The Cat in the Hat",
        "author": "Dr. Seuss",
        "genre": "fiction",
    },
    {
        "title": "Start-Up Nation",
        "author": "Dan Senor",
        "genre": "non fiction",
    }]

[x for x in books]


# In[633]:


#Prompt the user to enter a genre, 
#then loop through your books list and print out the titles of all the books in that genre.

gen = input('Please enter a genre: ')

while gen not in [x['genre'] for x in books]:
    gen = input('No books matching requested genre. Please enter a new genre: ')
    if gen in [x['genre'] for x in books]:
        break


for x in books:
    if gen == x['genre']:
        print('\n{} falls under the genre of {}'.format(x['title'], gen))


