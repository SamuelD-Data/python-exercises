#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Define a function named is_two. It should accept one input and return True if the passed input is either 
# the number or the string 2, False otherwise.

def is_two(x):
    assert type(x) == str or type(x) == int, 'argument passed is not a string or integer '  # check if x is a str or int
    
    if x != 2 and x != '2':                                # if x is not 2 or '2', return false
        print ('argument passed is not a 2')
        return False
    elif x == 2 or x == '2':                               # if x is 2 or '2', return true with a cool statement
        print('argument passed is 2, thats 2 cool!')
        return True

is_two('2')


# In[100]:


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(s):
    assert type(s) == str, 'argument passed is not a string' # check that argument is a string
    
    vowels = ['a','e','i','o','u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    if s.lower() in vowels:  # using list of single vowels to ensure double vowels (ae, iu, etc) dont pass check
        print (f'{s} is a vowel')
        return True
    elif s.lower() in consonants:    # using list of consontants to avoid double consonants being passed as a single consonant in next exercise
        print (f'{s} is a consonant')
        return False   
    else:
        print(f'{s} is a string of multiple characters, please pass a single character')
    
is_vowel('a')


# In[86]:


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(s):           # no assertion line necessary here bc is_vowel already has one
    if is_vowel(s) == False:   # running is_vowel to check if s is a vowel
        return True
    else:
        return False           # returning false if not a consonant
    
is_consonant('v')


# In[107]:


# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_consonant(s):
    assert type(s) == str, 'argument passed is not a string' # check if argument is a string
    
    if s[0].lower() not in 'aeiou': # check if first letter is a vowel. alternative is to remove .lower and add 'AEIOU' to string
        print(s.capitalize())       
        return s.capitalize()       # print and return string with capitalized first letter if first letter is a consonant
    else:
        print(s)
        return(s)                   # print and return string as normal if first letter is a vowel
        
capital_consonant('cat')


# In[112]:


# Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tp, bt):   # tip percentage and bill total set as parameters
    assert type(tp) == int or type(tp) == float, 'tip percent argument is not float or int' # assert arguments are correct type, float and int on both arguments in case of bill less than $1 or 100% tip
    assert type(bt) == int or type(bt) == float, 'bill total argument is not float or int'
    assert tp < 1 or bt < 1, 'tip percentage argument not between 0 and 1'                  # assert tip percentage is between 0 and 1 since the arguments in interchangable, only one needs to between 1 and 0
    
    amount_to_tip = tp * bt  # multiply the values that are passed to find amount to tip
    return amount_to_tip     # return amount to tip

calculate_tip(.05, 100)


# In[121]:


# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(op, dp):                # original price (op) and discount percentage (dp) set as parameters
    assert type(op) == int or type(op) == float, 'original price argument is not float or int' # assert arguments are correct type, float and int on both arguments in case original price less than $1 or 100% discount
    assert type(dp) == int or type(dp) == float, 'discount percentage argument is not float or int'
    assert dp >= 0 and dp <= 1, 'discount percentage, dp (right argument), must be between 0 and 1'   # assert discount argument between 0 and 1
    
    price_after_discount = op - (op * dp)  # op * dp to find disc amount then subtracted from op to find disc price
    return(price_after_discount)           # return disc price

apply_discount(50, .1)


# In[136]:


# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(s):   
    assert type(s) == str, 'argument must be in string format' # check that argument type is str
    
    no_commas = float(s.replace("," , ""))   # using .replace to remove commas and int() to convert string to int and store as variable   
    return (no_commas)   # return new variable
 
handle_commas('4,000,000.25') # float type allows decimals to be preserved


# In[143]:


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(i):
    assert type(i) == int or type(i) == float, 'argument must be in int format' # check if argument is int or float type
    
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
    
get_letter_grade(95)


# In[150]:


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(s):
    assert type(s) == str, 'argument must be in str format' # check if argument is str type
    
    no_vowels = ""                            # create empty string
    for letter in s:                          # iterate through string
        if letter.lower() not in 'aeiou':     # check if letter is a vowel
            no_vowels += letter               # if not a vowel, add letter to empty string variable 
    return(no_vowels)               
    
remove_vowels('banana')


# In[149]:


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
    assert type(s) == str, 'argument must be in str format' # check if argument is str type
    
    new_string = (s.strip(" ").lstrip("0123456789").lower().replace(" ", "_"))   # remove whitespace from ends, numbers from left side, lower case all, replace spaces in string with "_"
    string2 = ""                                                      # create empty string
    for c in new_string:
        if c not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":                    # remove special characters
            string2 += c                                              # fill empty string with remaining characters
    return(string2)

normalize_name(' 123R $( )Abc2 ')


# In[154]:


# Write a function named cumulative_sum that 
# accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumalative_sum(l):
    assert type(l) == list, 'argument must be in list format' # check if argument is list type
    running_total = 0                                         # create variable with value of zero
    n = []                                                    # create empty list
    for i in l:
        running_total += i                                    # use iteration to keep running total
        n.append(running_total)                               # append values to empty list by adding running total to i
    return(n)
        
cumalative_sum([1,2,3,4])


# In[135]:


# ~~~~~~~~~~~~~~~~~ BONUS ~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and return a string that is the 
# representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

from datetime import datetime                               # importing datetime for use in function

def twelveto24(t):
    assert type(t) == str, 'argument must be in str format' # check if argument is string type 
    
    time_convert = datetime.strptime(t, "%I:%M%p")          # convert argument to raw 24 hour format
    only_time = datetime.strftime(time_convert, "%H:%M")    # specify format HH:MM 
    return(only_time)

twelveto24("3:45pm")
    


# In[240]:


# Bonus write a function that does the opposite

from datetime import datetime                          # importing datetime for use in function

def twentyfourto12(t): 
    assert type(t) == str, 'argument must be in str format' # check if argument is string type  
    time_convert = datetime.strptime(t,"%H:%M")        # convert to non-24 hour format
    return time_convert.strftime("%I:%M%p").lower()    # specify format HH:MMpm or HH:MMam

twentyfourto12("22:30")


# In[ ]:


"""
Create a function named col_index. 
It should accept a spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27
"""



# In[ ]:






