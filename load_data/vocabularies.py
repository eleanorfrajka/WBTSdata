dims_rename_dict = {'sg_data_point': 'N_MEASUREMENTS'}

# Specify the preferred units, and it will convert if the conversion is available in unit_conversion
preferred_units = ['m s-1', 'dbar', 'S m-1']

# String formats for units.  The key is the original, the value is the desired format
unit_str_format = {
    'm/s': 'm s-1',
    'cm/s': 'cm s-1',
    'S/m': 'S m-1',
    'meters': 'm',
    'degrees_Celcius': 'Celcius'
}

# Various conversions from the key to units_name with the multiplicative conversion factor
unit_conversion = {
    'cm/s': {'units_name': 'm/s', 'factor': 0.01},
    'cm s-1': {'units_name': 'm s-1', 'factor': 0.01},
    'm/s': {'units_name': 'cm/s', 'factor': 100},
    'm s-1': {'units_name': 'cm s-1', 'factor': 100},
    'S/m': {'units_name': 'mS/cm', 'factor': 0.1},
    'S m-1': {'units_name': 'mS cm-1', 'factor': 0.1},
    'mS/cm': {'units_name': 'S/m', 'factor': 10},
    'mS cm-1': {'units_name': 'S m-1', 'factor': 10},
    'dbar': {'units_name': 'Pa', 'factor': 10000},
    'Pa': {'units_name': 'dbar', 'factor': 0.0001},
    'dbar': {'units_name': 'kPa', 'factor': 10},
}

# Based on https://github.com/voto-ocean-knowledge/votoutils/blob/main/votoutils/utilities/vocabularies.py
standard_names = {
    "latitude": "LATITUDE",
    "longitude": "LONGITUDE",
    "gps_lat": "LATITUDE_GPS",
    "gps_lon": "LONGITUDE_GPS",
    "gps_time": "TIME_GPS",
    "ctd_time": "TIME",
    "eng_pitchAng": "PITCH",
    "eng_rollAng": "ROLL",
    "eng_head": "HEADING",
    "ctd_depth": "DEPTH",
    "pressure": "PRES",
    "conductivity": "CNDC",  #Conductivity corrected for anomalies
#    "oxygen_concentration": "DOXY",
#    "chlorophyll": "CHLA",
    "temperature": "TEMP",
    "salinity": "PSAL",
#    "salinity_raw": "PSAL_RAW",
#    "temperature_raw": "TEMP_RAW",
#    "conductivity_raw": "CNDC_RAW",
    "ctd_density": "POTDENS0", # Seawater potential density - need to check standard name for sigma
    "profile_index": "PROFILE_NUMBER",
    "vert_speed": "GLIDER_VERT_VELO_MODEL",
    "horz_speed": "GLIDER_HORZ_VELO_MODEL",
    "speed": "GLIDE_SPEED",
    "glide_angle": "GLIDE_ANGLE"
#    "adcp_Pressure": "PRES_ADCP",
#    "particulate_backscatter": "BBP700",
#    "backscatter_scaled": "BBP700",
#    "backscatter_raw": "RBBP700",
#    "potential_temperature": "THETA",
#    "down_irradiance_380": "ED380",
#    "down_irradiance_490": "ED490",
#    "downwelling_PAR": "DPAR",
#    "temperature_oxygen": "TEMP_OXYGEN",
#    "potential_density": "POTDENS0",
#    "chlorophyll_raw": "FLUOCHLA",
#    "ad2cp_pitch": "AD2CP_PITCH",
#    "ad2cp_roll": "AD2CP_ROLL",
#    "ad2cp_heading": "AD2CP_HEADING",
#    "ad2cp_time": "AD2CP_TIME",
#    "ad2cp_pressure": "AD2CP_PRES",
#    "turbidity": "TURB",
#    "cdom": "CDOM",
#    "cdom_raw": "FLUOCDOM",
#    "phycoerythrin": "PHYC",
#    "phycoerythrin_raw": "FLUOPHYC",
#    "tke_dissipation_shear_1": "EPSIFY01",
#    "tke_dissipation_shear_2": "EPSIFY02",
}

