# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.models import TileModel

# Command class, inherit from arches BaseCommand
class Command(BaseCommand):

    # Self and optional variables required
    def handle (self, *args, **options):

        postcode_list = []
        roadname_list = []

        # Filter only postcode nodegroup id
        tiles = TileModel.objects.filter(nodegroup_id = "83f77cbe-21fc-11ed-9e6f-00155d7d8bf7")
        
        for tile in tiles:
            for key in tile.data.keys():
                if tile.data[key] == 'S1 234':
                    postcode_list.append(tile.resourceinstance_id)


        # Filter for road names   
        # Would like to filter for both coordinates and road name but cant figure out how 
        # .filter(nodegroup_id = x and nodegroup_id = y) doesnt work 
        # nor does (nodegroup_id = x, nodegroup_id = y)
        tiles = TileModel.objects.filter(nodegroup_id = "852d089c-21fc-11ed-9e6f-00155d7d8bf7") 
        loctiles = TileModel.objects.filter(nodegroup_id = "9a778e3e-21fc-11ed-af09-00155d7d8bf7")

        for tile in tiles:
            
            if tile.resourceinstance_id in postcode_list:
                for key in tile.data.keys():
                    if tile.data[key] == 'TestThree Road':
                        tile.data[key] = tile.data[key] + " - Coords Flipped"
                        roadname_list.append(tile.resourceinstance_id)
            
            tile.save()


        for tile in loctiles:

            if tile.resourceinstance_id in roadname_list:
                # Tuple of (UUID: {type: FeatureCollection, features: [{}]})                    
                for mainval in tile.data.values():
                    feature_dict = mainval['features']
                    for nesteddict in feature_dict:
                        # Val was a list that contained a dictionary:
                        # [{'id': '', 'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [-x,y]}, 'properties': {}}]
                        # This unpacked the dictionary so i can obtain values
                        # Find the vales from the geometry key 
                        geom = nesteddict['geometry']
                        # Find the coordinates values from the coordinate key
                        coords = geom['coordinates']

                        # Flip coords
                        newcoords = []
                        newcoords.append(coords[1])
                        newcoords.append(coords[0])
                        geom['coordinates'] = newcoords
            
            
            
            tile.save()

                        

