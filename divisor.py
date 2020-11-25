from __future__ import division

#Logo

print "   -------------------"
print "   |                  /"
print "   |                  \ r1 "
print " -----                /   "
print "  ---  V              ---* Vmedio   " 
print "   |                  |   "
print "   |                  /"
print "   |                  \ r2"
print "   |                  /   "
print "   -------------------    "

        
#Variables

r1 = input('Ingresar el valor de R1 en ohms:')
r2 = input('Ingresar el valor de R2 en ohms:')
v = input('Ingresar el valor de la fuente V:')

i = v/(r1+r2)
print "La corriente es de :",i,"A"
v = r2*i
print "Tension punto medio es:",v,"V"
