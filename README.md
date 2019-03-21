# Python Html to Pdf Converter with Mini Gui Support (Tkinter)

## Setting up
```
Just install the packages from the requirements.py

To create a pdf, the code works in the following steps.
1. DJANGO - Initialize a template and load it as a Context which will be rendered. (DJANGO provides this functionality by setting up a light version of itself). So, the code will first configure Django Settings in configureDjangoSettings()

2. PDFKIT - On the rendered Context, variables are present which are filled by data provided by a dictionary. PDFKIT does this but it require a package called "WKHTMLtoPDF" which comes as an exe and can be installed to the "static_files" directory. An Attribute "config = wkhtmltopdf" is passed to PDFkit for the creation of pdf. Refer configureWkhtmltopdf() and the main html to pdf function is writeHtmlToPdf().

3. TKINTER - It only provides an interface here to provide a feel good feature.
```

### References
```
Converting to HTML - https://document.online-convert.com/convert-to-html
Tkinter Usage Implementation - https://sebsauvage.net/python/gui/#to_exe
```

### Packages required
```
tkinter
pdfkit
Django
isntall wkhtmltox-0.12.5-1.msvc2015-win64 in BASE_DIR/static_files/wkhtmltox

The requirements.txt file contains these which can be installed using:
pip install -r requirements.txt
```
