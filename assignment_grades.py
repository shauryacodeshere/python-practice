marks=int(input ('Enter the marks:'))
if marks in range (91,101):
    print('Excellent! Your grade is \'A+\' ')
elif marks in range (81,91):
    print('Well Done! Your grade is \'A\' ')    
elif marks in range (71,81):
    print('Very good, Your grade is \'B+\' ')
elif marks in range (61,71):
    print('Good ,Your grade is \'B\' ')
elif marks in range (51,61):
    print('Can do better ,Your grade is \'C\' ')    
elif marks in range (41,51):
    print('Need improvement,Your grade is \'D\' ')    
elif(marks<0 or marks>100) :
    print('Invalid input')
else :
    print('You have failed ,Your grade is \'F\' ')    