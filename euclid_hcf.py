def hcf(x,y):
  while(y):
    x,y = y,x%y
  return x

print("The hcf of (9,36) is: ",hcf(9,36))
