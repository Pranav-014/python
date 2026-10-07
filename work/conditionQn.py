# 1. Student Grade Calculator
# mark = int(input("Enter your mark: "))

# if mark >= 90 and mark <=100:
#     print("A+")
# elif mark >= 80 and mark <=100:
#     print("A")
# elif mark >= 70 and mark <=100:
#     print("B")
# elif mark >= 60 and mark <=100:
#     print("C")
# elif mark >= 50 and mark <=100:
#     print("D")
# else:
#     print("Fail")


# 2. ATM Withdrawal
# balance = int(input("Enter account balance: "))
# amount = int(input("Enter withdrawal amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of 100")
# else:
#     print("Withdrawal Successful")

# 3. Online Shopping Delivery
# amount = int(input("Enter order amount: "))

# if amount >= 5000:
#     delivery = 0
# elif amount >= 2000:
#     delivery = 50
# else:
#     delivery = 100

# final_amount = amount + delivery

# print("Delivery charge:", delivery)
# print("Final amount:", final_amount)

# 4. Employee Performance Rating
# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")

# 5. Electricity Bill
# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + ((units - 400) * 7)
# print("Electricity bill:", bill)

# 6 — Movie Ticket Pricing.
# age = int(input("Enter your age: "))

# if age < 5:
#     print("Free")
# elif age <= 12:
#     print("₹100")
# elif age <= 59:
#     print("₹200")
# else:
#     print("₹120")

# 7. Traffic Fine System
# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No fine")
# elif speed <= 80:
#     print("Fine: ₹500")
# elif speed <= 100:
#     print("Fine: ₹1000")
# else:
#     print("Fine: ₹2000")
#     print("License Review")

# 8. Restaurant Billing System
# bill = float(input("Enter total bill: "))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 15 / 100
# elif bill >= 1000:
#     discount = bill * 10 / 100
# else:
#     discount = 0

# final_bill = bill - discount

# print("Discount:", discount)
# print("Final bill:", final_bill)

  # 9. College Admission
# score = int(input("Enter entrance score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")


    # 10. Bank Loan Risk
# score = int(input("Enter credit score: "))
# default = input("Existing loan default? (yes/no): ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# elif score >= 750:
#     print("Low Risk")
# elif score >= 650:
#     print("Medium Risk")
# elif score >= 550:
#     print("High Risk")
# else:
#     print("Very High Risk")


    # 11. Hotel Room Pricing
# room = input("Enter room type: ").lower()
# nights = int(input("Enter number of nights: "))

# if room == "standard":
#     price = 2000
# elif room == "deluxe":
#     price = 3500
# elif room == "suite":
#     price = 5000
# else:
#     price = 0
#     print("Invalid room type")

# total = price * nights

# if nights > 5:
#     discount = total * 10 / 100
# else:
#     discount = 0

# final_bill = total - discount

# print("Final bill:", final_bill)

# 12. Employee Bonus
# salary = float(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))

# if performance >= 90:
#     bonus = salary * 20 / 100
# elif performance >= 75:
#     bonus = salary * 15 / 100
# elif performance >= 60:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0

# print("Bonus:", bonus)

# 13. Mobile Data Plan
# data = float(input("Enter monthly data usage in GB: "))

# if data < 5:
#     print("Basic Plan - ₹199")
# elif data <= 20:
#     print("Standard Plan - ₹399")
# elif data <= 50:
#     print("Premium Plan - ₹699")
# else:
#     print("Unlimited Plan - ₹999")


# 14. Parking Fee
# hours = int(input("Enter parking hours: "))
# ev = input("Is it an electric vehicle? (yes/no): ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if ev == "yes":
#     fee = fee - (fee * 20 / 100)

# print("Final parking fee:", fee)

# 15. Online Exam Result
# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory >= 40 and practical >= 40:

#     average = (theory + practical) / 2

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")
# else:
#     print("Fail")

