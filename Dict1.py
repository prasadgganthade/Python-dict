#Python | Sort Python Dictionaries by Key or Value
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
mykeys = list(myDict.keys())
mykeys.sort()
sorted_dict = {i: myDict[i] for i in mykeys}
print(sorted_dict)
print(mykeys)
def dictionary():
    key_value = {}

    # initializing key value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print(key_value)

    for i in sorted(key_value.keys()):
        print(i,end=" ")
def main():
    dictionary()
# main function calling
if __name__ == "__main__":
    main()
print()
#Handling missing keys in Python dictionaries
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
# .get() - method
print(country_code.get('India','Not found'))
print(country_code.get('Japan','Not found'))
# using setdefault
country_code.setdefault('Japan','Not present')
print(country_code['India'])
print(country_code['Japan'])
# Python dictionary with keys having multiple inputs
# Python program to find the sum of all items in a dictionary
# method 1 - using inbuilt sum function

mydict = {'a': 1000,'b':2000,'c':3000}

"""
def return_sum(mydict):
    list1 = []
    for i in mydict:
        list1.append(mydict[i])

    final = sum(list1)
    return final
print(return_sum(mydict))
"""
# method 2 - for loop through values
def return_sum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
    return sum
print('The sum of values',return_sum(mydict))

# Find the size of a Dictionary in Python
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print('The size of',dic1.__sizeof__())
print('The size of',dic2.__sizeof__())
print('The size of',dic3.__sizeof__())

#Get length of dictionary in Python
dict1 ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}
print('Length is',len(dict1))

# How to find length of dictionary values?
dict1 = {'a': [1, 2, 3],
         'b': [1, 2, 3],
         'c': 5,
         'd': "nopqrs",
         'e': ["A", "B", "C"]}

count = sum([1 if isinstance(dict1[i], (str,int)) else len(dict1[i]) for i in dict1])
print('The length of values is',count)
# Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter
list1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(list1,key=itemgetter('age')))
print(sorted(list1,key=itemgetter('age','name')))
print(sorted(list1,key=itemgetter('age'),reverse=True))

# Python | Merging two Dictionaries
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# using update method
"""
def merge(dict1,dict2):
    return dict2.update(dict1)
print(merge(dict1,dict2))
print(dict2)
"""

# using for loop
"""
def merge(dict1,dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1
dict3 = merge(dict1,dict2)
print(dict3)
"""

# Using ** in Python
def merge(dict1,dict2):
    res = {**dict1,**dict2}
    return res
dict3 = merge(dict1,dict2)
print(dict3)

# Ways to sort list of dictionaries by values in Python – Using lambda function
list1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(list1, key=lambda i: i['age']))
print(sorted(list1, key=lambda i: i['age'], reverse=True))

#Program to create grade calculator in Python
jack = { "name":"Jack Frost",
        "assignment" : [80, 50, 40, 20],
        "test" : [75, 75],
        "lab" : [78.20, 77.20]}
james = { "name":"James Potter",
        "assignment" : [82, 56, 44, 30],
        "test" : [80, 80],
        "lab" : [67.90, 78.72]}
dylan = { "name" : "Dylan Rhodes",
        "assignment" : [77, 82, 23, 39],
        "test" : [78, 77],
        "lab" : [80, 80]}
jess = { "name" : "Jessica Stone",
        "assignment" : [67, 55, 77, 21],
        "test" : [40, 50],
        "lab" : [69, 44.56]}
tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]}
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum/len(marks)

def calculate_total_average(students):
    assignment = get_average(students['assignment'])
    test = get_average(students['test'])
    lab = get_average(students['lab'])
    return (0.1 * assignment + 0.7 * test + 0.2 * lab)

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

def class_average(student_list):
    result_list = []

    for student in student_list:
        student_average = calculate_total_average(student)
        result_list.append(student_average)
        return get_average(result_list)

students = [jack,james,dylan,jess,tom]

for i in students:
    print(i['name'])
    print('The average marks %s is : %s'%(i['name'],calculate_total_average(i)))
    print('The grade %s is : %s'%(i['name'],assign_grade(calculate_total_average(i))))
    print('-------------------------------------------------------------')

print('The class average is %s'%(class_average(students)))
print('Grade of the class is %s'%(assign_grade(class_average(students))))
#Python – Insertion at the beginning in OrderedDict
#Find common elements in three sorted arrays by dictionary intersection
# Dictionary and counter in Python to find winner of election
# Python – Key with maximum unique values
test_dict = {"Gfg": [5, 7, 5, 4, 5,8],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
max_val = 0
max_key = None
for i in test_dict:
    if len(set(test_dict[i])) > max_val:
        max_val =  len(set(test_dict[i]))
        max_key = i

print('Maximum unique values',max_key)

# Find all duplicate characters in string
# Group Similar items to Dictionary Values List
from collections import defaultdict
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

result = defaultdict(list)
for i in test_list:
    # appending similar items
    result[i].append(i)
print('Similat dict',dict(result))
# K’th Non-repeating Character in Python using List Comprehension and OrderedDict
#Python – Replace String by Kth Dictionary value
# Ways to remove a key from dictionary
test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
del test_dict['Mani']
print(test_dict)
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
removed_value = test_dict.pop('Haritha')
print('Dict after pop operations',test_dict)
print('The removed key',removed_value)
# Python – Replace words from Dictionary
test_str = 'geekforgeeks best for geeks'
lookup_dict = {'best': 'good and better', 'geeks': 'all cs students'}
temp = test_str.split()
res = []
for i in temp:
    res.append(lookup_dict.get(i,i))
res = " ".join(res)
print('Replaced string',res)
# Python – Remove Dictionary Key Words
test_str = 'gfg is best for geeks'
test_dict = {'geeks':5,'best':2}
temp = test_str.split(' ')
temp1 = [word for word in temp if word.lower() not in test_dict]
res = " ".join(temp1)
print(res)
# Python | Remove all duplicates words from a given sentence
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
    if (s.count(i) >= 1 and (i not in k)):
        k.append(i)
print(k)
print(' '.join(k))
# above using set

string = 'Python is great and Java is also great'
print(" ".join(set(string.split())))
# Python – Remove duplicate values across Dictionary Values
from collections import Counter
test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}
cnt = Counter()
for idx in test_dict.values():
    cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1]
       for idx, j in test_dict.items()}
print('Uncommon elements records',res)
# Python Dictionary to find mirror characters in a string
# Counting the frequencies in a list using dictionary in Python
def countfrequency(my_list):
    frequency = {}
    for item in my_list:
        if (item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1

    for key, value in frequency.items():
            print("% d : % d"%(key,value))
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    countfrequency(my_list)

# Python – Dictionary Values Mean









