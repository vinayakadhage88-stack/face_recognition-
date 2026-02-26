import time 
import random 
import matplotlib .pyplot as plt

def linearsearch(a, key):
	for i in range(len(a)):
		if a[i]==key:
			return i
	return 1
a=[10,20,30,40,50,60]
print("the array element is :",a)
k=int(input("enter the element to search:"))
result=linearsearch(a, k)
if result==-1:
	print("search unseccuseful")
else:
	print("seaesh succesfull find at the location:",result+1)
input_sizes=[100,200,300,400,500,600,700,800,900,1000]
execution_times=[]

for size in input_sizes:
	test_list=[random.randint(1,1000) for _ in range(size)]
	start=time.time()
	key=-1
	end=time.time()
	execution_times.append(test_list)
plt.plot(input_sizes,execution_times,marker="o")
plt.title("linearsearch time complexity")
plt.xlabel("input_size")
plt.ylabel("execution_time")
plt.grid(True)
plt.show()