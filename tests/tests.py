'''
Contains tests for various parts of svo
'''
import os
import unittest
import cv2

import context
from svo.core import *

# Set up paths for loading testing images, etc
PATH = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(PATH, 'test_images')
OUT_PATH = os.path.join(PATH, 'test_out')

if not (os.path.exists(OUT_PATH)):
    os.makedirs(OUT_PATH)

class CoreTester(unittest.TestCase):
    def __init__(self, image=None):
        if image is None:
            image = os.path.join(IMAGE_PATH, 'Pictures1847.jpg')
            self.image = cv2.imread(os.path.join(IMAGE_PATH, '47.jpg'))
        else:
            self.image = image

    def test_feature_finder(self):
        # Test FeatureFinder and save the resultant image
        finder = FeatureFinder()
        kp = finder.detect(self.image)

        img2 = cv2.drawKeypoints(self.image, kp, None, color=(255,0,0))
        cv2.imwrite(os.path.join(OUT_PATH, 'FeatureFinder_out.png'), img2)

def test_all():
    tests = CoreTester()
    tests.test_feature_finder()
