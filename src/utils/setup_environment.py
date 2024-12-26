# Importing necessary libraries for data processing, visualization, and deep learning
import numpy as np 
import pandas as pd  
import os  

# Libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Libraries for deep learning
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2  # For image processing tasks

# Pre-trained models for transfer learning
from tensorflow.keras.applications import VGG16, InceptionResNetV2

# Regularization and optimizers
from keras import regularizers
from tensorflow.keras.optimizers import Adam, RMSprop, SGD, Adamax
