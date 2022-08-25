from django.http import JsonResponse
from arches.app.models.resource import Resource
from arches.app.models.models import TileModel

import json


def parkingType(request):

    '''
    Decription:
    Count the numbers of each type of parking 
    e.g. disabled, permit holder only etc
    Store data as Json
    '''

    tiles = TileModel.objects.filter(nodegroup_id = "40adf37a-21fc-11ed-a389-00155d7d8bf7")

    counter = {}

    # Create dict counter
    for tile in tiles:
        for val in tile.data.values():
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1

    # Convert to json
    counter = json.dumps(counter)
    json_counter = json.loads(counter)


    return JsonResponse(json_counter)   
