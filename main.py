import Modelos.Automata as Automata

def main():
    print("Hello, World!")
    # Crear un autómata
    a = Automata.leer_dfa_desde_entrada('./Data/dfa.txt')
    b = Automata.leer_dfa()
    a.graficar()
    b.graficar()

if __name__ == "__main__":
    main()
