#  Agente de Navegación en Grid World usando DFS

## Descripción

Este proyecto implementa un agente inteligente capaz de navegar desde un punto inicial (A) hasta una meta (B) en un entorno tipo Grid World con obstáculos.

El entorno es **parcialmente observable**, ya que el agente solo puede percibir las celdas adyacentes en cada iteración, por lo que no cuenta con conocimiento global del mapa.

---

## Enfoque de la solución

Para resolver el problema se implementó un agente basado en el algoritmo **Depth-First Search (DFS)**.

Este enfoque permite explorar el entorno de manera sistemática sin necesidad de conocer el mapa completo.

El agente utiliza:

* Un conjunto de celdas visitadas para evitar ciclos
* Una pila para realizar **backtracking** cuando no encuentra nuevos caminos

---

## Función de utilidad

La utilidad del agente se define como el **número de pasos necesarios para alcanzar la meta**.

El objetivo es minimizar esta cantidad. Sin embargo, DFS no garantiza encontrar el camino más corto, pero sí una solución válida en entornos desconocidos.

---

## Funcionamiento del agente

En cada iteración, el agente realiza:

1. Observa su posición y entorno inmediato
2. Verifica si la meta está en una celda adyacente
3. Si no, busca una celda libre no visitada
4. Se mueve hacia esa celda y la registra
5. Si no hay opciones, realiza backtracking
6. Repite el proceso hasta encontrar la meta

---

## Estructura del proyecto

* `entorno.py` → entorno del problema (no editable)
* `mi_agente.py` → implementación del agente
* `main.py` → configuración y ejecución

---

## Código del agente

El agente fue implementado en el archivo `mi_agente.py`:

---

## Pruebas realizadas

Se realizaron pruebas con distintas configuraciones del entorno:

* Prueba 1: (15x15, 30% paredes, semilla 10)
* Prueba 2: (15x15, 30% paredes, semilla 20)
* Prueba 3: (15x15, 30% paredes, semilla 30)

En todos los casos, el agente logró alcanzar la meta.

---

## Resultados

El agente navega correctamente en diferentes escenarios, explorando el entorno mediante DFS.

Aunque el camino no siempre es el más corto, el agente cumple con el objetivo de llegar a la meta de forma consistente.

---

## Conclusión

El algoritmo DFS resulta adecuado para este problema debido a la naturaleza parcialmente observable del entorno.

A diferencia de algoritmos como BFS o A*, que requieren conocimiento global, DFS permite explorar el mapa de manera eficiente y garantizar una solución.

Asimismo, se descartó el uso de algoritmos como Wall-Follower debido a su posible ineficiencia en ciertos casos.

---

## Autor

* César Valdivia Huayllas