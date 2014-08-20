# NZPUG Auckland Meeting - MicroPython - Slides
# Jeremy Stott jeremy@stott.co.nz

import pyb

# Turn on the blue LED so we know it's booted.
pyb.LED(4).on()

# Define our ASCII escape codes
# {P}urple
# {B}lue
# {G}reen
# {Y}ellow
# {R}ed
# {E}nd ascii sequence
# {C}lear screen
colors = {
    '{P}': '\033[95m',
    '{B}': '\033[94m',
    '{G}': '\033[92m',
    '{Y}': '\033[93m',
    '{R}': '\033[91m',
    '{E}': '\033[0m',
    '{C}': '\033[2J\033[;H'
}

# Create our slides as a list of strings
slideshow = [
    """{C}
{P} Embedded Python!{E}
{B}----------------------------------------{E}
 
 
 
 
 
 
                           {Y}Jeremy Stott{E}
                      jeremy@stott.co.nz
""",

    """{C}
{P} Raspberry Pi{E}
{B}----------------------------------------{E}

 {G}* Huge community{E}

 * Very easy to get started

 * Cheap

 * Runs a full Python install
""",

    """{C}
{P} Cubieboard{E}
{B}----------------------------------------{E}

 * Similar to the Raspberry Pi

 * More powerful (1GB RAM, Dual Core)

 * Smaller community

 * Runs a full Python install
""",

    """{C}
{P} OLIMEX{E}
{B}----------------------------------------{E}

 * Similar to the Cubieboard

 * Slightly less powerful

 {Y}* Open source! Open Hardware!{E}

 * Cheap

 * Based in Bulgaria
""",

    """{C}
{P} Odroid U3{E}
{B}----------------------------------------{E}

 * Blows the others out of the water!

 {R}* Quad core, 2GB of RAM{E}

 * Good community

 * Pre-built Linux images (including a
  robotics image with OpenCV)

 * $69 USD
""",

    """{C}
{P} MicroPython{E}
{B}----------------------------------------{E}

 {G}* Python running on a micro controller!{E}

 * Can control low level hardware, servos,
  accelerometers, or embed in another
  project

 * Open Source, Open Hardware!

 * Demo..
"""
]

def play():
    for slide in slideshow:
        for key, escape in colors.items():
            # Loop through all the slides and replace the placeholders with the escape codes
            slide = slide.replace(key, escape)

        # Print the slide to the console
        print(slide)

        # Wait for the user to press Enter before continuing
        input()
