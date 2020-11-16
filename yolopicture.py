import sys
import argparse
from yolo import YOLO
from PIL import Image

def detect_img():
    yolo = YOLO()
    image = Image.open('03.jpg')
    r_image = yolo.detect_image(image)
    yolo.close_session()
    r_image.show()


FLAGS = None

if __name__ == '__main__':
    detect_img()

