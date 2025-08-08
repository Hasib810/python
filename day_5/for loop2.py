marks = [10, 20, 30, 40, 50]
#total = sum(marks)
#print(total)
#sum = 0
#for mark in marks:
    #sum += mark
#print(sum)

max_mark = 0
for mark in marks:
    if mark > max_mark:
        max_mark = mark
print(max_mark)