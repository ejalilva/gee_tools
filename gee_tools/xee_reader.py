import ee
import xarray as xr
import pandas as pd
from .geometry import create_rectangle
import rioxarray as rio

class XeeDataset:
    """
    A class for handling Google Earth Engine datasets with xarray integration.
    """
    
    def __init__(self, gee_address):
        """
        Initialize the XeeDataset with a Google Earth Engine dataset address.
        
        Parameters:
        gee_address (str): The GEE dataset address
        """
        if not isinstance(gee_address, str):
            raise TypeError("gee_address must be a string")
        self.ee_data = ee.ImageCollection(gee_address)
        self.original_data = self.ee_data

    def ee_bands(self):
        """
        Get basic metadata about the collection's bands.
        
        Returns:
        pandas.DataFrame: DataFrame containing band information
        """
        info = self.ee_data.first().getInfo()
        return pd.DataFrame({'bands': [band['id'] for band in info['bands']] if 'bands' in info else []})

    def ee_subset_time(self, date_range):
        """
        Filter the dataset by date range.
        
        Parameters:
        date_range (list): [start_date, end_date] in YYYY-MM-DD format
        """
        self.ee_data = self.ee_data.filterDate(date_range[0], date_range[1])
        return self

    def ee_crop(self, bbox):
        """
        Crop the dataset to a bounding box.
        
        Parameters:
        bbox (list): [lat_min, lat_max, lon_min, lon_max]
        """
        self.ee_data = self.ee_data.filterBounds(create_rectangle(bbox))
        return self

    def ee_var_sel(self, var):
        """
        Select variables from the dataset.
        
        Parameters:
        var (str): Variable name to select
        """
        self.ee_data = self.ee_data.select(var)
        return self

    def to_xarray(self, scale, var,crs = 'EPSG:4326'):
        """
        Convert to xarray dataset.
        
        Parameters:
        scale (float): spatial resolution, for WGS84 it would be decimal degree e.g. 0.01 ~ 1km 
        var (str): Variable name
        crs (str): coordinate reference system e.g. 'EPSG:4326'
        """
        self.data = xr.open_dataset(self.ee_data, engine='ee', crs=crs, scale=scale)[var]
        return self

    def xr_crop(self, bbox):
        """
        Crop the xarray dataset.
        
        Parameters:
        bbox (list): [lat_min, lat_max, lon_min, lon_max]
        """
        lat_min, lat_max, lon_min, lon_max = bbox
        self.data = self.data.sel(
            lat=slice(lat_min, lat_max),
            lon=slice(lon_min, lon_max)
        )
        return self

    def calculate_monthly_mean(self, month):
        """
        Calculate temporal mean for a specific month.
        
        Parameters:
        month (int): Month number (0-11)
        
        Returns:
        xarray.DataArray: Monthly mean values
        """
        return self.data.groupby('time.month')[month].mean(dim='time')