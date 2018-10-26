from view import View
from control import Control
from modelo import Model

m = Model()
# Instancia a View
v = View()
# Instanciar a Control
c = Control(v, m)
# Guardando a Control na View
v.set_control(c)

#exibir menu
c.exibir_menu()
