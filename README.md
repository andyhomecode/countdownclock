# countdownclock

Installed adafruit hardware clock, pcf8523 to keep time when offline:

https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-rtc-time


edited .config/lxsession/LXDE-pi/autostart to add 
   @python3 countdownv2.py 
to get script to run on boot

Edit the source to add key dates and times

