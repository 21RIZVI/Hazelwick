name = input("What is your name:")
height = int(input("enter your height in cms:"))
print("Hi",name.title())
height_m = height/100
print("your height is", height_m ,"in metres")
height_i = round(height/2.54)
print("That is", height_i ,"inches")
over = height > 180
print("Taller than 180 cm:" ,over)
