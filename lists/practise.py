marks = [85, 90, 78, 92, 88, 95, 80, 91, 87, 89]

for i in range(len(marks)):
    mark = float(input("Enter a mark: "))

    if mark == 90:
        print("Excellent")
    
    elif mark in marks:
        print("Good — the index of that mark is:", marks.index(mark))
    else:
        print("That mark is not found in the list.")

    break

