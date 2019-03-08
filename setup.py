from setuptools import setup


setup(name='esrijson',
      version='0.4.1',
      description='Bindings and utilities for EsriJSON',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      license='BDS',
      author='Loic Gasser',
      author_email=u'loicgasser4@gmail.com',
      url='https://github.com/geoadmin/lib-esrijson',
      packages=['esrijson'],
      package_dir={'esrijson': 'esrijson'},
      test_suite='nose.collector',
      install_requires=['shapely'],
      )
