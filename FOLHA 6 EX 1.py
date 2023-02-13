#.FOLHA 6 EX 1    


from math import acos
from math import sin
class vec:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norm(self):
        return ((self.x**2+self.y**2+self.z**2)**0.5)
    def __or__(self,other):               #escalar
        return (self.x*other.x+self.y*other.y+self.z*other.z)
    def ang(self,other):
        return(acos((self|other)/(self.norm()*other.norm())))
    def __and__(self,other):                     #vetorial
        return sin(self.ang(other))*self.norm()*other.norm()
     
class Univec(vec):
    def __init__(self,x,y,z):
        vec.__init__(self,x,y,z)
        n=self.norm()
        self.x/=n
        self.y/=n
        self.z/=n
       
u=vec(1,2,3)
v=vec(2,2,3)
p=Univec(1,2,1)
print(u.norm())
print(v.norm())
print(u|v)
print(u.ang(v))
print(u&v)
print(p.x)
print(p.y)
print(p.z)








































