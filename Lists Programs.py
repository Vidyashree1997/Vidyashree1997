


#4 How To Find the Length of a List in Python

list=[1,2,3,4,5,6]
listlen=len(list)
print(listlen)


counter = 0
for i in list:
	counter=counter+1
print("lenght of the counter is",str(counter))

test_list = [1, 4, 5, 7, 8]
length = sum(1 for _ in test_list)
print("Length of list using list comprehension is:", length)

#5 Find Maximum of two numbers in Python

a=2;b=4
max=lambda a,b:a if a>b else b
print(f'{ max(a,b)} is  a max number')


#6 Find Minimum of two numbers in Python

a=3;b=1
min=lambda a,b:a if a<b else b
print(f'{min(a,b)} is a min number')

#7 Check if element exists in list

list=[1,2,3,4,5,6]
i=9
for i in list:
	print("exists")
else:
	print("not exists")
	
#8 Different ways to clear a list in Python

list=[1,2,3]
list.clear()
print(list)

#9 Reversing a List in Python

def reverse(lst):
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

#10  Cloning or Copying a list

def Cloning(li1):
	li_copy = li1[:]
	return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


def Cloning(li1):
	li_copy = [i for i in li1]
	return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


#11 Count Occurrences of Item in Python List

def Cloning(lst1):
	lst_clon=[i for i in lst1]
	return lst_clon
lst1=[1,2,3,4]
lst2=Cloning(lst1)
print(lst2)



#12 Find sum and average of List in Python

list=[13,5,4]
count=0
for i in list:
	count+=i
	avg=count/len(list)
print("the of avg",avg)
print("the sum of sum",count)


"""from functools import reduce
lst=[1,23,5]
count=reduce(lambda x,y:x+y,lst)
avg=count/len(lst)

print("sum of",count)
print("avg of",avg)"""
#13 Python  Sum of number digits in List doubt

lst=[1,2,3]
print("the original list",str(lst))
res=list(map(lambda ele: sum(int(sub) for sub in str (ele)),lst))
print(str(res))

#14 Python3 program to multiply all values in the list using lambda function and reduce()

from functools import reduce

list1=[1,2,3]
list2=[12,28,3]
results1=reduce((lambda x,y:x*y),list1)
results2=reduce((lambda x,y:x*y),list2)
print(results1)
print(results2)

#15 Sorting the list to find smallest number in a list

list1=[1,2,3,4]
list1.sort()
print("smallest number in a list is",list1[0])

list1.sort(reverse=True)
print("smallest number in a list is",list1[-1])


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

# 1 Python program to swap(interchange) first and last element of a list
# Approach1: Find the length of the list and simply swap the first element with (n-1)th element.
"""def swaplist(givenlist):
	size=len(givenlist)

	temp=givenlist[0]
	givenlist[0]=givenlist[size-1]
	givenlist[size - 1]=temp

	return givenlist
givenlist=[1,2,3,4,5]
print(swaplist(givenlist))"""

# Approach2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].
"""def swaplist(givenlist):
	givenlist[0],givenlist[-1]=givenlist[-1],givenlist[0]
	return givenlist
givenlist=[21,22,23,24,25]
print(swaplist(givenlist))"""

# Approach3: Swap the first and last element is using tuple variable. Store the first and last element as a pair in a tuple variable, say get,
# and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped.

"""def swaplist(givelist):

	get=givenlist[0],givenlist[-1]
	givenlist[-1],givenlist[0]=get

	return givenlist

givenlist=[111,222,333,444,555]
print(swaplist(givenlist))"""

# Approach 5: Swap the first and last elements is to use the inbuilt function list.pop(). Pop the first element and store it in a variable.
# Similarly, pop the last element and store it in another variable.  Now insert the two popped element at each other’s original position.

