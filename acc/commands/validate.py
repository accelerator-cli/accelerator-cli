"""The validate command."""

from .base import Base
import os.path
import yaml
import jsonschema

class Validate(Base):

    def run(self):
        if self.options['<file>'] is None:
        	file = 'descriptor.yml'
        else:
        	file = self.options['<file>']
        
        absPath = self.getAbsolutePath(file)

        if os.path.exists(absPath) and os.path.isfile(absPath):
        	with open(absPath, 'r') as f:
    			doc = yaml.load(f)
                print doc['acc-version']
    	else:
            if self.options['<file>'] is None:
                print("file 'desciptor.yml' does not exists, exiting")
            else:
                print("file '" + self.options['<file>'] + "' does not exists, exiting")

    @staticmethod
    def getAbsolutePath(pathString):
        dir = os.getcwd()
        if os.path.isabs(pathString):
            absPath = pathString
        else:
            absPath = os.path.join(dir, pathString)
        return absPath