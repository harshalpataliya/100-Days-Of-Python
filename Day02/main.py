print("Welcome To The TIP CALCULATOR !")

Bill=float(input("Enter the your bill amount here =$"))
Tip=int(input("Enter the Tip amount percentage would you like to give? 10 12 20 or 50 "))
People=int(input("Enter the Number of People Would you like to Split it.."))

#Now here, calculate the  TOTAL TIP PERCENTAGE as per amount

tip_as_percent= Tip / 100
total_tip_amount= Bill * tip_as_percent 
 
total_bill= Bill + total_tip_amount

bill_per_person= total_bill / People
final_amount= round(bill_per_person,2)

print(f"Each person should pay ${final_amount}")