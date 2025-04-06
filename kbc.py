name=input('Hello! please enter your name:')
q=['What is the capital of India?','How many faces does a cube have?','When did partition of Bengal take place?']
print(q[0])
a=[['Delhi','Mumbai','Kolkata','Chennai'],['8','12','4','6'],['1940','1857','1905','1947']]
print(a[0])
sum=0
if (sum==0):
    for q[0] in q:
    
        ans=str(input("Enter your answer:"))
        if (ans==a[0][0]):
         print("Congrats,",name,"your answer is right you win 10L")
         sum=sum+1
        elif(ans=='i quit'):
         print("Okay",name,",your winnings are:0L") 
         break 
        else:
          print("Unfortunaterly,your answer is wrong.You take home nothing")
        break 
if (sum==1):
    print(q[1])
    print(a[1])
    for q[1] in q:
        ans=str(input("Enter your answer:"))
        if (ans==a[1][3]):
            print("Congrats,",name,"your answer is right you win 20L")
            sum=sum+1
            break
        elif(ans=='i quit'):
            print("Okay",name,",your winnings are:10L") 
            break           
        else:
            print("Unfortunaterly,your answer is wrong.You take home nothing")
            break 
if(sum==2):       
        print(q[2])
        print(a[2])    
        for q[2] in q:
            ans=str(input("Enter your answer:"))
            if (ans==a[2][2]):
                print("Congrats,",name,"your answer is right you win 30L")
                break 
            elif(ans=='i quit'):
                print("Okay",name,",your winnings are:20L")   
                break    
            else:
                print("Unfortunaterly,your answer is wrong.You take home nothing")
                break
              
print('Thanks for playing')            


