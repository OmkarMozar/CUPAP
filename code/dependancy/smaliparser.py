from smalisca.core.smalisca_main import SmaliscaApp
from smalisca.modules.module_smali_parser import SmaliParser
from smalisca.core.smalisca_app import App
from smalisca.core.smalisca_logging import log
from smalisca.modules.module_sql_models import AppSQLModel
import smalisca.core.smalisca_config as config

import multiprocessing
import os
from cement.core import controller
from cement.core.controller import CementBaseController
import json

def parsesmali(location):
	# Create new smalisca app
	# You'll have to create a new app in order to set logging
	# settins and so on.
	print "Parsing smali files.."
	app = SmaliscaApp()
	app.setup()

	# Set log level
	app.log.set_level('info')

	# Specify the location where your APK has been dumped
	#location = '/root/Downloads/Project/Gmailnew'

	# Specify file name suffix
	suffix = 'smali'

	# Create a new parser
	parser = SmaliParser(location, suffix)

	# Go for it!
	parser.run()

	# Get results
	results = parser.get_results()
	'''
	data=app.get_all()

	with open('iii.json', 'w') as outfile:
		json.dump(data, outfile)
	'''
	ap = App(__name__)
	ap.add_location(location)
	ap.add_parser("%s - %s" % (config.PROJECT_NAME, config.PROJECT_VERSION))

		        # Append classes
	for c in results:
		ap.add_class_obj(c)

		        # Write results to JSON
	log.info("Exporting results to JSON")
	base=os.path.basename(location)	
	
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.json'
	ap.write_json(out_path)
	print out_path," created"
	
