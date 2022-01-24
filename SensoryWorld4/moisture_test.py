from gpiozero import MCP3008

moisture = MCP3008(0)

while True:  
    print("Moisture: %-3.2f mV   " % (3300 * moisture.value), end = "\r")

