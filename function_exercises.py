#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Define a function named is_two. It should accept one input and return True if the passed input is either 
# the number or the string 2, False otherwise.

def is_two(x):
    # check if x is a str or int
    assert type(x) == str or type(x) == int, 'argument passed is not a string or integer '  
    
    # if x is not 2 or '2', return false
    if x != 2 and x != '2':                                
        return False
     # if x is 2 or '2', return true with a cool statement
    elif x == 2 or x == '2':                            
        return True

is_two('2')


# In[100]:


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(s):
    # check that argument is a string
    assert type(s) == str, 'argument passed is not a string' 
    
    # create variable that holds list of vowels
    vowels = ",".join('aeiou')
    # create variable that holds list of consonants
    consonants = ",".join('bcdfghjklmnpqrstvwxyz')
    
    # using list of single vowels to ensure double vowels (ae, iu, etc) dont pass check
    if s.lower() in vowels:  
        return True
    # using list of consontants to avoid double consonants being passed as a single consonant in next exercise
    elif s.lower() in consonants:   
        return False   
    # print message telling user they entered a string with multiple characters if neither of the other two conditions are met  
    else:
        return(f'{s} is a string of multiple characters, please pass a single character')
 
is_vowel('u')


# In[86]:


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(s):
    # no assertion line necessary here bc is_vowel already has one  
    # running is_vowel to check if s is a vowel         
    if is_vowel(s) == False:   
        return True
    # returning false if not a consonant
    else:
        return False           
    
is_consonant('v')


# In[107]:


# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_consonant(s):
    # check if argument is a string
    assert type(s) == str, 'argument passed is not a string' 
    
    # check if first letter is a vowel. alternative is to remove .lower and add 'AEIOU' to string 
    if s[0].lower() not in 'aeiou': 
    # return string with capitalized first letter if first letter is a consonant   
        return s.capitalize()  
    # return string as normal if first letter is a vowel     
    else:
        return(s)                  
        
capital_consonant('cat')


# In[112]:


# Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# tip percentage and bill total set as parameters
def calculate_tip(tp, bt):   
    # assert arguments are correct type, float and int on both arguments in case of bill less than $1 or 100% tip
    assert type(tp) == int or type(tp) == float, 'tip percent argument is not float or int' 
    assert type(bt) == int or type(bt) == float, 'bill total argument is not float or int'
    # assert tip percentage is between 0 and 1 since the arguments in interchangable, only one needs to between 1 and 0
    assert tp < 1 or bt < 1, 'tip percentage argument not between 0 and 1'                  
    
    # multiply the values that are passed to find amount to tip
    amount_to_tip = tp * bt
    # return amount to tip  
    return amount_to_tip     

calculate_tip(.05, 100)


# In[121]:


# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

 # original price (op) and discount percentage (dp) set as parameters
def apply_discount(op, dp):                
    # assert arguments are correct type, float and int on both arguments in case original price less than $1 or 100% discount
    assert type(op) == int or type(op) == float, 'original price argument is not float or int' 
    assert type(dp) == int or type(dp) == float, 'discount percentage argument is not float or int'
     # assert discount argument between 0 and 1
    assert dp >= 0 and dp <= 1, 'discount percentage, dp (right argument), must be between 0 and 1'  
    
    # op * dp to find disc amount then subtracted from op to find disc price
    price_after_discount = op - (op * dp)  
    # return disc price
    return(price_after_discount)           

apply_discount(50, .1)


# In[136]:


# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(s):   
    # check that argument type is str
    assert type(s) == str, 'argument must be in string format' 
    
    # using .replace to remove commas and int() to convert string to int and store as variable   
    no_commas = float(s.replace("," , ""))  
    # return new variable 
    return (no_commas)   

# float type allows decimals to be preserved 
handle_commas('4,000,000.25') 


# In[143]:


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(i):
    # check if argument is int or float type
    assert type(i) == int or type(i) == float, 'argument must be in int format' 
    
    # set if and elif statements to return letter grade based on argument passed
    # using int(i) in case grade passed is grade in string form
    if int(i) >= 88:     
        return 'A'       
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
    # check if argument is str type
    assert type(s) == str, 'argument must be in str format' 
    
    # create empty string
    no_vowels = ""                
    # iterate through string            
    for letter in s:            
        # check if letter is a vowel              
        if letter.lower() not in 'aeiou':
            # if not a vowel, add letter to empty string variable      
            no_vowels += letter               
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
    # check if argument is str type
    assert type(s) == str, 'argument must be in str format' 
    
    # remove whitespace from ends, numbers from left side, lower case all, replace spaces in string with "_"
    new_string = (s.strip(" ").lstrip("0123456789").lower().replace(" ", "_"))  
    # create empty string 
    string2 = ""                                                      
    for c in new_string:
        # remove special characters
        if c not in "!@#$%^&*()+=-[]{}\/|?.<>,`~": 
            # fill empty string with remaining characters                   
            string2 += c                                              
    return(string2)

normalize_name(' 123R $( )Abc2 ')


# In[154]:


# Write a function named cumulative_sum that 
# accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumalative_sum(l):
    # check if argument is list type
    assert type(l) == list, 'argument must be in list format' 
      # create variable with value of zero
    running_total = 0                               
    # create empty list        
    n = []                                                    
    for i in l:
         # use iteration to keep running total
        running_total += i   
          # append values to empty list by adding running total to i                                
        n.append(running_total)                             
    return(n)
        
cumalative_sum([1,2,3,4])


# In[135]:


# ~~~~~~~~~~~~~~~~~ BONUS ~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm and return a string that is the 
# representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# importing datetime for use in function
from datetime import datetime                               

def twelveto24(t):
    # check if argument is string type 
    assert type(t) == str, 'argument must be in str format' 
    
    # convert argument to raw 24 hour format
    time_convert = datetime.strptime(t, "%I:%M%p")       
     # specify format HH:MM    
    only_time = datetime.strftime(time_convert, "%H:%M")   
    return(only_time)

twelveto24("3:45pm")
    


# In[240]:


# Bonus write a function that does the opposite

# importing datetime for use in function
from datetime import datetime                          

def twentyfourto12(t): 
    # check if argument is string type 
    assert type(t) == str, 'argument must be in str format' 
    # convert to non-24 hour format 
    time_convert = datetime.strptime(t,"%H:%M")       
    # specify format HH:MMpm or HH:MMam 
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



# In[ ]:






