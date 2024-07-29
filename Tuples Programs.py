#1.	Write a program to reverse an integer in Python

"""number= int(input("Enter the number"))
revs_number=0
while number > 0:
    remainder= number%10
    revs_number=(revs_number * 10) +remainder
    number=number//10
    print("The reverse number is:{}".format(revs_number))"""

#2.	Write a program in Python to check whether an integer is Armstrong number or not

"""num = int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    digit= temp %10
    sum+=digit**3
    temp//=10
    if num == sum:
        print(num,"is an amstrong number")
    else:
        print(num,"is not a amstrong number")
"""
#3.	Write a program in Python to check given number is prime or not.

"""num = int(input("Enter the number:"))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""

#4.	Write a program in Python to print the Fibonacci series using iterative method.

"""n=int(input("Enter the number"))
first,second=0,1
print("fibonacci series are:")
for i in range(0,n):
    if(i<=1):
        result=i
    else:
        result=first+second
        first=second
        second=result
        print(result)"""

#5.	Write a program in Python to print the Fibonacci series using recursive method.

"""n = int(input("please give a number for fibonacci series : "))
first,second=0,1
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("fibonacci series are : ")
for i in range(0,n):
    print(fibonacci(i))
"""
#6.	Write a program in Python to check whether a number is palindrome or not using iterative method.

"""n = int(input("please give a number : "))
reverse,temp = 0,n
while temp!=0:
    reverse = reverse*10 + temp%10;
    temp=temp//10;
if reverse==n:
    print("number is palindrom")
else:
    print("number is not palindrom")"""


#7.Write a program in Python to check whether a number is palindrome or not using recursive method

"""n = int(input("please give a number : "))
def reverse(num):
    if num<10:
      return num
    else:
      return int(str(num%10) + str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome")
"""

#8.	Write a program in Python to find greatest among three integers.

"""num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)"""


#9.	Write a program in Python to check if a number is binary?


"""num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary") 
"""

#10.	Write a program in Python to find sum of digits of a number using recursion?

"""def sum_of_digits(n):
    if n==0:
        return 0
    return (n%10+sum_of_digits(int(n/10)))
num=int(input("Enter the number:"))
result=sum_of_digits(num)
print("Sum of digits",num,"is",result)"""

#11.	Write a program in Python to swap two numbers without using third variable?

"""a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
a=a-b
b=a+b
a=b-a

print("after swapping:")
print("Value of a is:",a)
print("Value of b is:",b)"""

#12.	Write a program in Python to swap two numbers using third variable?

"""a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
k=a
a=b
b=k

print("Value of a & b after swapping is:",a, "and",b,"respectively")"""


#13.	Write a program in Python to find prime factors of a given integer.


#14.	Write a program in Python to add two integer without using arithmetic operator?


#15.	Write a program in Python to find given number is perfect or not?

"""n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")"""

#17.	Python Program to calculate factorial using iterative method.
"""def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        facr=1
        while(n>1):
            fact *=n
            n-=1
            return fact
        num =int(input("Enter the number:"))
        print("factoril of",num,"is",factorial(num))
"""

#18.	Python Program to calculate factorial using recursion
"""def factorial(n):
    if (n == 1 or n == 0):
                return 1
            else:
                return (n * factorial(n - 1))
        num = int(input("Enter the number:"))
        print("number : ", num)
        print("Factorial : ", factorial(num))
"""

#19.	Python Program to check a given number is even or odd

"""num=int(input("Enter the number:"))
if num%2==0:
    print()"""
#22.	Python Program to find Smallest number among three.

"""n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
n3=float(input("Enter the third number:"))
my_list=[n1,n2,n3]
smallest=min(my_list)
print("The smallest number is",smallest)
"""

#26.	Python Program to calculate the square of a given number.

"""num=int(input("Enter the number:"))
square=num*num
square=num**2
square=pow(num,2)
print(square)"""
#27.	Python Program to calculate the cube of a given number.

"""num=int(input("Enter the number:"))
cube=num*num*num
print("cube of {0} is {1}".format(num,cube))
"""

#28.	Python Program to calculate the square root of a given number.


"""import math
num=int(input("Enter the number"))
SqRoot=math.sqrt(num)
print(f"the square root of {num}is",SqRoot)"""

#29.	Python program to calculate LCM of given two numbers.

"""num1=int(input("Enter the n1 number:"))
num2=int(input("Enter the n2 number:"))
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)
"""
#30.	Python Program to find GCD or HCF of two numbers.

"""num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
gcd=1
for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of",num1, "and",num2 ,"is", gcd)
"""


#31.	Python Program to find GCD of two numbers using recursion.

"""
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)"""

#32.	Python Program to Convert Decimal Number into Binary.

