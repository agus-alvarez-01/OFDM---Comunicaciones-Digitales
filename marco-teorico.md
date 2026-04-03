# **OFDM** 

## ¿Qué es?
OFDM (Multiplexación por División de Frecuencia Ortogonal) es un método de modulación multiportadora digital para transmisión de símbolos. Divide un canal de alta velocidad en múltiples subportadoras de baja velocidad. Estas subportadoras están matemáticamente diseñadas para ser ortogonales, lo que permite que sus espectros se solapen sin interferirse mutuamente, transmitiendo datos en paralelo, mejorando la eficiencia espectral. 

Básicamente, en lugar de enviar los datos en una sola portadora, OFDM divide la señal en muchas señales más pequeñas y las transmite simultáneamente, permitiendo mayor resistencia a la interferencia y a la dispersión en el canal.

Uno de los elementos clave de la implementación de OFDM es el uso de la transformada rápida de Fourier (FFT) y su inversa (IFFT), que permiten una conversión eficaz de la señal entre los dominios de la frecuencia y el tiempo.

# Transmisor OFDM

La información que se quiere transmitir es una secuencia binaria.
La agrupación de estos binarios forman símbolos, que luego son modulados digitalmente, por ejemplo en modulación **QAM16**.
Al usar esta modulación los símbolos quedan mapeados como números complejos, obteniendo así una secuencia de **símbolos complejos**.

## Símbolos Complejos
Los símbolos complejos resultantes se asignan a las distintas subportadoras en el dominio de la frecuencia. La **IFFT** permite transformar esta representación en frecuencia al dominio temporal para su transmisión física.

## Señal OFDM en tiempo discreto
Para transmitir los símbolos en paralelo sobre múltiples subportadoras ortogonales, la IFFT genera en el dominio temporal la combinación lineal de exponenciales complejas ortogonales.
Para implementarlo, se generan muestras de los símbolos a transmitir.
Podemos definir $N$ como la cantidad de muestras por símbolo, a $T$ como el periodo de cada símbolo y a $T_s$ como el periodo de muestreo $(T_s=T/N)$.
Con un paso de $t=nT_s$ ($t=nT/N$), la señal OFDM se determina como:

$$
s[n] = \sum_{k=0}^{N-1} X_k \, e^{j 2\pi \frac{kn}{N}}
$$

Para $n=0,1,2,...,N-1$

Donde:
- $X[k]$ son los símbolos complejos asignados a cada subportadora.
- Cada término exponencial representa una subportadora ortogonal.

## Garantía de Ortogonalidad
La ortogonalidad entre subportadoras se garantiza cuando el espaciamiento en frecuencia cumple $\Delta f=1/T$

---
---
---
---

$$
s(t) = \sum_{k=0}^{N-1} X[k] \, e^{j 2\pi f[k] t}, \quad 0 \le t < T
$$

Donde:
- $X[k]$ = símbolo complejo en la subportadora $k$
- $f[k]$ = frecuencia de la subportadora
- $N$ = número total de subportadoras
- $T$ = duración del símbolo OFDM
- Cada término exponencial representa una subportadora ortogonal

## Garantia de Ortogonalidad
La ortogonalidad entre subportadoras se garantiza cuando el espaciamiento en frecuencia cumple $\Delta f=1/T$






# Prefijo ciclico 
---
---
---
---

$$
s[n] = \sum_{k=0}^{N-1} X_k \, e^{j 2\pi \frac{kn}{N}}
$$

Para $n=0,1,2,...,N-1$

Donde:
- $X[k]$ son los símbolos complejos asignados a cada subportadora.
- Cada término exponencial representa una subportadora ortogonal.
<!-- Corroborar está parte, no está bien explicado quizas -->
- La ortogonalidad entre subportadoras se garantiza cuando el espaciamiento en frecuencia cumple $\Delta f=1/T$, donde $T$ es la duración del símbolo OFDM.

De esta forma, se obtiene una señal OFDM que transmite múltiples símbolos en paralelo con alta eficiencia espectral.




## Garantia de Ortogonalidad
La ortogonalidad entre subportadoras se garantiza cuando el espaciamiento en frecuencia cumple $\Delta f=1/T$, donde $T$ es la duración del símbolo OFDM.




## IFFT
$$
x[n] = \frac {1}{N} \sum_{k=0}^{N-1} X[k] \, e^{j 2\pi kn/N}
$$

$n=0,1,2,...,N-1$
![transmisor_ideal](imagen-transmisor.png)
.....................................

---
https://www.tme.com/mx/es/news/library-articles/glossary/page/69328/ofdm-multiplexacion-por-division-de-frecuencias-ortogonales-definicion/

Uno de los elementos clave de la implementación de OFDM es el uso de la transformada rápida de Fourier (FFT) y su inversa (IFFT), que permiten una conversión eficaz de la señal entre los dominios de la frecuencia y el tiempo.
---
---
** --- **
---
# Prefijo ciclico 

1/N --> escala la potencia 

## IFFT
Para generar las subportadoras y transmitir los símbolos en paralelos se útiliza una algoritmo llamado **IFFT**(Inverse Fast Fourier Transform), el cual nos permite montar los simbolos y garantizar ortogonalidad entre subportadoras.
---


## ¿Cómo es matemáticamente?

Matemáticamente, la señal OFDM en el dominio temporal es: 

$$
s(t) = \sum_{k=0}^{N-1} X_k \, e^{j 2\pi f_k t}, \quad 0 \le t < T
$$

Donde:
- $𝑋_𝑘$ = símbolo complejo en la subportadora $k$
- $𝑓_𝑘$ = frecuencia de la subportadora
- $N$ = número total de subportadoras
- $T$ = duración del símbolo OFDM

### ¿Cómo garantizamos ortogonalidad?

Para garantizar ortogonalidad $𝑓_𝑘$ es equivalente a $k.\Delta f$, donde $\Delta f=1/T$. Entonces:

$$
s(t) = \sum_{k=0}^{N-1} X_k \, e^{j 2\pi k \frac{t}{T}}
$$

# que hace esto en la ortogonalidad? explicar mas, llegar a lo de producto punto.

### ¿Cómo se implementa en tiempo discreto?

Para implementarlo se generan muestras de los símbolos a transmitir.
Podemos definir $N$ como la cantidad de muestras por símbolo, a $T_s$ como el periodo de muestreo $(T_s=T/N)$, y a $t=nT_s=nT/N$. 

Al sustituir y simplificar en la ecuacion anterior se obtiene:

$$
s[n] = \sum_{k=0}^{N-1} X_k \, e^{j 2\pi \frac{kn}{N}}
$$

Para $n=0,1,2,...,N-1$

--- 
## método de modulación multiportadora digital para transmisión de símbolos
## IFFT



decir que es, como se define matematicamente y hacer la relacion con la formula anterior.

### ¿Como pasamos de un modelo en dominio temporal continuo a garantizar ortogonalidad en tiempo discreto?

A través de una **IFFT** (Transformada inversa rápida de Fourier).

$𝑓_𝑘$ es equivalente a $k.\Delta f$, y $\Delta f=1/T$ 

## ¿IFFT?




¿a que se refiere con que sea de alta y baja velocidad?
¿Para qué sirve? ¿Qué ventaja tiene al usarla?
¿Qué representa la fórmula matemática?
¿Qué decía evangelista sobre la OFDM? 

https://es.wikipedia.org/wiki/Diagrama_de_constelaci%C3%B3n --> explicación para la constelación
