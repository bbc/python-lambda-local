'''
python-lambda-local: Run lambda function in python on local machine.

Copyright 2015-2018 HDE, Inc.
Licensed under MIT.
'''
import io
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


version = "0.1.8"

setup(name="python-lambda-local",
      version=version,
      description="Run lambda function in python on local machine.",
      long_description=io.open("README.rst", encoding="utf-8").read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'License :: OSI Approved :: MIT License'
      ],
      keywords="AWS Lambda",
      author="YANG Xudong",
      author_email="xudong.yang@hde.co.jp",
      url="https://github.com/HDE/python-lambda-local",
      license="MIT",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=2.7,!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4',
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      install_requires=['boto3'],
      entry_points={
          'console_scripts': ['python-lambda-local=lambda_local:main']
      })
