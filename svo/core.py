'''
    Contains core objects to run the Semidirect Visual Odometry Algorithm
        in python.

    Copyright (C) 2017  Alec Graves (shadySource)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import cv2

class FeatureFinder(object):
    def __init__(self):
        # TODO: add detector params
        self.fast = cv2.FastFeatureDetector_create()

    def detect(self, image):
        return self.fast.detect(image, None)

