#!/usr/bin/env python
# coding: utf-8

# In[74]:


# Define a function named is_two. It should accept one input and return True if the passed input is either 
# the number or the string 2, False otherwise.

def is_two(x): 
    if x == 2:                # check if x is numeric 2
        return True
    elif x.isdigit() == True: # check if x is digit
        if int(x) == 2:       # check if x is '2' after isdigit check to avoid letter string being passed to int(x) and causing error
            return True
    else:
        return False          # return false if not 2 or '2'

is_two('2')


# In[47]:


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(s):
    if s.lower() in "aeiou":            # using .lower() to ensure vowel matches regardless if its uppercase
        print (f'{s} is a vowel')
        return True
    else:
        print (f'{s} is a consonant')
        return False                    # return false if not vowel
    
is_vowel('e')


# In[46]:


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(s):
    if is_vowel(s) == False:   # running is_vowel to check if s is a vowel
        return True
    else:
        return False           # returning false if not a consonant
    
is_consonant('g')


# In[56]:


# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_consonant(s):
    if s[0].lower() not in 'aeiou': # check if first letter is a vowel. alternative is to remove .lower and add 'AEIOU' to string
        print(s.capitalize())  
        return s.capitalize()       # print and return word with capitalized first letter if first letter is a consonant
    else:
        print(s)
        return(s)                   # print and return word as normal if first letter is a vowel
        
capital_consonant('cat')


# In[62]:


# Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tp, bt):   # tip percentage and bill total set as parameters
    amount_to_tip = tp * bt  # multiply the values that are passed to find amount to tip
    return amount_to_tip     # return amount to tip

calculate_tip(.25, 100)


# In[76]:


# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(op, dp):                # original price (op) and discount percentage (dp) set as parameters
    price_after_discount = op - (op * dp)  # op * dp to find disc amount then subtracted from op to find disc price
    return(price_after_discount)           # return disc price
    
apply_discount(50, .10)


# In[83]:


# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(s):                      
    no_commas = int(s.replace("," , ""))   # using .replace to remove commas and int() to convert string to int and store as variable   
    return (no_commas)   # return new variable
 
handle_commas('4,000')


# In[243]:


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(i):
    if int(i) >= 88:     # set if and elif statements to return letter grade based on argument passed
        return 'A'       # using int(i) in case grade passed is grade in string form
    elif int(i) >= 80:
        return 'B'
    elif int(i) >= 67:
        return 'C'
    elif int(i) >= 60:
        return 'D'
    elif int(i) < 60:
        return 'F'
    
get_letter_grade(99)


# In[108]:


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(s):
    no_vowels = ""                            # create empty string
    for letter in s:                          # iterate through string
        if letter.lower() not in 'aeiou':     # check if letter is a vowel
            no_vowels += letter               # if not a vowel, add letter to empty string variable 
    return(no_vowels)               
    
remove_vowels('banana')
            
            


# In[170]:


"""
Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed
"""

def normalize_name(s):
    new_string = (s.strip("0123456789 ").lower().replace(" ", "_"))   # remove numbers and whitespace, replace spaces in string with "_"
    string2 = ""                                                      # create empty string
    for c in new_string:
        if c not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":                    # remove special characters
            string2 += c                                              # fill empty string with remaining characters
            
    return(string2)

normalize_name(' 123R $( )Abc ')


# In[172]:


# Write a function named cumulative_sum that 
# accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumalative_sum(l):
    running_total = 0               # create variable with value of zero
    n = []                          # create empty list
    for i in l:
        running_total += i          # use iteration to keep running total
        n.append(running_total)     # append values to empty list by adding running total to i
    return(n)
        
cumalative_sum([1,2,3,4])


# In[239]:


# ~~~~~~~~~~~~~~~~~ BONUS ~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and return a string that is the 
# representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

from datetime import datetime                             # importing datetime for use in function

def twelveto24(t):
    time_convert = datetime.strptime(t, "%I:%M%p")        # convert argument to raw 24 hour format
    only_time = datetime.strftime(time_convert, "%H:%M")  # specify format HH:MM 
    return(only_time)

twelveto24("10:45pm")
    


# In[240]:


# Bonus write a function that does the opposite

from datetime import datetime                          # importing datetime for use in function

def twentyfourto12(t):                                 # convert argument to normal format
    time_convert = datetime.strptime(t,"%H:%M")        # specify format HH:MMpm or HH:MMam
    return time_convert.strftime("%I:%M%p").lower()

twentyfourto12("22:30")


# In[ ]:


"""
Create a function named col_index. 
It should accept a spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27
"""




