import time

a = pow(2, 20) #This is how far you want to look for prime numbers. I.e. this script will only check 0 to a for prime numbers

count = 1; 
primes = [1]

start_time = time.time()

for i in range(2, a):

    flag = 0

    for j in range(2, int(pow(i, 1/2)+1) ):

        if (i%j == 0):
            flag = 1
            break

    if (flag == 0):
        primes.append(i)
        count += 1 



print("TIME: ", str(time.time() - start_time) + " seconds")
print("There were ", str(count), "prime numbers")
print(primes)