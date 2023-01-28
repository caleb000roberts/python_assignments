# m02 Case Study
# author: Caleb Roberts
# created: 1/27/2023
# program takes student data as input and determines based on gpa
# if student is on the dean's list or the honor roll




# get last name
last_name = input("What is student's last name? ")
print(f"Student's last name is {last_name}.")

# quit
if last_name == "ZZZ" :
    quit

# get first name
first_name = input("What is student's first name? ")
print(f"Student's first name is {first_name}.")

# get gpa as a float
gpa = float(input("What is student's GPA? "))
print(f"Students GPA is {gpa}.")

# determine if student is on DL or HR and display message
if gpa >= 3.50 :
    print(f"{first_name} {last_name} has made the Dean's List with a GPA of {gpa}.")
elif gpa < 3.50 and gpa >= 3.25 :
    print(f"{first_name} {last_name} has made the Honor Roll with a GPA of {gpa}.")
else:
    print(f"{first_name} {last_name} did not make the Dean's List or Honor Roll with a GPA of {gpa}.")



