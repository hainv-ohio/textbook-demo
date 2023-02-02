import datetime
import os
import requests
import aspose.words as aw
from fastapi import APIRouter
from loguru import logger
from bs4 import BeautifulSoup


converter_router = APIRouter(prefix='/convert')

@converter_router.get('/pdf-to-html', name='Convert PDF to HTML')
async def pdf_to_html(filename: str):
    logger.info(filename)
    logger.info(os.getcwd())
    file_data = requests.get(filename).text
    timestamp = int(datetime.datetime.now().timestamp())
    file_name = f'features/convert_pdf/temp/temp-file-{timestamp}.pdf'
    output_file = f"features/convert_pdf/temp/Output-{timestamp}.html"
    output_image = f'features/convert_pdf/temp/Output-{timestamp}.001.png'
    with open(file_name, 'wb') as pdf_file:
        pdf_file.write(bytes(file_data, 'utf-8'))
    doc = aw.Document(file_name)
    doc.save(output_file)

    spare_elements = [
        '<div style="-aw-headerfooter-type:footer-primary; clear:both"><p style="margin-top:0pt; margin-bottom:0pt"><span style="font-weight:bold; color:#ff0000">Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/</span></p></div>',
        '<p style="margin-top:0pt; margin-bottom:0pt"><span style="font-weight:bold; color:#ff0000">Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.</span></p>',
        f'<div style="-aw-headerfooter-type:header-primary; clear:both"><p style="margin-top:0pt; margin-bottom:0pt"><span style="height:0pt; display:block; position:absolute; z-index:-65537"><img src="Output-{timestamp}.001.png" width="548" height="298" alt="" style="margin-top:242.12pt; -aw-left-pos:0pt; -aw-rel-hpos:margin; -aw-rel-vpos:margin; -aw-top-pos:0pt; -aw-wrap-type:none; position:absolute"></span><span style="-aw-import:ignore">&nbsp;</span></p></div>'
        ]
    with open(output_file, 'r') as html_file:
        html_str = str(html_file.read())
        for element in spare_elements:
            html_str = html_str.replace(element, '')
        # with open(f'{output_file}-test.html', 'w') as test:
        #     test.write(html_str)
    
    os.remove(file_name)
    os.remove(output_file)
    os.remove(output_image)
    return html_str