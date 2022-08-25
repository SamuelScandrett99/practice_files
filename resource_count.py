from django.http import JsonResponse
from arches.app.models.resource import Resource
from arches.app.models.models import TileModel

import json


def resourceCount(request):

    '''
    Json page of the numbers of each resource instance
    using a particular resource model.
    '''

    # UUID for CarParkingV3_Address  : a634604a-21fb-11ed-af4b-00155d7d8bf7
    # UUID for TreeTypes             : 3edf41ac-2459-11ed-81ce-00155d7d8122

    counter = {}

    resources = Resource.objects.all()
    for res in resources:
        key = 'graph_id'
        dictview = vars(res)
        
        if key in dictview:
            # UUID was type UUID so wouldnt match unless converted to string
            strval = str(dictview[key])

            if strval == "a634604a-21fb-11ed-af4b-00155d7d8bf7":
                # Adds the readable name to the dict 
                # Adds with 1 as the else will not be registered after first if
                # therefore one is not missed out
                if "CarParkingV3_Address" not in counter:
                    counter["CarParkingV3_Address"] = 1  
                else:
                    counter["CarParkingV3_Address"] += 1             
                

            elif strval == "3edf41ac-2459-11ed-81ce-00155d7d8122":
                if "TreeType" not in counter:
                    counter["TreeType"] = 1  
                else:
                    counter["TreeType"] += 1            

    # Convert to json
    counter = json.dumps(counter)
    json_counter = json.loads(counter)

    return JsonResponse(json_counter)   
