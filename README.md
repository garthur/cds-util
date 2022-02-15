# CDS Utils

Utilities for climate data science.

## ERA5 CLI

Example Uses:
`cds-era5 --dataset reanalysis-era5-single-levels --var 2m_temperature --dates 1996-05-31 --grid 0.25 0.25 --area 13.55 -59.90 12.82 -59.20 --outfile ./brb.nc`
`cds-era5 --dataset reanalysis-era5-single-levels-monthly-means --var 2m_temperature --dates 2021-02-01 --grid 0.25 0.25 --dry_run`