import sys, os
print('python:', sys.executable)
print('version:', sys.version)
print('cwd:', os.getcwd())
print('files:', os.listdir('.'))
print('PYTHONPATH:', os.environ.get('PYTHONPATH'))
