# Question ---> 1
''''To count the number of occurrences of each word or
    character entered by the user'''

input_string = str(input("Enter a string : \n"))
list = input_string.split()   # To split the elements of the string in the list
dict = {}     # To initialise an empty dictionary

if list.__len__() == 1:   # To be considered when a single word is entered in the string
    for i in list[0]:
        if i in dict:
            dict[i] += 1
        else:             # To be considered when more than one word is entered in the string
            dict[i] = 1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    print(dict)
    print("\n")



# Question ---> 2
# To write a python program to next date of the date entered by the user
# Example ---> If input date = 28-02-1999 , then output date = 01-03-1999

year = int(input("Enter the year between 1800 to 2025 : "))

while(True):
    if (1800 <= year <= 2025):
        break
    else:
        print("Please enter the year between 1800 and 2025")

if (year % 400 == 0):   # To check whether the year is a leap year or not
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Enter the month between 1 to 12: "))

while(True):
    if (1 <= month <= 12):
        break
    else:
        print("Please enter valid month")

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:      # To check the cases of February
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Enter the day between 1 to 31: "))

while(True):
    if (1 <= day <= 31):
        break
    else:
        print("Please enter a valid day")
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next date is : %d-%d-%d" % (day, month, year))



# Question ---> 3
'''To create a list of tuples with first element as the number
 and second element as square of the number'''

input_list = list(map(int, input("Enter the elements separated by a space : ").split()))
resultant_tuple = []   # To create an empty list

for i in input_list:
    power = (i, i**2)
    resultant_tuple.append(power)

print("\nThe resultant tuple formed is :\n", end="")
print(resultant_tuple)



# Question ---> 4
# To print the grade of a student between 4 and 10

grade_points = int(input("Enter your grade points : "))

if (grade_points == 10):
    print("Your Grade is 'A+' and 'Outstanding' performance")
elif (grade_points == 9):
    print("Your Grade is 'A' and 'Excellent' performance")
elif (grade_points == 8):
    print("Your Grade is 'B+' and 'Very Good' performance")
elif (grade_points == 7):
    print("Your Grade is 'B' and 'Good' performance")
elif (grade_points == 6):
    print("Your Grade is 'C+' and 'Average' performance")
elif (grade_points == 5):
    print("Your Grade is 'C' and 'Below Average' performance")
elif (grade_points == 4):
    print("Your Grade is 'D' and 'Poor' performance")
elif (grade_points > 10):
    print("Invalid input")
else:
    print("Failed !")



# Question ---> 5
# To write a program to print the following pattern
'''ABCDEFGHIJK
    ABCDEFGHI
     ABCDEFG
     ABCDE
      ABC
       A '''

input_string = 'ABCDEFGHIJK'
i = 11
while (i>0):
    print(' '*int((11-i)/2), input_string[0:i])
    i=i-2


# Question ---> 6
# To store name and SID of students in a dictionary

SID = int(input("Enter student's SID : "))
Name = input("Enter student's name : ")
students_list = {SID : Name}

while (True):
    available_option = input("Do you want to enter another student's details (Y or N) : ").upper()
    if available_option == "Y":
        SID = int(input("Enter student's SID : "))
        Name = input("Enter student's name : ")
        students_list[SID] = Name
    elif available_option == "N":
        break
    else:
        print("Invalid input")

# Part (a)
# To print students' details stored in the dictionary
print("Students' details = ", students_list)

# Part (b)
# To sort the dictionary using students' names
print("Sorted dictionary using names = ", {sid : name for sid,name in sorted(students_list.items(), key= lambda x:x[1])})

# Part (c)
# To sort the dictionary using students' SID
print("Sorted dictionary using SID = ", {sid : name for sid,name in sorted(students_list.items())})

# Part (d)
# To search a student's name using his/her SID
SID = int(input("Please search student's name with his/her SID : "))
print("Searched student's name = ", students_list[SID])



# Question ---> 7
# To write a python program to print Fibonacci sequence
# Also print average of the resultant Fibonacci series

def recursive_sequence(n):
    if n <= 1:
        return n
    else:
        return (recursive_sequence(n-1) + recursive_sequence(n-2))

number_of_terms = int(input("Enter the number of terms in the sequence : "))
if number_of_terms <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    print("The Fibonacci sequence is : ")

    sum = 0
    for i in range(number_of_terms):
        print(recursive_sequence(i))
        sum = sum + recursive_sequence(i)

average = float(sum / number_of_terms)
print("The average of the resultant fibonacci sequence is : ", average)



# Question ---> 8
# Given problem is based on sets

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

# Part (a)
# To create a new set of all elements that are in set1 and set2 but not both
s1 = set1.union(set2)
s2 = s1 - set1.intersection(set2)
print(s2)     # Here s1 and s2 are variable sets

# Part (b)
# To create a new set of all elements that are in only one of the three sets set1, set2 and set3
s3 = set1.union(set2) - set1.intersection(set2)

s4 = set1.union(set3) - set1.intersection(set3)

s5 = s3.union(s4) - s3.intersection(s4)

s6 = s5.union(set1) - s5.intersection(set1)
print(s6)     # Here s3, s4, s5 and s6 are variable sets

# Part (c)
# To create a new set of all elements that are exactly two of the sets set1, set2 and set3
s7 = set1.intersection(set2)

s8 = set1.intersection(set3)

s9 = s7.union(s8)
print(s9)     # Here s7, s8 and s9 are variable sets

# Part (d)
# To create a new set of all integers in the range 1 to 10 that are not in set1
s10 = set(range(1, 11))

s11 = s10 - set1
print(s11)    # Here s10 and s11 are variable sets

# Part (e)
# To create a new set of all integers in range 1 to 10 that are not in set1, set2 and set3
s12 = s10 - set1 - set2 - set3
print(s12)    # Here s12 is a variable set


