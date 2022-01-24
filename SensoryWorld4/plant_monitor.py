from gpiozero import MCP3008
from time import sleep
from pushbullet import Pushbullet

pb = Pushbullet("Your Access Token")
print(pb.devices)

message = ""
moisture = MCP3008(0)
liquid = MCP3008(1)

def alert():
    device = pb.get_device('Your Device')
    push = device.push_note("Plant monitor alert: ", message)
    sleep(60)
        
while True:
    moisture_mv = 3300 * moisture.value
    liquid_mv = 3300 * liquid.value
    print("Moisture: %-3.2f mV   " % moisture_mv, "Liquid level: %-3.2f mV   " % liquid_mv, end = "\r")
    
    if moisture_mv < 500:
        message = "Soil moisture too low! Water me!"
        alert()
    elif liquid_mv < 1000:
        message = "Reservoir level too low! Fill it!"
        alert()
