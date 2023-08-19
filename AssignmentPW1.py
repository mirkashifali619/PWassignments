#!/usr/bin/env python
# coding: utf-8
Q1. Create one variable containing following type of data: (i) string (ii) list (iii) float (iv) tupleANS:(i)
# In[1]:


variable_name = "Mir Kashif Ali"
print("My name is", variable_name)
print(type(variable_name))

ANS:(ii)
# In[2]:


variable_details = [ "kashif" , 1 ,2, 3, 4 ,5 ,6]
print(variable_details)
print(type(variable_details))

ANS:(iii)
# In[3]:


variable_weights = 82.5
print("My weight is" , variable_weights)
print(type(variable_weights))

ANS:(IV)
# In[4]:


variable_std = ("Mir Ali" , "3rd year" , 15)
print("Student name is" , variable_std[0])
print("Student year is" , variable_std[1])
print("Student roll no. is" , variable_std[2])
print(type(variable_std))

Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.ANS(i) var1 = ‘ ‘= Sting data type
ANS(ii)  var2 = ‘[ DS , ML , Python]’ =  Sting data type
ANS(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ] = List data type
ANS(iv) var4 = 1 = INT data typeQ3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **ANS:(i) / = This operator is used for divison between data types
(ii) % = This operator is used for finding the remainder 
(ii) // = in Python, the double forward slash // is the floor division operator. It is used for performing division where the result should be the largest integer less than or equal to the quotient of the division. In other words, it performs division and truncates the decimal part of the result.
(iv) ** = In Python, the double asterisk ** is the exponentiation operator. It is used to raise a number to a certain power.Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
# In[5]:


details_lists = [1 ,2 ,3 ,4,5.5,6,7,"a" , 9 , 10]
for i in details_lists:
    print(i , type(i))

Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
# In[1]:


# Input two numbers A and B
A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))

# Initialize a counter to keep track of how many times A can be divided by B
count = 0

# Use a while loop to check divisibility and count
while A % B == 0:
    A = A / B
    count += 1

# Check if A can be purely divided by B
if A == 1:
    print(f"{A} can be purely divided by {B} {count} times.")
else:
    print(f"{A} cannot be purely divided by {B}. The remainder is {A}.")
    
    

Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.
# In[18]:


list_data = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
for i in list_data:
    if i%3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 3")

Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.Mutable and immutable data types are terms used in computer science and programming to describe whether the data stored in a variable can be changed after it has been created.

Immutable Data Types:
Immutable data types are those whose values cannot be modified after they are created. Any operation that appears to modify an immutable data type actually creates a new value with the modified content. Immutable data types are often considered safer and more predictable because they prevent accidental changes.

Examples of immutable data types:

Strings: In most programming languages, strings are immutable. When you perform operations like concatenation or substring extraction, you create new string objects rather than modifying the original one.
Mutable Data Types:
Mutable data types are those whose values can be modified after they are created. This means you can change the content of the variable without creating a new object.

Examples of mutable data types:

Lists: Lists in Python are mutable. You can add, remove, or modify elements within a list.
Dictionaries: Dictionaries in Python are also mutable. You can add, remove, or update key-value pairs.