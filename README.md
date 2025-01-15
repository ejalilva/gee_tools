# GEE Tools

A Python package for working with Google Earth Engine data using xarray integration.

## Prerequisites

Before installing this package, make sure you have:
1. A Google Earth Engine account
2. Python 3.7 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ejalilva/gee_tools 
cd gee_tools
```

2. Install the package and all its dependencies:
```bash
pip install -e . # note the "." at the end
```
This will automatically install all required dependencies including `earthengine-api`, `xee`, and other required packages.

3. Authenticate with Earth Engine (only needed once):
```bash
earthengine authenticate
```

## Usage

Basic example of using the package:

```python
from gee_tools import initialize_gee, XeeDataset

# Initialize Earth Engine with your project
initialize_gee('your-project-id')

# Create dataset instance
dataset = XeeDataset('MODIS/061/MOD13A2')

# Define your region of interest
bbox = [lat_min, lat_max, lon_min, lon_max]  # [24.4, 49.4, -125.0, -66.9] for CONUS

# Chain operations for data processing
result = (dataset
          .ee_subset_time(['2020-01-01', '2020-12-31'])
          .ee_crop(bbox)
          .ee_var_sel('NDVI')
          .to_xarray(0.01, 'NDVI')
          .xr_crop(bbox))

# Access the data
result.data
```

## Examples

Check the `examples` folder for Jupyter notebooks demonstrating:
- Basic usage with MODIS NDVI data
- Working with SMAP soil moisture data
- Custom data processing workflows

## Package Structure

```
project_root/
├── gee_tools/
│   ├── __init__.py
│   ├── auth.py        # Authentication utilities
│   ├── geometry.py    # Geometric operations
│   └── xee_reader.py  # Main dataset handling class
├── examples/
│   └── example_usage.ipynb  # Jupyter notebook with usage examples
├── README.md         # Package documentation
├── LICENSE          # License file
├── .gitignore       # Git ignore file
└── setup.py         # Package installation and dependencies
```

## Contributing

Feel free to submit issues and enhancement requests!
