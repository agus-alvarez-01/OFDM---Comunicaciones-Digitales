# Ejemplo completo de recepción OFDM con QPSK

Partimos de la señal temporal generada por el transmisor.

La secuencia transmitida era:

$$
\boxed{
0,\;0,\;0,\;1-j,\;
0,\;-1-j,\;0,\;0
}
$$

Como utilizamos $N=4$, dividimos la señal en bloques de cuatro muestras.

---

# 1. Separación de los símbolos OFDM

La señal recibida, suponiendo un canal ideal sin ruido, es:

$$
r[n]=x[n]
$$

Dividimos la secuencia:

### Símbolo OFDM recibido #0

$$
r^{(0)}=
[
0,\;
0,\;
0,\;
1-j
]
$$

### Símbolo OFDM recibido #1

$$
r^{(1)}=
[
0,\;
-1-j,\;
0,\;
0
]
$$

Ahora debemos recuperar los símbolos QPSK originales.

Para esto aplicamos una FFT.

---

# 2. FFT

La FFT/DFT utilizada en el receptor es:

$$
X[k]=
\sum_{n=0}^{N-1}
r[n]e^{-j2\pi kn/N}
$$

Como:

$$
N=4
$$

tenemos:

$$
X[k]=
\sum_{n=0}^{3}
r[n]e^{-j2\pi kn/4}
$$

Calcularemos:

$$
X[0],\;X[1],\;X[2],\;X[3]
$$

La razón por la cual recuperamos los símbolos originales es que:

$$
\mathrm{FFT}\{\mathrm{IFFT}\{X[k]\}\}=X[k]
$$

---

# 3. Recuperación del símbolo OFDM #0

Tenemos:

$$
r[0]=0
$$

$$
r[1]=0
$$

$$
r[2]=0
$$

$$
r[3]=1-j
$$

Debemos recuperar:

$$
X[0],X[1],X[2],X[3]
$$

---

## 3.1. Recuperación de $X[0]$

La ecuación es:

$$
X[0]=
\sum_{n=0}^{3}
r[n]e^{-j2\pi(0)n/4}
$$

Como todos los exponentes son 1:

$$
X[0]=r[0]+r[1]+r[2]+r[3]
$$

Reemplazamos:

$$
X[0]=
0+0+0+(1-j)
$$

Por lo tanto:

$$
\boxed{X[0]=1-j}
$$

Este era exactamente el símbolo QPSK original colocado en la subportadora 0.

---

# 4. Recuperación de $X[1]$

Tenemos:

$$
X[1]=
\sum_{n=0}^{3}
r[n]e^{-j2\pi n/4}
$$

Los exponentes son:

$$
e^{j0}=1
$$

$$
e^{-j\pi/2}=-j
$$

$$
e^{-j\pi}=-1
$$

$$
e^{-j3\pi/2}=j
$$

Entonces:

$$
X[1]=
r[0]-jr[1]-r[2]+jr[3]
$$

Como:

$$
r[0]=0
$$

$$
r[1]=0
$$

$$
r[2]=0
$$

$$
r[3]=1-j
$$

queda:

$$
X[1]=
j(1-j)
$$

Desarrollamos:

$$
j(1-j)
=
j-j^2
$$

Como:

$$
j^2=-1
$$

entonces:

$$
j-j^2=j+1
$$

Por lo tanto:

$$
\boxed{X[1]=1+j}
$$

Recuperamos nuevamente el símbolo QPSK original.

---

# 5. Recuperación de $X[2]$

La ecuación es:

$$
X[2]=
\sum_{n=0}^{3}
r[n]e^{-j2\pi(2)n/4}
$$

Los exponentes son:

$$
1,\;-1,\;1,\;-1
$$

Por lo tanto:

$$
X[2]=
r[0]-r[1]+r[2]-r[3]
$$

Reemplazamos:

$$
X[2]=
0-0+0-(1-j)
$$

Entonces:

$$
\boxed{X[2]=-1+j}
$$

Nuevamente recuperamos el símbolo original.

---

# 6. Recuperación de $X[3]$

Tenemos:

$$
X[3]=
\sum_{n=0}^{3}
r[n]e^{-j2\pi(3)n/4}
$$

Los exponentes son:

$$
1,\;j,\;-1,\;-j
$$

Entonces:

$$
X[3]=
r[0]+jr[1]-r[2]-jr[3]
$$

Reemplazando:

$$
X[3]=
-j(1-j)
$$

Primero:

$$
j(1-j)=1+j
$$

por lo tanto:

$$
-j(1-j)=-1-j
$$

Entonces:

