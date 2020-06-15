from django.http import JsonResponse
from geopy import distance
import json
import re


def calculate_distance(origin, destination):
    return distance.distance(origin, destination).km


def load_data(file):
    with open(file) as infile:
        data = json.load(infile)
        return data


def find_restaurants(q, lat, lon):
    data = load_data('restaurants.json')
    customer_location = (lon, lat)
    search_key = re.compile(q, re.IGNORECASE)
    match = list()
    distance_error = 0  # for match outside search range
    for restaurant in data['restaurants']:
        if list(filter(search_key.match, restaurant['tags'])) \
                or search_key.match(restaurant['description']) \
                or search_key.match(restaurant['name']):
            _distance = calculate_distance(restaurant['location'], customer_location)
            if _distance < 3:
                match.append(restaurant)
            else:
                distance_error += 1
    return match, distance_error


def validate_input(request):
    error = list()
    missing_coordinate = False
    if not request.GET.get('q'):
        error.append({'error': 'search key is missing'})
    if not request.GET.get('lat'):
        missing_coordinate = True
        error.append({'error': 'latitude is missing'})
    if not request.GET.get('lon'):
        missing_coordinate = True
        error.append({'error': 'longitude is missing'})
    if not missing_coordinate:
        try:
            float(request.GET.get('lat'))
            float(request.GET.get('lon'))
        except ValueError:
            error.append({'error': 'latitude and longitude have to be numbers'})
    return error if error else False


def search(request):
    if request.method == 'GET':
        input_error = validate_input(request)
        if input_error:
            return JsonResponse(input_error, safe=False)
        q = request.GET.get('q')
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        result = find_restaurants(q, lat, lon)
        match, distance_error = result[0], result[1]
        if match:
            return JsonResponse(match, safe=False)
        elif distance_error != 0:
            message = {'message': f'{distance_error} restaurant(s) found outside 3km search range'}
            return JsonResponse(message, safe=False)
        else:
            message = {'message': 'no restaurants found'}
            return JsonResponse(message, safe=False)
