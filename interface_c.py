import rhinoscriptsyntax as rs

from rhinopython_modular import core_functions
reload(core_functions)


fc1 = core_functions.Functions_01()
fc2 = core_functions.Functions_02()


fc2.func_print_current_time()