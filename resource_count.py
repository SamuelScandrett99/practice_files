from django.http import JsonResponse
from arches.app.models.resource import Resource
from arches.app.models.models import TileModel
from arches.app.models.graph import Graph
from arches.settings import SYSTEM_SETTINGS_RESOURCE_ID
import json


def resource_count(request):

    '''
    Json page of the numbers of each resource instance
    using a particular resource model.
    '''

    graph_id_list = []
    readable_name_list = []
    counter = {}

    # Go through graphs
    # Select for resources over branches
    # Get graphids and append to list
    graphs = Graph.objects.all()
    for x in graphs:
        if x.isresource == True and str(x.graphid) != "ff623370-fa12-11e6-b98b-6c4008b05c4c":
            graph_id_list.append(x.graphid)
            string_version = str(x)
            readable_name_list.append(string_version)
            

    # Have two identical lists, one with the UUID 
    # and one with the human readable name
    # Filter for each UUID in first list and append len of results 
    # to dict with key name as readable from other list 
    for each_id, each_name in zip(graph_id_list, readable_name_list):
        resources = Resource.objects.filter(graph_id = each_id)
        counter[each_name] = len(resources)
       

    # Convert to json
    counter = json.dumps(counter)
    json_counter = json.loads(counter)

    return JsonResponse(json_counter)   
