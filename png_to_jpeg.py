from PIL import Image
import os


PIC_FOLDER = input('Enter the image folder: ')
pics = os.listdir(PIC_FOLDER)

for pic in pics:
    if pic[-3:] == 'jpg':
        continue
    if pic[-3:] == 'png':

        PIC_PATH = os.path.join(PIC_FOLDER, pic)
        im = Image.open(PIC_PATH)
        jpeg_im = im.convert('RGB')

        jpeg_im.save(pic[:-4] + '.jpg')
