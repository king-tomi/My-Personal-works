from PIL import Image
import playsound,pyttsx3

def read_image(filename: str) -> Image.Image:
    try:
        im = Image.open(filename)
        print(f"Image read successfully. Image format is {im.format}")
        return im
    except (FileNotFoundError,OSError):
        print("Error loading file, file does not exist or file not specified correctly")

def crop_and_transform_image(image,left: int,top: int,right: int,bottom: int,rotate=True):
    cropped = image.crop(left,top,right,bottom)
    if rotate:
        rotated = cropped.transpose(Image.ROTATE_180)
        image.paste(rotated,left,top,right,bottom)