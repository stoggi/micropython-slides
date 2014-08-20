# NZPUG Auckland Meeting - MicroPython Slides

This repo contains the slides used for the MicroPython presentation at the NZPUG Auckland meeting on 20/08/2014.

## Usage

1. Copy `slides.py` onto the SD card or internal flash of the PyBoard.
2. Plug the PyBoard in with the micro USB cable.
3. Open a serial connection with `screen /dev/ttyUSB0`. (You may need root permissions, otherwise add yourself to the `dialout` group)
4. When prompted with the interactive shell start the slides

    import slides
    slides.play()

## Future Work

Slide animations? Haha, just kidding.