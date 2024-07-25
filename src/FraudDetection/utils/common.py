import os
from box.exceptions import BoxValueError
import yaml
from FraudDetection.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and returns
    
    Args:
      path_to_yaml (str): path like input.
      
    Raises:
        ValueError: If the YAML file is empty
        e: empty file
    
    Returns:
     ConfigBox: a Box object with the loaded YAML
     """
    try:
        with open(path_to_yaml) as yaml_file: 
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The YAML file {path_to_yaml} is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """Create directories if they don't exist
    
    Args:
      path_to_directory (list): list of directory paths like ['dir1', 'dir2']
      verbose (bool): whether to print messages or not. Defaults to True.
    """
    for path in path_to_directory:
       os.makedirs(path, exist_ok=True)
       if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(data: dict, path_to_json: Path):
    """Save a dictionary to a JSON file
    
    Args:
      data (dict): data to be saved in JSON format
      path_to_json (str): path like output.json
    """
    with open(path_to_json, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    logger.info(f"Successfully saved JSON file: {path_to_json}")

@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """Load a JSON file and returns
    
    Args:
        path_to_json (str): path like input.json
    
    Returns:
     ConfigBox: a Box object with the loaded JSON
    """
    with open(path_to_json, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"Successfully loaded JSON file: {path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_binary(data: Any, path_to_binary: Path):
    """Save a binary file
    
    Args:
        data (Any): data to be saved
        path_to_binary (str): path like output.pkl
    """
    joblib.dump(data, path_to_binary)
    logger.info(f"Successfully saved binary file: {path_to_binary}")

@ensure_annotations
def load_binary(path_to_binary: Path) -> Any:
    """Load a binary file and returns
    
    Args:
        path_to_binary (str): path like input.pkl
    
    Returns:
     Any: loaded data
    """
    data = joblib.load(path_to_binary)
    logger.info(f"Successfully loaded binary file: {path_to_binary}")
    return data

@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """Get the size of a file
    
    Args:
        path_to_file (str): path like input.txt
    
    Returns:
     str: size of the file in human-readable format
    """
    size_in_kb = round(os.path.getsize(path_to_file)/1024)
    return f"~ {size_in_kb} KB"