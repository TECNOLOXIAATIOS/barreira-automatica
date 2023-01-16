neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)

def on_forever():
    if PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J1,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM) > 3 and PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J1,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM) < 30:
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 180)
        basic.pause(3000)
    else:
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 90)
        basic.pause(3000)
basic.forever(on_forever)
