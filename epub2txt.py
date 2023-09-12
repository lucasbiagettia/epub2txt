
# Install the necessary libraries
#!pip install ebooklib
#!pip install bs4

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os


epub_directory = '/content/borgesEpub'
txt_directory = '/content/borgesTxt'

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    plain_text = []

    for item in book.items:
        if isinstance(item, epub.EpubHtml):
            content = item.content
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            plain_text.append(text)

    return '\n'.join(plain_text)




# List all files in the EPUB directory
epub_files = [file for file in os.listdir(epub_directory) if file.endswith('.epub')]

# Iterate over each EPUB file and apply the function
for epub_file in epub_files:
    full_path = os.path.join(epub_directory, epub_file)
    extracted_text = extract_text_from_epub(full_path)

    # Save the extracted text in a plain text file with the same name but .txt extension
    txt_file_name = os.path.splitext(epub_file)[0] + '.txt'
    output_txt_path = os.path.join(txt_directory, txt_file_name)

    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_text)

print('EPUBs have been converted to plain text files in the output folder.')
