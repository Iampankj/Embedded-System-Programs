from sense_hat import SenseHat
import time
sense = SenseHat()
while True:
  #go throw all joystick's events
  for event in sense.stick.get_events():
    #check if the joystick was pressed
    if event.action == "pressed":
      #check which direction
      if event.direction == "up":
        sense.show_letter("U") #up arrow
      elif event.direction == "down":
        sense.show_letter("D") #down arrow
      elif event.direction == "left":
        sense.show_letter("L") #left arrow
      elif event.direction == "right":
        sense.show_letter("R") #right arrow
      elif event.direction == "middle":
        sense.show_letter("M") #Enter key
      #wait a while and then clear the screen
      time.sleep(0.5)
      sense.clear()