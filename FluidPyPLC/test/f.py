#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk

from get_sequence import Sequence
from diagrams import diagrams
from plc import Plc
from GUI import Gui

import argparse
import json
import os
import pkg_resources
import subprocess
import textwrap


config_file_path = pkg_resources.resource_filename('FluidPyPLC', 'resources/config.json')
try:
    with open(config_file_path) as f:
        config = json.load(f)
        path = config["folder_path"]
except Exception as e:
    print(e)


def create_folders(folder_path):
    plots_folder = os.path.join(folder_path, 'Plots')
    plc_folder = os.path.join(folder_path, 'plc')

    # Create the Plots and plc folders
    os.makedirs(plots_folder, exist_ok=True)
    os.makedirs(plc_folder, exist_ok=True)

    print(f"Created 'Plots' and 'plc' folders inside '{folder_path}'.")

    # Set this path to the config.json file
    with open(config_file_path) as f:
        config = json.load(f)
    config["folder_path"] = folder_path

    with open(config_file_path, 'w') as f:
        json.dump(config, f, indent=4)

# function to start the terminal version
def terminal():
    sequence = Sequence()
    s = sequence.s
    diagrams(s)
    Plc(s)

# args management
def main():
    parser = argparse.ArgumentParser(
        description='FluidPyPLC',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
        f.py --gui # to use the user interface mode
        f.py -t # to use the terminal version
        f.py --plc # to display the plc ST code
        ''')
    )
    parser.add_argument('-g', '--gui', action='store_true', help='gui mode')
    parser.add_argument('-t', '--terminal', action='store_true', help='terminal mode')
    parser.add_argument('--plc', action='store_true', help='show plc code')
    parser.add_argument('-f', '--folder', type=str, help='Config.json folder path to create the Plot and plc folders')
    args = parser.parse_args()
    if args.folder:
        folder_path = args.folder
        create_folders(folder_path)
        exit(0)
    if args.gui:
        # gui mode
        gui = Gui()
        gui.gui_mode()
        exit(0)
    elif args.terminal:
        # terminal mode
        terminal()
        exit(0)
    elif args.plc:
        try:
            # open plc ST code with notepad
            dir = os.path.join(path, 'plc/plc.st')
            subprocess.call(['notepad.exe', dir])
        except Exception as e:
            print("There is a problem opening the file:")
            print(e)
    else:
        # default argument
        terminal()
        exit(0)

if __name__ == "__main__":
    main()