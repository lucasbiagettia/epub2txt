
# EPUB to Plain Text Converter

This simply Python script is designed to convert EPUB files to plain text format. It extracts the textual content from EPUB documents, removes any HTML tags, and saves the resulting plain text in separate .txt files. Below are instructions on how to use this script effectively.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

1. **Python**: This script is written in Python, so you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **pip**: The Python package manager `pip` is required to install the script's dependencies. You can usually install `pip` along with Python, but if you encounter issues, refer to the [pip installation guide](https://pip.pypa.io/en/stable/installation/) for assistance.

## Installation

1. Clone this repository or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
This command will ensure that all necessary Python packages are installed.

# Usage
To convert EPUB files to plain text, follow these steps:

1. Place your EPUB files in a directory of your choice. You can create a new directory or use an existing one.

2. Modify the epub_directory variable in the script to specify the path to the directory containing your EPUB files. For example:

```python
epub_directory = 'path/to/your/epub/files'
```
3. Specify the directory where you want the resulting plain text files to be saved by modifying the txt_directory variable:

```python
txt_directory = 'path/to/output/directory'
```
Open a terminal or command prompt, navigate to the directory where the script is located, and run the script:

```bash
python epub_to_plain_text.py
```
The script will process all EPUB files in the specified directory and save the plain text versions in the output directory.

# Output
After running the script, you will find plain text files (.txt) in the specified output directory. Each text file corresponds to an EPUB file and contains the extracted textual content.

# Troubleshooting
If you encounter any issues while using this script or have questions, feel free to reach out for assistance.

# License
This script is provided under the MIT License. You can find the license information in the LICENSE file.

Thank you for using the epub2txt. Happy converting!