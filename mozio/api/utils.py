from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from core.models import Polygon as Polychecked


def check_if_in_polygon(point):
    areas = Polychecked.objects.all()
    contained_areas = []

    for area in areas:
        point = Point(point)
        
        polygon_to_check = Polygon(area)
        
        if polygon_to_check.contains(point):
            contained_areas.append(polygon_to_check)

    return contained_areas


