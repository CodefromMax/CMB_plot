import numpy as np
import pandas as pd

import healpy as hp

import matplotlib.pyplot as plt
PLA_Data = pd.read_csv("data/planck_simulation/PLA-Results.csv")

# Store the names of the datasets into PLA_Data_List
PLA_Data_List = PLA_Data['SIMULATED_MAP.FILE_ID'].to_list()


# Initialize PLA_Data_Dict : (key:frequnecy, value: [csv path])
PLA_Data_Dict = dict()
for each_csv_path in PLA_Data_List:
    PLA_Data_Dict[each_csv_path[20:23]] = ["data/planck_simulation/"+each_csv_path]
# display(PLA_Data_Dict)

# Read the CMB datasets and store them inside the PLA_Data_Dict
# Update PLA_Data_Dict : (key:frequnecy, value: [csv path, hp map dat ])
 
for frequency, storage_list in PLA_Data_Dict.items():
    storage_list.append(hp.read_map(storage_list[0]))
# display(PLA_Data_Dict)

# Convert the unit from unitMJy/steradian to K_CMB
# Source: https://wiki.cosmos.esa.int/planckpla2015/index.php/UC_CC_Tables

PLA_Data_Dict["545"][1] = PLA_Data_Dict["545"][1]/58.0356
PLA_Data_Dict["857"][1] = PLA_Data_Dict["857"][1]/2.2681