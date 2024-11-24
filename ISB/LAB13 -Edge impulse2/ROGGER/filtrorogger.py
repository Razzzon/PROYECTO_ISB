from scipy.signal import butter, filtfilt
import numpy as np
import matplotlib.pyplot as plt

def filtro_paso_banda(signal, fs=1000, lowcut=0.5, highcut=100, order=6):
    """
    Aplica un filtro paso banda a una señal.
    :param signal: Lista o array con la señal a procesar
    :param fs: Frecuencia de muestreo (Hz)
    :param lowcut: Frecuencia mínima del filtro (Hz)
    :param highcut: Frecuencia máxima del filtro (Hz)
    :param order: Orden del filtro
    :return: Señal filtrada
    """
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')  # Coeficientes del filtro
    return filtfilt(b, a, signal)  # Filtra la señal en ambos sentidos


# # Ejemplo de uso
# if __name__ == "__main__":
#     # Configuración de la señal de prueba
#     fs = 500  # Frecuencia de muestreo (Hz)
#     t = np.linspace(0, 2, 2 * fs, endpoint=False)  # 2 segundos de duración

#     # Señal de prueba: mezcla de frecuencias
#     señal_original = (
#         np.sin(2 * np.pi * 1 * t) +    # Frecuencia de 1 Hz (debe pasar)
#         np.sin(2 * np.pi * 50 * t) +  # Frecuencia de 50 Hz (debe pasar)
#         np.sin(2 * np.pi * 150 * t)   # Frecuencia de 150 Hz (debe ser filtrada)
#     )

#     # Añadimos ruido aleatorio
#     señal_ruidosa = señal_original + 0.5 * np.random.normal(size=t.shape)

#     # Aplicar el filtro paso banda
#     señal_filtrada = filtro_paso_banda(señal_ruidosa, fs, lowcut=0.5, highcut=100, order=6)

#     # Gráficos para comparar señales
#     plt.figure(figsize=(12, 6))
#     plt.subplot(3, 1, 1)
#     plt.plot(t, señal_ruidosa, label="Señal con ruido", color="gray")
#     plt.title("Señal original con ruido")
#     plt.xlabel("Tiempo (s)")
#     plt.ylabel("Amplitud")
#     plt.legend()

#     plt.subplot(3, 1, 2)
#     plt.plot(t, señal_filtrada, label="Señal filtrada (0.5 - 100 Hz)", color="blue")
#     plt.title("Señal filtrada")
#     plt.xlabel("Tiempo (s)")
#     plt.ylabel("Amplitud")
#     plt.legend()

#     plt.subplot(3, 1, 3)
#     plt.plot(t, señal_original, label="Señal original (sin ruido)", color="green")
#     plt.title("Señal original (frecuencias esperadas)")
#     plt.xlabel("Tiempo (s)")
#     plt.ylabel("Amplitud")
#     plt.legend()

#     plt.tight_layout()
#     plt.show()
