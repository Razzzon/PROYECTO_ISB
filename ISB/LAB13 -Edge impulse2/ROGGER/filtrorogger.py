from scipy.signal import butter, filtfilt, iirnotch
import numpy as np

def filtro_paso_banda(signal, fs=1000, lowcut=0.5, highcut=100, order=6):
    """
    Aplica un filtro paso banda a una señal.
    :param signal: Señal de entrada (array)
    :param fs: Frecuencia de muestreo (Hz)
    :param lowcut: Frecuencia mínima del filtro paso banda (Hz)
    :param highcut: Frecuencia máxima del filtro paso banda (Hz)
    :param order: Orden del filtro
    :return: Señal filtrada
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

def filtro_rechaza_banda(signal, fs=1000, freq=60, Q=30):
    """
    Aplica un filtro rechaza banda para eliminar ruido en una frecuencia específica.
    :param signal: Señal de entrada (array)
    :param fs: Frecuencia de muestreo (Hz)
    :param freq: Frecuencia a rechazar (Hz)
    :param Q: Factor de calidad del filtro
    :return: Señal filtrada
    """
    nyquist = 0.5 * fs
    w0 = freq / nyquist  # Frecuencia normalizada
    b, a = iirnotch(w0, Q)
    return filtfilt(b, a, signal)

# Código principal para pruebas
if __name__ == "__main__":
    # Simula una señal de entrada con ruido
    fs = 1000  # Frecuencia de muestreo (Hz)
    t = np.linspace(0, 2, 2 * fs, endpoint=False)  # 2 segundos de duración
    señal = (
        np.sin(2 * np.pi * 10 * t) +  # Frecuencia de 10 Hz (dentro del rango paso banda)
        np.sin(2 * np.pi * 60 * t) +  # Ruido de 60 Hz (debe ser eliminado)
        0.5 * np.random.normal(size=t.shape)  # Ruido aleatorio
    )

    # Aplicar el filtro paso banda
    señal_pasabanda = filtro_paso_banda(señal, fs, lowcut=0.5, highcut=100, order=6)

    # Aplicar el filtro rechaza banda en 60 Hz
    señal_final = filtro_rechaza_banda(señal_pasabanda, fs, freq=60, Q=30)

    # Resultados
    print("Procesamiento completado. Señal lista para usar.")

    # Graficar las señales
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, señal, label="Señal original")
    plt.title("Señal original con ruido")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, señal_pasabanda, label="Señal después del paso banda (0.5-100 Hz)", color="blue")
    plt.title("Señal después del filtro paso banda")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, señal_final, label="Señal después del rechaza banda (60 Hz)", color="green")
    plt.title("Señal final (paso banda + rechaza banda)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()

    plt.tight_layout()
    plt.show()

