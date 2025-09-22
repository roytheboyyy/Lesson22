#square values finder
list1 = [1,2,3,4,5,6,7,8,9,10]
for square in list1:
    print("the square of", square , "is" , square**2)
#Odd and even filteration
for list1 in range(1,21):
    if list1 % 2 == 0:
        print(list1 , "is even")
    else:
        print(list1 , "is odd")