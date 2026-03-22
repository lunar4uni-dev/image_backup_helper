# Image Backup Helper

## Overview

Image Backup Helper is a Python-based utility designed to assist in organizing and backing up image files from a specified input folder. The tool recursively searches for image files, classifies them into albums based on filename prefixes, and duplicates them into an output folder with appropriate album labels. This script is particularly useful for reorganizing Google Photo Takeouts where image files need to be categorized and archived efficiently.

## Features

- **Recursive Image Search**: Scans the input folder and all subfolders for supported image file formats.
- **Album Classification**: Automatically categorizes images into predefined albums (e.g., Screenshot, WhatsApp, Instagram, FCMobile-Highlights, Camera) based on filename prefixes. Supports custom album names derived from filenames.
- **Image Duplication**: Creates copies of images in the output folder, prefixed with the album name for easy identification.
- **Interactive Input**: Prompts users for input and output folder paths via command-line interface.
- **Error Handling**: Checks for the existence of input and output folders, creating the output folder if necessary.

## Requirements

- Python 3.x (tested with Python 3.8+)
- Standard Python libraries: `os`, `glob`, `shutil` (no external dependencies required)

## Installation

1. Download the `image_classifier.py` script to your local machine.
2. Ensure Python 3.x is installed on your system.
3. No additional installation steps are required as the script uses built-in Python modules.

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory containing `image_classifier.py`.
3. Run the script using the following command:
   ```
   python image_classifier.py
   ```
4. When prompted, enter the full path to the folder containing the images (input folder).
5. When prompted, enter the full path to the folder where duplicated images should be saved (output folder).
6. The script will process the images, display the album contents, and duplicate the files accordingly.

### Example

```
Enter the folder path containing images: C:\Users\Username\Pictures\Input
Enter the folder path to save duplicated images: C:\Users\Username\Pictures\Output
```

The script will then output the classification results and perform the duplication.

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)
- WebP (.webp)

## Limitations

- **Command-Line Interface Only**: The tool currently lacks a graphical user interface (GUI), requiring users to interact via terminal commands.
- **Filename-Based Classification**: Images are classified solely based on filename prefixes separated by underscores (_) or hyphens (-). This may not accurately reflect the actual content or intended categorization.
- **No Duplicate Detection**: The script does not check for duplicate images within or across albums; it simply duplicates all found files.
- **Limited Album Types**: While custom albums are supported, the script has predefined categories that may not cover all use cases.
- **Windows-Specific Paths**: The script uses forward slashes in path handling, which may cause issues on non-Windows systems (though it should work with standard Python path operations).

## Future Enhancements

- **Graphical User Interface**: Develop a user-friendly GUI to improve accessibility and ease of use for non-technical users.
- **Advanced Classification**: Implement content-based image analysis or metadata reading for more accurate album assignment.
- **Duplicate Detection**: Add functionality to identify and handle duplicate images, preventing unnecessary storage usage.
- **Cross-Platform Compatibility**: Enhance path handling and testing for broader operating system support.
- **Configuration File Support**: Allow users to define custom album categories and settings via a configuration file.
- **Batch Processing**: Enable processing of multiple input folders in a single run.
- **Progress Indicators**: Add progress bars and detailed logging for large-scale operations.

