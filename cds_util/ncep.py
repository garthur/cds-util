import argparse
import xarray as xr
import pandas as pd

NCEP_REMOTE_RESOURCES = {
    'temperature':'https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis/surface/air.sig995.{}.nc'
}

def slice_gridded_data(
        dates=None,
        area=[90, -180, -90, 180],
        round_area_to_grid=False
    ):
    '''
    '''
    # convert longitude to [0,360]
    LONGITUDE_CONSTANT = 180
    area[1] = area[1] + LONGITUDE_CONSTANT
    area[3] = area[3] + LONGITUDE_CONSTANT
    # 
    if round_area_to_grid:
        COORD_GRID = 2.5
        area = [COORD_GRID * round(coord / COORD_GRID) for coord in area]

    def slice_gridded_data_(resource) -> xr.Dataset:
        # open remote resource
        dataset = xr.open_dataset(resource)
        
        # slice by latitude and longitude
        location_slice = dataset.sel(
            lat=slice(area[0], area[2]),
            lon=slice(area[1], area[3])
        )

        # restrict to relevent times
        sliced_dataset = location_slice.sel(time=slice(*dates))

        return sliced_dataset

    return slice_gridded_data_

def get_ncep(
        var='temperature',
        #TODO specify functional defaults for dates
        dates=None,
        area=[90, -180, -90, 180],
        round_area_to_grid=False,
        download_flag=False,
        download_file='./output.nc'
    ) -> xr.Dataset:
    '''Get NCEP/NCAR reanalysis data from NOAA.

    National Centers for Environmental Prediction/National Weather Service/NOAA/U.S. Department of Commerce. 
    1994, updated monthly. NCEP/NCAR Global Reanalysis Products, 1948-continuing. 
    Research Data Archive at NOAA/PSL: /data/gridded/data.ncep.reanalysis.html.

    Parameters
    ----------
    var: str, default temperature
        name of variable to download. corresponding resource must be added to NCEP_REMOTE_RESOURCES
    dates: list of strings, default
    area: list, default [90, 0, -90, 360]
        area extent to download [N, W, S, E]
    round_area_to_grid: True or False, default False

    Returns
    -------
    merged_data: xarrayDataset
        data merged from variouse NCER files, sliced by location and time
    '''

    dates_dt = pd.to_datetime(dates)
    years_in_scope = range(dates_dt[0].year, dates_dt[1].year + 1)

    remote_resources = list(map(
        lambda x: NCEP_REMOTE_RESOURCES[var].format(x), 
        years_in_scope
    ))

    sliced_datasets = list(map(
        slice_gridded_data(dates, area),
        remote_resources
    ))

    merged_data = xr.concat(sliced_datasets, dim="time")

    if download_flag:
        merged_data.to_netcdf(f"{download_file}")

    return merged_data

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--var",
        choices=list(NCEP_REMOTE_RESOURCES.keys())
    )

    parser.add_argument(
        "--dates",
        nargs=2
    )

    parser.add_argument(
        "--area",
        nargs=4,
        type=float,
        default=[90, -180, -90, 180]
    )

    parser.add_argument(
        "--round_area",
        action="store_true"
    )

    parser.add_argument(
        "--outfile",
        default=None
    )

    return parser.parse_args()

def main() -> None:
    args = parse_args()

    _ = get_ncep(
        var=args.var,
        dates=args.dates,
        area=args.area,
        round_area_to_grid=args.round_area,
        download_flag=(args.outfile is not None),
        download_file=args.outfile
    )