# SRI-Deteccion-de-Plagio-Documentos

## Integrantes

- Carlos Arturo Pérez Cabrera
- Diana Laura Pérez Tujillo

## Descripción del problema  

El problema consiste en desarrollar un sistema de detección de plagio en documentos. El objetivo es determinar el porcentaje de probabilidad de plagio entre dos textos dados.

El sistema debe comparar y analizar los documentos para identificar similitudes y coincidencias que puedan indicar plagio. Se utilizan técnicas como el preprocesamiento de los textos, la tokenización y la comparación de estructuras y contenido. Para ello se realiza un análisis semántico y léxico, calculando ambas similitudes, y concluyendo con una similitud final.



## Consideraciones tomadas a la hora de desarrollar la solución

La solución ha sido implementada orientada a textos en el idioma inglés. Además los documentos se encontrarán dentro de la carpeta documents, permitiendo así ser leídos por el programa.

## Explicación de como ejecutar el proyecto. Posibles entradas de parámetros

Para ejecutar el proyecto se debe ejecutar el archivo startup.py que llamará a la función 'detect_plagiarism'. Luego se realiza la interacción con el usuario, donde se listarán por consola todos los documentos a escoger para la comparación.

## Explicación de la solución desarrollada

La solución desarrollada resulta de dos pasos importantes: Cálculo de la Similitud Léxica y Cálculo de la Similitud Semántica. Para la Similitud Léxica se utilizó el Algoritmo TF-IDF, siendo de apoyo algunas bibliotecas de Python. Para el Cálculo de la Similitud Semántica se utilizó BERT. En ambos casos se calcula la similitud con Similitud de Coseno. Con la puntuación devuelta se calcula el por ciento de similitud que se devuelve al usuario.

### Similitud del coseno

La similitud del coseno es una medida utilizada para calcular cuánto se parecen dos vectores de características. Se basa en el ángulo entre los vectores en un espacio n-dimensional. Cuanto más cerca estén los vectores, mayor será su similitud del coseno.

### TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) es una técnica utilizada en el procesamiento de texto para evaluar la importancia de una palabra en un documento dentro de una colección de documentos. TF-IDF se basa en dos conceptos clave:

1. Frecuencia de término (TF): Mide la frecuencia con la que aparece un término específico en un documento. Cuanto más veces aparezca un término en un documento, mayor será su valor de TF.

2. Frecuencia inversa de documentos (IDF): Mide la importancia de un término en una colección de documentos. Palabras que aparecen con frecuencia en varios documentos tendrán un valor de IDF más bajo, mientras que aquellas palabras que son más raras en la colección tendrán un valor de IDF más alto.

La fórmula general para calcular TF-IDF de un término en un documento es el producto de su frecuencia de término (TF) y su frecuencia inversa de documentos (IDF).

El objetivo de TF-IDF es asignar un peso más alto a los términos que son relevantes y distintivos para un documento en particular, y un peso más bajo a los términos que son comunes en la colección de documentos.

### BERT

BERT (Bidirectional Encoder Representations from Transformers) es un modelo de lenguaje basado en transformers. Es una biblioteca de procesamiento de lenguaje natural (NLP) que ha demostrado un rendimiento sobresaliente en una amplia gama de tareas de procesamiento de texto, como clasificación de texto, extracción de información y respuesta a preguntas.

BERT tiene la capacidad única de comprender el contexto y la relación entre las palabras en una oración al utilizar un enfoque de codificación bidireccional. A diferencia de los modelos de lenguaje anteriores que procesaban las palabras secuencialmente en una sola dirección (de izquierda a derecha o de derecha a izquierda), BERT considera el contexto de las palabras circundantes en ambas direcciones. Esto le permite capturar relaciones más complejas y mejorar la comprensión del lenguaje.

La biblioteca BERT proporciona modelos pre-entrenados en grandes conjuntos de datos y también ofrece herramientas y recursos para adaptar y ajustar estos modelos a tareas de procesamiento de texto específicas.

## Insuficiencias de la solución  y mejoras propuestas

- Se propone una mejor ponderación para la Similitud Léxica y la Similitud Semántica, puesto que los respectivos umbrales de las puntuaciones de cada una, difieren bastante. En la solución presentada se establece una proporción de 3/4 para Similitud Léxica y 1/4 para Similitud Semántica, pero se podría ahondar con vistas a encontrar una mejor proporción.
- Actualmente, se leen documentos tipo .txt, pero podrían implementarse la posibilidad de lectura de otros formatos de archivo.
- La interacción con el usuario se realiza mediante consola, se propone el desarrollo de una interfaz de usuario más cómoda.
