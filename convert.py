import os

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image

# =========================
# CONFIG
# =========================

INPUT_FOLDER = "th"

OUTPUT_SIZE = 512

# =========================
# CONVERT
# =========================

for filename in os.listdir(INPUT_FOLDER):

    if filename.lower().endswith(".svg"):

        svg_path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        png_name = filename.replace(
            ".svg",
            ".png"
        )

        png_path = os.path.join(
            INPUT_FOLDER,
            png_name
        )

        try:

            drawing = svg2rlg(svg_path)

            renderPM.drawToFile(
                drawing,
                png_path,
                fmt="PNG"
            )

            # Resize PNG
            img = Image.open(png_path)

            img = img.resize(
                (OUTPUT_SIZE, OUTPUT_SIZE)
            )

            img.save(
                png_path,
                optimize=True
            )

            print(
                f"SUCCESS : {png_name}"
            )

        except Exception as e:

            print(
                f"ERROR : {filename}"
            )

            print(e)

print("\nDONE")

input("Press Enter to exit...")