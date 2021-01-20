import sys, os
import logging
logging.basicConfig(stream=sys.stderr)
PROJECT_FOLDER = '/var/www/opm'
PROJECT_HOME = '/var/www/opm/app'
activate_this = os.path.join(PROJECT_FOLDER, 'virtualenv', 'bin', 'activate_thi$
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__f$

# add your project directory to the sys.path
#if project_home not in sys.path:
#sys.path = [project_home] + sys.path
sys.path.append(PROJECT_HOME)
sys.path.append('/var/www/opm/virtualenv/lib/python3.7/site-packages/')
# import flask app but need to call it "application" for WSGI to work
from app import app as application
