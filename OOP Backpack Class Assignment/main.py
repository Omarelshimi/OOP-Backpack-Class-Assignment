# OOP Backpack Class Assignment by Omar Elshimi

class Backpack:
   def __init__(self, colorinit, sizeinit):
      #Properties
      self.color = colorinit
      self.size = sizeinit
      self.items = []
      self.open = False

   def openBag(self):
      self.open = True
      print("Your backpack is now open.")
      
   def closeBag(self):
      self.open = False
      print("Your backpack is now closed.")
      
   def putin(self, item):
      if self.open:
         self.items.append(item)
         print("Your " + item + " has been added to your backpack.")
   
   def takeout(self, item):
      if self.open:
         self.items.remove(item)
         print(item + " has been removed from your backpack.")
         
   def printBP(self):
        print(f"{self.size} {self.color} backpack")
         
backpack1 = Backpack("blue", "small")
backpack2 = Backpack("red", "medium")
backpack3 = Backpack("green", "large")

backpack1.openBag()
backpack1.putin("lunch")
backpack1.putin("jacket")
backpack1.closeBag()
backpack1.openBag()
backpack1.takeout("jacket")
backpack1.closeBag()
   
       