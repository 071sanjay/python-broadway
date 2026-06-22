# marks = 80

# if (marks>=80 and marks<=100):
#     print("Dis")
# elif (marks>=60):
#     print("first")
# else:
#     print("fail")

# marks = int(input("enter the number"))

# if (marks>=80 and marks<=100):
#     print("Dis")
#     if marks == 100:        #nested if
#         print("topper")
#     elif(marks==80):
#         print("lucky dis")
# elif (marks>=60 and marks<=79):
#     print("first")
# else:
#     if marks == 59:
#         print("unlucky")
#     print("fail")

# loan approval
# income = int(input("Enter your income "))
# cs = int(input("Enter your credit score "))
# gr = input("Enter y if you have gurantor ").lower()
# if(income>=3000):
#     if(cs>=700):
#         print("Loan is approved")
#     else:
#         print("Loan is rejected")
# elif(income<3000):
#     if(cs>=750):
#         if(gr=="y"):
#             print("The loan is approved")
#         else:
#             print("Loan is rejected")
#     else:
#         print("Loan is rejected")


# gender = "M"
# if gender == "M":
#     print("Male")
# else:
#     print("Female")

# data = "Male" if gender =="M" else "Female"
# print(data)

# 1. Online Shopping Discount System
# total_purchase = int(input("enter the total purchase"))
# customer = input("enter y if customer is premium").lower()
# if (total_purchase>=100):
#     if(customer == " y"):
#         print("discount is 20%")
#     else:
#      print("discount is 10%")
# else:
#     if (total_purchase >=50):
#         if (customer == " y"):
#             print("discount is 5%")
#         else:
#             print("there is no discount")
#     else:
#         print("there is no discount")


#3. Employee Bonus Calculation

# years = int(input("enter a number"))
# rating = int(input("enter a number"))
# training = input("enter y if training courses is completed").lower()

# if (years>=5):
#     if (rating>=8):
#         print("larger bonus")
#     else:
#         print("medium bonus")
# else: #if years<5 no needed!!!
#     if (rating>=9):
#             if (training=="y"):
#                 print("medium bonus")
#             else:
#                 print("no bonus")
#     else:
#         print("no bonus")


# 6. Hotel Room Upgrade Eligibility
booked_nights = int(input("enter number of days booked:"))
member_type = input("Are they loyalty members? (y/n): ").lower()
previous_stay = input("Enter y if they have stayed more than 10 times before:").lower()
if (booked_nights>=5):
    if (member_type == "y"):
        if (previous_stay == "y"):
            print("luxury upgrade")
        else:
            print("standard upgrade")
    else:
        print("no upgrade")
else:
    total_spending = int(input("Enter spending amount this year:"))
    if (member_type == "y"): 
        if (total_spending>2000):
            print("standard upgrade")
        else:
            print("no upgrade")
    else:
        print("no upgrade")