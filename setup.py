from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='allen.content.jokes',
      version=version,
      description="jokes",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='allen content jokes',
      author='Alin Voinea',
      author_email='alin.voinea@gmail.com',
      url='http://github.com/avoinea/allen.content.jokes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['allen', 'allen.content'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
