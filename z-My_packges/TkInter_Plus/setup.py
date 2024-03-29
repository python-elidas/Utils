from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n'
)

setup(
    name = 'extended-tk',
    version = '0.14.0',
    description='An add-on for the tkinter package',
    long_description = long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    keywords = 'Tkinter',
    author = 'Elidas',
    license = 'GNUGPLv3',
    packages = ['extended_tk']
)
