#SCMAKEYBot Robot Control
#Raspberry Pi Global Setting
#import gpiozero
from gpiozero import LED
import time

#Raspberry Pi
#Using BCM GPIO3 I/O
red_led = LED(3)
yellow_led = LED(4)
green_led=LED(2)




def stop_light(traffic_light_):
    print(traffic_light_)
   
    #iterate throught the dictionary
    it = iter(traffic_light_.values())
    red = next(it)
    yellow = next(it)
    green = next(it)

#check if red is on first, turn it off, check yellow, turn it off, and finally check green and turn it off
    if red == 1:
        print("RED LED On")
        red_led.on()
        time.sleep(1)
#         red_led.off()
#         print("RED LED Off")
#         red = 0
#         time.sleep(1)
    if red != 1 and yellow == 1:
        print("YELLOW LED On")
        yellow_led.on()
        time.sleep(1)
        yellow_led.off()
        yellow = 0
        time.sleep(1)
        print("YELLOW LED Off")
    if red != 1 and yellow !=1 and green == 1:
        print("GREEN LED On")
        green_led.on()
        time.sleep(1)
        green_led.off()
        green = 0
        time.sleep(1)
        print("GREEN LED Off")
       
#Asks the user for input of color and the value
#based on the input, checks to see if color is in the dictionary, and then turns on the led the user wants
def update(traffic):
    it = iter(traffic)
    red = next(it)
    yellow = next(it)
    green = next(it)
    red_val=int(input("Turn on red? ENTER 0 or 1: "))
    yellow_val=int(input("Turn on yellow? ENTER 0 or 1: "))
    green_val=int(input("Turn on green? ENTER 0 or 1: "))

    traffic[red]=red_val
    traffic[yellow]=yellow_val
    traffic[green]=green_val
           
   
def main():
