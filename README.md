# Introducción a los Modelos Gráficos Probabilísticos - Verano 2022

En este repositorio se encuentra el material para el curso de modelos gráficos probabilísticos en el periodo de verano del 2022.

Este curso está dividido en tres módulos.

#### Módulo 1. Introducción al modelado probabilístico.

En este módulo introduciremos los contenidos del curso y usaremos un ejemplo sencillo para motivar el estudio de los modelos gráficos probabilísticos. Exploraremos modelos probabilísticos básicos, dejando de lado la parte gráfica por un momento, y en el camino recordaremos tópicos fundamentales de teoría de probabilidad, estimación de máxima verosimilitud, y además discutiremos acerca del enfoque Bayesiano. Todo esto lo usaremos en una aplicación básica que nos conducirá a la implementación de un modelo de regresión que puede trabajar online.

1. Introducción y motivación al curso.
  - Presentación de la guía de aprendizaje
  - Instalación de herramientas de trabajo.
  - Ejemplo introductorio.
  
2. Repaso de probabilidad.
  - Conceptos básicos de probabilidad.
  
3. Estimadores de máxima verosimilitud.
  - Modelos probabilísticos e inferencia.
  - Función de verosimilitud y estimación de máxima verosimilitud.
  - Ajuste de curvas: mínimos cuadrados y el problema del overfitting.
   
4. Enfoque Bayesiano.
  - MAP: efecto regularizador de la distribución previa.
  - Enfoque Bayesiano.
  - Distribuciones previas conjugadas.

5. Regresión lineal Bayesiana.
  - Derivación de las ecuaciones.
  - Ejemplo.


#### Módulo 2. Representación e inferencia en modelos gráficos probabilísticos.

En este módulo aprenderemos acerca de las dos representaciones de modelos gráficos básicas: las redes Bayesianas (grafos dirigidos) y las redes de Markov (grafos no dirigidos). Estudiaremos tanto las propiedades teóricas de dichas representaciones así como su uso en la práctica. Así mismo, aprenderemos cómo responder preguntas usando las estructuras gráficas. Adicionalmente, analizaremos una extensión importante de estas representaciones que nos permitirán representar procesos de toma de decisión.

1. Redes Bayesianas.
  - Definición y ejemplos básicos.
  - Relación entre estructura e independencia.
  - Inferencia básica en redes Bayesianas.

2. Redes de Markov
  - Definición y ejemplos básicos.
  - Relación entre estructura e independencia.
  - Inferencia básica en redes de Markov.
  
3. Teoría de decisión.
  - Funciones de utilidad.
  - Máxima utilidad esperada.
  - Valor de la información.
  
4. Inferencia exacta: Algoritmo de eliminación de variables.
  - Introducción: Tipos de inferencia.
  - Descripción del algoritmo.
  - Inferencia de probabilidad condicional.
  - Inferencia MAP.
   
5. Inferencia aproximada: Métodos de muestreo.
  - Muestreo en redes Bayesianas.
  - Cadenas de Markov Montecarlo:
      - ¿Qué son?.
      - ¿Cómo se usan?.
      - Algoritmo de muestreo de Gibbs.
      - Algoritmo Metrópolis Hastings.


#### Módulo 3. Aprendizaje en modelos gráficos.

A partir de los aprendizajes en el primer y segundo módulo, en este módulo aprenderemos cómo un modelo gráfico probabilístico puede aprenderse a partir de un conjunto de datos. Dsicutiremos los problemas principales que aparecen en la estimación de parámetros tanto en redes Bayesianas como en redes de Markov, así como en el aprendizaje estructural para redes dirigidas.

1. Estimación de parámetros en redes Bayesianas.
  - Estimación de máxima verosimilitud.
  - Estimación Bayesiana de parámetros.
  
2. Modelo de variables latentes: Algoritmo de maximización de la esperanza.
  - Variables latentes.
  - Algoritmo de maximización de la esperanza.
  - Modelo de mezclas Gaussianas.
  
3. Aprendizaje estructural.
  - Funciones de costo para aprendizaje estructural:
      - Verosimilitud.
      - Bayesiana.
  - Optimizando sobre estructuras:
      - Aprendizaje de estructuras de árbol.
      - Aprendizaje de estructuras genéricas: heurísicas.



