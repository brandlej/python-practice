import sys
from PIL import Image


def main():
    images = []

    # get cli args for file names
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    # clever trick to create a new gif
    # by sticking two images together and saving them as one
    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )


if __name__ == "__main__":
    main()
