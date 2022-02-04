"""
Pruebas de la clase MakinaBolas
"""
import unittest
from makinabolas import MakinaBolas, MONEDA, BOLA

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
        """ Prueba de moneda de 50 cts es incorrecta"""
        maquina = MakinaBolas()
        resp = maquina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False)

    def test_giro_manivela_correcto(self):
        """ Si gira correctamente es True"""
        maquina = MakinaBolas()
        giro = 360
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp, True)

    def test_giro_manivela_no_360_incorrecto(self):
        """ Si gira menos de 360º es incorrecto"""
        maquina = MakinaBolas()
        giro = 30
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp, False)

    def test_moneda_y_giro_correctos_suelta_bola(self):
        """ Si las condiciones son correctas suelta una bola"""
        maquina = MakinaBolas()
        dep = maquina.deposito
        mon = maquina.monedero
        resp = maquina.soltar_bola()

        self.assertEqual(resp, BOLA)
        self.assertEqual(maquina.deposito, dep-1)
        self.assertEqual(maquina.monedero, mon+1)

