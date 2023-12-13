#   a123_apple_1.py
import turtle as trtl
import random as rand
import time as t
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
bg_image = "background.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image)
wn.addshape(apple_image)
wn.addshape(bg_image)

 # Make the screen aware of the new file
wn.bgpic(bg_image)

# fruit turtles
apple = trtl.Turtle()
pear = trtl.Turtle()

drawer = trtl.Turtle()# draws the letters on the fruit
drawer.penup()# to not add extra marks

#list of letter
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
# This function takes care of font and color.
def draw_an_A(letter):
  drawer.color("blue")
  drawer.write(letter, font=("Arial", 35, "bold"))



def draw_fruit(active_fruit,image):# the actice fruit is the turtle variable while the image ariable is the the image you want to draw
  active_fruit.shape(image)
  drawer.goto(active_fruit.xcor()-15 ,active_fruit.ycor()-40)
  wn.update()

def drop():
  if(apple.ycor() == 0):
      apple.penup()
      apple.goto(apple.xcor(),-200)
      apple.pendown()
  apple.hideturtle()
  drawer.clear()
  
def applepress():
  apple.penup()
  if(apple.ycor() == 0):
    print("not pressed")
    drop()
    t.sleep(1)
  apple.goto(rand.randint(-100,100),0)
  apple.showturtle()# brings the turtle back 
  letter = letters[rand.randint(0,25)]
  draw_fruit(apple,apple_image)
  draw_an_A(letter.capitalize())# used the capitalize method to make it more readable
  t.sleep(0.2)
  wn.onkeypress(drop ,letter)
  wn.listen()# listeninfg for the key stroke
  t.sleep(0.5)

  applepress()
  print("Waiting")
# Main code

applepress()
