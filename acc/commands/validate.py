"""The validate command."""

from json import dumps
from .base import Base
import os.path
import yaml

class Validate(Base):

    def run(self):
        if self.options['<file>'] is None:
        	file = './descriptor.yml'
        else:
        	file = "./" + self.options['<file>'] 
        if os.path.exists(file) and os.path.isfile(file):
        	with open(file, 'r') as f:
    			doc = yaml.load(f)
    	else:
    		print("file '" + file + "' or desciptor.yml does not exists, exiting")

    	print doc['acc-version']