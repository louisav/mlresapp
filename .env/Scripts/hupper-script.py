#!C:\Projects\mlres\mlresapp\.env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hupper','console_scripts','hupper'
__requires__ = 'hupper'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hupper', 'console_scripts', 'hupper')()
    )
