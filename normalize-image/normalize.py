import tensorflow as tf
import numpy as np 
import sys

def normalizeImage(image):
    normalizedImage = tf.keras.utils.img_to_array(image)
    normalizedImage = np.expand_dims(normalizedImage, axis = 0)
    return normalizedImage


sys.modules[__name__] = normalizeImage
