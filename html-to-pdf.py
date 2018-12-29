import django
from django.conf import settings
from django.template import Template, Context

import pdfkit
import os, io
import tkinter
from tkinter.messagebox import showinfo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs = io.open(BASE_DIR + '\\static_files\\logs.txt', 'w')

def configureDjangoSettings():
	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [
	        	os.path.join(BASE_DIR, 'static_files'),
	        ],
	    }
	]
	
	try:
		settings.configure(TEMPLATES = TEMPLATES) # We have to do this to use django templates standalone
		django.setup()
		logs.write(str('Successfully configured Django Settings\n'))
	except Exception as e:
		logs.write(str(e))

def configureWkhtmltopdf():
	try:
		# Change path of pdfkit configuration to specify location of wkhtmltox.exe
		config = pdfkit.configuration(wkhtmltopdf=BASE_DIR + '\\static_files\\wkhtmltox\\bin\\wkhtmltopdf.exe')
		logs.write('wkhtmltopdf configured\n')
		return config
	except Exception as e:
		logs.write(str(e))

def read_html_template():
	with io.open(BASE_DIR + '\\static_files\\html-templates\\template.html', 'r') as inputfile:
		template = str(inputfile.read())
	return template

def writeHtmlToPdf(data):
	configureDjangoSettings()
	wkhtmlconfig = configureWkhtmltopdf()
	html_template = read_html_template()

	try:
		t = Template(html_template)
		c = Context(data)
		logs.write('Template and Context Loaded.\n')
	except Exception as e:
		logs.write(e)

	try:
		pdfkit.from_string(t.render(c), data['output_path'], configuration=wkhtmlconfig)
	except Exception as e:
		logs.write(str(e))

def write_dict_to_logs(data):
	for key,value in data.items():
		logs.write(key + ' : ' + value + '\n')

class simpleapp_tk(tkinter.Tk):
	data = {
		'name' : '',
		'background_img' : '',
		'output_path': BASE_DIR + '\\output.pdf',
	}

	def __init__(self, parent):
		tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()
	
	def initialize(self):
		self.grid()

		self.entryVariable = tkinter.StringVar()
		self.entryVariable.set(u'Enter Name')
		self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0, row=0, sticky='EW')
		# self.entry.bind("<Return>", self.OnPressEnter)

		button = tkinter.Button(self,
								text=u'Submit',
								command=self.onButtonClick)
		button.grid(column=1, row=0)

		self.grid_columnconfigure(0, weight=1)
		self.resizable(True, False)

	def onButtonClick(self):
		self.data['name'] = self.entry.get()
		self.data['background_img'] = BASE_DIR + "\\static_files\\html-templates\\background.png"

		write_dict_to_logs(self.data)
		writeHtmlToPdf(self.data)

		self.popup_showinfo()
		self.closeApp()

	def popup_showinfo(self):
		showinfo("Window", 'Success ' + str(self.data['output_path']))

	def closeApp(self):
		self.destroy()

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('Html To Pdf')
	app.mainloop()

# https://www.online-convert.com/result/245d6293-52ef-4976-a132-003c652cb50a

# https://stackoverflow.com/questions/5458048/how-to-make-a-python-script-standalone-executable-to-run-without-any-dependency
# https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
# https://stackoverflow.com/questions/43834226/django-error-no-djangotemplates-backend-is-configured
# https://stackoverflow.com/questions/6748559/generating-html-documents-in-python

# https://pythonhosted.org/PyInstaller/spec-files.html
# https://sebsauvage.net/python/gui/#to_exe