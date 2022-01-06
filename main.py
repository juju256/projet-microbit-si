def run_motor(motor: number):
    if motor == 1:
        chois = maqueen.Motors.M1
    elif motor == 2:
        chois = maqueen.Motors.M2
    while maqueen.ultrasonic(PingUnit.CENTIMETERS) < 30:
        maqueen.motor_run(chois, maqueen.Dir.CW, 100)

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) > 40:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
        basic.show_number(0)
    else:
        basic.show_number(1)
        maqueen.motor_stop(maqueen.Motors.ALL)
        if randint(0, 10) <= 6:
            run_motor(1)
        else:
            run_motor(2)
basic.forever(on_forever)
