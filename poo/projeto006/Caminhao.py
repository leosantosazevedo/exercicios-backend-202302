import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, eixo, lotacao, marca, modelo, ano, potencia, tipoCaminhao ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.eixo = eixo
        self.lotacao = lotacao
        self.tipoCaminhao = tipoCaminhao
        self.potencia = potencia
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
""" Aqui comeca o teste """
CaminhaoNovo = Caminhao('8885AZKG01Z12A33921312', 6, 2500, 'Mercedes', '1113', '2022', 5.8, 'TRUCK')
print(CaminhaoNovo.get_tipo())
print(CaminhaoNovo.potencia)
print(CaminhaoNovo.eixo)
print(CaminhaoNovo.lotacao)
print(CaminhaoNovo.tipoCaminhao)
print(CaminhaoNovo.ligar())
