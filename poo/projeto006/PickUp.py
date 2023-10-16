import Veiculo
class PickUp ( Veiculo.Veiculo ):
    def __init__(self, chassi, eixo, lotacao, marca, modelo, ano, potencia, tipoPickUp ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("PickUp")
        self.eixo = eixo
        self.lotacao = lotacao
        self.tipoPickUp = tipoPickUp
        self.potencia = potencia
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
""" Aqui comeca o teste """
PickUpNovo = PickUp('8885AZKG01Z12A33921312', 6, 2500, 'Mercedes', '1113', '2022', 5.8, 'TRUCK')
print(PickUpNovo.get_tipo())
print(PickUpNovo.potencia)
print(PickUpNovo.eixo)
print(PickUpNovo.lotacao)
print(PickUpNovo.tipoPickUp)
print(PickUpNovo.ligar())