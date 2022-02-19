from Model import Usuario
import unittest

class TestModel(unittest.TestCase):
    def test_buscarUsuario(self):
        datos = Usuario().buscarUsuario('david@gmail.com')
        # self.assertEqual(datos, bool({'Nombres': 'David','Apellidos': 'Lievano Gonzalez','Edad': 28,'Email': 'david@gmail.com'}))
        # self.assertFalse(Usuario().buscarUsuario('juan'))
        # self.assertTrue(Usuario().buscarUsuario('marta@gmail.com'))
        # self.assertEqual({}, {})
        self.assertDictEqual({'Nombres': 'David','Apellidos': 'Lievano Gonzalez','Edad': 28,'Email': 'david@gmail.com'}, datos)
