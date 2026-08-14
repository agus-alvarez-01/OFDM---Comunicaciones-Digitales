# Receptor OFDM

El objetivo es recuperar la secuencia de bits transmitida a partir de la señal OFDM recibida.

Se considera una transmisión en **banda base** y un **canal ideal**, por lo tanto no hay ruido, desvanecimiento, interferencia ni distorsión del canal.

---

## Obtención de la señal

En un sistema real, la señal analógica recibida por la antena pasa por un conversor analógico-digital (ADC), que realiza el muestreo y cuantización de la señal para obtener una representación digital de la misma. Esta señal digital es la que posteriormente puede ser procesada por el receptor OFDM.

<!--Luego sacar--> 

El proceso de recepción puede resumirse en:

1. Recepción de la señal OFDM en tiempo discreto.
2. Eliminación del prefijo cíclico.
3. Aplicación de la DFT para recuperar los símbolos en el dominio de la frecuencia.
4. Demodulación de los símbolos complejos.
5. Recuperación de la secuencia de bits original.

---

## Señal recibida

Como el canal es ideal, no existe ninguna modificación sobre la señal transmitida. Por lo tanto, podemos considerar:

$$
r[n] = x[n]
$$

donde:

* $x[n]$ es la señal OFDM transmitida.
* $r[n]$ es la señal OFDM recibida.
* $n=0,1,...,N-1$ representa las muestras del símbolo OFDM.

---

## Eliminación del Prefijo Cíclico

Antes de aplicar la DFT es necesario eliminar el prefijo cíclico agregado en el transmisor.

Si el símbolo OFDM tiene $N$ muestras y el prefijo cíclico tiene una longitud $L_{CP}$, la señal recibida tendrá:

$$
N+L_{CP}
$$

muestras.

El receptor elimina las primeras $L_{CP}$ muestras, conservando únicamente las $N$ muestras correspondientes al símbolo OFDM original.

Podemos expresar esta operación como:

$$
r_{OFDM}[n] = r[n+L_{CP}]
$$

Para: $n=0,1,2,...,N-1$
---

## Transformación al dominio de la frecuencia

Ya con las $N$ muestras del símbolo OFDM disponibles, para recuperar los símbolos complejos que fueron asignados a las subportadoras, se aplica la DFT.

La DFT de la señal recibida se define como:

$$
Y[k] = \sum_{n=0}^{N-1} r[n] e^{-j2\pi\frac{kn}{N}}
$$

Para: $k=0,1,...,N-1$

La DFT permite transformar nuevamente la representación de la señal desde el dominio temporal hacia el dominio de la frecuencia.

En un canal ideal, debido a que:

$$
r[n] = x[n]
$$

y considerando que la DFT es la operación inversa de la IDFT, se obtiene:

$$
Y[k] = X[k]
$$

Por lo tanto, los símbolos complejos recuperados en cada subportadora son exactamente iguales a los símbolos transmitidos.

---

## Recuperación de los símbolos

La señal obtenida después de aplicar la DFT está formada por $N$ símbolos complejos:

$$
Y[0],Y[1],...,Y[N-1]
$$

Cada símbolo $Y[k]$ corresponde a la información transportada por una subportadora.

<!--Hasta acá-->

Por ejemplo, en una modulación QPSK, cada símbolo complejo representa **2 bits**. En una modulación QAM16, cada símbolo representa **4 bits**.

La cantidad de bits representados por cada símbolo depende de la modulación utilizada:

$$
b = \log_2(M)
$$

donde $M$ es el orden de la modulación.

Por lo tanto:

* QPSK: $M=4 \rightarrow b=2$ bits por símbolo.
* QAM16: $M=16 \rightarrow b=4$ bits por símbolo.
* QAM64: $M=64 \rightarrow b=6$ bits por símbolo.

---

## **Demodulación**

Los símbolos complejos recuperados mediante la DFT deben ser demodulados para obtener nuevamente la secuencia de bits original.

La demodulación realiza el proceso inverso al mapeo realizado en el transmisor.

Por ejemplo, en QPSK, los símbolos recibidos se encuentran en cuatro posibles posiciones del plano complejo:

$$
X[k] \in
\left{
\frac{1+j}{\sqrt{2}},
\frac{-1+j}{\sqrt{2}},
\frac{-1-j}{\sqrt{2}},
\frac{1-j}{\sqrt{2}}
\right}
$$

Cada posición representa una combinación diferente de dos bits.

El demodulador determina a qué símbolo de la constelación pertenece cada valor complejo recibido y asigna nuevamente la combinación de bits correspondiente.

En QAM16 el procedimiento es equivalente, pero se dispone de 16 posibles símbolos, por lo que cada símbolo representa 4 bits.

Finalmente, los grupos de bits obtenidos de cada símbolo se concatenan para formar nuevamente la secuencia de bits transmitida.

---

## **Diagrama del receptor OFDM**

El proceso completo del receptor puede representarse mediante el siguiente esquema:

$$
\boxed{\text{Señal recibida}}
\rightarrow
\boxed{\text{Eliminar CP}}
\rightarrow
\boxed{\text{DFT}}
\rightarrow
\boxed{\text{Símbolos complejos}}
\rightarrow
\boxed{\text{Demodulación}}
\rightarrow
\boxed{\text{Bits}}
$$

De esta manera, la DFT permite recuperar en el dominio de la frecuencia los símbolos que fueron utilizados para generar el símbolo OFDM en el transmisor.

---

## **Relación entre transmisor y receptor**

El transmisor y el receptor realizan operaciones inversas entre sí.

En el transmisor:

$$
\text{Bits}
\rightarrow
\text{Modulación}
\rightarrow
X[k]
\rightarrow
\text{IDFT}
\rightarrow
x[n]
$$

En el receptor:

$$
r[n]
\rightarrow
\text{DFT}
\rightarrow
Y[k]
\rightarrow
\text{Demodulación}
\rightarrow
\text{Bits}
$$

En condiciones ideales:

$$
Y[k]=X[k]
$$

por lo que los símbolos recuperados son iguales a los símbolos transmitidos y, en consecuencia, la secuencia de bits recuperada debe ser idéntica a la secuencia de bits original.

Por lo tanto, en un canal ideal y sin ruido, se espera que la tasa de error de bits sea:

$$
BER=0
$$

Esto permite verificar inicialmente el correcto funcionamiento del transmisor y receptor OFDM antes de introducir ruido y otros efectos propios de un canal de comunicaciones real.
