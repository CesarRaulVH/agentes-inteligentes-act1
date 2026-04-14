"""
mi_agente.py — Agente DFS simple (exploración + backtracking)
"""

from entorno import Agente


class MiAgente(Agente):

    def __init__(self):
        super().__init__(nombre="Agente DFS")
        self.visitadas = set()
        self.pila = []

    def al_iniciar(self):
        self.visitadas.clear()
        self.pila.clear()

    def decidir(self, percepcion):
        pos = percepcion['posicion']
        self.visitadas.add(pos)

        # 1. Si la meta está al lado → ir directo
        for direccion in self.ACCIONES:
            if percepcion[direccion] == 'meta':
                return direccion

        # 2. Priorizar dirección hacia la meta (opcional pero útil)
        vert, horiz = percepcion['direccion_meta']
        prioridades = []

        if vert != 'ninguna':
            prioridades.append(vert)
        if horiz != 'ninguna':
            prioridades.append(horiz)

        # completar con otras direcciones
        for d in self.ACCIONES:
            if d not in prioridades:
                prioridades.append(d)

        # 3. Ir a celdas no visitadas
        for direccion in prioridades:
            if percepcion[direccion] == 'libre':
                dr, dc = self.DELTAS[direccion]
                nueva_pos = (pos[0] + dr, pos[1] + dc)

                if nueva_pos not in self.visitadas:
                    self.pila.append(direccion)
                    return direccion

        # 4. Backtracking (retroceder)
        if self.pila:
            ultima = self.pila.pop()
            opuesto = {
                'arriba': 'abajo',
                'abajo': 'arriba',
                'izquierda': 'derecha',
                'derecha': 'izquierda'
            }
            return opuesto[ultima]

        # 5. Fallback (caso extremo)
        return 'abajo'