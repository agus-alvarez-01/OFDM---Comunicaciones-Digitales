# Ejemplo completo de transmisión OFDM con QPSK

Vamos a realizar un ejemplo completo de un sistema OFDM utilizando:

- Modulación QPSK.
- 8 símbolos QPSK.
- $N=4$ subportadoras.
- Por lo tanto, se generan $2$ símbolos OFDM.
- Se utilizará una IFFT de tamaño $N=4$.

---

## 1. Datos binarios

Supongamos que queremos transmitir los siguientes 16 bits:

$$
10\quad 00\quad 01\quad 11\quad
11\quad 01\quad 00\quad 10
$$

Como QPSK utiliza 2 bits por símbolo:

$$
\log_2(4)=2
$$

agrupamos los bits de a dos.

Por lo tanto tenemos 8 símbolos QPSK:

$$
10,\;00,\;01,\;11,\;11,\;01,\;00,\;10
$$

---

## 2. Mapeo QPSK

Utilizamos la siguiente constelación:

$$
00 \rightarrow 1+j
$$

$$
01 \rightarrow -1+j
$$

$$
11 \rightarrow -1-j
$$

$$
10 \rightarrow 1-j
$$

Por lo tanto:

| Bits | Símbolo QPSK |
|:---:|:---:|
| $10$ | $1-j$ |
| $00$ | $1+j$ |
| $01$ | $-1+j$ |
| $11$ | $-1-j$ |
| $11$ | $-1-j$ |
| $01$ | $-1+j$ |
| $00$ | $1+j$ |
| $10$ | $1-j$ |

El flujo serial de símbolos complejos es:

$$
\boxed{
1-j,\;
1+j,\;
-1+j,\;
-1-j,\;
-1-j,\;
-1+j,\;
1+j,\;
1-j
}
$$

---

## 3. Serial → Paralelo

Tenemos $N=4$ subportadoras.

Por lo tanto, agrupamos los símbolos QPSK de a cuatro.

### Símbolo OFDM #0

Los primeros cuatro símbolos forman:

$$
X^{(0)} =
\begin{bmatrix}
1-j\\
1+j\\
-1+j\\
-1-j
\end{bmatrix}
$$

Es decir:

$$
X^{(0)}[0]=1-j
$$

$$
X^{(0)}[1]=1+j
$$

$$
X^{(0)}[2]=-1+j
$$

$$
X^{(0)}[3]=-1-j
$$

Cada elemento $X^{(0)}[k]$ representa el símbolo QPSK que será colocado sobre la subportadora $k$.

---

### Símbolo OFDM #1

Los siguientes cuatro símbolos forman:

$$
X^{(1)} =
\begin{bmatrix}
-1-j\\
-1+j\\
1+j\\
1-j
\end{bmatrix}
$$

Es decir:

$$
X^{(1)}[0]=-1-j
$$

$$
X^{(1)}[1]=-1+j
$$

$$
X^{(1)}[2]=1+j
$$

$$
X^{(1)}[3]=1-j
$$

---

# 4. IFFT

La IFFT transforma los símbolos en frecuencia $X[k]$ en muestras temporales $x[n]$.

La ecuación es:

$$
x[n]=
\frac{1}{N}
\sum_{k=0}^{N-1}
X[k]e^{j2\pi kn/N}
$$

Como $N=4$:

$$
x[n]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi kn/4}
$$

Debemos calcular:

$$
x[0],\;x[1],\;x[2],\;x[3]
$$

Estas cuatro muestras constituyen un símbolo OFDM en tiempo discreto.

---

# 5. Cálculo del símbolo OFDM #0

Tenemos:

$$
X[0]=1-j
$$

$$
X[1]=1+j
$$

$$
X[2]=-1+j
$$

$$
X[3]=-1-j
$$

---

## 5.1. Cálculo de $x[0]$

Para $n=0$:

$$
x[0]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi k(0)/4}
$$

Como:

$$
e^{j0}=1
$$

queda:

$$
x[0]=
\frac{1}{4}
\left[
X[0]+X[1]+X[2]+X[3]
\right]
$$

Reemplazamos:

$$
x[0]=
\frac{1}{4}
[
(1-j)+(1+j)+(-1+j)+(-1-j)
]
$$

Partes reales:

$$
1+1-1-1=0
$$

Partes imaginarias:

$$
-j+j+j-j=0
$$

Por lo tanto:

$$
\boxed{x[0]=0}
$$

---

## 5.2. Cálculo de $x[1]$

Para $n=1$:

$$
x[1]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi k/4}
$$

Los exponentes son:

$$
e^{j0}=1
$$

$$
e^{j\pi/2}=j
$$

$$
e^{j\pi}=-1
$$

$$
e^{j3\pi/2}=-j
$$

Entonces:

$$
x[1]=
\frac{1}{4}
[
X[0]+jX[1]-X[2]-jX[3]
]
$$

Reemplazando:

$$
x[1]=
\frac{1}{4}
[
(1-j)
+j(1+j)
-(-1+j)
-j(-1-j)
]
$$

Calculamos:

$$
j(1+j)=j+j^2=-1+j
$$

$$
-(-1+j)=1-j
$$

$$
-j(-1-j)=j+j^2=-1+j
$$

Por lo tanto:

$$
x[1]=
\frac{1}{4}
[
(1-j)+(-1+j)+(1-j)+(-1+j)
]
$$

$$
x[1]=0
$$

Entonces:

$$
\boxed{x[1]=0}
$$

---

## 5.3. Cálculo de $x[2]$

Para $n=2$:

