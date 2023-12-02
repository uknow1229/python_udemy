# from distutils.core import setup
from setuptools import setup, find_packages


setup(
  name='python_programming_demo_app',
  version='0.0.2',
  packages=find_packages(),
  package_data={'roboter': ['templates/*.txt']},
  url='http://sakaijunsoccer.appspot.com',
  license='MIT',
  author='jsakai',
  author_email='example@example.com',
  install_requires=['termcolor==1.1.0'],
  description='roborer description',
  tests_require=['pytest']
  # test_suits='tests',
)