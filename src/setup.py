'''
Created on Apr 4, 2011

@author: shroffk
'''

from distutils.core import setup

setup(name='ChannelFinderAPI',
      version='1.0',
      description='Python ChannelFinder Client Lib',
      author='Kunal Shroff',
      author_email='shroffk@bnl.gov',
      packages=['lib'],
      py_modules=['Channel', 'ChannelFinderClient']
     )