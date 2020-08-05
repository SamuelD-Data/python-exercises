#!/usr/bin/env python
# coding: utf-8

# In[35]:


# import the module and refer to the function with the . syntax

# import function_exercises
import function_exercises
from function_exercises import is_vowel  

# import is_vowel to determine if string is a vowel
function_exercises.is_vowel('a') 


# In[36]:


# use from to import the function directly

# using from to import handle_commas with no alias
from function_exercises import handle_commas 

# using handle_commas to remove comma from string
handle_commas('3,000.25')                        


# In[37]:


# use from and give the function a different name

# using from to import capital_consonant with alias 'capcon'
from function_exercises import capital_consonant as capcon 

# using capcon function to capitalize argument if it starts with a consonant
capcon('bird')                                             


# In[38]:


# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product # import product from itertools 

# make a list using itertools product to find all combinations and assign to a variable
combo_list = list(product('abc', '123'))    
# count number of combinations in list and assign to variable
combo_count = len(list(product('abc', '123'))) 

# print findings
print(f'as shown below there are {combo_count} different combinations that can be made using ABC and 123\n') 
print(combo_list)


# In[39]:


# How many different ways can you combine two of the letters from "abcd"?

# import itertools
from itertools import combinations 

# calc number of possible combinations using len on list of combinations and store as variable 
combo_count = len(list(combinations('abcd', 2)))

# calc all combinations using itertools combinations
combinations = list(combinations('abcd', 2))

# combinations creates combinations and will not make combinations if a group of values has been used already, even if they change positions
print(f"we can create {combo_count} combinations of letters using abcd\n")
print(combinations)


# In[40]:


# JSON EXERCISES

# importing json
import json

# open json file - assigned to a variable
f = open('profiles.json') 

# read json document from file - stored as variable
data = json.load(f) 


# In[41]:


# Total number of users

# counting number of id values in dictionaries
idcount = len([i['_id'] for i in data]) 

# print our results
print(f'The total number of users is {idcount}') 


# In[42]:


# Number of active users

# counting number of users with isActive status set to True
active = len([i['_id'] for i in data if i['isActive'] == True]) 

# print our results
print(f'The total number of active users is {active}') 


# In[43]:


# Number of inactive users

# counting number of users with isActive status set to False
inactive = len([i['_id'] for i in data if i['isActive'] == False]) 

# print our results
print(f'The total number of inactive users is {inactive}') 


# In[44]:


# Grand total of balances for all users

# Create a variable with value 0
running_total = 0    

# iterate through dictionaries to keep a running total of every balance
# the code that to the right of running total removes the '$' and "," from each balance and then converts it to a float
for x in data:       
    running_total += float(x['balance'].replace(",", '').replace("$", "")) 

# print our results while rounding the total for readability
print(f'The grand total of all balances of all user is {round(running_total, 2)}')  


# In[45]:


# Average balance per user

# stores the number of total accounts
accounts = len([x['_id'] for x in data])    

# set a variable to 0 that will be used to track the total amount of in all acounts
running_total = 0

# Average balance per user via sum of all accounts divided by total number of accounts
# we sum the balance of all acounts after removing '$' and ',' and converting to float
for x in data: 
    running_total += float(x['balance'].replace(",", '').replace("$", ""))

# divide the total balance by the total number of accounts, round to 2 decimals to get the overall average
total_average = round(running_total / accounts, 2)
    
# print our results
print(f'If we divide the sum of all accounts by the number of users, we find the overall average balance to be {total_average}')


# In[46]:


# User with the lowest balance

#assign a variable equal to the lowest balance of all users via list iteration and the min method
lowestbalance = min([x['balance'] for x in data]) 

# assign a variable with the name of the person with the lowest balance found via list iteration
lowbalname = [x['name'] for x in data if x['balance'] == min([x['balance'] for x in data])] 

# print our findings. to avoid the name appearing as list we can specify its place in the range so that the value appears with brackets
print(f"The lowest balance is {lowestbalance}, which belongs to {lowbalname[0]}") 


# In[47]:


# User with the highest balance

# assign a variable equal to the highest balance of all users via list iteration and the min method
highestbalance = max([x['balance'] for x in data]) 

# assign a variable with the name of the person with the highest balance found via list iteration
highbalname = [x['name'] for x in data if x['balance'] == max([x['balance'] for x in data])] 

