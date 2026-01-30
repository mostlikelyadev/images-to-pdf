# Images to PDF

Easily convert your image collections into well-formatted PDFs!

This tool is designed to handle directory structures, such as scanned books or comics, and compile them into a single document.

## Directory Structure

Organize your folders like the example below. The tool will automatically detect the nested folders and files to generate the PDF in the correct order.

```text
Book Title/
├── 01/
│   ├── 01.jpg
│   ├── 02.jpg
│   └── ...
│   └── 27.jpg
├── ...
└── 23/
    ├── 01.jpg
    ├── 02.jpg
    └── ...
    └── 45.jpg
```

## Features

*   **Recursive Scanning:** Automatically finds images in nested subdirectories.
*   **Natural Sorting:** Handles numbered files correctly (e.g., `1.jpg`, `2.jpg`, `10.jpg`).
*   **Simple Output:** Generates a clean, single PDF from your structure.

## Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/mostlikelyadev/images-to-pdf.git
    ```

2.  Navigate to the folder:
    ```bash
    cd images-to-pdf
    ```

3.  Edit the script to include your target folder and run it:
    ```bash
    python image_to_pdf.py
    ```

## Requirements

*   Python 3.x
*   Pillow (PIL)
*   fpdf
