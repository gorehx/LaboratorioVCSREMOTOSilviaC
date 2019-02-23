a= float(input("Digite el número"))
b= float(input("Digite el número"))
c= float(input("Digite el número"))
d=(((b**2)-(4*a*c))**(1/2))
x1=(-b+(d**(1/2)))/(2*a)
x2=(-b-(d**(1/2)))/(2*a)
igual= ((-1*b)/(2*a))
if d>0:
  print ("La parte positiva es",x1,"La parte negativa es",x2)
else:
  if d==0:
   print ("El resultado es",igual)
  else:
   print ("No existe solución en los números reales")

  
  
  
  