$$
\boxed{X[3]=-1-j}
$$

Recuperamos el cuarto símbolo QPSK.

---

# 7. Resultado del símbolo OFDM #0

El receptor recuperó:

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

Comparemos con lo que había enviado el transmisor:

$$
X^{(0)}_{\mathrm{TX}}=
[
1-j,\;
1+j,\;
-1+j,\;
-1-j
]
$$

$$
X^{(0)}_{\mathrm{RX}}=
[
1-j,\;
1+j,\;
-1+j,\;
-1-j
]
$$

Son exactamente iguales.

---

# 8. Recuperación del símbolo OFDM #1

Ahora tenemos:

$$
r[0]=0
$$

$$
r[1]=-1-j
$$

$$
r[2]=0
$$

$$
r[3]=0
$$

---

## 8.1. Recuperación de $X[0]$

$$
X[0]=
r[0]+r[1]+r[2]+r[3]
$$

Entonces:

$$
X[0]=
0+(-1-j)+0+0
$$

Por lo tanto:

$$
\boxed{X[0]=-1-j}
$$

---

# 9. Recuperación de $X[1]$

Tenemos:

$$
X[1]=
r[0]-jr[1]-r[2]+jr[3]
$$

Reemplazamos:

$$
X[1]=
-j(-1-j)
$$

Desarrollamos:

$$
-j(-1-j)
=
j+j^2
$$

Como:

$$
j^2=-1
$$

obtenemos:

$$
j-1=-1+j
$$

Por lo tanto:

$$
\boxed{X[1]=-1+j}
$$

---

# 10. Recuperación de $X[2]$

Tenemos:

$$
X[2]=
r[0]-r[1]+r[2]-r[3]
$$

Reemplazamos:

$$
X[2]=
0-(-1-j)+0-0
$$

Por lo tanto:

$$
\boxed{X[2]=1+j}
$$

---

# 11. Recuperación de $X[3]$

Tenemos:

$$
X[3]=
r[0]+jr[1]-r[2]-jr[3]
$$

Reemplazamos:

$$
X[3]=
j(-1-j)
$$

Desarrollamos:

$$
j(-1-j)
=
-j-j^2
$$

Como:

$$
j^2=-1
$$

queda:

$$
-j+1
$$

Por lo tanto:

$$
\boxed{X[3]=1-j}
$$

---

# 12. Resultado del símbolo OFDM #1

El receptor obtuvo:

$$
\boxed{
X^{(1)}=
[
-1-j,\;
-1+j,\;
1+j,\;
1-j
]
}
$$

Que coincide exactamente con lo enviado:

$$
X^{(1)}_{\mathrm{TX}}=
[
-1-j,\;
-1+j,\;
1+j,\;
1-j
]
$$

---

# 13. Recuperación de los 8 símbolos QPSK

Ahora concatenamos los dos vectores recuperados:

$$
[
1-j,\;
1+j,\;
-1+j,\;
-1-j,\;
-1-j,\;
-1+j,\;
1+j,\;
1-j
]
$$

Estos son exactamente los 8 símbolos QPSK enviados.

---

# 14. Demapeo QPSK

Utilizamos nuevamente la tabla de la constelación:

| Símbolo QPSK | Bits |
|:---:|:---:|
| $1+j$ | $00$ |
| $-1+j$ | $01$ |
| $-1-j$ | $11$ |
| $1-j$ | $10$ |

Entonces:

$$
1-j \rightarrow 10
$$

$$
1+j \rightarrow 00
$$

$$
-1+j \rightarrow 01
$$

$$
-1-j \rightarrow 11
$$

$$
-1-j \rightarrow 11
$$

$$
-1+j \rightarrow 01
$$

$$
1+j \rightarrow 00
$$

$$
1-j \rightarrow 10
$$

Por lo tanto recuperamos:

$$
\boxed{
10\quad 00\quad 01\quad 11\quad
11\quad 01\quad 00\quad 10
}
$$

que son exactamente los bits originales.

---

# 15. Cadena completa del receptor

El proceso completo fue:

$$
\boxed{
\text{Señal recibida}
\rightarrow
\text{ADC}
\rightarrow
r[n]
\rightarrow
\text{Paralelo}
\rightarrow
\text{FFT}
\rightarrow
X[k]
\rightarrow
\text{Demapeo QPSK}
\rightarrow
\text{bits}
}
$$

En este ejemplo, como no agregamos ruido ni distorsión:

$$
\boxed{
\text{bits recibidos}
=
\text{bits transmitidos}
}
$$

Por lo tanto:

$$
\boxed{\mathrm{BER}=0}
$$