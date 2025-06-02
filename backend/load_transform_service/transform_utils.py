from pyproj import Transformer

def utm_to_latlon(zone, easting, northing, hemisphere='N'):
    """
    Converts UTM coordinates to geographic coordinates (latitude and longitude in decimal degrees).
    
    Parameters:
        zone (int): UTM zone number (e.g., 17)
        easting (float): Easting coordinate (meters)
        northing (float): Northing coordinate (meters)
        hemisphere (str): 'N' for northern hemisphere, 'S' for southern
    
    Returns:
        (latitude, longitude) in decimal degrees
    """
    # Define the UTM coordinate system
    proj_utm = f"+proj=utm +zone={zone} {'+south' if hemisphere.upper() == 'S' else ''} +datum=WGS84 +units=m +no_defs"

    # Create transformer to convert from UTM to lat/lon (EPSG:4326)
    transformer = Transformer.from_crs(proj_utm, "EPSG:4326", always_xy=True)

    # Perform the transformation
    longitude, latitude = transformer.transform(easting, northing)

    return latitude, longitude


if __name__ == "__main__":
    # Example UTM coordinates
    zone = 30 # Madrid
    st_x = 442703,668178519
    st_y = 4478108,85061351
    hemisphere = 'N'

    latitude, longitude = utm_to_latlon(zone, st_x, st_y, hemisphere)
    print(f"Latitude: {latitude[0]}, Longitude: {longitude[0]}")

