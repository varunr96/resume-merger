'''
to install dependencies:
    >> pip install python
    >> pip install PyPDF2

to run, move this file to the directory with all the resumes, and fire up terminal:

    cd ~/folder_with_resumes
    python resumeMerger.py
'''
import os
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

merger = PdfFileMerger()


for subdir, dirs, files in os.walk('./'):
    for file in files:
      if '.pdf' in file and 'resume' in file:
          merger.append(open(file, 'rb'))
result_name = raw_input("What company/organization is this resume book for?: ")
result_name += "-ThetaTau-Resumes.pdf"

with open(result_name, 'wb') as fout:
    merger.write(fout)
