
num = int(input("entre the num"))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(1, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")