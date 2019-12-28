# Bite 21. Query a nested data structure ???
# Given the provided cars dictionary:
# 
# Get all Jeeps
# Get the first car of every manufacturer.
# Get all vehicles containing the string Trail in their names (should work for other grep too)
# Sort the models (values) alphabetically

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    ret = ''
    for i in cars.get('Jeep'):
        ret = ret + f'{i}, '
    ret = ret[0:len(ret)-2]
    return ret


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_car = []
    for item in list(cars.items()):
        first_car.append(item[1][0])
    return first_car


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""   
    matching = []
    for i in cars:
        for j in cars[i]:
            if grep.lower() in j.lower():
                matching.append(j)
    matching = sorted(matching)
    return matching


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for i in cars:
        cars[i].sort()
    return cars
    

# print(get_all_jeeps(cars))
# print(get_first_model_each_manufacturer(cars))
# print(get_all_matching_models(grep = 'cher'))
# print(sort_car_models())

def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected

def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected



def test_get_all_matching_models_default_grep():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected


def test_get_all_matching_models_different_grep():
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected

test_get_all_jeeps()
test_get_first_model_each_manufacturer()
test_get_all_matching_models_default_grep()
test_get_all_matching_models_different_grep()
test_sort_dict_alphabetically()


# SOLUTION
# from itertools import chain
# 
# cars = {
#     'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
#     'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
#     'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
#     'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
#     'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
# }
# 
# def get_all_jeeps(cars=cars):
#     """return a comma  + space (', ') separated string of jeep models
#        (original order)"""
#     return ', '.join(cars['Jeep'])
# 
# 
# def get_first_model_each_manufacturer(cars=cars):
#     """return a list of matching models (original ordering)"""
#     return [models[0] for models in cars.values()]
# 
# 
# def get_all_matching_models(cars=cars, grep='trail'):
#     """return a list of all models containing the case insensitive
#        'grep' string which defaults to 'trail' for this exercise,
#        sort the resulting sequence alphabetically"""
#     grep = grep.lower()
#     # flatten list of lists (less obvious way: "sum(cars.values(), [])")
#     models = list(chain.from_iterable(cars.values()))
#     matching_models = [model for model in models
#                        if grep in model.lower()]
#     return sorted(matching_models)
# 
# 
# def sort_car_models(cars=cars):
#     """return a copy of the cars dict with the car models (values)
#        sorted alphabetically"""
#     return {manufacturer: sorted(models) for
#             manufacturer, models in cars.items()}