"""def swaplist(givenlist):
	first=givenlist.pop(0)
	last=givenlist.pop(-1)

	givenlist.insert(0,last)
	givenlist.append(first)
	return givenlist
givenlist=[91,92,93,94]
print(swaplist(givenlist))
"""
# Approcoach5:  Using * operand. This operand proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name
# which will be assigned a list of all items not assigned to a “regular” name.

"""def swaplist(givenlist):
	start,*middle,end=givenlist
	givenlist=[end,*middle,start]

	return givenlist
givenlist=[123,345,567,789,910]
print(swaplist(givenlist))"""

# Approach6 : Using slicing

"""def swap_first_last_3(lst):
	if len(lst) >= 2:
		lst = lst[-1:] + lst[1:-1] + lst[:1]
		return lst
inp=[12, 35, 9, 56, 24]
print(swap_first_last_3(inp))"""

# 2 Python Program to Swap Two Elements in a List

# Approach1: Swap Two Elements in a List using comma assignment

"""def swaplist(list,pos1,pos2):
	list[pos1],list[pos2]=list[pos2],list[pos1]
	return list
list=[1,2,3,4,5]
pos1,pos2=(1,3)
print(swaplist(list, pos1-1, pos2-1))
"""

# Approach2: Using Inbuilt list.pop() function to Swap Two Elements in a List

"""def swapPositions(list, pos1, pos2):

	first_ele = list.pop(pos1)
	second_ele = list.pop(pos2 - 1)

	list.insert(pos1, second_ele)
	list.insert(pos2, first_ele)
	return list

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))"""

# Approach3: Swap Two Elements in a List Using tuple variable

"""def swaplist(list,pos1,pos2):

	get=list[pos1],list[pos2]
	list[pos2],list[pos1]=get
	return list
newlist=[89,99,44,33]
pos1,pos2=1,3
print(swaplist(newlist,pos1-1,pos2-1))"""

# Approach4: Swap Two Elements in a List Using temp variable
"""def swaplist(list,pos1,pos2):

	temp=list[pos1]
	list[pos1]=list[pos2]
	list[pos2]=temp
	return list
lis=[1,2,3,4,5]
pos1,pos2=1,3
print(swaplist(lis,pos1-1,pos2-1))"""

# Approach5: Swap Two Elements in a List Using enumerate.
"""def swapPositions(lis, pos1, pos2):
	for i, x in enumerate(lis):
		if i == pos1:
			elem1 = x
		if i == pos2:
			elem2 = x
	lis[pos1] = elem2
	lis[pos2] = elem1
	return lis

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))"""

# 3)  Python program to Swap elements in String list.

# Approach1: Using replace() + list comprehension
"""test_list=['Gfg','is','best','for','Geeks']
print("The original list:"+str(test_list))
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
print("The given list:"+str(res))
"""
# Approach2: Using join() + replace() + split()
"""test_list=["Gfg",'is','best','Geeks']
print("The original list:"+str(test_list))
res=", ".join(test_list)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')
print("The Given String:"+str(res))"""

# Approach3: Using regex
"""import re
test_list=['Gfg','is','best','Geeks']
print("Original list:"+str(test_list))
res = [re.sub('-', 'e', re.sub('e', 'G', re.sub('G', '-', sub))) for sub in test_list]
print("The given list:"+str(res))
"""

# 4)   sum and average of list
# Approach1: Naive method
"""L=[1,2,3,4,5,6]
count=0
for i in L:
	count +=i
	avg=count/len(L)
print("sum is=",count)
print("avg is=",avg)"""

# Approach2: Using sum() method
"""L=[1,2,4,5,7,8,9,10]
count=sum(L)
avg=count/len(L)
print("sum is=",count)
print("avg is=",avg)
"""
# Approach3:Using sum() and statistics.mean()
"""import statistics
L=[1,2,3,4,5,6,7,8,9]
sum1=sum(L)
avg=statistics.mean(L)
print("sum is=",sum1)
print("avg is=",avg)"""

# Approach4:Using Recursion


