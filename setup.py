#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='WarHammer',
      version='0.2',
      
      packages = find_packages("WarHammer"),
      package_dir={"": "WarHammer"},
      package_data={"": ["Pickles/*.pickle"]},
      data_files=[('WarHammer/Pickles/', ['career_table.pickle',
                                          'classes_table.pickle',
                                          'eye_table.pickle',
                                          'hair_table.pickle',
                                          'RandTalent_table.pickle']
      )],
      include_package_data=True, # bad?

      # installed or upgraded on the target machine
      install_requires=["pandas>=1.0"],

      # metadata to display on PyPI
      author='Joe Howie',
      author_email='joehowie@protonmail.com',
      description='A plugin that allows the creation of warhammer characters',
      keywords='warhammer fantasy RPG',
      url='https://github.com/JoetheManHowie/WarHammer',
      #project_urls = {},
      classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
      ],
      # could also include long_description, download_url, etc.
      zip_safe=False)
