import os
import yaml

def make_folders(current_dir, cfg):

    dir_dict = {
        "script_dir" : os.path.join(current_dir, cfg["PATHS"]["SCRIPT_LOCATION"]),
        "point_cloud_dir" : os.path.join(current_dir, cfg["PATHS"]["POINT_CLOUD_LOCATION"]),
        "filt_point_cloud_dir" : os.path.join(current_dir, cfg["PATHS"]["FILTERED_POINT_CLOUD_LOCATION"]),
        "mesh_dir" : os.path.join(current_dir, cfg["PATHS"]["MESH_LOCATION"])
    }

    for value in dir_dict.values():
        try: 
            os.mkdir(value)
        except FileExistsError:
            print("Directory already exists")

    return dir_dict

def set_files(dir_dict, cfg):
    file_dict = {
        "script_name" : os.path.join(dir_dict["script_dir"], cfg["NAMES"]["SCRIPT_NAME"]),
        "point_cloud_name" : os.path.join(dir_dict["point_cloud_dir"], cfg["NAMES"]["POINT_CLOUD_NAME"]),
        "filt_point_cloud_name" : os.path.join(dir_dict["filt_point_cloud_dir"], cfg["NAMES"]["FILTERED_POINT_CLOUD_NAME"]),
        "mesh_name" : os.path.join(dir_dict["mesh_dir"], cfg["NAMES"]["MESH_NAME"])
    }

    return file_dict

def initialize():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, 'config.yaml')

    with open(config_file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    
    dir_dict = make_folders(current_dir, cfg) 
    file_dict = set_files(dir_dict, cfg)

    return file_dict

initialize()
