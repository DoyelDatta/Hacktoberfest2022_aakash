import cmath  
n1 = float(input('Enter a number: '))  
n2 = float(input('Enter second number: '))  
n3 = float(input('Enter third number: '))   
dis = (n2**2) - (4*n1*n3)  
r1 = (-n2-cmath.sqrt(dis))/(2*n3)  
r2 = (-n2+cmath.sqrt(dis))/(2*n3)  
print('The solution are {0} and {1}'.format(r1,r2))  
