# CDS Utils

Utilities for climate data science.

## ERA5 CLI

Example Uses:
`cds-era5 --dataset reanalysis-era5-single-levels-monthly-means --var 2m_temperature --dates 1996-05-31 2021-09-30 --grid 1.0 1.0 --area 13.55 -59.90 12.82 -59.20 --outfile ./data/brb.nc`
`cds-era5 --dataset reanalysis-era5-pressure-levels --var temperature --dates 1996-05-31 2021-09-30 --grid 1.0 1.0 --area 19.11 -65.6 9.83 -58.82 --outfile ./data/lesser_antilles.nc`
`cds-era5 --dataset reanalysis-era5-pressure-levels --var temperature --dates 1996-05-31 2021-09-30 --grid 1.0 1.0 --area 23.73 -85.05 17.13 -65.59 --outfile ./data/greater_antilles.nc`