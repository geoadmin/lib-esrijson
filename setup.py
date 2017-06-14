from setuptools import setup


setup(name='esrijson',
      version='0.1',
      description='Bindings and utilities for EsriJSON',
      classifiers=[],
      license='BDS',
      author=u'Loïc Gasser',
      author_email=u'loicgasser4@gmail.com',
      packages=['esrijson'],
      package_dir={'esrijson': 'esrijson'},
      test_suite='nose.collector',
      install_requires=['shapely'],
      )
