import string
import json

# raytracing algorithm
def is_point_inside_polygon(pt, vs):
    x, y = pt
    inside = False
    j = len(vs) - 1
    for i in range(len(vs)):
        xi, yi = vs[i]
        xj, yj = vs[j]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
        j = i
    return inside

def uace20_at_point(pt):
    f = open('tl_2020_us_uac20-5pct.json', 'r')
    for line in f:
        try:
            feature = json.loads(line.strip(string.whitespace + ','))
        except json.JSONDecodeError:
            continue
        if feature['geometry']['type'] == 'Polygon':
            polys = [feature['geometry']['coordinates']]
        elif feature['geometry']['type'] == 'MultiPolygon':
            polys = feature['geometry']['coordinates']
        for poly in polys:
            if is_point_inside_polygon(pt, poly[0]):
                return feature['properties']['UACE20']
    f.close()

print(uace20_at_point([-84.5, 39]))
