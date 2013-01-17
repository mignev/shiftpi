# Define MODES
ALL  = -1
HIGH = 1
LOW  = 0

# Define pins
_SER_pin   = 7;    #pin 14 on the 75HC595
_RCLK_pin  = 8;    #pin 12 on the 75HC595
_SRCLK_pin = 25;   #pin 11 on the 75HC595

# is used to store states of all pins
_registers = list()

#How many of the shift registers - change this
_number_of_shiftregisters = 1

def shiftregisters(num):
    global _number_of_shiftregisters
    _number_of_shiftregisters = num
    _all(LOW)

def _all_pins():
    return _number_of_shiftregisters * 8

def _all(mode):
    all_shr = _all_pins()

    for pin in range(0, all_shr):
        _setPin(pin, mode)
    _execute()

    return _registers

def _setPin(pin, mode):
    try:
        _registers[pin] = mode
    except IndexError:
        _registers.insert(pin, mode)

def digitalWrite(pin, mode):
    if pin == ALL:
        _all(mode)
    else:
        if len(_registers) == 0:
            _all(LOW)

        _setPin(pin, mode)
    _execute()

def _execute():
    pass