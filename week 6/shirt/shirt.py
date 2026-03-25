from PIL import Image, ImageOps
import sys


def main():
    # check correct # args
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    source = sys.argv[1]
    target = sys.argv[2]
    # check if either input is invalid
    if not is_valid_file_ext(source):
        sys.exit("Invalid input")
    if not is_valid_file_ext(target):
        sys.exit("Invalid output")

    # extension parsing is a bit brittle
    # could do source.lower().split(".")[-1] to grab from end
    # e.g. my.photo.png -> ["my", "photo", "png"] -> -3, -2, -1 indices -> png
    source_ext = source[source.index(".") :].lower()
    target_ext = target[target.index(".") :].lower()
    if source_ext != target_ext:
        sys.exit("Input and output have different extensions")

    try:
        source_image = Image.open(source)
        tshirt_image = Image.open("shirt.png")

        resized_source_image = ImageOps.fit(source_image, size=(600, 600))
        # 3rd arg tells paste to use the alpha channel (A in RGBA) of tshirt_image as a stencil,
        # where alpha controls pixel visibility (255 = opaque, 0 = transparent). This ensures
        # only visible shirt pixels are pasted and transparent pixels don’t overwrite the base background image and make it black.
        resized_source_image.paste(tshirt_image, (0, 0), tshirt_image)
        resized_source_image.save(target)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def is_valid_file_ext(filename: str):
    return filename.endswith((".jpg", ".jpeg", ".png"))


if __name__ == "__main__":
    main()
