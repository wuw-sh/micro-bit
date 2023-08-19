input.onButtonPressed(Button.A, function () {
    pressA = true
    if (checkTurn()) {
        y += -1
    } else if (checkTurn()) {
        y += 1
    } else {
    	
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    turn = true
})
function checkTurn () {
    return turn && y >= 0 ? true : turn && y < 5 ? true : false
}
input.onButtonPressed(Button.B, function () {
    pressB = true
    if (turn && x >= 0) {
        x += -1
    } else if (!(turn) && x < 5) {
        x += 1
    } else {
    	
    }
})
input.onGesture(Gesture.TiltRight, function () {
    turn = false
})
let j = 0
let i = 0
let pressB = false
let x = 0
let pressA = false
let y = 0
let turn = false
turn = false
pressA = false
x = 0
y = 0
led.plot(0, 0)
basic.forever(function () {
    i = x
    j = y
    if (pressA) {
        if (turn && y >= 0) {
            j += 1
            led.plot(x, y)
            led.unplot(i, j)
        } else if (!(turn) && y < 5) {
            j += -1
            led.plot(x, y)
            led.unplot(i, j)
        } else {
        	
        }
    } else if (pressB) {
        if (turn && x >= 0) {
            i += 1
            led.plot(x, y)
            led.unplot(i, j)
        } else if (!(turn) && x < 5) {
            i += -1
            led.plot(x, y)
            led.unplot(i, j)
        } else {
        	
        }
    } else {
    	
    }
    pressA = false
})
