#Qus.1
from PIL import Image,ImageFilter
img=Image.open('C:\\Users\\hp\\Music\\1.jpg')
filter=img.filter(ImageFilter.BLUR)
filter.rotate(180)
filter.thumbnail((400,200))
filter.save('C:\\Users\\hp\\Music\\blur1.jpg','png')
print(img.format)
img.save('C:\\Users\\hp\\Music\\photos_pdf.pdf','PDF',resolution=100.0)
print()

#Qus.2
import PyPDF2
import sys
my_file=open('C:\\Users\\hp\\Music\\day 21 output.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(my_file)
print(pdf_reader.numPages)
a=pdf_reader.getPage(0)

import os
output_file=open('C:\\Users\\hp\\Music\\new.pdf','wb')
pdf_writer=PyPDF2.PdfFileWriter()
pdf_writer.addPage(a)
pdf_writer.write(output_file)

merger=PyPDF2.PdfFileMerger()
for items in os.listdir():
    if items.endswith('.PDF'):
        merger.append(items)
merger.write('C:\\Users\\hp\\Music\\merged_pdf.pdf')
merger.close()