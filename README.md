# Skribbl.io Drawing Bot

This project automates drawing in *Skribbl.io* by downloading images, resizing them, and drawing them on the canvas in the game. The bot identifies pixel colors and replicates the image by using mouse automation.

## Features

- Automatically downloads an image from Google Images based on the input query.
- Resizes and processes the image to fit the Skribbl.io drawing canvas.
- Maps pixel colors to the closest available colors in the game.
- Automates drawing the image on the Skribbl.io canvas using `pyautogui`.

## Prerequisites

You need to install the following Python libraries:

```bash
pip install numpy pyautogui selenium pillow pickle-mixin
```

Additionally, ensure that you have the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) installed for the `selenium` browser automation.

## Setup

Before running the bot, you need to create a color dictionary file (`colordict.pk`) that maps RGB values to the colors available in *Skribbl.io*. This is required for the bot to identify and replicate colors accurately.

### Steps to Create `colordict.pk`

1. Run the `dictcreator` function in the script:

```python
dictcreator('colordict')
```

2. This will generate the `colordict.pk` file which is necessary for the bot to categorize colors.

## How It Works

1. **Color Categorization**: The bot uses the `colordict.pk` file to map pixel RGB values to the available colors in *Skribbl.io*. The colors are mapped using the Manhattan distance to find the closest color available in the game.

2. **Image Download**: The `imagedownload()` function downloads an image of the query provided by the user from Google Images.

3. **Image Resizing**: The downloaded image is resized to fit the Skribbl.io drawing canvas while maintaining the aspect ratio.

4. **Drawing on Canvas**: The bot maps each pixel of the resized image to the nearest color available on Skribbl.io and automates mouse clicks to draw the image.

## Running the Script

1. Start the script by running the following command:

```bash
python skribbl_drawing_bot.py
```

2. You will be prompted to input a search query for the image you want to draw.

3. The bot will download, resize, and process the image and then draw it on the Skribbl.io canvas.

4. The bot will automatically detect the canvas and begin drawing.

## Important Notes

- **Mouse Calibration**: Ensure the mouse positions for the color palette (`colorcoords`) and the canvas area are correctly aligned with your screen. You may need to adjust the coordinates depending on your screen resolution.

- **Selenium WebDriver**: Ensure that your WebDriver path is correctly set in the `imagedownload()` function. Replace the path with your local WebDriver path.

```python
driver = webdriver.Chrome(r'path_to_your_chromedriver')
```

## Future Enhancements

- Add error handling for different screen resolutions and dynamically adjust canvas and palette positions.
- Allow drawing complex images with higher accuracy by improving pixel color matching and reducing noise in images.


---

Enjoy automating your Skribbl.io drawings!
