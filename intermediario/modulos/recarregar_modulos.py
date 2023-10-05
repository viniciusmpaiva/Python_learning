import importlib

import exemplo

for i in range(10):
    importlib.reload(exemplo)
    #Recarrega o módulo