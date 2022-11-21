from datetime import datetime
current = datetime.now().time()

print(current)
departure_hour = 19
departure_minute = 30

if (departure_hour == current.hour) and (departure_minute == current.minute):
    print("Ya puedes salir")
elif ((departure_hour < current. hour) and (departure_minute < current.minute)):
    print("Ya se ha pasado la hora, vete ya!!!")
else:
    left_hours = departure_hour - current.hour
    left_minutes = departure_minute - current.minute
    if left_minutes < 0:
        left_hours = left_hours - 1
        left_minutes = (-1*left_minutes) + 30
    print(f"Quedan {left_hours} horas y {left_minutes} minutos")
