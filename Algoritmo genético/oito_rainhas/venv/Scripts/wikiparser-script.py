#!"C:\Users\Eric\Python\Algoritmo genético\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'wikiparser==1.0.2','console_scripts','wikiparser'
__requires__ = 'wikiparser==1.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wikiparser==1.0.2', 'console_scripts', 'wikiparser')()
    )
