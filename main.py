"""
.h5ant-reader

Made by: Anders Kristensen
"""

import h5py
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl 



delta_horizontal = "readings/patch_antenna_Delta_horizontal.h5ant"
delta_vertical = "readings/patch_antenna_Delta_vertical.h5ant"
sigma_horizontal = "readings/patch_antenna_zigma_horizontal.h5ant"
sigma_vertical = "readings/patch_antenna_zigma_vertical.h5ant"
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

    print(len(data))



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

def print_name(name, obj):
    if isinstance(obj, h5py.Dataset):
        print('Dataset:', name)
    elif isinstance(obj, h5py.Group):
        print('Group:', name)


if __name__ == "__main__":
    with h5py.File(delta_horizontal, "r") as f:
        f.visititems(print_name, )
        plt.plot(f['angles'][4000:5000], f['powers'][4000:5000,])
        plt.ylabel('Power [dB]')
        plt.xlabel('Angle [degrees]')
        plt.show()



    



