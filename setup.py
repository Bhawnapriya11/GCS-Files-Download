from setuptools import setup
setup(name="gcs-download",
version="0.1.0",
description="This is a package for downloading files from GCS bucket ,either all files or with a certain extension",
long_description="no long desc, description is enough",
author="bhawna",
packages=['gcs_down'],
install_requires=['google-cloud-storage','google-auth']
