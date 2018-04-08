using System;
class Rectangle 
{
  /* member variables */
  double length;
  double width;
  void Acceptdetails()
  {
     length = 4;    
     width = 3;
  }
  
  double GetArea()
  {
     return length * width; 
  }
  
  void Display()
  {
      print(length);
      print(width);
      print(GetArea());
  }
}

class ExecuteRectangle 
{
  void Main() 
  {
     Rectangle r = new Rectangle();
     r.Acceptdetails();
     r.Display();
     scan();
  }
}