vars_to_remove = [
    'dissolved_oxygen_sat',
    'depth', 
    'eng_depth',
    'eng_elaps_t',
    'eng_elaps_t_0000',
    'latitude_gsm',
    'longitude_gsm',
    'sigma_t',
    'sigma_theta',
    'sound_velocity',
    'theta',
    'time',
    'eng_sbect_condFreq',
    'eng_sbect_tempFreq',
    'glide_angle_gsm',
    'horz_speed_gsm',
    'north_displacement_gsm',
    'east_displacement_gsm',
    'speed_gsm',
    'vert_speed_gsm',
    'dive_num_cast',
    'density'
]

vocab_attrs = {
    "LATITUDE": {
        "coordinate_reference_frame": "urn:ogc:crs:EPSG::4326",
        "long_name": "Latitude north",
        "observation_type": "measured",
        "platform": "platform",
        "reference": "WGS84",
        "standard_name": "latitude",
        "units": "degrees_north",
        "valid_max": 90,
        "valid_min": -90,
        "axis": "Y",
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/LAT/",
    },
    "LONGITUDE": {
        "coordinate_reference_frame": "urn:ogc:crs:EPSG::4326",
        "long_name": "Longitude east",
        "observation_type": "measured",
        "platform": "platform",
        "reference": "WGS84",
        "standard_name": "longitude",
        "units": "degrees_east",
        "valid_max": 180,
        "valid_min": -180,
        "axis": "X",
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/LON/",
    },
    "DATETIME": {
        "long_name": "time of measurement",
#        "units": "seconds since 1970-01-01T00:00:00Z",
        "observation_type": "measured",
        "standard_name": "time",
        "URI": "https://vocab.nerc.ac.uk/collection/P02/current/AYMD/",
    },
    "DEPTH": {
        "source": "pressure",
        "long_name": "glider depth",
        "standard_name": "depth",
        "units": "m",
        "comment": "from science pressure and interpolated",
        "sensor": "sensor_ctd",
        "observation_type": "calculated",
        "accuracy": 1,
        "precision": 2,
        "resolution": 0.02,
        "platform": "platform",
        "valid_min": 0,
        "valid_max": 2000,
        "reference_datum": "surface",
        "positive": "down",
    },
    "DEPTH_Z": {
        "source": "pressure",
        "long_name": "glider depth",
        "standard_name": "depth",
        "units": "m",
        "comment": "Defined with positive up",
        "sensor": "sensor_ctd",
        "observation_type": "calculated",
        "platform": "platform",
        "valid_min": -4000,
        "valid_max": 0,
        "reference_datum": "surface",
        "positive": "up",
    },
    "DOXY": {
        "long_name": "oxygen concentration",
        "observation_type": "calculated",
        "standard_name": "mole_concentration_of_dissolved_molecular_oxygen_in_sea_water",
        "units": "mmol m-3",
        "valid_max": 425,
        "valid_min": 0,
        "URI": "https://vocab.nerc.ac.uk/collection/P02/current/DOXY/",
    },
    "PRES": {
        "comment": "ctd pressure sensor",
        "sensor": "sensor_ctd",
        "long_name": "Pressure (spatial coordinate) exerted by the water body by profiling pressure sensor and "
        "correction to read zero at sea level",
        "observation_type": "measured",
        "positive": "down",
        "reference_datum": "sea-surface",
        "standard_name": "sea_water_pressure",
        "units": "dbar",
        "valid_max": 2000,
        "valid_min": 0,
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/PRES",
    },
    "PSAL": {
        "long_name": "water salinity",
        "standard_name": "sea_water_practical_salinity",
        "units": "1e-3",
        "comment": "Practical salinity of the water body by CTD and computation using UNESCO 1983 algorithm",
        "sources": "CNDC, TEMP, PRES",
        "observation_type": "calculated",
        "sensor": "sensor_ctd",
        "valid_max": 40,
        "valid_min": 0,
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/PSAL/",
    },
    "TEMP": {
        "long_name": "Temperature of the water body by CTD ",
        "observation_type": "measured",
        "standard_name": "sea_water_temperature",
        "units": "Celsius",
        "valid_max": 42,
        "valid_min": -5,
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/TEMP/",
    },
    "THETA": {
        "long_name": "Potential temperature of the water body by computation using UNESCO 1983 algorithm.",
        "observation_type": "calculated",
        "sources": "salinity temperature pressure",
        "standard_name": "sea_water_potential_temperature",
        "units": "Celsius",
        "valid_max": 42,
        "valid_min": -5,
        "URI": "https://vocab.nerc.ac.uk/collection/OG1/current/THETA/",
    },
    "PROFILE_NUMBER": {
        "long_name": "profile index",
        "units": "1",
    },
}

