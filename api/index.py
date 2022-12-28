from flask import Flask
import sys
sys.path.append('/..')
from sd_app import create_app

app = create_app()



