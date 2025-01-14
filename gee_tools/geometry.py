import ee

def create_rectangle(bbox):
    """
    Create a rectangle geometry for Google Earth Engine.

    Parameters:
    bbox (list): [lat_min, lat_max, lon_min, lon_max]
    
    Returns:
    ee.Geometry.Polygon: A polygon geometry representing the rectangle.
    """
    lat_min, lat_max, lon_min, lon_max = bbox
    coords = [
        [lon_min, lat_max],  # Top left
        [lon_max, lat_max],  # Top right
        [lon_max, lat_min],  # Bottom right
        [lon_min, lat_min],  # Bottom left
        [lon_min, lat_max]   # Back to Top left to close the polygon
    ]
    return ee.Geometry.Polygon(coords)