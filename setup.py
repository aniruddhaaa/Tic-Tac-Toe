import sys
from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

build_exe_options = {'packages': ['os'], 'include_files': ['icon.ico']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

target = Executable(
    script = 'game.py',
    base = 'Win32GUI',
    icon = 'icon.ico'
    )

setup(
    name = 'Tic Tac Toe',
    version = '1.0',
    description = 'Play Tic Tac Toe',
    options = {'build_exe': build_exe_options},
    executables = [target]
)