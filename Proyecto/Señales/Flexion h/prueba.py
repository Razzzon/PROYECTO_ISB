import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from IPython.display import HTML
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
def funcion_emg(nombre):
    # Abrir el archivo de texto
    with open(nombre, "r") as f:
        # Saltar las tres primeras líneas
        next(f)
        next(f)
        next(f)
        
        # Leer todas las líneas restantes
        all_data = f.readlines()   
    
    # Procesar cada línea, dividiendo por tabulaciones
    all_data = [line.strip().split('\t') for line in all_data]
    
    # Extraer la primera columna (muestra)
    sample = [int(row[0]) for row in all_data]  # Primera columna

    # Crear una secuencia de números para la muestra (opcional, según tu lógica)
    sample = np.arange(0, len(sample))  # Reemplaza los valores por una secuencia 0, 1, 2, ..., n
    
    # Extraer la sexta columna (amplitud)
    amplitude = [int(row[5]) for row in all_data]  # Sexta columna (índice 5)
    amplitude = np.array(amplitude)
    return sample, amplitude  # Devolver los valores de la muestra y amplitud
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def fourier(s_filtrada):
    T=1/1000
    frequencies = np.fft.fftfreq(len(s_filtrada[:]), T)
    signal_fft = np.fft.fft(s_filtrada[:])
    # Solo tomamos la parte positiva de la transformada
    positive_frequencies = frequencies[:len(frequencies)//2]
    positive_signal_fft = np.abs(signal_fft[:len(signal_fft)//2])
    return positive_frequencies,positive_signal_fft



def grafica(sample,amplitude,filtrada):
    plt.figure(figsize=(12, 6))
    referencia1=np.max(amplitude)
    # Gráfico de la señal original
    plt.subplot(1, 2, 1)
    plt.plot(sample/1000, amplitude)
    plt.title('Señal EMG Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
 
    # Gráfico de la señal filtrada
    plt.subplot(1, 2, 2)
    plt.plot(sample / 1000, filtrada)
    plt.title('Señal EMG Filtrada')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud Filtrada')

    # Mostrar ambos gráficos
    plt.tight_layout()
    plt.show()
    frecuencia,signalFFT=fourier(filtrada)
    referencia = signalFFT/signalFFT.max()

    plt.figure(figsize=(12, 6))

    # Gráfico de la Transformada de Fourier
    plt.subplot(1,2,1)
    plt.plot(frecuencia, signalFFT)
    plt.title('Transformada de Fourier')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Amplitud')
    plt.subplot(1,2,2)
    plt.plot(frecuencia, 10*np.log10(referencia))
    plt.title('Transformada de Fourier')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Amplitud db')

    plt.tight_layout()
   
    plt.show()
# Aumentar el límite del tamaño de la animación
# Aumentar el límite del tamaño de la animación
mpl.rcParams['animation.embed_limit'] = 100  # Aumentar el límite a 50 MB


# Suponiendo que tienes los datos de la señal
sample, amplitude = funcion_emg("medicion 3.txt")
sample = sample[20000:30000]
amplitude = amplitude[20000:30000]

# Crear la figura y el eje para la animación
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Configurar límites de los ejes
ax.set_xlim(np.min(sample), np.max(sample))
ax.set_ylim(np.min(amplitude), np.max(amplitude))

# Función para inicializar la gráfica vacía

def init():
    line.set_data([], [])
    return line,

# Función para actualizar la gráfica en tiempo real

def update(frame):
    step_size =5000  # Ajustar el tamaño del paso (actualizar 5 datos por frame)
    line.set_data(sample[:frame*step_size], amplitude[:frame*step_size])

    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(sample), init_func=init, blit=True)

# Mostrar la animación en Jupyter
HTML(ani.to_jshtml())



# Mostrar la gráfica de señal original y filtrada


plt.show()