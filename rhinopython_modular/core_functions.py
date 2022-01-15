import rhinoscriptsyntax as rs


class Functions_01():

    def func_print_01(self):
        print("Hello 01")

    def func_add_point(self, pt_x, pt_y, pt_z):
        rs.AddPopint(pt_x, pt_y, pt_z)

    def func_add_circle(self, center_x, center_y, center_z, rad):
        rs.AddCircle((center_x, center_y, center_z), rad)


class Functions_02():

    def func_print_02(self):
        print("Hello 02")
    
    def func_print_msg(self, msg):
        
        print(msg)
    
    def func_add_line(self, start_x, start_y, start_z, end_x, end_y, end_z):
        rs.AddLine((start_x, start_y, start_z), (end_x, end_y, end_z))
