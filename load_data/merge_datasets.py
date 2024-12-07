import numpy as np
import pandas as pd
import os
import xarray as xr
import datetime
from load_data import load_vel_files, load_cal_files, tools, convert


def dir_list_CTD(input_dir):
    '''create a list with all the directories that contain the CTD data'''
    dir_list_CTD = []
    for root, dirs,files in os.walk(input_dir):
        if 'CTD' in dirs: 
            dir_list_CTD.append(os.path.join(root, 'CTD'))
    dir_list_CTD.sort()
    for i in dir_list_CTD:
        if 'Created_files' in i:
            dir_list_CTD.remove(i)
    return dir_list_CTD

def dir_list_ADCP(input_dir):
    ### create a list with all the directories that contain the LADCP data
    dir_list_ADCP = []
    for root, dirs,files in os.walk(input_dir):
        if 'FINAL_ADCP_PRODUCTS' and 'ladcp_velfiles' in dirs: 
            dir_list_ADCP.append(os.path.join(root, 'ladcp_velfiles'))
        if 'FINAL_ADCP_PRODUCTS' and 'LADCP_velfiles' in dirs:
            dir_list_ADCP.append(os.path.join(root, 'LADCP_velfiles'))
    dir_list_ADCP.sort()
    ### exclude the 2019_12 path since it is empty
    for i in dir_list_ADCP:
        if '2019_12' in i:
            dir_list_ADCP.remove(i)
    return dir_list_ADCP


def create_coordinates_with_ADCPtimes(cal_dir, input_dir=None):
    '''create the coordinates for the calibration data with the time from the ADCP data.'''
    if not isinstance(input_dir, str):
        config = tools.get_config()
        input_dir = config['input_dir']
    year = cal_dir[-11:-4]
    for j in dir_list_ADCP(input_dir):
        if year in j:
            _,coords_ADCP,_ = load_vel_files.create_coordinates(j)
            coords_CTD = load_cal_files.create_coordinates(cal_dir)
            for coords_i in coords_ADCP:
                Cast = coords_i[0] 
                for coords_j in coords_CTD:
                    if Cast == coords_j[0]:
                        coords_j[3] = coords_i[2]
                        break
                    else:
                        continue
            coordinates = coords_CTD
    return coordinates

def create_CTD_Dataset_with_ADCPtimes(cal_dir, config=None):
    """Create a xr.Dataset from the calibration data files in a directory.
    """
    if not isinstance(config, dict):
        config = tools.get_config()
    cal_list = load_cal_files.load_cal_from_file(cal_dir)
    coordinates = create_coordinates_with_ADCPtimes(cal_dir)

    nc_list = []
    Cast = np.zeros(len(coordinates))
    Lat = np.zeros(len(coordinates))
    Lon = np.zeros(len(coordinates))
    time_flag = np.zeros(len(coordinates))
    for i in range(len(cal_list)):
        cal_list[i].insert(loc=0, column='DATETIME', value=np.full(len(cal_list[i]),datetime.datetime.strptime(coordinates[i][3], '%Y-%m-%d %H:%M:%S')))
        nc_list.append(cal_list[i].set_index(['DATETIME','pr']).to_xarray())
        Cast[i] = coordinates[i][0]
        Lat[i] = coordinates[i][1]
        Lon[i] = coordinates[i][2]
        time_flag[i] = coordinates[i][4]
    ds = xr.concat(nc_list, dim='DATETIME')
    ### assign Longitude, Latitude as coordinates and the Cast number as a variable
    ds.coords['latitude'] = ('DATETIME', Lat)
    ds.coords['longitude'] = ('DATETIME', Lon)
    ds = ds.assign({'TIME_FLAG': ('DATETIME', time_flag)})
    ds = ds.assign({'CAST': ('DATETIME', Cast)})
    ### Add a string variable for each datetime which is the string 'GC_YYYY_MM' from the string cal_dir
    gc_string = [s for s in cal_dir.split('/') if s.startswith('GC')][0]
    gc_string = gc_string[:10]
    ds['gc_string'] = ('DATETIME', [gc_string] * len(ds['DATETIME']))

    ### add attributes and variable information
    ds,_ = convert.process_dataset(ds, config)
    ### sort the dataset by longitude
    ds = ds.sortby('LONGITUDE')
    return ds



def merge_datasets(cal_dir, vel_dir, config=None):
    """Merge velocity and calibration data into a single xarray dataset.
    """
    if not isinstance(config, dict):
        config = tools.get_config()
    ds_CTD = create_CTD_Dataset_with_ADCPtimes(cal_dir, config)
    ds_ADCP = load_vel_files.create_Dataset(vel_dir, config)
    ## change coordinates name of PRES to DEPTH for ADCP data
    ds_CTD = ds_CTD.rename({'PRES': 'DEPTH'})
    ## merge the two datasets
    ds_merge = xr.merge([ds_CTD, ds_ADCP], compat='override')
    ### change their attributes
    ds_merge.attrs['title'] = 'CTD and LADCP data of the Abaco Cruise'
    ds_merge.attrs['platform'] = 'CTD and Lowered Acoustic Doppler Current Profilers (LADCP)'
    return ds_merge
    
