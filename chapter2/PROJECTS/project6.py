'''
The kinetic energy of a moving object is given by the formula
KE=(1/2)mv^2 , where m is the object's mass and v is its velocity. Modify
the program you created in Project 5 so that it prints the object's kinetic
energy as well as its momentum.
'''



m = input("mass is(kg):  ")

v = input("velocity is(m/s): ")


print "momentum is", m*v, "kgm/s"
print "kinetic energe is" , m*v**2/2
