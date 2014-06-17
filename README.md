ShiftPi
=======

ShiftPi is the easiest way to work with `74HC595` shift registers on your Raspberry Pi in Arduino style :). If you are an Arduino fan ... you will love it :) This library is inspired from this article: [Can you move over? The 74HC595 8 bit shift register](http://bildr.org/2011/02/74hc595/)

# How to connect Pi with `74HC595`
![Scheme](http://i.picresize.com/images/2014/03/11/xM26G.jpg)

#Quick Example ... Arduino style :)
So ... Let's have a look how can we create some magic :)

    from shiftpi import HIGH, LOW, digitalWrite, delay

    while True:
        digitalWrite(1, HIGH)
        delay(1000)
        digitalWrite(1, LOW)
        delay(1000)

Looks familiar? :)) The Blink example ?? Do you like it? :) Cool :))

# How can I use the library?

So if you are not familiar with python you can use the library in 2 ways:

    import shiftpi

    # turns shift register's pin 1 to HIGH
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.delay(1000)

    # turns shift register's pin 1 to LOW
    shiftpi.digitalWrite(1, shiftpi.LOW)
    shiftpi.delay(1000)

    # turns all shift register pins to HIGH
    shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
    shiftpi.delay(1000)

or you can use the library methods as shown in the first example, with importing all methods from the `shiftpi` library. If I want to set all shift register's pins to `HIGH` I can do the following:

    from shiftpi import HIGH, LOW, ALL, digitalWrite, delay

    digitalWrite(ALL, HIGH)

That's it! :)

# The API look and feel

In all examples below i will use the second way of importing methods. (from shiftpi import bla bla)

## Constants

* `HIGH` # this is mode of pin
* `LOW`  # this is mode of pin
* `ALL`  # you can use it as pin number.


## pinsSetup(dict)
By the way by default `SER`, `RCLK`, `SRCLK` are set as follow:

* SER   = 25  (GPIO RPI)  #pin 14 on the 75HC595
* RCLK  = 24  (GPIO RPI)  #pin 12 on the 75HC595
* SRCLK = 23  (GPIO RPI)  #pin 11 on the 75HC595

But ... if you want to use other GPIOs ... you can define them with the following method:

    pinsSetup({"ser": SER_PIN, "rclk": RCLK_PIN, "srclk": SRCLK_PIN}) # that's it!

## shiftRegisters(num)
By default shiftpi works with 1 shift register, but if you use more than one shift register you can set the number of all shift registers you use, with this method:

    shiftRegisters(3) # if you use 3 shift registers

## startupMode(mode or dict, execute)
By default if you use the library for first time all your pins will be set to `LOW`, but if you want to use some other different configuration you can try with this method.

    # this will set all your pins to `HIGH` but will not execute them.
    startupMode(HIGH)

    # if you want to set all your pins to `HIGH` and it will execute them automaticaly ... try this
    startupMode(HIGH, True) # works just like digitalWrite(ALL, HIGH)

    # if you want to set only few pins to some mode ... try this
    startupMode({1: HIGH, 4: HIGH, 6: HIGH})

    # and if you want to execute them ...
    startupMode({1: HIGH, 4: HIGH, 6: HIGH}, True)

## digitalWrite(pin, mode)
The digitalWrite method is inspired from the Arduino API and it works as you expect

If you want to turn 3rd pin of the shift register to `HIGH`

    digitalWrite(3, HIGH)

or if you want to turn on all pins of the shift register to `HIGH`

    digitalWrite(ALL, HIGH) # will turn on all pins to HIGH

## delay(millis)
If you are an Arduino guy you just need to know that this method works just like the Arduino's `delay`

    delay(30) # will sleep for 30 millis

#Requirements

* Raspberry Pi
* Python 2.6+ and Python development tools
* RPi.GPIO (latest version recommended)

# Installation

First install RPi.GPIO library and Python development tools:

    # sudo apt-get update && sudo apt-get -y install python-rpi.gpio python-dev

Get `shiftpi` source and install it:

    # git clone git://github.com/mignev/shiftpi.git
    # sudo python shiftpi/setup.py install

After installation, you can remove the folder as it is no longer needed by running:
    
    # sudo rm -rf shiftpi

# Testing
TODO

# Contributing
Fork the [shiftpi repo on GitHub](https://github.com/mignev/shiftpi), make your super duper awesome changes :) and send me a Pull Request. :)

# Contributors

- [Marian Ignev](https://github.com/mignev) 
- [Nathan Bookham](https://github.com/inversesandwich)
- [Felix Breidenstein](https://github.com/f-breidenstein)

# Useful links
* [How Shift Registers work?](http://www.youtube.com/watch?feature=player_embedded&v=6fVbJbNPrEU#!) (Video)

#Copyright
Copyright (c) 2013 Marian Ignev. See LICENSE for further details.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/mignev/shiftpi/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

