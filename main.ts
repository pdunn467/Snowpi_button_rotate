input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Press = 1
    while (Press == 1) {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(1000)
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        basic.pause(1000)
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
        basic.pause(1000)
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
        basic.pause(1000)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.pause(1000)
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Press = 0
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
})
let Press = 0
let strip : neopixel.Strip = null
strip = neopixel.create(DigitalPin.P2, 12, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    
})
