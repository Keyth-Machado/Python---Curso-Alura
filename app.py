from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante__praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 5.0, '700 ml')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Francesinho', 2.0, 'Pão francês')
prato_paozinho.aplicar_desconto()
restaurante__praca.adicionar_no_cardapio(bebida_suco)
restaurante__praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante__praca.exibir_cardapio

if __name__ == '__main__':
    main()