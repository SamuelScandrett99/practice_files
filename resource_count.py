from django.http import JsonResponse
from arches.app.models.resource import Resource
from arches.app.models.models import TileModel
from arches.app.models.graph import Graph
import json


def resourceCount(request):

    '''
    Json page of the numbers of each resource instance
    using a particular resource model.
    '''

    graphIDlist = []
    readableName = []
    counter = {}

    # Go through graphs
    # Select for resources over branches
    # Get graphids and append to list
    graphs = Graph.objects.all()
    for x in graphs:
        if x.isresource == True:
            graphIDlist.append(x.graphid)
	    stringVersion = str(x)
            readableName.append(stringVersion)

    # Have two identical lists, one with the UUID 
    # and one with the human readable name
    # Filter for each UUID in first list and append len of results 
    # to dict with key name as readable from other list 
    for each_id, each_name in zip(graphIDlist, readableName):
        resources = Resource.objects.filter(graph_id = each_id)
        counter[each_name] = len(resources)
       

    # Convert to json
    counter = json.dumps(counter)
    json_counter = json.loads(counter)

    return JsonResponse(json_counter)   
