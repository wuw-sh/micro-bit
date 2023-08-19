def on_button_pressed_a():
    global pressA, y
    pressA = True
    if turn and y >= 0:
        y += -1
    elif not (turn) and y < 5:
        y += 1
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global turn
    turn = True
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    global pressB, x
    pressB = True
    if turn and x >= 0:
        x += -1
    elif not (turn) and x < 5:
        x += 1
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global turn
    turn = False
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

j = 0
i = 0
pressB = False
y = 0
x = 0
pressA = False
turn = False
turn = False
pressA = False
x = 0
y = 0
led.plot(0, 0)

def on_forever():
    global i, j, pressA
    i = x
    j = y
    if pressA:
        if turn and y >= 0:
            j += 1
            led.plot(x, y)
            led.unplot(i, j)
        elif not (turn) and y < 5:
            j += -1
            led.plot(x, y)
            led.unplot(i, j)
        else:
            pass
    elif pressB:
        if turn and x >= 0:
            i += 1
            led.plot(x, y)
            led.unplot(i, j)
        elif not (turn) and x < 5:
            i += -1
            led.plot(x, y)
            led.unplot(i, j)
        else:
            pass
    else:
        pass
    pressA = False
basic.forever(on_forever)
