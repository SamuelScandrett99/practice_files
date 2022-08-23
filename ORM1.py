# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource

# Command class, inherit from arches BaseCommand
class Command(BaseCommand):

    # Self and optional variables required
    def handle (self, *args, **options):

        # Get all resources 
        resources = Resource.objects.all()

        # List for resource instances with the postcode NW1 1NJ
        res_id = []

        # For each object in resources (consist of resourceinstanceid, graphid, tiles etc followed by UUID)
        for res in resources:
            # Load the tiles object (where report information stored)
            res.load_tiles() 

            # For each tile (consists resourceinstance_id, nodegroup_id, data etc followed by UUID)
            for tile in res.tiles:
                print(vars(tile))
                # tile.data (data is dictionary) conisists of key UUID and value of the data e.g. {'x': 'Road Name Av'}  
                # For each of the keys in the dictionary so printing each key (UUID)            
                for key in tile.data.keys():
                    # UUID for postcode nodegroup = 415a032a-1ca9-11ed-be51-00155df90ec4
                    # If the key is equal, and thus the nodegroup for postcode
                    if key == '415a032a-1ca9-11ed-be51-00155df90ec4':
                        # If the postcode dictionary value is NW1 1NJ
                        if tile.data[key] == "NW1 1NJ":
                            # Append to res_id list
                            res_id.append(tile.resourceinstance_id)

                            
                            

            # If the resource UUID == whats stored ie the resources have the postcode NW1 1NJ
            if res.resourceinstanceid in res_id:
                
                # Go through each tile
                for tile in res.tiles:
                    # Go through all keys in data dictionary
                    for key in tile.data.keys():
                        # Road name UUID = 41dca2d0-1ca9-11ed-be51-00155df90ec4 
                        # If the UUID key is equal to road name key
                        if key == "41dca2d0-1ca9-11ed-be51-00155df90ec4":
                            # Add text to dict value
                            tile.data[key] = tile.data[key] + " - I've been here"
                            
                    # Save updated tiles
                    #tile.save()

                        

