#!C:\Projects\mlres\mlresapp\.env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'waitress','console_scripts','waitress-serve'
__requires__ = 'waitress'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('waitress', 'console_scripts', 'waitress-serve')()
    )
