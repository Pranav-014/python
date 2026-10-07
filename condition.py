# 1) Desition Making statements

# if statement
# if-else statement
# if-elif-if statement
# Nested statement

#  if condition:
        # block of code.
        # .
        # .

# if condition:
        # if block:
# else:
        # else block

# if condition:
     # if block:
# elif condition:
    # blck of code
# elif condition:
    # blck of code
# else:
        # else block

        
# age=60
# if age >=18:
#     print('Adult')


# if age >=18:
#     print('Adult')   
# else:
#     print("child")


# if age >0 and age<13 :
#     print('Child')
# elif age >=13 and age <20:
#     print('Teen')
# elif age >20 and age <60 :
#     print('Adult')
# elif age>=60:
#     print('Senior Citezon')
# else:
#     print('Invalid input')

# print('--------------------')  

# age = int(input("Enter your age:"))
# mark=int(input("Enter your mark:"))

# if age>=18:
#     print("Age recuirenment satisfied..")
#     if mark>=50:
#         print("Admission approved")
#     else:
#         print("Admission rejected:insufficent marks")
# else:
#     print("Admission rejected: Age requirement is not satisfied")


# ----Match case

# match expression:
    # case 1:
        # print ("1st statement")
    # case 2:
        # print ("2st statement")
    # case n:
        # print ("nst statement")
    # case _:
        # print("default statement")

# ----------

# day = int(input("Enter the no of days:"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3: 
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Fri")
#     case 6: 
#         print("Sat")
#     case 7: 
#         print("Sun")
#     case _:
#           print("Invalid Entry")

# ----
# mark = int(input("Enter th e mark:"))
# if mark>90 and mark <=100 :
#     print("A+")
# elif mark>80 and mark<=90:
#     print("A")
# elif mark>70 and mark<=80:
#     print("B+")
# elif mark>60 and mark<=70:
#     print("B")
# elif mark>50 and mark<=60:
#     print("C+")
# elif mark>40 and mark<=50:
#     print("D")
# elif mark>0 and mark<=40 :
#     print("E")
# else:
#     print("Invalid Entry")

# -----
day = "mon"

match day.capitalize():
    case "Mon" | "Tue" | "Wed " | "Thu" | "Fri" :
        print("Working Day")
    case "Sun" | "Sat" :
        print("Weekend")
    case _:
        print("Invalid entry")