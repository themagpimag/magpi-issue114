from gpiozero import MCP3008

liquid = MCP3008(1)

while True:  
    print("Liquid level: %-3.2f mV   " % (3300 * liquid.value), end = "\r")