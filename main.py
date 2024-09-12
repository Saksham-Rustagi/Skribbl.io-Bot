# Imports
import numpy as np
import pyautogui
import time
from numpy import asarray
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle
from PIL import Image

colors = {0: (0.0, 0.0, 0.0),  # black
          1: (255.0, 255.0, 255.0),  # white
          2: (193, 193, 193),  # light grey
          3: (231, 0, 29),  # red
          4: (248, 103, 36),  # orange
          5: (251, 227, 61),  # yellow
          6: (45, 207, 47),  # lime
          7: (61, 181, 251),  # light blue
          8: (52, 29, 206),  # purple
          9: (160, 0, 182),  # magenta
          10: (207, 119, 169),  # light pink
          11: (156, 77, 50),  # light brown
          12: (76, 76, 76),  # dark grey
          13: (112, 0, 13),  # maroon
          14: (188, 40, 21),  # dark red
          15: (227, 159, 44),  # gold
          16: (13, 87, 24),  # dark green
          17: (31, 87, 155),  # blue
          18: (22, 7, 98),  # navy blue
          19: (84, 0, 102),  # dark magenta
          20: (163, 80, 115),  # dark pink
          21: (96, 45, 19)}  # brown
pyautogui.PAUSE = 0.001

def colorcategorizer(color_value):
    rgb_value = (color_value[0:3])
    manhattan = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
    distance = {k: manhattan(v, rgb_value) for k, v in colors.items()}
    color = min(distance, key=distance.get)
    return color


def imagedownload(keyword):
    driver = webdriver.Chrome(r'C:\chromedriver.exe')
    driver.get('https://www.google.com/imghp?hl=en&tab=ri&authuser=0&ogbl')
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    box.send_keys(keyword)
    box.send_keys(Keys.ENTER)
    for i in range(1, 2):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot(
                r'C:\Users\adite\Desktop\python\Skribbl\(' + keyword + str(i) + ').png')
        except:
            pass


def dictcreator(name):
    colordict = {}
    for i in range(256):
        for j in range(256):
            for k in range(256):
                print(str(i) + str(j) + str(k))
                colordict[(i, j, k)] = colorcategorizer((i, j, k))

    with open(name + '.pk', 'wb') as fi:
        # dump your data into the file
        pickle.dump(colordict, fi)


if __name__ == '__main__':
    """
    time.sleep(2)
    pyautogui.moveTo(472,875)
    pyautogui.dragRel(835, 0)
    pyautogui.dragRel(0, -625)
    pyautogui.dragRel(-835, 0)
    pyautogui.dragRel(0, 625)
    """
    # load Color Dictionary
    with open('colordict.pk', 'rb') as fi:
        allcolors = pickle.load(fi)

    # Getting Images
    query = input("What to draw: ")
    imagedownload(query)
    img = Image.open(r'C:\Users\adite\Desktop\python\Skribbl\(' + query + '1).png')

    # Rescaling Images
    if img.size[0] / img.size[1] > 835 / 625:
        img_scl = img.resize((835, int(835 * img.size[1] / img.size[0])))
    else:
        img_scl = img.resize((int(625 * img.size[0] / img.size[1]), 625))
    print(str(tuple(int(ti/10) for ti in img_scl.size)))
    img_scl = img_scl.resize(tuple(int(ti/10) for ti in img_scl.size))

    # Image to Array of Colors
    pxl_arr = asarray(img_scl)
    color = np.empty((pxl_arr.shape[0], pxl_arr.shape[1]), dtype=int)
    for row in range(pxl_arr.shape[0]):
        for col in range(pxl_arr.shape[1]):
            color[row, col] = (allcolors[tuple(pxl_arr[row, col, 0:3])])

    # get Coords of Color on Screen and click
    colorcoords = {0: (585, 919),
                   1: (585, 895),
                   2: (609, 895),
                   3: (633, 895),
                   4: (657, 895),
                   5: (681, 895),
                   6: (705, 895),
                   7: (729, 895),
                   8: (752, 895),
                   9: (777, 895),
                   10: (801, 895),
                   11: (825, 895),
                   12: (609, 919),
                   13: (633, 919),
                   14: (657, 919),
                   15: (681, 919),
                   16: (705, 919),
                   17: (729, 919),
                   18: (752, 919),
                   19: (777, 919),
                   20: (801, 919),
                   21: (825, 919)}
    for i in range(len(colorcoords)):
        if i != 1:
            time.sleep(0.5)
            pyautogui.leftClick(colorcoords[i])
            where = np.where(color == i)
            for j in range(int(len(where[0]))):
                pyautogui.leftClick(where[1][j]*10+472, where[0][j]*10+250)


