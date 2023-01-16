from os import path
import sys


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return path.join(sys._MEIPASS, relative)
    return path.join(relative)