$$
x[2]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi k(2)/4}
$$

Los exponentes son:

$$
1,\;-1,\;1,\;-1
$$

Por lo tanto:

$$
x[2]=
\frac{1}{4}
[
X[0]-X[1]+X[2]-X[3]
]
$$

Reemplazamos:

$$
x[2]=
\frac{1}{4}
[
(1-j)-(1+j)+(-1+j)-(-1-j)
]
$$

Agrupando:

$$
(1-j)-(1+j)=-2j
$$

y:

$$
(-1+j)-(-1-j)=2j
$$

Entonces:

$$
x[2]=
\frac{1}{4}(-2j+2j)
$$

Por lo tanto:

$$
\boxed{x[2]=0}
$$

---

## 5.4. Cálculo de $x[3]$

Para $n=3$:

$$
x[3]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi k(3)/4}
$$

Los exponentes son:

$$
1,\;-j,\;-1,\;j
$$

Entonces:

$$
x[3]=
\frac{1}{4}
[
X[0]-jX[1]-X[2]+jX[3]
]
$$

Reemplazando:

$$
x[3]=
\frac{1}{4}
[
(1-j)
-j(1+j)
-(-1+j)
+j(-1-j)
]
$$

Calculamos:

$$
-j(1+j)=1-j
$$

$$
-(-1+j)=1-j
$$

$$
j(-1-j)=1-j
$$

Entonces:

$$
x[3]=
\frac{1}{4}
[
(1-j)+(1-j)+(1-j)+(1-j)
]
$$

$$
x[3]=
\frac{1}{4}(4-4j)
$$

Por lo tanto:

$$
\boxed{x[3]=1-j}
$$

---

# 6. Resultado del símbolo OFDM #0

En frecuencia teníamos:

$$
\boxed{
X^{(0)}=
[
1-j,\;
1+j,\;
-1+j,\;
-1-j
]
}
$$

Después de aplicar la IFFT obtenemos:

$$
\boxed{
x^{(0)}=
[
0,\;
0,\;
0,\;
1-j
]
}
$$

Estas cuatro muestras representan un único símbolo OFDM en tiempo discreto.

---

# 7. Cálculo del símbolo OFDM #1

Tenemos:

$$
X[0]=-1-j
$$

$$
X[1]=-1+j
$$

$$
X[2]=1+j
$$

$$
X[3]=1-j
$$

Aplicamos nuevamente:

$$
x[n]=
\frac{1}{4}
\sum_{k=0}^{3}
X[k]e^{j2\pi kn/4}
$$

---

## 7.1. $x[0]$

$$
x[0]=
\frac{1}{4}
[
(-1-j)+(-1+j)+(1+j)+(1-j)
]
$$

Las partes reales e imaginarias se cancelan:

$$
\boxed{x[0]=0}
$$

---

## 7.2. $x[1]$

$$
x[1]=
\frac{1}{4}
[
X[0]+jX[1]-X[2]-jX[3]
]
$$

Reemplazando:

$$
x[1]=
\frac{1}{4}
[
(-1-j)+j(-1+j)-(1+j)-j(1-j)
]
$$

Calculamos:

$$
j(-1+j)=-1-j
$$

y:

$$
-j(1-j)=-1-j
$$

Entonces:

$$
x[1]=
\frac{1}{4}
[
(-1-j)+(-1-j)+(-1-j)+(-1-j)
]
$$

Por lo tanto:

$$
\boxed{x[1]=-1-j}
$$

---

## 7.3. $x[2]$

$$
x[2]=
\frac{1}{4}
[
X[0]-X[1]+X[2]-X[3]
]
$$

$$
=
\frac{1}{4}
[
(-1-j)-(-1+j)+(1+j)-(1-j)
]
$$

$$
=
\frac{1}{4}(-2j+2j)
$$

Por lo tanto:

$$
\boxed{x[2]=0}
$$

---

## 7.4. $x[3]$

$$
x[3]=
\frac{1}{4}
[
X[0]-jX[1]-X[2]+jX[3]
]
$$

Reemplazando:

$$
x[3]=
\frac{1}{4}
[
(-1-j)-j(-1+j)-(1+j)+j(1-j)
]
$$

Calculamos:

$$
-j(-1+j)=1+j
$$

$$
j(1-j)=1+j
$$

Entonces:

$$
x[3]=
\frac{1}{4}
[
(-1-j)+(1+j)+(-1-j)+(1+j)
]
$$

Por lo tanto:

$$
\boxed{x[3]=0}
$$

---

# 8. Resultado final de la transmisión

Los 8 símbolos QPSK originales eran:

$$
\boxed{
1-j,\;
1+j,\;
-1+j,\;
-1-j,\;
-1-j,\;
-1+j,\;
1+j,\;
1-j
}
$$

Se agruparon en dos símbolos OFDM:

$$
X^{(0)}=
[
1-j,\;
1+j,\;
-1+j,\;
-1-j
]
$$

$$
X^{(1)}=
[
-1-j,\;
-1+j,\;
1+j,\;
1-j
]
$$

Después de la IFFT:

$$
x^{(0)}=
[
0,\;
0,\;
0,\;
1-j
]
$$

$$
x^{(1)}=
[
0,\;
-1-j,\;
0,\;
0
]
$$

Por lo tanto, la secuencia temporal que sale del transmisor es:

$$
\boxed{
0,\;0,\;0,\;1-j,\;
0,\;-1-j,\;0,\;0
}
$$

Esta secuencia es la que posteriormente puede pasar por el DAC, realizarse el upconversion a la frecuencia portadora y transmitirse por la antena.