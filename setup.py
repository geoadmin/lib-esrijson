from setuptools import setup


setup(name='esrijson',
      version='0.2',
      description='Bindings and utilities for EsriJSON',
      classifiers=[],
      license='BDS',
      author='Loic Gasser',
      author_email=u'loicgasser4@gmail.com',
      packages=['esrijson'],
      package_dir={'esrijson': 'esrijson'},
      test_suite='nose.collector',
      install_requires=['shapely'],
      )
