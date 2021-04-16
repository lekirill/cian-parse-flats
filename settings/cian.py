import os

CIAN_URL_TO_REQUEST = os.getenv('CIAN_URL_TO_REQUEST') or 'https://api.cian.ru/search-offers/v2/search-offers-desktop/'

CIAN_PAYLOAD = os.getenv('CIAN_URL_TO_REQUEST') or {
    "jsonQuery": {
        "region": {
            "type": "terms",
            "value": [
                1  # Moscow
            ]
        },
        "_type": "flatsale",  # flat sale
        "engine_version": {
            "type": "term",
            "value": 2
        },
        "room": {
            "type": "terms",
            "value": [
                1,  # 1 room
                2,  # 2 room
                3,  # 3 room
                4,  # 4 room
                5,  # 5 room
                6,  # 6 room
                9,  # studio
                7  # free space
            ]
        },
        "total_area": {
            "type": "range",
            "value": {
                "gte": 62
            }
        },
        "is_first_floor": {
            "type": "term",
            "value": False
        },
        "not_last_floor": {
            "type": "term",
            "value": True
        },
        "house_year": {
            "type": "range",
            "value": {
                "gte": 2018,
                "lte": 2021
            }
        },
        "publish_period": {
            "type": "term",
            "value": 3600  # за последний час
        },
        "price": {
            "type": "range",
            "value": {
                "lte": 15_000_000
            },

        },
        "is_by_homeowner": {
            "type": "term",
            "value": False
        },
        # "building_status": {
        #     "type": "term",
        #     "value": 1  # 1 secondary market / 2 - new buildings  / remove block - both
        # },
        "repair": {
            "type": "terms",
            "value": [
                # 1, # no repair
                2,  # cosmetic repair
                3,  # euro repair
                4  # designers repair
            ]
        },
        # # search only flats
        # "only_flat": {
        #     "type": "term",
        #     "value": True
        # },
        # # search only appartments
        # "apartment": {
        #     "type": "term",
        #     "value": True
        # }
    }
}
