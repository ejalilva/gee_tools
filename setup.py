from setuptools import setup, find_packages

setup(
    name="gee_tools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'earthengine-api',
        'google-auth',
        'xarray',
        'pandas',
        'matplotlib',
	'xee'
    ],
    author="Ehsan Jalilvand",
    description="A package for handling Google Earth Engine data with xarray integration",
)
