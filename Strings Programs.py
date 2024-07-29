
#1.	    Python program to remove given character from String.

"""
x="VIDYASHREE"
index=3
print("Given String is",x)
resultstr=""
print("Length of the String is",len(x))
for i in range (0,len(x)):
	if i!=index:
		resultstr=resultstr+x[i]
print("Result after removing String is",resultstr)

y="GREEN SOUL"
z=y[:-1]
print("after Removing character is",z)


a="LOHITVIDYA"
b=a.rstrip("A")
print("after removing",b)

c="MONKEY LOHIT"
d=""
for i in range(len(c)-1):
	d+=c[i]
print("After removing",d)


e="MONKEY LOHIT"
last_suffix="T"
if e.endswith(last_suffix):
	e=e.replace(last_suffix,"")
	print("After deleting ",e)
	
	"""
	
#2.	    Python Program to count occurrence of a given characters in string.

#Using Native Method
"""x="GeeksofGeeks"
count=0
for i in x:
	if i=="e":
		count=count+1
print("Count of e in GeeksforGeeks is  " + str(count))"""

#Using Count() Method
"""y="GeeksofGeeks"
counter=y.count('e')
print("count the number of e is :"+ str(counter))
"""
#Using Collections.Counter() Method
"""y="GeeksofGeeks"
counter=sum(map(lambda x: 1 if 'e' in x else 0,y))
print("countmm the number of e is :"+ str(counter))"""

#Using Lambda Functions
#Using Regular Expressions
#Using Operator.countOf() Method
#Using Reduce() Method




#3.	    Python Program to check if two Strings are Anagram.
# Using sorted() function
"""def check(s1, s2):
	
	if (sorted(s1) == sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")

s1 = "listen"
s2 = "silent"
check(s1, s2)"""



 #Using Counter() function
"""from collections import Counter

def check(str1,str2):
	if(Counter(str1)==Counter(str2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")
		
str1 = "listen"
str2 = "silent"
check(str1, str2)
"""

#4.	    Python program to check a String is palindrome or not.
#Using the reverse and join method

"""def isPalindrome(string):
	revstr="".join(reversed(string))
	if revstr==string:
		return "The string is Palindrome"
		return "The string is not Palindrome"
string=input("Enter the input")

print(isPalindrome(string))
"""
#Using the for loop method

"""string=input("Enter the input")
revstr=""
for i in string:
	revstr=i+revstr
	print("revsersed string is ",revstr)
	if revstr==string:
		print("string is palindrome")
	else:
		print("the string is not palindrome")"""

#Using the reverse and compare method
"""def isPalindrome(string):
	if(string==string[::-1]):
		return "string is palindrome"
	else:
		return"sting is not palindrome"
string=input("enter the string")
print(isPalindrome(string))
	"""
	

#5.	    Python program to check given character is vowel or consonant.
"""def vowelOrConsonant(x):
	if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
		print("vowel")
	else:
		print("consonants")
vowelOrConsonant('x')
vowelOrConsonant('e')
		"""
		
#6.	    Python program to check given character is digit or not.
"""ch=input("Enter the input")
if(ch.isdigit()):
	print("the given character",ch,"is digit")
else:
	print("the character",ch,"is not digit")"""

#7.	    Python program to check given character is digit or not using isdigit() method.


#8.	    Python program to replace the string space with a given character.

"""s="Good Morning"
new_string=s.replace(' ','-')
print(new_string)
"""
"""s="Good Morning"
s=s.replace(' ','_')
print(s)"""

"""s= "India is my country"
s=s.replace(' ','_',2)
print(s)"""

#9.	    Python program to replace the string space with a given character using replace() method.
#10.	Python program to convert lowercase char to uppercase of string.

"""string=input("Enter the string")
new_string=string.upper()
print(new_string)"""

#11.	Python program to convert lowercase vowel to uppercase in string.

"""vowel='a' 'e' 'i' 'o' 'u'
vowel=vowel.upper()
print(vowel)"""

"""string=input("Enter the input")
vowels='aeiou'
for character in string:
	if character in vowels:
		new=character.upper()
		string=string.replace(character,new)
print("Updated String is",string)"""

#12.	Python program to delete vowels in a given string.

"""string=input("Enter the vowels")
vowels=['a','e','i','o','u']
result=""
for char in string:
	if char not in vowels:
		result=result+char
print("vowels removed string",result)
"""

#13.	Python program to count the Occurrence Of Vowels & Consonants in a String.

