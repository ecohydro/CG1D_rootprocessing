import numpy as np
from astropy.io import fits
import time
import scipy.ndimage as imp
import datetime

from scipy import ndimage
from skimage.morphology import skeletonize
import scipy.misc
from scipy.signal import medfilt
from PIL import Image
import os

from RP_timerstart import RP_timerstart
from RP_timerprogress import RP_timerprogress
from RP_timerend import RP_timerend

def RP_rootimage(parameters):
    '''
    SUMMARY:
    'RP_rootimage': creates image of only root values (as determined by mask).
    
    USING CODE:
    Using water content values in 'wc' and mask values in 'imagefilter', image is multipled together.
    
    PARAMETERS: 
    1. wc_filename: filename of evaluated water content image.
    2. mask_filename: filename of evaluated mask image.
    3. output_filename: filename where image is to be saved.
    
    '''
    starttime = time.time()
    scriptname = 'rootimage'
    
    RP_timerstart(scriptname)
    
    wc_filename = parameters['wc_filename']
    mask_filename = parameters['mask_filename']
    output_filename = parameters['output_filename']
        
    wcimage = Image.open(wc_filename)    
    mask = Image.open(mask_filename)
    
    wcimage = np.array(wcimage)
    mask = np.array(mask)
    mask = mask > 0
    
    wcimage[~mask] = 0
    wcimage = Image.fromarray(wcimage)

    wcimage.save(output_filename)
    
    RP_timerend(starttime)
   