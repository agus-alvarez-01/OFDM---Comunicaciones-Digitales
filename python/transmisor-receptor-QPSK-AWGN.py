# Librerías
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (8,5)
plt.rcParams["font.size"] = 12

np.random.seed(10)   # Para que siempre genere los mismos bits

#-------------------------------------------------------------------#

# Configuración de parámetros de la simulación

N = 64          # Número de subportadoras OFDM
CP = 16         # Longitud del prefijo cíclico
N_OFDM = 500    # Cantidad de símbolos OFDM

k = 2           # QPSK: 2 bits por símbolo

SNR_dB = 1     # Relación señal a ruido en dB

# Cantidad total de bits
N_BITS = N * N_OFDM * k

#-------------------------------------------------------------------#

# Generación de bits

bits_tx = np.random.randint(0, 2, N_BITS)

print("Bits generados:", len(bits_tx))
print("Primeros 10 bits generados:", bits_tx[:10])

#-------------------------------------------------------------------#

# Modulador QPSK

def qpsk_modulator(bits):
    """
    Convierte una secuencia de bits en símbolos QPSK complejos.

    Cada símbolo QPSK representa 2 bits.

    Mapeo:

        00 ->  1 + 1j
        01 -> -1 + 1j
        11 -> -1 - 1j
        10 ->  1 - 1j

    Los símbolos se normalizan para tener potencia promedio unitaria.
    """

    bits = bits.reshape((-1, 2))

    constellation = {
        (0, 0):  1 + 1j,
        (0, 1): -1 + 1j,
        (1, 1): -1 - 1j,
        (1, 0):  1 - 1j
    }

    symbols = []

    for b in bits:
        symbol = constellation[tuple(b)]
        symbols.append(symbol)

    symbols = np.array(symbols)

    # Normalización
    return symbols / np.sqrt(2)

#-------------------------------------------------------------------#

# Demodulador QPSK

def qpsk_demodulator(symbols):
    """
    Convierte símbolos QPSK complejos nuevamente en bits.

    La decisión se realiza según el cuadrante
    en el que se encuentra cada símbolo.
    """

    # Deshacer la normalización
    symbols = symbols * np.sqrt(2)

    bits = []

    for s in symbols:

        I = s.real
        Q = s.imag

        if I >= 0 and Q >= 0:
            bits.extend([0, 0])

        elif I < 0 and Q >= 0:
            bits.extend([0, 1])

        elif I < 0 and Q < 0:
            bits.extend([1, 1])

        else:
            bits.extend([1, 0])

    return np.array(bits)

#-------------------------------------------------------------------#

# FUNCIONES OFDM

def serial_to_parallel(symbols, N):
    """
    Convierte un vector de símbolos en una matriz.

    Cada fila representa un símbolo OFDM.
    Cada columna representa una subportadora.

            Serie

    x1 x2 x3 ... x64 x65 ...

            ↓

    | x1  x2 ... x64 |
    | x65 .........  |
    | ...            |

    """

    return symbols.reshape((-1, N))


def parallel_to_serial(matrix):
    """
    Convierte una matriz nuevamente en un vector.
    """

    return matrix.reshape(-1)


def add_cp(ofdm_symbol, CP):
    """
    Agrega el prefijo cíclico.

    OFDM:
    |---------------------------|
          64 muestras

    CP:
    |----|----------------------|
      16       64
    """

    cp = ofdm_symbol[-CP:]

    return np.concatenate((cp, ofdm_symbol))


def remove_cp(ofdm_symbol, CP):
    """
    Elimina el prefijo cíclico.
    """

    return ofdm_symbol[CP:]

#-------------------------------------------------------------------#

# TRANSMISOR OFDM

def ofdm_transmitter(symbols, N, CP):
    """
    Transmisor OFDM.

    Etapas:
        Serie → Paralelo
        IFFT
        Agregar CP
        Paralelo → Serie
    """

    # Serie -> Paralelo
    symbols_matrix = serial_to_parallel(symbols, N)

    tx_signal = []

    # Procesar cada símbolo OFDM
    for block in symbols_matrix:

        # Transformación al dominio del tiempo
        time_signal = np.fft.ifft(block)

        # Agregar prefijo cíclico
        time_signal = add_cp(time_signal, CP)

        tx_signal.extend(time_signal)

    return np.array(tx_signal)

#-------------------------------------------------------------------#

# MODULACIÓN QPSK

symbols_tx = qpsk_modulator(bits_tx)

print("Cantidad de símbolos QPSK:", len(symbols_tx))

#-------------------------------------------------------------------#