"""def decimalToBinary(num):

    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
    
number = int(input("Enter any decimal number: "))

decimalToBinary(number)
"""
#33.	Python Program to convert Decimal number to Octal number.

"""decimal = int(input("Enter the decimal:"))
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")
    """
#34.	Python Program to check the given year is a leap year or not.

"""year=int(input("Enter the year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is leap year")
else:
    print("The year is not leap year")

"""


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



#1 Python3 program to swap first and last element of a list

"""def swapnumbers(newList):
	size=len(newList)
	temp=newList[0]
	newList[0]=newList[size-1]
	newList[size-1]=temp
	return newList
newList=[1,2,3,4,5]
print(swapnumbers(newList))
"""


#2 Python Program to Swap Two Elements in a List

"""def swapnumbers(list,pos1,pos2):
	list[pos1],list[pos2]=list[pos2],list[pos1]
	return list
list=[1,2,3,4,5]
pos1,pos2=1,3
print(swapnumbers(list, pos1, pos2))"""


#3 Python3 code to demonstrate Swap elements in String list using regex

"""list=['vidya', 'is' ,' a', 'good' ,'gril','but' ,'her','husband','is','a','bad','boy']
print("Original string is ",str(list))
res=[sub.replace('G','-').replace('e','G').replace('-','e') for sub in list]
print("result string is",str(res))
"""

#4 How To Find the Length of a List in Python

"""list=[1,2,3,4,5,6]
listlen=len(list)
print(listlen)


counter = 0
for i in list:
	counter=counter+1
print("lenght of the counter is",str(counter))

test_list = [1, 4, 5, 7, 8]
length = sum(1 for _ in test_list)
print("Length of list using list comprehension is:", length)"""

#5 Find Maximum of two numbers in Python

"""a=2;b=4
max=lambda a,b:a if a>b else b
print(f'{ max(a,b)} is  a max number')
"""

#6 Find Minimum of two numbers in Python

"""a=3;b=1
min=lambda a,b:a if a<b else b
print(f'{min(a,b)} is a min number')"""

#7 Check if element exists in list

"""list=[1,2,3,4,5,6]
i=9
for i in list:
	print("exists")
else:
	print("not exists")"""
	
#8 Different ways to clear a list in Python

"""list=[1,2,3]
list.clear()
print(list)"""

#9 Reversing a List in Python

"""def reverse(lst):
	new_list=lst[::-1]
	return new_list
lst=[1,2,3,4]
print(reverse(lst))


lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reversed() ", list(reversed(lst)))


original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
            for i in range(1, len(original_list)+1)]
print(new_list)
"""


#10  Cloning or Copying a list

"""def Cloning(li1):
	li_copy = li1[:]
	return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)"""


"""def Cloning(li1):
	li_copy = [i for i in li1]
	return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""

#11 Count Occurrences of Item in Python List

"""def Cloning(lst1):
	lst_clon=[i for i in lst1]
	return lst_clon
lst1=[1,2,3,4]
lst2=Cloning(lst1)
print(lst2)
"""


#12 Find sum and average of List in Python

"""list=[13,5,4]
count=0
for i in list:
	count+=i
	avg=count/len(list)
print("the of avg",avg)
print("the sum of sum",count)
"""

"""from functools import reduce
lst=[1,23,5]
count=reduce(lambda x,y:x+y,lst)
avg=count/len(lst)

print("sum of",count)
print("avg of",avg)"""
#13 Python  Sum of number digits in List doubt

"""lst=[1,2,3]
print("the original list",str(lst))
res=list(map(lambda ele: sum(int(sub) for sub in str (ele)),lst))
print(str(res))"""



#14 Python3 program to multiply all values in the list using lambda function and reduce()


"""from functools import reduce

list1=[1,2,3]
list2=[12,28,3]
results1=reduce((lambda x,y:x*y),list1)
results2=reduce((lambda x,y:x*y),list2)
print(results1)
print(results2)"""

#15 Sorting the list to find smallest number in a list

"""list1=[1,2,3,4]
list1.sort()
print("smallest number in a list is",list1[0])

list1.sort(reverse=True)
print("smallest number in a list is",list1[-1])
"""

#16 Sorting the list to find largest number in a list

"""list1=[1,2,3,4]
list1.sort()
print("largest number in a list is",list1[-1])"""

#17 Python program to find second largest number in a list

"""list1 = [10, 20, 120, 4, 9, 199]

#list2 = list(set(list1))
#list2.sort()

print("Second largest element is:", sorted(list1)[-2])"""


#18 Python program to print even numbers in a list
"""list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
	if num % 2 == 0:
		print(num, end=" ")
