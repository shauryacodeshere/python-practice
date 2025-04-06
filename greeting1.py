name=input("Enter your name:")
h=int(input("Enter the hour of the day(in 24h formart):"))

if(h==0):
    print(f'{name},it is midnight.You should sleep.')
elif(h>0 and h<4):
     print(f'{name},it is late night.You should sleep.')
elif(h>=4 and h<6):
     print(f'{name},you are an early riser!Good morning.')
elif(h>=6 and h<12):
     print(f'Good morning {name}!I hope you have a great day.')
elif(h>=12 and h<16):
     print(f'Good afternoon {name}.')
elif(h>=16 and h<20):
     print(f'Good evening {name}!I hope you had a great day.')
elif(h>=20 and h<24):
     print(f'Good night {name}!')