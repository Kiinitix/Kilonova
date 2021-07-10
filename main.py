#DE using Pythagorean Triple Algorithm
def encrypt(p, q, alpha):
          alpha1='abcdefghijklmnoprstuvwxyz'
          
          x1=(2*(p**2))+(2*p*q)
          y1=(q**2)+(2*p*q)
          z1=(2*(p**2))+(q**2)+(2*p*q)

          x2=(2*(p**2))-(2*p*q)
          y2=(q**2)-(2*p*q)
          z2=(2*(p**2))+(q**2)-(2*p*q)

          x3=(2*p*q)
          y3=(p**2)-(2*p*q)
          z3=(p**2)+(q**2)

          pythagoreanTriple=[x1, y1, z1, x2, y2, z2, x3, y3, z3]

          key=[]
          
          for i in range(8):
                    key.append(pythagoreanTriple[i]%26)
          
          for i in range(0,len(key)):
                    if(key[i]<0):
                              key[i]=key[i]+26
          keyIndex=0
          Enum1=[]
          c=''

          for i in alpha:
                    index= ord(i.upper())-64
                    Enum= index + int(key[keyIndex])
                    if (Enum > 25):
                              Enum -= 26
                    Enum1.append(Enum)
                    keyIndex +=1
                    if (keyIndex>8):
                              keyIndex=0
          for i in Enum1:
                    c= c + alpha1[i]
          print(c)
encrypt(3,5,"hello")
