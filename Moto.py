from Veiculo import Veiculo
from Automovel import Automovel


class Moto(Automovel):
    def __init__(self, marca, qtd_Rodas, modelo, potenciaMotor ,partidaEletrica, velocidade = 0):
        Automovel.__init__(self, marca, qtd_Rodas, modelo, velocidade, potenciaMotor)
        self.partidaEletrica = partidaEletrica

    def imprimir_informacoes(self):
            print ("Marca: ", self.marca)
            print ("Modelo: : ", self.modelo)
            print ("Velocidade: ", self.velocidade)
            print ("Rodas: ", self.qtdRodas)
            print ("Potência do motor: ", self.potenciaMotor, " cavalos.")  
            print ("Partida Eletrica: ", self.partidaEletrica)