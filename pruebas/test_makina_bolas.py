"""
Pruebas de la clase MakinaBolas
"""
import unittest
from makinabolas import MakinaBolas, MONEDA

class TestMakina(unittest.TestCase):
    """ pruebas """
    def test_creacion_maquina(self):
        """ Prueba de existencia"""
        maquina = MakinaBolas()
        self.assertIsNotNone(maquina)

    def test_moneda_1e_es_valida(self):
        """ Prueba de moneda de un Euro es correcta"""
        maquina = MakinaBolas()
        resp = maquina.aceptar_moneda(MONEDA)
        self.assertEqual(resp, True)

    def test_moneda_50cent_es_invalida(self):
        """ Prueba de moneda de un Euro es correcta"""
        maquina = MakinaBolas()
        resp = maquina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False)
