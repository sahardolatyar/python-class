#tamrine(069)
>>> tuple1= ("Astralia", "UK", "USA", "Germany", "Sweden")
t = input ("insert one of the countries:Astralia ,UK , USA ,Germany,Sweden: ")

    print (tuple1.index(t))

#tamrine (070)
tuple1=("Astralia", "UK", "USA", "Germany", "Sweden") 
t = input ("insert one of the countries: Astralia ,UK , USA ,Germany,Sweden: ")

    print (tuple1.index(t))

u = int (input ("insert the number of country: "))

    print (tuple1[u-1])

#tamrine (071)
sports=['roller skate','swimming']
a=str(input('whats your favorite sport?: '))
sports.append(a)
sports.sort()
print(sports)

#tamrine(072)
list1= ["mathematics","chemistry","bilology","algebra", "history","physics",]

   print (list1)
str1= input('which subject you do not like? ')
list1.remove(str1)

   print(list1)

#tamrine(073)
dict1= {}
str1= str(input ("qazaye morede alaqeye khod ra vared konid: 1: "))
dict1.setdefault(1,str1)
str2= str(input ('qazaye morede alaqeye khod ra vared konid: 2: '))
dict1.setdefault(2,str2)
str3= str(input ("qazaye morede alaqeye khod ra vared konid : 3: "))
dict1.setdefault(3,str3)
str4= str(input ("qazaye morede alaqeye khod ra vared konid : 4: "))
dict1.setdefault(4,str4)
print(dict1)
a= int (input("which one you want get rid of? "))
dict1.pop(a)
print (dict1.items())



#tamrine(074)
list1= ["sabz", "zard", "banafsh", "qermez", "narengi", "surati", "tusi", "sefid", "arqavani", "sormei"]
c= int (input("yek adad beyne 0 va 4 vared konid: "))
d= int (input("yek ada beyne 5 va 9 vared konid: "))
print (list1[c:d+1])



#tameine(075)
list2= [112, 220, 360, 110]
print (list2[0])
print (list2[1])
print (list2[3])
print (list2[2])
b= int (input("adad vared shavad: "))
if b in list2:
    print (list2.index(b))
else:
    print("That is not in the list")

#tamrine(076)
str1 = str(input("insert name of first friend for your party: "))
str2 = str(input("insert name of second friend for your party: "))
str3 = str(input("insert name of third friend for your party: "))
list3= [str1, str2, str3]

str4= input("do you want to add some one else? ")
while str4=="yes":
    str5= input("insert his name: ")
    list3.append(str5)
    str4= input("do you want to add some one else? ")
if str4== "no":
    print (len(list3))


#tamrine(077)
str1 = str(input("insert name of first friend for your party: "))
str2 = str(input("insert name of second friend for your party: "))
str3 = str(input("insert name of third friend for your party: "))
list3= [str1, str2, str3]

str4= input("do you want to add some one else? ")
while str4=="yes":
    str5= input("insert his name: ")
    list3.append(str5)
    str4= input("do you want to add some one else? ")
if str4== "no":
    print (list3)

a = input("type one of the names of the list: ")
print (list3.index(a))
b= input ("do you still want to have him in party? ")
if b== "no":
       list3.remove(a)

print (list3)


#tamrine(078)
list10= ["asrejadid", "paytakht", "dorehami", "akhbar"]
print(list10[0])
print(list10[1])
print(list10[2])
print(list10[3])
c= str (input('add another show: '))
d= int (input('where the position? '))
list10.insert(d,c)
print (list10)



#tamrine(079)
nums=[]
a= int (input("insert a number: "))
nums.append(a)
print (nums)
b= int (input("insert a number: "))
nums.append(b)
print (nums)
c= int (input("insert a number: "))
nums.append(c)
print (nums)
d= input("do you still want to save the last one to save?")
if d== "no":
    del(nums[2])
    print (nums)


    
