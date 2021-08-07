import random
random_list=[]

while True:
    k=int(input("please enter the number : "))

    random_list= random.sample(range(0, 20), k)
    print(random_list)