x= int (input ('Является ли год високосным?'))

if (((x % 4 == 0) and (x % 100 !=0)) or (x % 400 ==0)):
    print ('да')
else:
    print ('нет')
