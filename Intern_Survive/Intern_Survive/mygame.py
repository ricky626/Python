import os
import platform

if(platform.architecture()[0] == '32bit'):
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
import logo_state

game_framework.run(logo_state)