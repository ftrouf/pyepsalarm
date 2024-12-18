from setuptools import setup

__version__ = '1.0.5'

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pyepsalarm',
    py_modules=["pyepsalarm"],
    version=__version__,
    description='A simple library to interface with EPS systems, built for use with Home-Assistant',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Parv Arm',
    author_email='parvarm@outlook.fr',
    url='https://github.com/ftrouf/pyepsalarm',
    download_url='https://github.com/ftrouf/pyepsalarm',
    license='Apache 2.0',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords=['eps', 'homiris', 'alarm', 'hass', 'home assistant'],
    packages=['pyepsalarm'],
    include_package_data=True,
    install_requires=['requests>=2.0.0'],
)
