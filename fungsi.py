import random
def a(x,y):
	return (3*(x**2))+(2*(y**2))-(4*x)+((y*1.0)/2)
print a(1,0)
def int_to_bin(x,y):
	bin_x='{0:03b}'.format(x)
	bin_y='{0:03b}'.format(y)
	return bin_x+bin_y
def bin_to_int(bin):
	mid=len(bin)/2
	int_x=int(bin[:mid],2)
	int_y=int(bin[mid:],2)
	return [int_x,int_y]
pop=[[str(random.randint(0,1)) for x in range(8)] for y in range(10)]
#print pop
listpop=[bin_to_int(''.join(pop[x])) for x in range(10)]
fitnes=[a((listpop[x][0]),listpop[x][1]) for x in range(10)]
for i in range(len(pop)):
	pop[i].append(fitnes[i])
for i in pop :
	print i