"""str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1
    else:
        consonants=consonants+1
#consonant counter is incremented by 1
print("The number of vowels:",vowels)
print("\nThe number of consonant:",consonants)"""


#14.	Python program to print the highest frequency character in a String.
"""from collections import Counter
string=input("enter the string")
result=Counter(string)
result=max(result,key=result.get)
print("frequency character",result)"""




#15.	Python program to Replace First Occurrence Of Vowel With ƒ_~-ƒ_~ in String.
#16.	Python program to count alphabets, digits and special characters.

"""string=input("Enter the input")
alphabets=0
digits=0
specialChars=0
for i in string:
	if i.isalpha():
		alphabets+=1
	elif i.isdigit():
		digits+=1
	else:
		specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)"""

		


#17.	Python program to separate characters in a given string.

"""string="GeeksofGeeks"
list=[]
list.extend(string)
print(list)

string="vidyashree"
list=[x for x in string]
print(list)

string="lohit"
list=[]
list[:]=string
print(list)"""


#18.	Python program to remove blank space from string.

"""string=" G E E K S"
result=string.replace(" ","")
print(result)


string="V i d y a"
string=''.join(list(map(lambda x:x .strip(),string.split())))
print(string)
"""
#19.	Python program to concatenate two strings using join() method.

"""str1=input("enter the first string")
str2=input("enter the second string")
result=''.join([str1,str2])
print("concatenate two strings is",result)"""

#20.	Python program to concatenate two strings without using join() method.
"""str1="vidya"
str2="shree"
result=str1+str2
print(result)
print("%s %s" %(str1,str2))
x="{} {}".format(str1,str2)
print(x)
print(str1,str2)"""

#21.	Python program to remove repeated character from string.

"""string= "GeeksofGeeks"
p=""
for char in string:
	if char not in p:
		p=p+char
print(p)"""

#22.	Python program to calculate sum of integers in string.

"""import re
def find_sum(str1):
	return sum(map(int, re.findall('\d+', str1)))
str1 = "12abc20yz68"
print(find_sum(str1))
"""

#23.	Python program to print all non repeating character in string.



#24.	Python program to copy one string to another string.

"""string=input("enter the string")
result=str(string)
print(result)
result=string[:]
print(result)"""

#25.	Python Program to sort characters of string in ascending order

"""string="Vidyashree"
strlst=list(string)
sortedstring=''.join(sorted(strlst))
print(sortedstring)
"""
#26.	Python Program to sort character of string in descending order.

"""string="Vidyashree"
strlst=list(string)
sortedstring=''.join(sorted(strlst,reverse=True))
print(sortedstring)"""

#27.Python program to print words with their length of a string

"""def splitString(str):
    str = str.split(" ")
    for words in str:
        print(words, " (", len(words), ")")
str = "Hello How are you?"
splitString(str)"""

#28 print the EVEN length words

"""string="Python is a Programming Language"
words=list(string.split(" "))
print(words)
for w in words:
	if len(w)%2==0:
		print(w)"""
#29 Python program to count vowels in a string

"""str = "Hello world"
count = 0
for i in str:
    if (
        i == "A"
        or i == "a"
        or i == "E"
        or i == "e"
        or i == "I"
        or i == "i"
        or i == "O"
        or i == "o"
        or i == "U"
        or i == "u"
    ):
        count += 1
print("Total vowels are: ", count)"""

# 30 Python program to pass a string to the function

"""def printstrfun(str):
	print(str)
printstrfun("Hello world!")
printstrfun("Hi! I am good.")"""

# 31 Python program to find the length of a string (different ways)

"""mystr= input("enter the string")
result=len(mystr)
print(result)


strlen=0
for i in mystr:
	strlen =strlen+1
print(strlen)

while mystr[strlen:]:
	strlen=strlen +1
print(strlen)"""

#31 Python program to find the least frequent character in the string  or doubt

"""myStr =  input('Enter the string : ')
freq = {}
for i in myStr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
leastFreq = min(freq, key = freq.get)
print("Entered String is ", myStr)
print(leastFreq , "is the least frequent character with frequency of " , freq[leastFreq])
		"""

#32 Program to split and join a string

"""str=input("Enter the string")
separater=input("Enter the string")

str=str.split(' ')
joined=separater.join(str)
print(str)
print(joined)"""

"""#33

str=input("enter the input")
vowels=0
for i in str:
	if (i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U' ):
		vowels +=1
print(vowels)"""




