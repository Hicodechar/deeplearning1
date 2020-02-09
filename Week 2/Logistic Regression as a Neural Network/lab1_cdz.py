import numpy as np 
import matplotlib.pyplot as plt 
import h5py
import scipy
import pylab
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

if __name__ == "__main__":
    # Loading the data (cat/non-cat)
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

    # Example of a picture
    index = 25
    plt.imshow(train_set_x_orig[index])
    pylab.show()
    print("y = " + str(train_set_y[:, index]) + ", it's a " + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") + "' picture.")