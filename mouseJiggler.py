import pyautogui as pg
import time
import sys

try: 
  arg = int(sys.argv[1])
except:
  arg = False

size = pg.size()
position = pg.position()
curX, curY = pg.position()
movX, movY = (curX - 20), (curY + 20)
wiggleTime = arg or 3

def app():
  print("Staring Wiggle")
  while True: 
    time.sleep(wiggleTime)
    print("Wiggle Wiggle!")
    pg.moveTo(movX, movY)
    time.sleep(.2)
    pg.moveTo(curX, curY)

if __name__ == "__main__": 
  print(size)
  print(position)
  print("wiggleTime: " + str(wiggleTime))
  app()
