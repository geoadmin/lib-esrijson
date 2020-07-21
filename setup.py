from setuptools import setup


with open("README.md", "r") as fh:
        long_description = fh.read()

setup(name='esrijson',
      version='0.4.4',
      description='Bindings and utilities for EsriJSON',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      license='BSD',
      author='Loic Gasser',
      author_email=u'loicgasser4@gmail.com',
      url='https://github.com/geoadmin/lib-esrijson',
      packages=['esrijson'],
      package_dir={'esrijson': 'esrijson'},
      test_suite='nose.collector',
      install_requires=['shapely'],
      )
