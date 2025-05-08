import numpy as np
import cv2

class GeometryDataSynthesizer:
    def generate_grid(self, size=256, spacing=32):
        img = np.ones((size, size), dtype=np.uint8) * 255
        for x in range(0, size, spacing):
            cv2.line(img, (x, 0), (x, size), 0, 1)
            cv2.line(img, (0, x), (size, x), 0, 1)
        return img

    def generate_circles(self, size=256, count=4):
        img = np.ones((size, size), dtype=np.uint8) * 255
        center = (size // 2, size // 2)
        max_radius = size // 2 - 10
        for i in range(count):
            radius = max_radius * (i + 1) // count
            cv2.circle(img, center, radius, 0, 1)
        return img
