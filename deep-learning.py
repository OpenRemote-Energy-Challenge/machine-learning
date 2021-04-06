import numpy as np
#from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Import keras modules
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import random_normal
from tensorflow.keras.utils import plot_model
import tensorflow as tf

print('keras version:', tf.keras.__version__)
print('tensorflow version:', tf.__version__)