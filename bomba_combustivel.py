class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self._valor_litro = valor_litro
        self._quantidade_disponivel = quantidade_disponivel
   
    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return -1
        litros = valor / self._valor_litro
        if litros > self._quantidade_disponivel:
            return -1
        self._quantidade_disponivel -= litros
        return litros
   
    def abastecer_por_litro(self, litros):
        if litros <= 0 or litros > self._quantidade_disponivel:
            return -1
        valor = litros * self._valor_litro
        self._quantidade_disponivel -= litros
        return valor
   
    @property
    def valor_litro(self):
        return self._valor_litro
   
    @valor_litro.setter
    def valor_litro(self, valor_litro):
        self._valor_litro = valor_litro
   
    @property
    def quantidade_disponivel(self):
        return self._quantidade_disponivel
   
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade_disponivel):
        self._quantidade_disponivel = quantidade_disponivel
