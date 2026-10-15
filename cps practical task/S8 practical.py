#fuction 1 : celsius to fahrenheit converter
def celsius_to_farh(Celsius):
    F = Celsius * 1.8 + 32
    return(F)
def print_conversersion_table(start,end,step):
    print("celsius             Fahrenheit")
    for i in range (start,end+1,step):
        print(f"{i:<10} {celsius_to_farh(i)}")

#main program
far = cel = float(input("enter Celsius:"))
print("Fahrenheit is:", far)
start = int(input("enter start value"))
end = int(input("enter end value:"))

print_conversersion_table(start,end,10)