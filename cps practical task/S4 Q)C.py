age = int(input("enter your age"))
card = input("do you have a student card y/n:")
if age <= 0:
    print("error, age must be greater than 0")
elif age > 12:
    print( "Ticket price:£5.00")
elif age <= 17:
    print("Ticket price:£7.00")
elif age <=64:
    if card == "y":
        print("Ticket price:£8.00")