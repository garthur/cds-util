# Climate Data Science (CDS) Utils

Utilities for downloading datasets related to the climate for personal use.

## ERA5 CLI

Data from ERA5, maintained by the Climate Data Service.

**Example Uses**:

`cds-era5 --dataset reanalysis-era5-single-levels-monthly-means --var 2m_temperature --dates 1996-05-31 2021-09-30 --grid 1.0 1.0 --area 13.55 -59.90 12.82 -59.20 --outfile ./data/brb.nc`

## NCEP/NCAR Reanalysis Data

Data from NCEP/NCAR Reanalysis, provided by NOAA's Physical Sciences Laboratory.

National Centers for Environmental Prediction/National Weather Service/NOAA/U.S. Department of Commerce. 1994, updated monthly. NCEP/NCAR Global Reanalysis Products, 1948-continuing. Research Data Archive at NOAA/PSL: [/data/gridded/data.ncep.reanalysis.html](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html).

**Example Uses**:

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 18.81 -90.28 15.56 -85.97 --outfile ./data/caricom_zone_1.nc`

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 24.42 -85.97 18.81 -78.14 --outfile ./data/caricom_zone_2.nc`

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 27.16 -78.41 17.43 -74.37 --outfile ./data/caricom_zone_3.nc`

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 23.49 -74.37 17.43 -63.78 --outfile ./data/caricome_zone_4.nc`

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 19.17 -63.78 12.67 -58.83 --outfile ./data/caricom_zone_5.nc`

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 12.67 -62.26 5.95 -57.03 --outfile ./data/caricom_zone_6.nc`