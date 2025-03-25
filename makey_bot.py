# Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Servo
import time
from time import sleep

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

warning_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if warning_messages : print("Warning Message are 'ON'")
else : print("Warning Message are 'OFF'")
# Raspberry Pi Pins
red_pwm_pin = PWMLED(14)
green_pwm_pin = PWMLED(15)
blue_pwm_pin = PWMLED(18)

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

myGPIO = 21

myCorrection = 0.45
maxPW = (2.0+myCorrection)/1000
minPW = (1.0+myCorrection)/1000

servo = Servo(myGPIO, min_pulse_width = minPW, max_pulse_width = maxPW)

def wave():
    wave_delay = 0.5
    servo.max()
    sleep(wave_delay)
    servo.min()
    sleep(wave_delay)



def stop_light(traffic_light):


    it = iter(traffic_light.values())
    red = next(it)
    yellow = next(it)
    green = next(it)

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

def eyes_RGB(eyes):
    red, green, blue = eyes
    red_pwm_pin.value = eyes[red]
    green_pwm_pin.value = eyes[green]
    blue_pwm_pin.value = eyes[blue]


def get_robot_feature_data():
    hex = ("0", "1", "2","3", "4", "5","6", "7", "8","9", "A", "B", "C", "D", "E","F")
    #stoplight
    red_val=int(input("Turn on red? ENTER 0 or 1: "))
    yellow_val=int(input("Turn on yellow? ENTER 0 or 1: "))
    green_val=int(input("Turn on green? ENTER 0 or 1: "))
    stop_light = {'red_LED':red_val, 'yellow_LED':yellow_val, 'green_LED':green_val}

    #color:
    color = input("Give a hex code#: ").upper()
    if (len(color) != 6):
        raise Exception("Not a valid code")
    else:
        for i in color:
            if i not in hex:
                raise Exception("Not a valid code")
    red_rgb = int[color[0:2],16]/255
    green_rgb = int[color[2,4], 16]/255
    blue_rgb = int[color[4:],16]/255
    
    eye = {'red_rgb_led': red_rgb, 'green_rgb_color':green_rgb, 'blue_rgb_color':blue_rgb}
    # servo
    rfd = [stop_light, eye]

    return(rfd)

def main():
    print("Welcome To The STEAM Clown Makey Bot")
#    robot_features = get_robot_feature_data()
    stop_light_LEDs, eyes_rgb = get_robot_feature_data()


    stop_light(stop_light_LEDs)

    eyes_RGB(eyes_rgb)
    wave()

main()