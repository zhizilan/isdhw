 class Dimension:
     delf_init_(self,x,y):
         self.x=x
         self.y=y
     delf area(self):
         pass

 class Ellipse(Dimension):
     delf_init_(self,a,b):
         Dimension_init_(self,a,b)
     delf area(self):
         return 3.14*self.x*self.y

 class Square(Dimension):
     delf_init_(self,c):
         Dimension_init_(self,c)
         return self.x*self.x

 class Rectangle (Dimension):
     delf_init_(self,w,h):
         Dimension_init_(self,w,h)
     delf area(self):
         return self.x*self.y

class Circle(Dimension):
     delf_init_(self,r):
         Dimension_init_(self,r,0)
     delf area(self):
         return 3.14*self.x*self.x

  d1=Ellipse(10.0,20.0)
  d2=Square(15.0)
  d3=Rectangle(20.0,15.0)
  d4=Circle（5.0）
   print(d1.area(),d2.area(),d3.area(),d4.area())

   shapes=[Ellipse(10.0,20.0),Square(15.0),Rectangle(20.0,15.0),Circle（5.0)]
   total_area=compute_area(shapes)
   print(total_area)
 
 
