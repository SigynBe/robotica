from abc import ABC, abstractmethod

class Robo(ABC):
    @abstractmethod
    def mover(self, direcao):
        pass

    @abstractmethod
    def realizar_tarefa(self):
        pass

class RoboLimpeza(Robo):
    def mover(self, direcao):
        direcoes = {
            'frente': 'Robo de limpeza movendo para frente',
            'tras': 'Robo de limpeza movendo para trás',
            'esquerda': 'Robo de limpeza movendo para a esquerda',
            'direita': 'Robo de limpeza movendo para a direita'
        }
        # Introduzir um erro de sintaxe aqui propositalmente
        return direcoes.get(direcao, 'Direção inválida'

    def realizar_tarefa(self):
        return 'Robo de limpeza está limpando a área'

class RoboConstrucao(Robo):
    def mover(self, direcao):
        direcoes = {
            'frente': 'Robo de construção movendo para frente',
            'tras': 'Robo de construção movendo para trás',
            'esquerda': 'Robo de construção movendo para a esquerda',
            'direita': 'Robo de construção movendo para a direita'
        }
        # Introduzir um erro de sintaxe aqui propositalmente
        return direcoes.get(direcao, 'Direção inválida'

    def realizar_tarefa(self):
        return 'Robo de construção está construindo uma estrutura'

# Exemplo de uso
if __name__ == '__main__':
    limpeza = RoboLimpeza()
    print(limpeza.mover('frente'))  # Saída esperada: Erro de sintaxe durante a compilação
    print(limpeza.realizar_tarefa())

    construcao = RoboConstrucao()
    print(construcao.mover('direita'))  # Saída esperada: Erro de sintaxe durante a compilação
    print(construcao.realizar_tarefa())
