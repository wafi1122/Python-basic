minMarks = 30
studentMarks = float(input('enter a student marks :'))
if (studentMarks >= minMarks):
    print('you are eligibal')
elif (studentMarks >= 25):
    print('you have been put into the waiting list')
else:
    print('you are not eligibale')