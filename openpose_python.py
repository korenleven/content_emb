import sys
import os
from openpose.build.python.openpose import pyopenpose as op

def main(**params):
    
    print(os.getcwd())
    try:
        # Import Openpose (Windows/Ubuntu/OSX)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        params["model_folder"] = "../../../models/"
        # Starting OpenPose
        opWrapper = op.WrapperPython(op.ThreadManagerMode.Synchronous)
        opWrapper.configure(params)
        opWrapper.execute()

    except Exception as e:
        print(e)
        return
