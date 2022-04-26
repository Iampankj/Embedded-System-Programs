from time import time
#start the timer
start = time()

def print_factors(x):
   for i in range(2, x):
       if x % i == 0:
           print(i)
print('Please enter a number: ')
num = int(input())
#num = 26324
print_factors(num)

#stop the timer
end = time()

print('Elasped time:{}seconds'.format(end-start))