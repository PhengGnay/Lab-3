
"""
create a list to store 5 numbers (float)
capture user's input 5 times for their grades
each time we capture a user's input, we append the number to the list
sort the list ascending, then splice the item starting at index 2
once we have 3 highest number in the list, we sum then up and divide by 3
output a message to the user
end
"""

""" PSUDOCODE
create list
capture input
append number to list
capture input
append number to list
capture input
append number to list
capture input
append number to list
capture input
append number to list

sort the list, then splice out the two lowest numbers
print message to user
"""

grades = []
grade = input("Enter the 1st garde: ")
grades.append(float(grade))
grade = input("Enter the 2nd garde: ")
grades.append(float(grade))
grade = input("Enter the 3rd garde: ")
grades.append(float(grade))
grade = input("Enter the 4th garde: ")
grades.append(float(grade))
grade = input("Enter the 5th garde: ")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades / 3
print("Average Grade {0:.2f}%".format(result))
print(grades, 'results', result)