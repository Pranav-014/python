# collage event
# age = int(input("Enter age: "))
# student = input("Are you a student? ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible")
# else:
#     print("Not eligible")


# online shopping discount
amount = int(input("Enter order amount: "))
premium = input("Are you a premium member? ")

if amount >= 3000 or premium == "yes":
    print("Discount available")
else:
    print("No discount")


# airport checkin
    ticket = input("Ticket confirmed? ")
passport = input("Passport valid? ")
hours = int(input("Hours until departure: "))

if ticket == "yes" and passport == "yes" and hours > 2:
    print("Check-in available")
else:
    print("Check-in not available")

    # movie ticket
    age = int(input("Enter age: "))

if age < 12 or age >= 60:
    print("Special ticket price")
else:
    print("Normal ticket price")

    # bank loan

    income = int(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))
default = input("Existing loan default? ")

if income >= 40000 and credit >= 700 and default == "no":
    print("Eligible")
else:
    print("Not eligible")

    # food delivary shipping

    amount = int(input("Enter order amount: "))
premium = input("Premium member? ")
disabled = input("Delivery disabled? ")

if (amount >= 500 or premium == "yes") and disabled == "no":
    print("Free delivery")
else:
    print("Free delivery not available")


# working home eligibility
months = int(input("Months in company: "))
remote = input("Project allows remote work? ")

if months >= 6 and remote == "yes":
    print("Can work from home")
else:
    print("Cannot work from home")

    # hotel booking
    available = input("Room available? ")
payment = input("Valid payment method? ")
stopped = input("Hotel stopped reservations? ")

if available == "yes" and payment == "yes" and stopped == "no":
    print("Booking can proceed")
else:
    print("Booking cannot proceed")