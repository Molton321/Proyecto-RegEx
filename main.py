import Modelos.Automata as Automata

#casos de prueba 
# a = Automata.build_automaton_from_regex("ab+|b+a*")
# a = Automata.build_automaton_from_regex("ab+"
# a = Automata.build_automaton_from_regex("b+a*")
# a = Automata.build_automaton_from_regex("abb*")
# a = Automata.build_automaton_from_regex("ab|b+a+b*")
# Ejemplo de uso
if __name__ == "__main__":
    # no uso de () en la expresión regular
    regex = input("Ingrese una expresión regular: ")
    a = Automata.build_automaton_from_regex(regex)
    # graficar automata desde archivo
    #a = Automata.leer_dfa_desde_entrada("./Data/dfa.txt")
    a.graficar()

