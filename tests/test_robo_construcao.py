import unittest
from robos import RoboConstrucao

class TestRoboConstrucao(unittest.TestCase):
    def setUp(self):
        self.robo = RoboConstrucao()

    def test_mover_frente(self):
        self.assertEqual(self.robo.mover('frente'), 'Robo de construção movendo para frente')

    def test_mover_tras(self):
        self.assertEqual(self.robo.mover('tras'), 'Robo de construção movendo para trás')

    def test_mover_esquerda(self):
        self.assertEqual(self.robo.mover('esquerda'), 'Robo de construção movendo para a esquerda')

    def test_mover_direita(self):
        self.assertEqual(self.robo.mover('direita'), 'Robo de construção movendo para a direita')

    def test_mover_direcao_invalida(self):
        self.assertEqual(self.robo.mover('cima'), 'Direção inválida')

    def test_realizar_tarefa(self):
        self.assertEqual(self.robo.realizar_tarefa(), 'Robo de construção está construindo uma estrutura')

if __name__ == '__main__':
    unittest.main()
