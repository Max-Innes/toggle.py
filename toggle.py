
# Use the Pin method from the machine software library
import machine
import time
# Define the inputs and outputs and assign them to software objects
# First argument is a GPIO pin number, rather than a physical pin number
led1 = Pin(18, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(16, Pin.OUT)
led4 = Pin(17, Pin.OUT)
led5 = Pin("LED", Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Initial states
led1_state = False
led2_state = False
led3_state = False
led4_state = False
led5_state = False

def toggle():
    global led1_state, led2_state, led3_state, led4_state, led5_state
    #makes it on or off
    led1_state = not led1_state
    led2_state = not led2_state
    led3_state = not led3_state
    led4_state = not led4_state
    led5_state = not led5_state    
    #changes value
    led1.value(led1_state)
    led2.value(led2_state)
    led3.value(led3_state)
    led4.value(led4_state)
    led5.value(led5_state)
# Main loop
while True:
    if button_pin.value() == 1:
        toggle()
        # Debounce delay
        time.sleep(0.2)
    time.sleep(0.01)