# Approach5:using the built-in functions reduce() and lambda
"""from functools import reduce
L=[1,2,3,4,5,6]
count=reduce(lambda x,y:x+y,L)
avg=count/len(L)
print("sum is=",count)
print("avg is=",avg)
"""
# Approach6:using only the built-in functions sum() and len():
"""L=[9,8,2,3,4,5]
count=sum(L)
avg=count/len(L)
print("sum =",count)
print("avg=",avg)"""

# 5)     remove duplicate from a list of integers
# Approach1:Using set() method
"""L=[1,2,3,3,4,5,6,7,8,1]
print("The originall list is"+str(L))
test_list=list(set(L))
print("The test list is"+str(test_list))"""

# Approach2:Using list comprehension
"""L=[1,1,2,9,2,3,4,5]
res=[]
[res.append(x) for x in L if x not in res]
print("The test_list is",str(res))"""

# Approach3:Using list comprehension with enumerate()
# res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]

# Approach4:Using collections.OrderedDict.fromkeys()
"""from collections import OrderedDict
L=[1,2,3,4,5,6,7,2]
result=list(OrderedDict.fromkeys(test_list))
print("The result is", str(result))"""

# Approach5:Using in, not in operators
"""l=[2,3,4,4,5,6]
res=[]
for i in l:
	if i not in res:
		res.append(i)
print("The result is",str(res))"""

# Approach6:Using list comprehension and Array.index() method
"""arr=[9,9,8,8,5,4,3]
res = [arr[i] for i in range(len(arr)) if i == arr.index(arr[i]) ]
print(str(res))"""

# Approach7:Using Counter() method
"""from collections import Counter
arr=[1,2,2,3,1,3,2,1]
temp=Counter(arr)
res=[*temp]
print("The result is",str(res))"""

# 6   Python Program to Split the Even and Odd elements into two different lists
# Approach1:
"""def Split(mix):
	even_list=[ele for ele in mix if ele % 2==0]
	odd_list=[ele for ele in mix if ele % 2!=0]
	print("Even List is",even_list)
	print("Odd List is",odd_list)
mix=[2, 5, 13, 17, 51, 62, 73, 84, 95]
Split(mix)"""

# Approach2:
"""def Split(mix):
	even_list=[]
	odd_list=[]
	for i in mix:
		if i % 2==0:
			even_list.append(i)
		else:
			odd_list.append(i)
			print("Even List is",even_list)
			print("Odd List is",odd_list)

mix = [2, 5, 13, 17, 51, 62, 73, 84, 95]
Split(mix)"""

# 7)  Python program to find the missing  and additional elements.
# Approach1:
"""list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# prints the missing and additional elements in list2
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))

# prints the missing and additional elements in list1
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))"""

# 8)  Python | Maximum sum of elements of list in a list of lists
# Approach1:Traversal of list in lists
# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using traversal

"""def maximumSum(list1):
	maxi = 0
	for x in list1:
		sum = 0
		for y in x:
			sum += y
		maxi = max(sum, maxi)

	return maxi
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))"""

# Approach2:Traversal of lists
# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using traversal

"""def maximumSum(list1):
	maxi = 0
	for x in list1:
		maxi = max(sum(x), maxi)
	return maxi
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))"""

# Approach3:Sum and maximum function
"""def maximumSum(list1):
	return (sum(max(list1, key=sum)))

list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))"""

# Approach4:sum() and sort() method
"""def maximumSum(list1):
	x = []
	for i in list1:
		x.append(sum(i))
	x.sort()
	return x[-1]
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))"""

# Approach5:Using reduce

"""from functools import reduce
def maximum_sum(lists):

	max_sum = reduce(lambda x, y: x if sum(x) > sum(y) else y, lists)
	return sum(max_sum)

lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximum_sum(lists)"""

