### HEIC to JPEG Converter

This is a command-line utility script written in Python that converts HEIC (High Efficiency Image Format) files to JPEG format using the `pillow_heif` library. The script takes an input directory containing HEIC files and converts them to JPEG format, saving the converted files in an output directory.

#### Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your system
- The `Pillow` library installed (`pip install pillow`)
- The `pillow_heif` library installed (`pip install pillow_heif`)

#### Usage

To use the script, follow these steps:

1. Download the `heic.py` script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `heic.py` script is located.

3. Run the script with the following command:

`python heic.py input_directory output_directory`


Replace `input_directory` with the path to the directory containing the HEIC files you want to convert, and `output_directory` with the path to the directory where you want to save the converted JPEG files.

For example:

`python heic.py /path/to/input_directory /path/to/output_directory`


4. The script will convert all HEIC files in the input directory to JPEG format and save them in the output directory. The converted files will have the same name as the original files, but with the `.jpg` extension.

5. The script will display a message for each file converted, indicating the original file name and the corresponding JPEG file name.

#### Example

Let's say you have a directory named `heic_dir` that contains HEIC files, and you want to convert them to JPEG format and save them in a directory named `jpg_dir`. Here's how you would use the script:

`python heic.py heic_dir jpg_dir1`


The script will convert all HEIC files in the `heic_dir` directory to JPEG format and save them in the `jpg_dir` directory.

Please note that the script assumes the input directory contains only HEIC files and will not convert any other file formats. It also assumes that the output directory exists or can be created.
