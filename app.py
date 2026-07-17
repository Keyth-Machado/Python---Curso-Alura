from modelos.restaurante import Restaurante

restaurante__praca = Restaurante('Praça', 'Gourmet')

restaurante__praca.receber_avaliacao('Gui', 10)
restaurante__praca.receber_avaliacao('Lais', 8)
restaurante__praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()