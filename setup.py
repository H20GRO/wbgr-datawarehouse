from setuptools import setup, find_packages

with open('./requirements.txt') as f:
    required = f.read().splitlines()
setup(
   name='wbgr_datawarehouse',
   version='0.0.2',
   author='Johan Nienhuis',
   author_email='-',
   packages=['wbgr_datawarehouse'],
   #scripts=['bin/script1','bin/script2'],
   url='-',
   license='-',
   description='Connection to wbgr datawarehouse',
   long_description='',
   install_requires=required,
)
