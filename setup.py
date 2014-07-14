from distutils.core import setup
import py2exe

setup(
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip', 'XMLEditor.*'],
        }
    },
    console = [{'script': 'Main.py'}]
)
