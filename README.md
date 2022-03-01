# CDS Utils

Utilities for climate data science.

## ERA5 CLI

Example Uses:
`cds-era5 --dataset reanalysis-era5-single-levels-monthly-means --var 2m_temperature --dates 1996-05-31 2021-09-30 --grid 1.0 1.0 --area 13.55 -59.90 12.82 -59.20 --outfile ./data/brb.nc`

## NCEP/NCAR Reanalysis Data

National Centers for Environmental Prediction/National Weather Service/NOAA/U.S. Department of Commerce. 1994, updated monthly. NCEP/NCAR Global Reanalysis Products, 1948-continuing. Research Data Archive at NOAA/PSL: [/data/gridded/data.ncep.reanalysis.html](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html).

`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 19.11 -65.6 9.83 -58.82 --outfile ./data/lesser_antilles.nc`
`cds-ncep --var temperature --dates 1996-05-31 2021-09-30 --area 23.73 -85.05 17.13 -65.59 --outfile ./data/greater_antilles.nc`