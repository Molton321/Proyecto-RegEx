import random
from graphviz import Digraph


class Automata:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.id = random.randint(1,1000)
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion

    def procesar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False  # El símbolo no está en el alfabeto
            estado_actual = self.transiciones.get((estado_actual, simbolo), None)
            if estado_actual is None:
                return False  # No hay transición para el símbolo actual
        return estado_actual in self.estados_aceptacion

    def graficar(self):
        dot = Digraph()

        for estado in self.estados:
            if estado in self.estados_aceptacion:
                dot.node(estado, shape='doublecircle')
            else:
                dot.node(estado)

        dot.edge('', self.estado_inicial)

        for transicion, destino in self.transiciones.items():
            origen, simbolo = transicion
            dot.edge(origen, destino, label=simbolo)

        dot.render(f'./Images/automata{self.id}', format='png', cleanup=True)
        print(f"Se ha generado el archivo 'automata{self.id}.png'.")

def leer_dfa():
    # Definir detalles del DFA
    estados = {'q0', 'q1', 'q2'}
    alfabeto = {'0', '1'}
    estado_inicial = 'q0'
    estados_aceptacion = {'q2'}

    # Definir las transiciones del DFA
    transiciones = {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q0',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q0',
        ('q2', '0'): 'q2',
    }

    return Automata(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def leer_dfa_desde_entrada(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        estados = set(file.readline().strip().split(','))
        alfabeto = set(file.readline().strip().split(','))
        estado_inicial = file.readline().strip()
        estados_aceptacion = set(file.readline().strip().split(','))

        transiciones = {}
        for line in file:
            origen, simbolo, destino = line.strip().split(',')
            transiciones[(origen, simbolo)] = destino

    return Automata(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)
