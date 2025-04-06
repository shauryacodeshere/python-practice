def ly(n):
    if(n%4==0 and n%100!=0) or (n%400==0):
        return 1
    else:
        return 0
    
year=int(input('Enter the year:'))
ans=ly(year)
    
if(ans):
    print("Leap year")
else:
    print("Not a Leap year")