def make_car(model, manufacturer, **info):
    car = {}
    car['model'] = model
    car['manufacturer'] = manufacturer

    for key, value in info.items():
        car[key] = value

    return car

car = make_car(
    'Reventon',
    'Lamborghini',
    released='2018',
    max_speed=320
)

print(car)
