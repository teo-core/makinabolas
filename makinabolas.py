"""
Máquina expendedora
"""
MONEDA = 'Euro_1'

class MakinaBolas():
    """ Clase que representa la máquina"""
    def aceptar_moneda(self, moneda_insertada):
        """ Método para aceptar una moneda y
            devuelve T/F dependiendo si es correcta"""
        return moneda_insertada == MONEDA