# 9)   Python | Check if two lists have at-least one element common
# Approach1: using traversal of list
# Python program to check
# if two lists have at-least
# one element common
# using traversal of list
"""def common_data(list1, list2):
	result = False

	for x in list1:
		for y in list2:

			if x == y:
				result = True
				return result
	return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))"""
# Approach2:  Using Set and Property
"""def common_member(a,b):
	a_set=set(a)
	b_set=set(b)
	if(a_set & b_set):
		return True
	else:
		return False

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))
"""
# Approach3: Using Set Intersection
"""def common_member(a,b):
	a_set=set(a)
	b_set=set(b)
	if len(a_set.intersection(b_set))>0:
		return True
	return False

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))"""

# Approach4: Using the any() function and the list comprehension method.
"""def common_member(a, b):
	return any(i in b for i in a)
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_member(a, b))"""

# Approach 5 : Using operator.countOf() method
# 10)  Python program to merge and sort two list
"""""def mergeLists(list1,list2):
	finallist=list1+list2
	finallist.sort()
	return finallist
list1=[1,2,3,4,5,44,37,89,98,12]
list2=[97,76,65,45,53]
print(mergeLists(list1,list2))"""""

# 11)   Python | Intersection of two lists
# Approach1:
"""def intersectionList(list1,list2):
	list3=[value for value in list1 if value in list2]
	return list3
list1=[24,67,78,98,79,23]
list2=[34,56,89,46,37,90,78,65,24]
print(intersectionList(list1, list2))"""

# Approach2:
"""def mergeLists(list1,list2):
	list=(set(list1) & set(list2))
	return list
list1=[23,46,6,89,1,27,71]
list2=[71,46,6,89]
print(intersectionList(list1, list2))"""

# Approach3:
"""def intersection(list1,list2):
	final_list=set(list1).intersection(list2)
	return final_list
list1=[23,46,6,89,1,27,71]
list2=[71,46,6,89]
print(intersection(list1, list2))"""

# Approach4:Python program to illustrate the intersection of two lists, sublists and use of filter()
"""def intersection(lst1, lst2):
	lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
	return lst3
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))"""

# Approach:5 Using reduce():
"""from functools import reduce
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

intersection = reduce(lambda acc, x: acc + [x] if x in lst2 and x not in acc else acc, lst1, [])
print(intersection)"""

# 12) Python Program Union of two or more Lists
# 1)Approach : Python program to illustrate union

"""def Union(lst1, lst2):
	final_list = lst1 + lst2
	return final_list
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))"""

# 2)Approach : Python program to illustrate union

"""def Union(lst1, lst2):
	final_list = sorted(lst1 + lst2)
	return final_list

lst1 = [23, 15, 2, 14, 14, 16, 20, 52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))"""

# 3)Approach : Python program to illustrate Union of three lists

"""def Union(lst1, lst2, lst3):
	final_list = list(set().union(lst1, lst2, lst3))
	return final_list
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
print(Union(lst1, lst2, lst3))"""

"""#13) Python Program to Print all the common elements of two lists
#Approach 1:Using Set’s & property
def common_member(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common elements")

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)

#Approach 2:Using Set’s intersection property
def common_member(a, b):
	a_set = set(a)
	b_set = set(b)

	if len(a_set.intersection(b_set)) > 0:
		return (a_set.intersection(b_set))
	else:
		return ("no common elements")

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))

#Approach 3:Using for loop
def common_member(a, b):
	result = [i for i in a if i in b]
	return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

print("The common elements in the two lists are: ")
print(common_member(a, b))


#Approach 4:Using operator.countOf()
import operator as op
def common_member(a, b):
	result = [i for i in a if op.countOf(b,i)>0 ]
	return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

print("The common elements in the two lists are: ")
print(common_member(a, b))



#Approach 5:Using collections
import collections
def common_member(a, b):
	result = collections.Counter(a) & collections.Counter(b)
	return result.keys()
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

print("The common elements in the two lists are: ")
print(common_member(a, b))"""
