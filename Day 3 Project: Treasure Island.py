print('''
*****************************************************                                     
88                                     
88                                     
88                                     
88  ,adPPYba,  8b       d8  ,adPPYba,  
88 a8"     "8a `8b     d8' a8P_____88  
88 8b       d8  `8b   d8'  8PP"""""""  
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa  
88  `"YbbdP"'      "8"      `"Ybbd8"'  

***************************************************** 
''')


print("Welcome to Love Treasure Island.")
print("""Your mission is to find the treasure.
If you make a mistake "Game Over"
""") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#Write your code below this line 👇

name = input("The story begins with what is your name? \n")
print(f"Welcome to this game {name}")


flag1 = input("Choices: Left or Right? \n").lower()
if flag1 == "right":
  print("proceed")
  flag2 = input("Choices: Truth or Lie \n").lower()
  if flag2 == "true":
    print("proceed")
    flag3 = input("Choices: Do, Die or Love \n").lower()
    if flag3 == "love":
      print("You have found the treasure of love! <3 <3 <3")
    else:
      print("you dead!, Game Over")
  else:
    print("you dead!, Game Over")    
else:
  print("you dead!, Game Over")
