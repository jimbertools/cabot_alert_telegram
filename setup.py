#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cabot_alert_telegram',
      version='0.1',
      description='A Telegram alert plugin for Cabot by Arachnys',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='https://github.com/codesyntax/cabot_alert_telegram',
      license='GPL',
      install_requires=[
        'pyTelegramBotAPI'
      ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
)