"""

#19 Python program to print odd numbers in a list

"""list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
	if num % 2 != 0:
		print(num, end=" ")"""
	
#20 Python program to print all even numbers in a range

"""start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
	if num % 2 == 0:
		print(num, end=" ")"""
		
#21 Python program to print all odd numbers in a range

"""start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
	if num % 2 != 0:
		print(num, end=" ")"""
		
#22 Python program to count Even and Odd numbers in a List

"""list=[1,22,34,45,67,85,98,74,3,7]

even_count,odd_count=0,0
for num in list:
	if num % 2 == 0:
		even_count +=1
	else:
		odd_count +=1
print("even count",even_count)
print("odd count",odd_count)
"""

#23 Python program to print positive numbers in a list

"""list1 = [-10, -21, -4, 45, -66, 93]

pos_no = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", pos_no)"""

#24 Python program to print negative numbers in a list

"""list1 = [-10, -21, -4, 45, -66, 93]

pos_no = [num for num in list1 if num < 0]

print("Negative numbers in the list: ", pos_no)"""

#25 Python program to print all positive numbers in a range

"""start,end=4,98
for num in range(start,end + 1):
	if num >=0:
		print(num, end=" ")
		"""
		
#26 Python program to print all negative numbers in a range

"""start, end = -4, 98
for num in range(start, end + 1):
	if num <= 0:
		print(num, end=" ")
		"""
#27 Python program to count positive and negative numbers in a list

"""list1 = [-10, -21, -4, -45, -66, -93, 11]

only_pos = [num for num in list1 if num >= 1]
pos_count = len(only_pos)

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", len(list1) - pos_count)
"""

#28 Python program to remove multiple

"""list1 = [11, 5, 17, 18, 23, 50]
list1 = [elem for elem in list1 if elem % 2 != 0]

print(*list1)"""

#29 Remove empty tuples from a list

"""def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))"""


#30 Program to print duplicates from a list of integers

"""from collections import Counter

l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)"""



#############################################################

#1 Sort Python Dictionaries by Key or Value

"""myDict = {'aavi': 10, 'rajnish': 9, 'kanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys=list(myDict.keys())
myKeys.sort()

sorted_dict={i:myDict[i] for i in myKeys}
print(sorted_dict)
"""

#2 Handling missing keys in Python dictionaries

"""ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
	print(ele["d"])
else:
	print("Key not found")"""

#3 Python dictionary with keys having multiple inputs
#4 Python program to find the sum of all items in a dictionary
"""def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))"""

#5 Python program to find the size of a Dictionary

"""import sys

dict1={"A":"Apple","B":"banana","C":"Orange"}
dict2={1:"A",2:"B",3:"O"}
dict3={"A":12,"B":7,"C":9}
dict4 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}

print("Size of dic1: " + str(sys.getsizeof(dict1)) + "bytes")
print("size of dic2:"+ str(sys.getsizeof(dict2))+"bytes")
print("size of dic3:"+ str(sys.getsizeof(dict3))+"bytes")
print("size of dic4:"+ str(sys.getsizeof(dict4))+"bytes")
"""


#6 Ways to sort list of dictionaries by values in Python – Using itemgetter

"""from operator import itemgetter

list=[{"name":"vidya","age": 7},
      {"name":"divya","age": 17},
      {"name":"ramya","age": 27}
]
print("list printed sorting by name")
print(sorted(list,key=itemgetter("name")))
print("\r")

print("list printed sorting by age and name")
print(sorted(list,key=itemgetter("age","name")))
print("/r")


print("print the list by age in desecending order")
print(sorted(list,key=itemgetter("age"),reverse=True))

"""
#7 Ways to sort list of dictionaries by values in Python – Using lambda function

list=[{"name":"vidya","age":20},
      {"name":"kavya","age":12},
      {"name":"neha","age":11}
      ]
print("list printed sorting by age")
print(sorted(list,key=lambda i: i['age']))
print("\r")

print("list printed sorting by age and name")
print(sorted(list,key=lambda i:(i['name'],i['age'])))
print("\r")

print("list printed desending order by age ")
print(sorted(list,key=lambda i:i['age'],reverse=True))



#8 Python | Merging two Dictionaries

"""def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1={"a":12,"b":45,"c":88}
dict2={"d":34,"e":67,"f":1}

print(Merge(dict1,dict2))
print(dict2)"""


#9 Program to create grade calculator in Python
print("Enter the marks obtained")
total1=56
total2=76
total3=63
total4=84
total5=55
total=total1+total2+total3+total4+total5
avg=total/5

if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
	

#10 Python – Insertion at the beginning in OrderedDict

"""def list_comprehension():
    num1=[1,2,3]
    num2=[9,10,5,6]
    
    num3=[x for n in (num1,num2) for x in n]
    print(num3)
list_comprehension()"""




list1 = [1,2,3,4,5]
list2= [10,20,30,40,50,60]
#Using stack
sorted_list =[]
while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))
sorted_list += list1
sorted_list += list2
print(sorted_list)









