print("welcome to the tip calculator!")
bill=float(input("what was the bill amout $"))
tip=int(input("Hoe much tip would you like to give?10,12 and 15?"))
persons=int(input("how many people to split the bill?"))
tip_per=tip/100
total_tip=bill*tip_per
total_bill=bill+total_tip
bill_per_person=total_bill/persons
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(final_amount)
print(f"Each per son shoud pay: ${final_amount} ")
