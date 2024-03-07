# 팁 계산 프로그램

print("Welcome to the tip calculator.")
charge = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
tip_percent = tip / 100
number = int(input("How many people to split the bill? "))

total_bill = charge + (charge * tip_percent)
bill_per_person = round(total_bill / number, 2)

print("Each person should pay: $" + str(bill_per_person))