import os
from pathlib import Path
import yaml
import pandas as pd
from pandas import json_normalize

def retrieve_data():
    root_dir = Path(os.path.realpath("handle_config.py")).parent
    config_path = os.path.join(root_dir, 'data/sites.yaml')
    with open(config_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except:
            raise Exception("Could not load site data.")

if __name__ == "__main__":
    df = pd.DataFrame(retrieve_data()['Sites']).reset_index(drop=True).transpose().reset_index()
    df.columns = ['name','address','lat','lng']
    print(df)