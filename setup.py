from distutils.core import setup
from setuptools import find_packages
 
setup(name = 'alpha',  #package name   
      version = '0.0.1',  
      description = '',
      long_description = '',
      author = 'shioyim',
      author_email = 'shioyim@163.com',
      url = 'https://github.com/shioyim/alpha',
      license = 'MIT',
      install_requires = [],
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Fanance'
      ],
      keywords = '',
      packages = find_packages('src'),  
      package_dir = {'':'src'},         
      include_package_data = True
)


