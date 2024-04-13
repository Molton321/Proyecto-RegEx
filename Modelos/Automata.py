import random
from graphviz import Digraph


class Automata:
    def __init__(self, estados = {'q0'}, alfabeto = {}, transiciones = {}, estado_inicial = 'q0', estados_aceptacion = {}):
        self.id = random.randint(1,1000)
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion

    def get_alphabet(self):
        return self.alfabeto

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
    
    def alphabet_from_regex(self, regex):

        for i in range(len(regex)):
            if regex[i]!=('+','-','|','?','(',')') and regex[i] not in self.alfabeto:
                self.alfabeto.add(regex[i])
        return 
    


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

def build_automaton_from_regex(regex):
    states = set()  # Conjunto de estados
    alphabet = set()  # Alfabeto
    transitions = {}  # Transiciones representadas como un diccionario
    initial_state = 'q0'  # Estado inicial
    accepting_states = set()  # Conjunto de estados de aceptación

    # Función para agregar una transición
    def add_transition(from_state, to_state, input_symbol):
        nonlocal states, alphabet, transitions
        states.add(from_state)
        states.add(to_state)
        alphabet.add(input_symbol)
        transitions[(from_state, input_symbol)] = to_state
    
    current_state = initial_state
    i = 0
    while i < len(regex):
        if i == len(regex) - 1:
            if regex[i] == "*":
                add_transition(current_state, current_state, "")
            elif regex[i] == "+":
                add_transition(current_state, current_state, "")
                accepting_states.add(current_state)
            else:
                add_transition(current_state, 'q' + str(i + 1), regex[i])
                accepting_states.add('q' + str(i + 1))
        elif regex[i] == "|":
            new_state1='q'+ str(i)
            new_state2='q'+ str(i)
            accepting_states.add(new_state1)
            accepting_states.add(new_state2)
            current_state = initial_state
            i += 1
            continue
        elif regex[i + 1] == "*":
            new_state = 'q' + str(i + 1)
            add_transition(current_state, current_state, regex[i])
            current_state = new_state
            i += 1
        elif regex[i + 1] == "+":
            new_state = 'q' + str(i + 1)
            add_transition(current_state, new_state, regex[i])
            add_transition(new_state, new_state, regex[i])
            accepting_states.add(new_state)
            current_state = new_state
            i += 1
        else:
            new_state = 'q' + str(i + 1)
            add_transition(current_state, new_state, regex[i])
            current_state = new_state
        
        i += 1

    print(f'''
    states: {states}
    alphabet: {alphabet}
    transitions: {transitions}
    initial_state: {initial_state}
    accepting_states: {accepting_states}
''')

    return Automata(states, alphabet, transitions, initial_state, accepting_states)
