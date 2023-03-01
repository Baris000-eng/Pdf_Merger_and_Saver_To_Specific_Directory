import PyPDF2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory


# Get the current user's home directory
home_dir = os.path.expanduser("~")

# Use the askdirectory function to prompt the user to select a directory to save the merged PDF file
root = Tk()
root.withdraw()
output_dir = askdirectory()

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Use the askopenfilenames function to prompt the user to select PDF files
file_paths = askopenfilenames(filetypes=[("PDF files", "*.pdf")])

# Save the merged PDF file to the selected directory
output_filename = input("Enter the name of the merged PDF file (including .pdf extension): ")
if not output_filename.endswith(".pdf"):
    output_filename = output_filename + ".pdf"
output_filepath = os.path.join(output_dir, output_filename)
with open(output_filepath, "wb") as output_file:
    merger.write(output_file)

# Ask user if they want to delete the input files
delete_files = input("Do you want to delete the input files? (Y/N): ").lower()
if delete_files == "y":
    for file_path in file_paths:
        os.remove(file_path)

