from gpiozero import MotionSensor, LED
from signal import pause
from mail import sendEmail
pir = MotionSensor(4)
led = LED(17)
led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    led.on()
    print ("Sending email...")
    sendEmail()
    print ("done!")
    pir.wait_for_no_motion()
    print("No Motion Detected!")
    led.off()

