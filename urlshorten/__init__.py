from flask import Flask

# importing the blueprint of our application
from . import urlshorten


# main app of our application
app = Flask(__name__)
# secret key 
app.secret_key="i127tge972g197eudu91038gdbcu"

# we have to register the blueprint in order to makeit do routing and send response and receive request
app.register_blueprint(urlshorten.bp)
