"""
.h5ant-reader

Made by: Anders Kristensen
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt


delta_horizontal = "/readings/patch_antenna_Delta_horizontal.hd5ant"
delta_vertical = "/readings/patch_antenna_Delta_vertical.hd5ant"
sigma_horizontal = "/readings/patch_antenna_zigma_horizontal.hd5ant"
sigma_vertical = "/readings/patch_antenna_zigma_vertical.hd5ant"
plot_instructions = """
asdasd
asd
asd
asd
asd
asd
"""

def open_file(filename: str, mode: str):
    if mode in ["r", "a", "w"]:
        return h5py.File(filename, mode)
    else:
        open_file(str, input("Invalid mode, please choose between:\n Read (r)\n,Write (w)\n,or Append (a)\n"))


def read_raw_data(file) -> None:
    print("Keys: %s" % file.keys())
    a_group_key = list(file.keys())[0]
    data = list(file[a_group_key])
    for i in data:
        print(i)



def plot(file, type:str):
    if type.upper() == "db":
        return
    elif type.upper() == "smith":
        return
    elif type.upper() == "":
        return
    else:
        print("Invalid plot-type:\n,plot_instructions")
        plot(file, input("Enter a new plot-type: "))


if __name__ == "__main__":
    # f = open_file(delta_horizontal, "r")
    # read_raw_data(f)

    h5py.File(delta_horizontal, "r")