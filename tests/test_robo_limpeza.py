import unittest
from robos import RoboLimpeza

class TestRoboLimpeza(unittest.TestCase):
    def setUp(self):
        self.robo = RoboLimpeza()

    def test_mover_frente(self):
        self.assertEqual(self.robo.mover('frente'), 'Robo de limpeza movendo para frente')

    def test_mover_tras(self):
        self.assertEqual(self.robo.mover('tras'), 'Robo de limpeza movendo para trás')

    def test_mover_esquerda(self):
        self.assertEqual(self.robo.mover('esquerda'), 'Robo de limpeza movendo para a esquerda')

    def test_mover_direita(self):
        self.assertEqual(self.robo.mover('direita'), 'Robo de limpeza movendo para a direita')

    def test_mover_direcao_invalida(self):
        self.assertEqual(self.robo.mover('cima'), 'Direção inválida')

    def test_realizar_tarefa(self):
        self.assertEqual(self.robo.realizar_tarefa(), 'Robo de limpeza está limpando a área')

if __name__ == '__main__':
    unittest.main()