# Various sensor vocabularies for OG1: http://vocab.nerc.ac.uk/scheme/OG_SENSORS/current/
sensor_vocabs = {
    "Seabird unpumped CTD": {
        "sensor_type": "CTD",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/130/",
        "sensor_maker": "Sea-Bird Scientific",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",
        "sensor_model": "Sea-Bird CT Sail CTD",
        "sensor_model_vocabulary": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL1188/",
        "long_name": "Sea-Bird CT Sail CTD",
    },
    "RBR legato CTD": {
         "sensor_type": "CTD",
         "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/130/",
         "sensor_maker": "RBR",
         "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0049/",
         "sensor_model": "RBR Legato3 CTD",
         "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1745/",
         "long_name": "RBR Legato3 CTD",
    },
    "Wetlabs BB2FL-VMT": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} ECO BB2FL-VMT backscattering fluorescence sensor",
        "sensor_model_vocabulary": "https://http://vocab.nerc.ac.uk/collection/L22/current/TOOL1310/",
        "long_name": "WET Labs ECO BB2FL-VMT",
    },
    "Wetlabs FLBBCD": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} ECO FLBBCD scattering fluorescence sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1141/",
        "long_name": "WET Labs ECO-FLBBCD",
    },
    "Wetlabs FLBBPC": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} ECO Puck Triplet FLBBPC scattering fluorescence sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1904/",
        "long_name": " WET Labs ECO FLBBPC",
    },
    "Wetlabs FLBBPE": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} ECO Triplet sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL0674/",
        "long_name": "WET Labs ECO-FLBBCE",
    },
    "Wetlabs FLNTU": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} ECO FLNTU combined fluorometer and turbidity sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL0215/",
        "long_name": " WET Labs ECO FLNTU",
    },
    "Nortek AD2CP": {
        "sensor_type": "ADVs and turbulence probes",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/384/",
        "sensor_maker": "Nortek",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0068/",
        "sensor_model": "Nortek Glider1000 AD2CP Acoustic Doppler Current Profiler",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1774/",
        "long_name": "Nortek AD2CP",
    },
    "JFE Advantech AROD_FT": {
        "sensor_type": "dissolved gas sensors",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/351/",
        "sensor_maker": "JFE Advantech",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0053/",
        "sensor_model": "JFE Advantech Rinko FT ARO-FT oxygen sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1783/",
        "long_name": "JFE Rinko ARO-FT",
    },
    "RBR coda TODO": {
        "sensor_type": "dissolved gas sensors",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/351/",
        "sensor_maker": "RBR",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0049/",
        "sensor_model": "RBR Coda T.ODO Temperature and Dissolved Oxygen Sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1783/",
        "long_name": "RBR Coda T.ODO",
    },
    "SeaBird OCR504": {
        "sensor_type": "radiometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/122/",
        "sensor_maker": "Sea-Bird Scientific",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",
        "sensor_model": "Satlantic {Sea-Bird} OCR-504 multispectral radiometer",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL0625/",
        "long_name": "Sea-Bird OCR-504 ",
    },
    "Seabird Deep SUNA": {
        "sensor_type": "nutrient analysers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/181/",
        "sensor_maker": "Sea-Bird Scientific",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",
        "sensor_model": "Satlantic {Sea-Bird} Submersible Ultraviolet Nitrate Analyser V2 (SUNA V2) nutrient analyser series",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1562/",
        "long_name": "Sea-Bird SUNA ",
    },
    "Franatech METS": {
        "sensor_type": "dissolved gas sensors",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/351/",
        "sensor_maker": "Franatech",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0303/",
        "sensor_model": "Franatech METS Methane Sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1244/",
        "long_name": "Franatech METS Methane Sensor ",
    },
    "Biospherical MPE-PAR": {
        "sensor_type": "radiometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/122/",
        "sensor_maker": "Biospherical Instruments",
        "sensor_maker_vocabulary": "http://vocab.nerc.ac.uk/collection/L35/current/MAN0028/",
        "sensor_model": "Biospherical PAR sensor (UnSpec model)",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1254/",
        "long_name": "Biospherical PAR sensor",
    },
    "Rockland Scientific MR1000G-RDL": {
        "sensor_type": "microstructure sensors",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/184/",
        "sensor_maker": "Rockland Scientific",
        "sensor_maker_vocabulary": "http://vocab.nerc.ac.uk/collection/L35/current/MAN0022/",
        "sensor_model": "Rockland MicroRider-1000",
        "sensor_model_vocabulary": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL1232/",
        "long_name": "Rockland MicroRider-1000",
    },
    "Seabird SlocumCTD": {
        "sensor_type": "CTD",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/130/",
        "sensor_maker": "Sea-Bird Scientific",
        "sensor_maker_vocabulary": "http://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",
        "sensor_model": "Sea-Bird Slocum Glider Payload {GPCTD} CTD",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1492/",
        "long_name": "Sea-Bird Slocum CTD",
    },
    "SeaOWL UV-A": {
        "sensor_type": "fluorometers",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/113/",
        "sensor_maker": "WET Labs",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0026/",
        "sensor_model": "WET Labs {Sea-Bird WETLabs} SeaOWL UV-A Sea Oil-in-Water Locator",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL1766/",
        "long_name": "WET Labs SeaOWL",
    },
    "Seabird SBE43F": {
        "sensor_type": "dissolved gas sensors",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/351/",
        "sensor_maker": "Sea-Bird Scientific",
        "sensor_maker_vocabulary": "http://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",
        "sensor_model": "Sea-Bird SBE 43F Dissolved Oxygen Sensor",
        "sensor_model_vocabulary": "https://vocab.nerc.ac.uk/collection/L22/current/TOOL0037/",
        "long_name": "Sea-Bird SBE 43F",
    },
    "Gill Instruments GMX560": {
        "sensor_type": "meteorological packages",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/102/",
        "sensor_maker": "Gill Instruments",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0121/",
        "sensor_model": "Gill Instruments MaxiMet Marine GMX560 weather station",
        "sensor_model_vocabulary": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL2098/",
        "long_name": "Gill Instruments MaxiMet Marine GMX560 weather station",
    },
    "Datawell MOSE-G1000": {
        "sensor_type": "wave recorders",
        "sensor_type_vocabulary": "https://vocab.nerc.ac.uk/collection/L05/current/110/",
        "sensor_maker": "Datawell B.V.",
        "sensor_maker_vocabulary": "https://vocab.nerc.ac.uk/collection/L35/current/MAN0124/",
        "sensor_model": "Datawell MOSE-G1000",
        "sensor_model_vocabulary": "Datawell MOSE-G1000",
        "long_name": "Datawell MOSE-G1000",
    },
}