# OFDM

tx_signal = ofdm_transmitter(symbols_tx, N, CP)

print("Longitud de la señal transmitida:", len(tx_signal))

#-------------------------------------------------------------------#

# Visualización de la señal transmitida

plt.figure(figsize=(12,4))

plt.plot(
    np.real(tx_signal[:400]),
    label="Parte Real (I)"
)

plt.plot(
    np.imag(tx_signal[:400]),
    label="Parte Imaginaria (Q)"
)

plt.title("Señal OFDM en Banda Base")

plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.grid(True)
plt.legend()

plt.show()

#-------------------------------------------------------------------#

# Constelación transmitida

plt.figure(figsize=(6,6))

plt.scatter(
    symbols_tx.real,
    symbols_tx.imag,
    s=8
)

plt.grid(True)

plt.xlabel("In-Phase (I)")
plt.ylabel("Quadrature (Q)")

plt.title("Constelación QPSK Transmitida")

plt.axis("equal")

plt.show()

#-------------------------------------------------------------------#

# CANAL AWGN

def awgn_channel(tx_signal, SNR_dB):
    """
    Canal AWGN (Additive White Gaussian Noise).

    Agrega ruido blanco gaussiano a la señal transmitida.

    SNR_dB:
        Relación señal a ruido expresada en decibeles.
    """

    # Potencia promedio de la señal
    signal_power = np.mean(np.abs(tx_signal)**2)

    # Conversión de SNR de dB a escala lineal
    SNR_linear = 10**(SNR_dB / 10)

    # Potencia del ruido
    noise_power = signal_power / SNR_linear

    # Ruido gaussiano complejo
    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(len(tx_signal))
        + 1j * np.random.randn(len(tx_signal))
    )

    # Señal recibida
    rx_signal = tx_signal + noise

    return rx_signal

#-------------------------------------------------------------------#

# RECEPCIÓN

# Canal AWGN
rx_signal = awgn_channel(tx_signal, SNR_dB)

#-------------------------------------------------------------------#

# Visualización de la señal recibida

plt.figure(figsize=(12,4))

plt.plot(
    np.real(rx_signal[:400]),
    label="Parte Real (I)"
)

plt.plot(
    np.imag(rx_signal[:400]),
    label="Parte Imaginaria (Q)"
)

plt.title(f"Señal OFDM Recibida - SNR = {SNR_dB} dB")

plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.grid(True)
plt.legend()

plt.show()

#-------------------------------------------------------------------#

# RECEPTOR OFDM

def ofdm_receiver(rx_signal, N, CP):
    """
    Receptor OFDM.

    Etapas:
        Serie -> Paralelo
        Eliminar CP
        FFT
        Paralelo -> Serie
    """

    symbol_length = N + CP

    n_symbols = len(rx_signal) // symbol_length

    received_symbols = []

    for i in range(n_symbols):

        # Extraer un símbolo OFDM
        start = i * symbol_length
        end = start + symbol_length

        block = rx_signal[start:end]

        # Eliminar prefijo cíclico
        block = remove_cp(block, CP)

        # Volver al dominio de la frecuencia
        freq_signal = np.fft.fft(block)

        received_symbols.extend(freq_signal)

    return np.array(received_symbols)

#-------------------------------------------------------------------#

# RECEPTOR OFDM

symbols_rx = ofdm_receiver(rx_signal, N, CP)

print("Cantidad de símbolos recibidos:", len(symbols_rx))

#-------------------------------------------------------------------#

# DEMODULACIÓN QPSK

bits_rx = qpsk_demodulator(symbols_rx)

print("Bits recibidos:", len(bits_rx))

#-------------------------------------------------------------------#

# BIT ERROR RATE

bit_errors = np.sum(bits_tx != bits_rx)

ber = bit_errors / len(bits_tx)

print("=" * 40)
print("RESULTADOS")
print("=" * 40)

print(f"SNR               : {SNR_dB} dB")
print(f"Bits transmitidos : {len(bits_tx)}")
print(f"Bits erróneos     : {bit_errors}")
print(f"BER               : {ber:.6e}")

#-------------------------------------------------------------------#

# Constelación recibida

plt.figure(figsize=(6,6))

plt.scatter(
    symbols_rx.real,
    symbols_rx.imag,
    s=8
)

plt.grid(True)

plt.xlabel("In-Phase (I)")
plt.ylabel("Quadrature (Q)")

plt.title(f"Constelación QPSK Recibida - SNR = {SNR_dB} dB")

plt.axis("equal")

plt.show()

#-------------------------------------------------------------------#
