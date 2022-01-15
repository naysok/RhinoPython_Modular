import rhinoscriptsyntax as rs

from rhinopython_modular import core_functions
reload(core_functions)


fc1 = core_functions.Functions_01()
fc2 = core_functions.Functions_02()


fc1.func_print_01()
fc1.func_add_circle(0, 5, 0, 5)

for i in xrange(10):
    # print(i)
    fc1.func_add_circle(i, i, 0, i+1)



fc2.func_print_msg("aa")