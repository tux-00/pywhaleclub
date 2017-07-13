#!/usr/bin/env python

from setuptools import setup

setup(name='pywhaleclub',
      version='1.0',
      description='Whaleclub.co python API wrapper',
      url='https://github.com/tux-00/pywhaleclub',
      author='Raphaël B',
      author_email='raphb.bis@gmail.com',
      license='GPLv3',
      classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Intended Audience :: Financial and Insurance Industry',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Topic :: Office/Business',
            'Topic :: Office/Business :: Financial'
      ],
      keywords='python python3 whaleclub trade trading api bitcoin wrapper',
      packages=['pywhaleclub'],
      install_requires=['requests'],
      zip_safe=False)

