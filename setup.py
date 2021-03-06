from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='rhaptos.atompub.plone',
      version=version,
      description="ATOMPUB service for plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Rhaptos Developers',
      author_email='rhaptos@rhaptos.org',
      url='http://rhaptos.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rhaptos', 'rhaptos.atompub'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[
          'PasteDeploy==1.5.0',
          'PasteScript==1.7.5',
          'Paste==1.7.5',
          ],
      paster_plugins=["ZopeSkel"],
      )
