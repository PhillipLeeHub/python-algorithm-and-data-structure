import requests
import re


def get_cars():
    return requests.get("http://www.shift.com/interview/inventory").json()


# print(len(get_cars()))

def get_count_for_make(make):
    car_data = get_cars()

    counter = 0
    # loop through all car obj
    for obj in car_data:
        if obj.get('make') == make:
            counter += 1
    return counter


# print(get_count_for_make("Toyota"))

"""
body_style  count avg_price
SUV         249   32000
Hatchback   93    18000
Sedan       267   ...
Van         10
Coupe       50
Wagon       21
Convertible 24
Truck       10
"""


def print_table(key):
    dict_count_cars = {}
    car_data = get_cars()

    # counting loop
    for obj in car_data:
        field = obj.get(key)
        price = int(obj.get('price').replace('$', '').replace(',', ''))

        # Check if make seen
        # dict_count_cars = {(count, running_price)}
        if field in dict_count_cars:
            curr_count, curr_price = dict_count_cars[field]
            dict_count_cars[field] = (curr_count + 1, curr_price + price)

        else:
            dict_count_cars[field] = (1, price)

    value_len = max(len(max(dict_count_cars.keys(), key=len)), len(key))
    str_format_padding = '%-' + str(value_len) + 's %5s %s'
    print(str_format_padding % (key, 'count', 'avg_price'))
    # loop through car dictionary

    for field in dict_count_cars:
        curr_count, curr_price = dict_count_cars[field]

        avg_price = int(curr_price / curr_count)
        print(str_format_padding % (field, dict_count_cars[field][0], str(avg_price)))


print_table('body_style')

#
# Your previous Plain Text content is preserved below:
#
# http://shift.com/interview/inventory
#
# [
#   {
#     "carid": "c196202",
#     "year": "2017",
#     "make": "Honda",
#     "model": "Accord Hybrid",
#     "trim": "Base",
#     "price": "$21,200",
#     "mileage": 7384,
#     "body_style": "Sedan",
#     "transmission": "CVT"
#   },
#   {
#     "carid": "c184210",
#     "year": "2015",
#     "make": "Volkswagen",
#     "model": "Passat",
#     "trim": "1.8T SE",
#     "price": "$11,500",
#     "mileage": 31091,
#     "body_style": "Sedan",
#     "transmission": "Automatic"
#   },
#   ...
# ]
