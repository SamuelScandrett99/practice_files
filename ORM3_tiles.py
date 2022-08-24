# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.models import TileModel

from django.db.models import Q

# Command class, inherit from arches BaseCommand
class Command(BaseCommand):
    '''
    Decription:
    Filter all resource instances with the postcode NW2 3QL (7)
    Append to the road name "24/08/22 Coordinates Flipped"
    and flip their coordinates 
    '''
    # Self and optional variables required
    def handle (self, *args, **options):

        postcode_list = []
        roadname_list = []

        # Using Django Q
        # Filter for Postcode, Road name and Location nodegroups
        tiles = TileModel.objects.filter(Q(
            nodegroup_id = "83f77cbe-21fc-11ed-9e6f-00155d7d8bf7") | Q(
            nodegroup_id = "852d089c-21fc-11ed-9e6f-00155d7d8bf7") | Q(
            nodegroup_id = "9a778e3e-21fc-11ed-af09-00155d7d8bf7"))
        
        # Through the tiles, set key to the UUID for postcode
        # If the key is in the data dictionary then specify the value postcode
        # Then append resourceinstance_id to list
        # Saving looping through every key in data
        for tile in tiles:
            key = "83f77cbe-21fc-11ed-9e6f-00155d7d8bf7"
            if key in tile.data:
                if tile.data[key] == 'NW2 3QL':
                    postcode_list.append(tile.resourceinstance_id)


            # For those reource instances with the postcode NW2 3QL
            if tile.resourceinstance_id in postcode_list:

                # Add text to the road name
                key_rn = "852d089c-21fc-11ed-9e6f-00155d7d8bf7"
                if key_rn in tile.data:
                    tile.data[key_rn] = tile.data[key_rn] + " 24/08/22 Coordinates Flipped"

            
                # Find coordinates within location
                key_loc = "9a778e3e-21fc-11ed-af09-00155d7d8bf7"
                if key_loc in tile.data:
                    for val in tile.data.values():
                        feature = val['features']
                        for nesteddict in feature:
                            geom = nesteddict['geometry']         
                            coords = geom['coordinates']    

                            #Flip coords
                            newcoords = []
                            newcoords.append(coords[1])
                            newcoords.append(coords[0])
                            geom['coordinates'] = newcoords
            

            tile.save()