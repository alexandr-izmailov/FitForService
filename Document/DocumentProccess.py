import os
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

def adjust_document():
    # Create the document
    document = Document()

    # Set the font to one suitable for mathematical expressions
    math_font = document.styles.add_style('MathFont', WD_STYLE_TYPE.PARAGRAPH)
    math_font.font.name = 'Cambria Math'
    math_font.font.size = Pt(12)

    return document

def save_new_report_file(directory, document:Document(), gc_or_lc = ''):
    # Find all docx files in the directory
    any_files = os.listdir(directory)
    print('any files are ', any_files)
    files = [f for f in any_files if f.endswith('.docx') and f.startswith(f'report_{gc_or_lc}')]
    print('files are ',files)

    # If no files found, create new file with v0001 suffix
    if not files:
        new_file_name = os.path.join(directory, f"report_{gc_or_lc}_v0001.docx")
    else:
        # Find the highest version number among the files
        versions = [int(f.split("_v")[1].split(".")[0]) for f in files]
        highest_version = max(versions)

        # Create new file with next version number
        new_file_name = os.path.join(directory, f"report_{gc_or_lc}_v{str(highest_version + 1).zfill(4)}.docx")

    # Save new report file
    document.save(new_file_name)
    print('file saved')
    return

