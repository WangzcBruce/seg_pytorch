import os
import os.path as osp
import numpy as np
import cv2

def mkdir_or_exist(dir_name, mode=0o777):
    if dir_name == '':
        return
    dir_name = osp.expanduser(dir_name)
    os.makedirs(dir_name, mode=mode, exist_ok=True)

def path_whether_exists(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(input_path)



def is_str(x):
    """Whether the input is an string instance.

    Note: This method is deprecated since python 2 is no longer supported.
    """
    return isinstance(x, str)

def pic_imread(img_path):
    with open(img_path, 'rb') as f:
        imageBin = f.read()
    img_np = np.frombuffer(imageBin, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    return img
# imread(r"F:\Potsdam\Potsdam_temp\tmpa4ve6nrx\2_Ortho_RGB\top_potsdam_2_10_RGB.tif")