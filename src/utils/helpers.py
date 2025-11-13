import ee
import pandas as pd
from datetime import datetime

def initialize_ee():
    """Initialize Earth Engine"""
    try:
        ee.Initialize()
        print("✅ Earth Engine ready")
    except:
        print("❌ Run: ee.Authenticate() first")
        raise

def calculate_ndwi(image):
    """NDWI = (Green - NIR) / (Green + NIR)
    
    Args:
        image: ee.Image - Input Sentinel-2 image
        
    Returns:
        ee.Image with NDWI band added
    """
    return image.normalizedDifference(['B3', 'B8']).rename('NDWI')

def calculate_mndwi(image):
    """MNDWI = (Green - SWIR) / (Green + SWIR)
    
    Args:
        image: ee.Image - Input Sentinel-2 image
        
    Returns:
        ee.Image with MNDWI band added
    """
    return image.normalizedDifference(['B3', 'B11']).rename('MNDWI')

def calculate_ndvi(image):
    """NDVI = (NIR - Red) / (NIR + Red)
    
    Args:
        image: ee.Image - Input Sentinel-2 image
        
    Returns:
        ee.Image with NDVI band added
    """
    return image.normalizedDifference(['B8', 'B4']).rename('NDVI')

def get_sentinel2_collection(start_date, end_date, geometry, cloud_percentage=20):
    """Get Sentinel-2 surface reflectance collection
    
    Args:
        start_date: str - Start date in 'YYYY-MM-DD' format
        end_date: str - End date in 'YYYY-MM-DD' format
        geometry: ee.Geometry - Area of interest
        cloud_percentage: int - Maximum cloud cover percentage (0-100)
        
    Returns:
        ee.ImageCollection of filtered Sentinel-2 images
    """
    collection = (ee.ImageCollection('COPERNICUS/S2_SR')
                 .filterDate(start_date, end_date)
                 .filterBounds(geometry)
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloud_percentage))
                 .select(['B2', 'B3', 'B4', 'B8', 'B11', 'QA60']))
    
    return collection

def add_water_indices(image):
    """Add water and vegetation indices to an image"""
    ndwi = calculate_ndwi(image)
    mndwi = calculate_mndwi(image)
    ndvi = calculate_ndvi(image)
    
    return image.addBands([ndwi, mndwi, ndvi])

def mask_clouds(image):
    """Mask clouds and cloud shadows"""
    qa = image.select('QA60')
    
    # Bits 10 and 11 are clouds and cirrus, respectively
    cloud_bitmask = 1 << 10
    cirrus_bitmask = 1 << 11
    
    # Both flags should be set to zero, indicating clear conditions
    mask = qa.bitwiseAnd(cloud_bitmask).eq(0) \
           .And(qa.bitwiseAnd(cirrus_bitmask).eq(0))
    
    return image.updateMask(mask)
