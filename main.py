def on_button_pressed_a():
    global Press
    Press = 1
    while Press == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(1000)
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        basic.pause(1000)
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        basic.pause(1000)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(1000)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Press
    Press = 0
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
input.on_button_pressed(Button.B, on_button_pressed_b)

Press = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 12, NeoPixelMode.RGB)

def on_forever():
    pass
basic.forever(on_forever)
