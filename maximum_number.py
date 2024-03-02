#input using input function
#cannot use max function
#use for loop
#use split and range
list1=[2,3,4,2,55,6,44]
length=0
for i in list1:
    length +=1
print(length)
maximum=list1[0]
for i in list1:
    if i > maximum:
        maximum=i
print(maximum)
    