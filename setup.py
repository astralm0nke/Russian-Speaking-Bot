## If running on a windows machine, you'll need py2exe to make a desktop icon for Yuri
from distutils.core import setup
import py2exe

setup(console=['Юрий_Компьютеров.py'])

# Go into terminal and type directory path>python setup.py py2exe, then run
#Then go into dist directory, run file.exe