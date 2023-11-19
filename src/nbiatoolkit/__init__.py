## __init__.py
# Path: projects/nbia-toolkit/src/__init__.py

# this is the __init__.py file 
# this file is run when the package is imported
# this file is used to import all the modules in the package
# this file is used to define the __all__ variable

# import the modules
from .nbia import NBIAClient
from .auth import OAuth2
from .utils.logger import setup_logger
from .utils.nbia_endpoints import NBIA_ENDPOINTS

# define the __all__ variable
__all__ = [
    'NBIAClient',
    'OAuth2',
    'setup_logger',
    'NBIA_ENDPOINTS'
]



## main.py
# Path: projects/tcia_python_wrapper/tcia_python_wrapper/main.py