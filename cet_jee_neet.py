condition=True
while condition:

    print("---MENU---\n")
    print("1.JEE\n2.CET\n3.NEET\n4.Exit\nNOTE:\na)Choose each option only once\nb)Insert a space after every name (except the last one) and click enter to submit ")

    choice=int(input("Enter your choice:"))

    if choice==4 :
         condition=False
         print('--exiting--')

    else:
        match choice:
            case 1: 
                     njee=set(input('Names of candidates appearing for jee:').split())
                    
            case 2: 
                    ncet=set(input('Names of candidates appearing for cet:').split())
                    
            case 3: 
                    nneet=set(input('Names of candidates appearing for neet:').split())
     
            case _:
                    print('Invalid input')


condition2=True
while condition2:
        
                print('Do you want in depth analysis?\n')
                print("1.Yes\n2.No\n")
                choice2=int(input("Enter your choice:"))

                if choice2==2:
                      print('Alright,thank you')
                      condition2=False

                elif(not(choice2==1 or choice2==2)):
                      print('Invalid input')
                      

                else:
                        print('1.CET or JEE or NEET\n2.CET and JEE\n3.CET but not JEE\n4.JEE and CET and NEET\n5.Exit')
                        choice3=int(input("Enter your choice:"))
                        
                        
                        if(choice3==5):
                               condition2=False
                               print("--Thank You--")

                        else:
                                match choice3:
                                
                                        case 1:
                                                print(f'Students appeared for CET or JEE or NEET:{njee | ncet | nneet}')
                                                
                                        case 2:
                                                print(f'Students appeared for CET and JEE:{njee & ncet}')

                                        case 3:
                                                print(f'Students appeared for CET but not JEE:{ncet-njee}')

                                        case 4:
                                                print(f'Students appeared for JEE and CET and NEET:{njee & ncet & nneet}') 

                                        case _:
                                                print('Invalid input')




