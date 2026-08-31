
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

---
