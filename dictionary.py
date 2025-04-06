dict={'kitaab':'book',266:'xyz',90:121}
print(dict)
print(dict.keys())
print(dict.values())
print(dict['kitaab'])
print(dict.items())
for key,value in dict.items():
    print('The value for key',key,'is',value)
    print(f'The value for key {key} is {value}')
    print(f'The value for key {key} is {dict[key]}')
print(dict.get('tree'))    
