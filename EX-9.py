#tamrine(045)
total=0
while(total<50):
    b=int(input('adadvared shavad: '))
    total +=b
    print('The total is... '+str(total))

    
#tamrine(046)
b=0
while b<=5 :
   b=int(input('adad vared shavad: '))
print('the last number you entered was... ' + str(b))

#tamrine(047)
e= int (input ("yek adad vared konid: "))
f= int (input ("yek adade digar vared konid"))
g= e+f

str1 = str (input ("do you want to add another number? (insert y for yes)"))
if str1 != 'y':
    print(str(g))
else:
    while str1 == 'y':
        h = int (input("yek adad vared konid"))
        i= g+h
        str1 = str (input ("do you want to add another number? (insert y for yes)"))
    str3 = str(i)
    print ("the total is: " + str3)
#tamrine (048)
b='y'
i=0
while b=='y':
    a=input('who do you want to invite?: ')
    i+=1
    print(a+' has been invited to your party')
    b=input('do you want to invite more people?:(y for yes) ')
print('you have invited ' + str(i)+' people to your party')


#tamrine(049)
compnum=50
a = int(input("enter a number: "))
i=1    
while a!= compnum:
    if a > compnum:
        i+=1
        a=int(input("insert a lower number"))
    else:
        i+=1
        a=int(input("insert a higher number"))

i= str(i)
print("Well done, you took "+i+ " attemps")


#tamrine(050)
a=int(input('enter a number between 10 and 20: '))
while a<10 or a>20:
    if a<10:
        print ('too low try again: ')
    if a>20:
        print ('too high try again: ')
    a=int(input('enter a number between 10 and 20: '))
print('Thank you')


#tamrine(051)
num=10
while num>0:
    print( str(num)+' green bottles sitting on the wall,And if one green bottle should accidentally fall,')
    a=int(input('How many green bottles will be hanging on the wall? '))
    num-=1
    while a!=num:
        print('no try again')
        a=int(input('How many green bottles will be hanging on the wall? '))
print('there no more bottles on the wall')
