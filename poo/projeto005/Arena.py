class Arena:
    def __init__( self, guerreiro01, guerreiro02, valorDoDado):
        self.__guerreiro01 = guerreiro01
        self.__guerreiro02 = guerreiro02
        self.__valorDoDado = valorDoDado
    def __render(self):
        self.__limpa_tela()
        print("-------------- Arena -------------- \n")
        print("Saude dos Guerreiros: \n")
        print("{0} {1}".format(self.__guerreiro01, self.__guerreiro01.barraDeSaude()))
        print("{0} {1}".format(self.__guerreiro02, self.__guerreiro02.barraDeSaude()))
    def __limpa_tela(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])
    def __print_mensagem(self, mensagem):
        import time as _time
        print(mensagem)
        _time.sleep(0.75)
    def lutar(self):
        print("Bem-vindos a Arena!")
        print("Hoje {0} lutara contra {1} !".format(self.__guerreiro01,self.__guerreiro02))
        print("Que comecem os jogos...", end=" ")
        #loop da luta
        while(self.__guerreiro01.estaVivo() and self.__guerreiro02.estaVivo() ):
            self.__guerreiro01.ataque(self.__guerreiro02)
            self.__render()
            self.__print_mensagem(self.__guerreiro01.get_mensagem())
            self.__print_mensagem(self.__guerreiro02.get_mensagem())
            self.__guerreiro02.ataque(self.__guerreiro01)
            self.__render()
            self.__print_mensagem(self.__guerreiro02.get_mensagem())
            self.__print_mensagem(self.__guerreiro01.get_mensagem())
            print("")