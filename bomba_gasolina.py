from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
   
    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            return -1
        
        valor_litro_aditivo = self._valor_litro * 1.05
        litros = valor / valor_litro_aditivo

        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return litros
   
    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0 or litros > self._quantidade_disponivel:
            return -1
        valor = litros * self._valor_litro * 1.05
        self._quantidade_disponivel -= litros
        return valor