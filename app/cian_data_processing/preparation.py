import json
import math
from datetime import datetime


def prepare_data(data):
    offers_to_insert = []
    offers = data.get('data', dict()).get('offersSerialized')
    for offer in offers:
        prepared_offer = dict()
        prepared_offer['flat_id'] = offer['id']
        prepared_offer['cian_id'] = offer['cianId']
        prepared_offer['raw_data'] = json.dumps(offer)
        prepared_offer['added_timestamp'] = datetime.fromtimestamp(offer['addedTimestamp'])
        prepared_offer['total_area'] = float(offer['totalArea'] or 0.0)
        prepared_offer['price_rur'] = offer['bargainTerms']['priceRur']
        prepared_offer['meter_price'] = float(offer['bargainTerms']['priceRur'] or 0.0) / \
                                        float(offer['totalArea'] or 0.0)
        prepared_offer['full_url'] = offer['fullUrl']
        prepared_offer['from_developer'] = bool(offer['fromDeveloper'])
        prepared_offer['is_premium'] = bool(offer['isPremium'])
        prepared_offer['kitchen_area'] = float(offer['kitchenArea'] or 0.0)
        prepared_offer['is_apartments'] = bool(offer['isApartments'])
        prepared_offer['jk_url'] = offer['jkUrl']
        prepared_offer['floors_count'] = int(offer['building']['floorsCount'] or 0.0)
        prepared_offer['build_year'] = int(offer['building']['buildYear'] or 0.0)
        prepared_offer['material_type'] = offer['building']['materialType']
        prepared_offer['coordinates_lat'] = offer['geo']['coordinates']['lat']
        prepared_offer['coordinates_lng'] = offer['geo']['coordinates']['lng']
        prepared_offer['distance_from_center'] = \
            get_distance_from_city_center(offer['geo']['coordinates']['lat'], offer['geo']['coordinates']['lng'])
        prepared_offer['nearest_underground'], prepared_offer['nearest_underground_dist'] \
            = find_nearest_underground(offer['geo']['undergrounds'])
        prepared_offer['balconies_count'] = int(offer['balconiesCount'] or 0.0)
        prepared_offer['floor_number'] = int(offer['floorNumber'] or 0.0)
        prepared_offer['is_by_homeowner'] = bool(offer['isByHomeowner'])
        prepared_offer['price_rur'] = offer['bargainTerms']['priceRur']
        prepared_offer['rooms_count'] = int(offer['roomsCount'] or 0.0)
        offers_to_insert.append(prepared_offer)
    return offers_to_insert


def find_nearest_underground(nearest_stations_list):
    nearest_station = None
    time_to_go = None
    for station in nearest_stations_list:
        if station['transportType'] == 'walk':
            if station['time'] < (time_to_go or 30):
                nearest_station = station['name']
                time_to_go = station['time']
    return nearest_station, time_to_go


def get_distance_from_city_center(lat, lng):
    city_center_lat = 55.755685
    city_center_lng = 37.615689
    earth_radius = 6373.0

    lat1 = math.radians(lat)
    lon1 = math.radians(lng)
    lat2 = math.radians(city_center_lat)
    lon2 = math.radians(city_center_lng)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    # Haversine formula
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return earth_radius * c


def prepare_string_to_send(data):
    msg = ''
    for offer in data:
        if offer["nearest_underground_dist"] and offer["nearest_underground"]:
            msg = msg + f'▪️ <a href="{offer["full_url"]}">{offer["rooms_count"]}-комнатн' + ('ые аппартаменты'
                if offer["is_apartments"] else 'ая квартира') + f'</a> {offer["nearest_underground_dist"]} минут \
                от метро {offer["nearest_underground"]}, {offer["price_rur"]}\
            за {offer["total_area"]} кв м\n\n'
        else:
            msg = msg + f'▪️ <a href="{offer["full_url"]}">{offer["rooms_count"]}-комнатн' + (f'ые аппартаменты'
                if offer["is_apartments"] else f'ая квартира') + \
             f'</a>, {offer["price_rur"]} за {offer["total_area"]} кв м\n\n'
    return msg
