#!/usr/bin/python3

import os, sys
from pathlib import Path
from sys import path

base = Path('.')

pypaths = [str(pdir.absolute()) for pdir in base.glob('**/*_pattern')] + os.environ.get('PYTHONPATH', "").split(':')

print('Please run below command in your shell to update PYTHONPATH')

print("export PYTHONPATH={}".format(":".join(pypaths)))