# print our findings. to avoid the name appearing as list we can specify its place in the range so that the value appears with brackets
print(f"The highest balance is {highestbalance}, which belongs to {highbalname[0]}")


# In[48]:


# Most common favorite fruit

# assign 3 variables to 0. these will be used to keep count of our fruits
s = 0       
b = 0
a = 0

# iterate through the data and each time a fruit is declared a favorite we add 1 to its counter
for x in data:
    if x['favoriteFruit'] == 'strawberry':  
        s += 1
    if x['favoriteFruit'] == 'banana':
        b += 1
    if x['favoriteFruit'] == 'apple':
        a += 1

# create a list of dictionaries. each dictionary stores the names of the fruits and their respective counts
fruits = [{'fruit' : 'strawberry', 'count' : s}, {'fruit' : 'banana', 'count' : b}, {'fruit' : 'apple', 'count' : a}]   

# assign a variable equal to the highest count from our list of dictionaries, fruits
maxfruit = max([x['count'] for x in fruits])  

# create an variable that will keep track of how many fruits are considered the most popular in order to check for ties
popfruit = 0

# iterate through our new dictionary 
# check if the count of a fruit matches the max count in our variable ie. most popular
# for each that is tied for most popular (if there is a tie) add 1 to popfruit
for x in fruits:                
    if x['count'] == maxfruit:  
        popfruit += 1           

# iterate through dictionary again, if there is a tie for most popular fruit, print a statement for each declaring a tie
# otherwise declare the single fruit as the most popular
for x in fruits:
    if x['count'] == maxfruit and popfruit == 1:
        print(f"{x['fruit']} is the most popular fruit among users with {x['count']} preferring it") # we print a statement declaring a fruit as the most popular if popfruit tells us there is only one winner
    if x['count'] == maxfruit and popfruit > 1:
         print(f"{x['fruit']} is tied for the most popular fruit among users with {x['count']} preferring it") # we print a statement for each fruit that is tied for most popular with altered text to reflect the tie


# In[49]:


# Least common fruit

# assign 3 variables to 0. these will be used to keep count of our fruits
s = 0        
b = 0
a = 0

# iterate through the data and each time a fruit is declared a favorite we add 1 to its counter
for x in data:
    if x['favoriteFruit'] == 'strawberry':  
        s += 1
    if x['favoriteFruit'] == 'banana':
        b += 1
    if x['favoriteFruit'] == 'apple':
        a += 1

# create a list of dictionaries. each dictionary stores the names of the fruits and their respective counts
fruits = [{'fruit' : 'strawberry', 'count' : s}, {'fruit' : 'banana', 'count' : b}, {'fruit' : 'apple', 'count' : a}]   

# assign a variable equal to the lowest count from our list of dictionaries, fruits
minfruit = min([x['count'] for x in fruits])  

# create an variable that will keep track of how many fruits are considered the least popular in order to check for ties
unpopfruit = 0

# iterate through our new dictionary 
# check if the count of a fruit matches the min count in our variable ie. least popular
# for each that is tied for least popular (if there is a tie) add 1 to popfruit
for x in fruits:                
    if x['count'] == minfruit:  
        unpopfruit += 1          

# iterate through dictionary again, if there is a tie for least popular fruit, print a statement for each declaring a tie
# otherwise declare the single fruit as the least popular
for x in fruits:
    if x['count'] == minfruit and unpopfruit == 1:
        print(f"{x['fruit']} is the least popular fruit among users with {x['count']} preferring it") # we print a statement declaring a fruit as the least popular if unpopfruit tells us there is only one winner
    if x['count'] == minfruit and unpopfruit > 1:
         print(f"{x['fruit']} is tied for the least popular fruit among users with {x['count']} preferring it") # we print a statement for each fruit that is tied for least popular with altered text to reflect the tie


# In[50]:


# Total number of unread messages for all users

# use list iteration and .strip to remove all non-numeric characters from each unread message and assign to a variable
msgnumbers = [int(x['greeting'].lower().strip("abcdefghijklmonpqrstuvwxyz!,. ")) for x in data if 'unread' in x['greeting']] 

# sum the total number of messages and assign to a variable
totalmsgs = sum(msgnumbers) 

# display results
print(f'there are a total of {totalmsgs} unread messages for all users') 


# In[ ]:





# In[ ]:




