myInt = 3       # Stores a number that isnt a decimal
myFloat = 3.4     # Stores a number that is a decimal
myString = "Quinn"  # Stores characters and text
myBool = False      # Its a switch
myList = [myString, myInt, myFloat]     # A collection of other data types

Birds = ['robin, quail, swan, duck, ostridge'] # A string 

print (myList[2]) # it will print the 3rd thing in the list, cause 0
print (Birds[-1]) # it will print the last thing in birds


x = 3
y = 4


sum = x * y # multiplying toghether
difference = x / y # dividing

print(myString + " is cool" * 3)

print(myString * myBool) # false = 0, true = 1, so in coding it works

print(f"good mornin {myString} how are you")

name = 'World'
for character in name:
     print(character) # this will write anything vertically

# when needing to do something like this 'W    W
#                                         o    o
#then writ print(char +'   ' + char) 

if True                         # this is an if state ment that will occur depending on if the condition is met
    
     condition = True
     print('This gets printed'/)

sentence = 'Hello World'

include = False  # since false isnt here for the first loop, it doesnt produce H
new_sentence = ''
for char in sentence:
    if include:
        new_sentence += char
    include = True #and is true for the rest, producing "ello World"

print(new_sentence)


sentence.upper # means if true will make the sentence uppercase
sentence.lower # means if true will make the sentence lowercase

if excited:
    sentence += '!'  
else:                # else means if false then output:
    sentence += '.'  # whatever here
print(sentence)

sentence = 'Hello world' # this code makes 'H' always upper
j = ''  
excited = True
for i in sentence:
    if excited:
        j += i.upper()
        excited = False
    else: 
        j+= i.lower()   # and 'ello world' always lower

print(1 +2 ==3) # True)    the code will tell you if it is true or false
print(4 + 5 == 6) # False) even without having to code it
print('ab' + 'c' =='a' + 'bc') #True)

#sentence = 'The e key on my keyboard is broken'
#new_sentence = '' 
#for c in sentence:
#    if c != 'e':, means if c is true (which its not), 'e' = '' which is nothing
#        new_sentence += c
#print(new_sentence), meaning print will print: th ky on my kyboard is brokn

# '>' and '<' can be used to ask which variable is bigger and how long a string is
# -for example 3<4, 2>3, and new_sentence<sentence

x1 = 30
x2 = 10
x3 = 20

#if x1 < x2 and x1 < x3:, honestly and is the most important thing to note is and will work in if statements
    #print(x1)
#elif x2 < x3:
#    print(x2)
#else:
#    print(x3)
# numbers = [3,1,4,1,5,9]
    
#total = 0
#for number in numbers:
#    total += number, this means that 

#print (total)

#numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

#big_numbers = []
#for number in numbers:
#    if number > 5:
#        big_numbers.append(number)
#print(big_numbers)



found = False
for thing in things:
    if thing == thing_to_find:
        found = True

print(found)

things = ['on','the', 'way', 'to', 'the', 'store']
to_find = 'the'
found = False
for i in range(len(things)):
    if things[i] == to_find and found == False:
        found = True
        print(i)
    



    #for i in range(len(string1)):, is saying for i in length of string1 which in this case is (0,5)

    #print(string1[i] + ' ' + string2[i]), 


#string1 = 'Goodbye'
#string2 = 'World' 

#if len(string1) < len(string2):
#    difference = len(string2) - len(string1)      
#    string1 += ' ' * difference 
#else:
#    difference = len(string1) - len(string2)
#   string2 += ' ' * difference 
#for i in range(len(string2)):
  

#    char2 = string2[i]
#   char1 = string1[i]  
#    print(char1 + ' ' + char2)

#x = ['a', 'b', 'c']
#y = x + [x[0]], creates a new list through concontanating
#print(y)
 