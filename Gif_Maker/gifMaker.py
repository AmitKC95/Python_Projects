import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "catwak.gif", save_all=True, append_images=images[1:], duration=200, loop=0
)
# python gifMaker.py cat01.png cat 02.png cat03.png
# because we are using sys and arg...
# hence the file names can simply be listed when running