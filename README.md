[![PyTests](https://github.com/jjjermiah/NBIA-toolkit/actions/workflows/main.yml/badge.svg)](https://github.com/jjjermiah/NBIA-toolkit/actions/workflows/main.yml)
[![Documentation Status](https://readthedocs.org/projects/nbia-toolkit/badge/?version=latest)](https://nbia-toolkit.readthedocs.io/en/latest/?badge=latest)

# NBIA Toolkit 
A python package that provides programmatic access to query the National Biomedical Imaging Archive (NBIA) database.

## Features
- Use NBIA Guest account to access public data OR authenticate using OAuth with user credentials for limited access data (requires approved data access).
- Query NBIA database for metadata on collections, patients, studies, series, and images
- Download images from NBIA
  - Calculate MD5 checksums for downloaded images
  - Auto-sort DICOM files using a user-defined pattern of DICOM tags



See Documentation at [NBIA-Toolkit Read The Docs](https://nbia-toolkit.readthedocs.io/en/latest/)

    TODO::readthedocs::error in the example first cell
    TODO::auth.py::implement better access token handling
    TODO::auth.py::implement better error handling
    TODO::auth.py::implement refresh token functionality
    TODO::auth.py::implement logout functionality
    TODO::auth.py::implement encryption for username and password
    TODO::nbia.py::implement better error handling
    TODO::nbia.py::implement better logging & logger configuration
    TODO::nbia.py::enforce type checking for all functions and add type hints
    TODO::nbia.py::implement return formats for dict, and pandas.DataFrames
    TODO::nbia.py::handle error case of if resposne is not bytes 
    TODO::nbia.py::add tests for download Series
    TODO::nbia.py::add functionality for downloadSeries to take in a list of seriesUIDs
    TODO::md5.py::add tests
    TODO::md5.py::add logging and error handling for non-existent files


Wiki is empty for now:
See the [Wiki](https://github.com/jjjermiah/NBIA-toolkit/wiki) for more information.



## Installation

`nbiatoolkit` will be made available on PyPI and Conda Forge soon. Until then, you can install the latest development version from GitHub by cloning the repository and running the following commands in the root directory:

```bash
pip install poetry
poetry install
```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`nbiatoolkit` was created by Jermiah Joseph. It is licensed under the terms of the MIT license.

## User Agreements and Disclaimers
The NBIA-toolkit is NOT a product of the National Cancer Institute (NCI) and is not endorsed by the NCI.
The NBIA-toolkit is provided as an open-source tool based on the [NBIA REST API](https://wiki.cancerimagingarchive.net/display/Public/NBIA+Advanced+REST+API+Guide).
The NBIA-toolkit is provided "AS IS" without warranty of any kind.

In no event shall the authors or contributors be liable for any claim, damages or other liability, arising from, out of or in connection with the NBIA-toolkit or the use or other dealings in the NBIA-toolkit.

Users of the NBIA-toolkit are required to abide by the NBIA REST API Terms of Service and the [NBIA Data Usage Policies and Restrictions](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/)
