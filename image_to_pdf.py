import os

from fpdf import FPDF
from PIL import Image

TARGET_FOLDER = "YOUR FOLDER HERE"


def generate_pdf_from_folder(source_folder):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=0)

    folder_name = os.path.basename(source_folder)
    pdf.set_title(folder_name)
    pdf.set_author("mostlikelyadev")

    subfolders = sorted([f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))])

    print(f"Processing: {folder_name}")

    for subfolder in subfolders:
        subfolder_path = os.path.join(source_folder, subfolder)

        images = sorted([i for i in os.listdir(subfolder_path) if i.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))])

        if not images:
            continue

        print(f"  -> Chapter {subfolder} ({len(images)} images)")

        is_first_image = True

        for image_file in images:
            image_path = os.path.join(subfolder_path, image_file)

            with Image.open(image_path) as img:
                width_px, height_px = img.size

                width_mm = width_px * 0.264583
                height_mm = height_px * 0.264583

                pdf.add_page(format=(width_mm, height_mm))

                if is_first_image:
                    pdf.start_section(name=f"Chapter {int(subfolder)}")
                    is_first_image = False

                pdf.image(image_path, x=0, y=0, w=width_mm, h=height_mm)

    output_filename = f"{folder_name}.pdf"
    print(f"Saving {output_filename}...")
    pdf.output(output_filename)
    print("Done!")


if __name__ == "__main__":
    if os.path.exists(TARGET_FOLDER):
        generate_pdf_from_folder(TARGET_FOLDER)
    else:
        print(f"Error: Folder '{TARGET_FOLDER}' not found.")
