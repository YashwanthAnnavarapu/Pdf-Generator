from flask import Flask, make_response, Response, request
import pdfkit as pdf
import pandas as pd

app = Flask(__name__)

@app.route("/generatePdf",methods=['POST','GET'])
def generatePdf():
    # print(request.json)
    #request.json is used to access the json data sent with the api or url
    df = pd.DataFrame(request.json)
    df.to_html("sample.html",border=1,sparsify=False,justify="center",max_cols=len(list(df.columns)),show_dimensions=True,)

    path = b".\wkhtmltopdf\\bin\wkhtmltopdf.exe"
    config = pdf.configuration(wkhtmltopdf=path)
    options = {
        'page-size': 'B0',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        # 'disable-smart-shrinking': False,
        # 'scale-size' : 40,
    }
    
    # creating pdf
    finalPdf = pdf.from_url(url="sample.html",configuration=config,options=options)
    
    response = make_response(finalPdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=sample.pdf'
    return response

if __name__ == '__main__':
   app.run()