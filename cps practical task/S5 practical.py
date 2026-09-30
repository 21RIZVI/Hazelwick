count = 0
total = 0
highest = 0
lowest = 0

mark= int(input("please enter mark"))
while mark != -1:
    if mark > 100 or mark<0:
     print("INVALID MARK - MUST BE BETWEEN 0 AND 100")
     mark= int(input("please enter mark"))
    elif mark <= 100 and mark >= 0:
        count = count + 1
        total = mark + total
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
        mark= int(input("please enter mark"))
average = total/count
print("marks entered", count)
print("Average:" average)


