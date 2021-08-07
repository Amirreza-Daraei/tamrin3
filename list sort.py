number_list=[]

while True:
    a=(input("please enter the number : "))

    if a=="ok" :     
        break

    else:
        number_list.append(int(a))

print("your number is" , number_list)

c=0
for i in range(len(number_list)-1) :
    if number_list[i] > number_list [i+1]:
        c =+ 1
        print("list is sort")

    else :
        print("list is not sort")


 