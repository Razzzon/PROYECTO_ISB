# LABORATORIO 6: Uso de OpenBCI en la adquisición de EEG

## **Tabla de contenidos:**
<div style="border: 2px solid gray; padding: 20px;border-radius: 15px; width: 40%; height: 180px;">

1. [**Introducción**](#1-introducción)  
2. [**Objetivos**](#2-objetivos)
3. [**Materiales y equipos**](#3-materiales-y-equipos)
4. [**Procedimiento**](#4-procedimiento)
5. [**Resultados**](#5-resultados)  
6. [**Conclusiones**](#6-conclusiones)
7. [**Referencias**](#7-referencias)

</div>
<br>

## **1) Introducción** 

### Electroencefalograma
<p align="justify">
Un electroencefalograma (EEG) es una herramienta que permite estudiar la actividad eléctrica a nivel cerebral [A6]. Este método es ampliamente utilizado en entornos médicos ya que posee una gran variedad de aplicaciones: estudiar las funciones cerebrales, diagnosticar trastornos neurológicos y analizar cómo responde el cerebro a tareas de distinta complejidad.
</p>  
  
<div align="center">
   <img src="./Imagenes/eeg.png" alt="EEG" width="400">

**Figura 1: Representación de un EEG**  
</div>
<br>

<p align="justify">
Uno de los aspectos más atractivos de esta técnica es su naturaleza no invasiva, ya que se basa en la colocación de electrodos sobre la cabeza. Estos se encargan de medir el potencial eléctrico desde distintos puntos, lo que a su vez permite cuantificar la actividad de los lóbulos cerebrales. El equipamiento básico de todo este sistema consiste de los electrodos, un amplificador, un monitor y una central de procesamiento (usualmente un computador) [A6].  
</p>  
  

<p align="justify">
Debido a que la cantidad de información está en gran parte dada por la cantidad de electrodos, existe un estándar para la cantidad de estos llamado sistema 10-20, que consta de 21 electrodos situados en la cabeza. Este estándar garantiza una ubicación consistente y reproducible de los electrodos, permitiendo así la comparación de EEGs entre diferentes estudios.
</p>



### OpenBCI
<p align="justify">  
Es una empresa enfocada en crear herramientas de código abierto relacionadas a biosensores y a la neurociencia, como interfaz cerebro-máquina (BCI en inglés). Entre los proyectos realizados por OpenBCI se tiene Galea, el cual es una plataforma que incluye hardware y software. Asimismo, incluye mediciones de EEG (electroencefalograma), EMG (electromiograma), EDA (actividad electrodermal), PPG (fotopletismografía) y seguimiento ocular, además que lo combina con inmersión de realidad aumentada y virtual. [WAOS]  
</p>
  

<div align="center">
   <img src="./Imagenes/galea.png" alt="Derivaciones" width="350">

**Figura 2: Imagen de Galea en la tienda de OpenBCI [MIAU]**  
</div>
<br>

<p align="justify">
Otro de los proyectos realizados por OpenBCI es el Ultracortex, el cual es un dispositivo que está diseñado para funcionar con el sistema OpenBCI y registrar la actividad EEG. En la actualidad, se cuenta con la versión de Ultracortex Mark IV (creado en enero de 2017) y continúa en desarrollo. [CHINCHIN]
</p>  

<div align="center">
   <img src="./Imagenes/ultracortex.jpg" alt="ultracortex" width="350">

**Figura 3: Dispositivo Ultracortex Mark IV (para EEG) [GRAJEAS]**  
</div>
<br>

<p align="justify">
Gracias a que es un dispositivo de código abierto, los usuarios pueden acceder al archivo STL, imprimirlo en 3D y ensamblarlo por su cuenta. Para esto, se cuenta con guías e información sobre la impresión 3D (configuración y parámetros, además de la talla), montaje, colocación de electrodos (basado en sistema 10-20) y cables, configuración de los módulos (conexión entre tablero Ganglion [4 canales], Cyton [8 electrodos] y/o ampliación con el módulo Daisy [16 electrodos] con Mark IV [headset]), vinculación con dispositivos (como laptop) y la visualización de las ondas cerebrales (usando el GUI OpenBCI) [GRAJEAS] [WAZA].
</p>
  
<div align="center">
   <img src="./Imagenes/ejemplo_resultados.jpg" alt="ejemplo usando GUI BCI" width="400">

**Figura 4: Ejemplo de resultados utilizando la GUI BCI [PAROXÍSTICO]**  
</div>
<br>
  
## **2) Objetivos**
* Analizar las bioseñales respecto a diferentes dispositivos(bitalino y Ultracortex Mark IV) 
* Ver los cambios de las bioseñales respecto a las actividades z
* Ver las frecuencias de cada bioseñal, respecto a las actividades realizadas:
    * 30 segundos de reposo  
    * Abrir y cerrar los ojos cada 5 segundos  
    * Problemas aritméticos sencillos   
    * Problemas aritméticos complejos  
<br>
  

## **3) Materiales**
* Materiales
* Bitalino
* Open Signals
* Laptop
* OpenBCI
* Ultracortex Mark IV
* Cyton board
<br>  
  
## **4) Procedimiento:**
  
### BITalino  
<p align="justify">
Para todas las actividaes relacionadas con el usó el Bitalino como  sensor y el Open Signals como el dispositivo que recolecta la información. Para esto primero se realizó la correcta conexión del Bitalino  con los cables de los electrodos y también la conexión con el software Open Signals. A la par también se colocaron los electrodos en la persona que se realizó la prueba. Para la colocación de los electrodos nos basamos respecto a esta imagen:
</p>
  
<div align="center">
   <img src="./Imagenes/colocacion_electrodos.png" alt="Colocacion de los electrodos" width="400">

**Figura 5: Colocación de los electrodos [R1]**  
</div>
<br>  
Posteriormente se realizaron 4 distintas actividades, con el fin de obtener EEG y analizar cómo varían.  
<br>

### Ultracortex Mark IV:
  
<p align="justify">
Este es un dispositivo de interfaz cerebro-computadora utilizado para la captura de las señales electroencefalográficas (EEG). Por lo tanto, el Ultracortex Mark IV permite registrar la actividad eléctrica cerebral no invasiva y convertirla en información útil. Para la captura de las señales EEG, se realizó la colocación de los electrodos mediante el sistema 10-20 internacional. Este sistema se basa en distancias porcentuales entre puntos anatómicos importantes como nasion, inion y orejas. Entonces los puntos de referencia utilizados para la colocación de los 8 electrodos son los siguientes:

* **FP**: áreas frontopolares
* **C**: áreas centrales
* **P**: +areas parietales
* **O**: áreas occipitales
</p>  
  
<div align="center">
   <img src="./Imagenes/ultracortex_electrodos.png" alt="Ultracortex Mark IV y colocación de electrodos" width="400">

**Figura 6: Imagen del Ultracortex Mark IV y tabla de colocación de electrodo-cable para el cyton board (8 canales)**  
</div>
<br>  
  
<p align="justify">
Durante la adquisición de la señal, se observa una interfaz donde se muestra la actividad eléctrica de los 8 canales, la Transformada Rápida de Fourier (FFT) y la potencia de las bandas de las bandas de frecuencia de las ondas cerebrales.
</p>
  
<div align="center">
   <img src="./Imagenes/interfaz.png" alt="Interfaz del BCI" width="400">

**Figura 7: Interfaz gráfica de usuario**  
</div>
<br>  

### Actividades:
* **30s1**
* **cerrar-abrir con 30s2**
* **Operaciones matemáticas de nivel fácil y difícil**

<p align="justify">
Si bien se tienen dos escenarios de operaciones aritméticas de distinta complejidad, la metodología de ambos es igual. Se buscaron 3 preguntas de la página Springerlink y se las preguntó al sujeto de prueba para cada caso, donde primero se le planteó al sujeto de pruebas las preguntas de nivel fácil y luego de nivel difícil. Se le repitió 3 veces cada pregunta y se esperó hasta que respondiera. Este procedimiento se siguió tanto para el caso de la toma de información vía BITalino como con el Ultracortex Mark IV. 
</p>
  
<div align="center">
   <img src="./Imagenes/facil.png" alt="Preguntas fáciles" width="400">

**Figura F1: Preguntas aritméticas fáciles[R2]**  
</div>
<br>
  
<div align="center">
   <img src="./Imagenes/compleja.png" alt="Preguntas complejas" width="400">

**Figura F2: Preguntas aritméticas complejas[R2]**  
</div>
<br>
  
<p align="justify">
Respecto al BITalino, una vez obtenidas las señales, se le realizó el procesamiento y posterior lectura de la información mediante el uso de Python. Se le aplicó un filtro pasa banda que contenía el rango de frecuencias de las ondas de interés (desde el 0.5 Hz que es el límite inferior para las ondas delta, hasta 50 Hz que es el límite superior para las ondas gamma)[MUEJEJE]. En el caso del Ultracortex Mark IV, la visualización de los datos se realizó desde el mismo programa.
</p>

## **5) Resultados:**  

### Bitalino:
* **30 segundos de respiración**
<div align="center">
   <img src="./Imagenes/30s1.png" alt="PSD de relajo" width="400">

**Figura XXX: noseojeofowf**  
</div>
<br>

* **Abrir y cerrar ojos**
<div align="center">
   <img src="./Imagenes/cerrar_abrir.png" alt="PSD en abrir y cerrar ojos" width="400">

**Figura XXX: noseojeofowf**  
</div>
<br>
<br>

* **Operaciones matemáticas fáciles**  
<p align="justify">
Para el análisis vía BITalino, se obtuvieron los siguientes resultados al momento de aplicar las operaciones matemáticas de un nivel de complejidad sencillo. Estos gráficos de barras fueron obtenidos luego de filtrar la señal vía Python, para posteriormente obtener su PSD y clasificar en base a frecuencias de interés.
</p>
  
<div align="center">
   <img src="./Imagenes/f5.png" alt="Señales ante operaciones matemáticas fáciles" width="400">

**Figura F5: Señal EEG filtrada en el tiempo y su transformada**  
</div>
<br>

<div align="center">
   <img src="./Imagenes/f3.png" alt="PSD por ondas ante operaciones matemáticas fáciles" width="400">

**Figura F3: Resultados para la señal producto de operaciones sencillas**  
</div>
<br>

<p align="justify">
No obstante, para un mejor análisis de frecuencias, se optó por un procesamiento adicional. Se cargaron los datos de la señal en estado de reposo a manera de vector. Este vector fue restado del vector con los datos del EEG correspondientes a las operaciones fáciles. El propósito de realizar esto fue para poder limpiar el vector con los datos de EEG de interés de la información perteneciente al estado basal, resaltando aún más las características propias de la señal resultante de las operaciones fáciles. El vector producto de esta resta fue luego procesado de igual manera que se hizo anteriormente:  se filtró la vía Python y para posteriormente obtener su PSD y clasificar en base a frecuencias de interés. 
</p>
  
<div align="center">
   <img src="./Imagenes/f4.png" alt="PSD resultado" width="400">

**Figura F4: Datos procesados para limpiar los datos de reposo**  
</div>
<br>  
  
<p align="justify">
En este nuevo gráfico de barras, destaca de mejor manera la mayor potencia de las ondas beta e incluso se percibe un aumento de la potencia de gamma. En particular, esto es de esperarse en el contexto de la prueba aplicada. Si bien se plantean preguntas de índole aritmética de un nivel sencillo, de todas formas esto implica cierto nivel de pensamiento, ya que la capacidad de raciocinio implica siempre un nivel de complejidad cerebral y de actividad neuronal relacionada a resolución de problemas. En particular, las ondas beta reflejan este estado, ya que estas suelen manifestarse al completar una tarea y durante la concentración activa, y su activación se ha asociado a una elevada capacidad de cálculo aritmético [A1]. De igual manera, se ha encontrado incluso que las ondas beta se manifiestan sólo por el simple hecho de que la persona se encuentre en un estado de concentración [A2], lo cual también va de la mano con el escenario de la prueba: estar atento a la pregunta y realizar una operación matemática básica.
</p>  
  
<p align="justify">
Destaca de igual manera una prevalencia de las ondas gamma. Estas se asocian a un nivel más elevado de concentración y conciencia [A1]. También está relacionada con un estado de atención sostenida y otros tipos de procesos cognitivos avanzados como la memoria, percepción visual, entre otros [A3]. En base a esto, tendría sentido que estas ondas estén presentes. Al realizar una tarea aritmética, por más simple que sea, el cerebro necesita coordinar diferentes áreas para procesar los números, entender la pregunta, recuperar el conocimiento matemático previo y responder.  
</p>  
<br>
  
* **Operaciones matemáticas fáciles**  
<p align="justify">
Se obtuvo la señal filtrada con su transformada de fourier, para realizar el análisis de las ondas. Se tomó en cuenta una señal previa que es la de reposar por 30 segundos por segunda vez, esta se usó como referencia para obtener la señal que solo se considera cuando se está realizando la operación matemática. 
</p>  
  
<div align="center">
   <img src="./Imagenes/dificil1.png" alt="Señales en difícil" width="400">

**NO HAY NADADADADADADA** 
</div>
<br>  
  
<p align="justify">
Para esto se realizó una resta entre la señal de actividad compleja y la señal cuando está respirando por 30 segundos. Una vez obtenido la señal y su FFT es difícil de analizar la señal en el tiempo y la señal en frecuencia (FFT), para esto se realizó la PSD (power spectral density) de la señal con el fin de obtener un diagrama de barras, de tal forma que sea más fácil analizar, debido a que en el diagrama de barras se puede realizar mediante rangos, es decir, por ondas cerebrales:
</p>  
  
<div align="center">
   <img src="./Imagenes/dificil2.png" alt="PSD por ondas en difícil" width="400">

**NO HAY NADADADADADADA** 
</div>
<br> 
  
<p align="justify">
Respecto a la imagen obtenida hay que tener en cuenta, que se puede ver una alta actividad en las ondas delta (0.5 hz - 4 Hz), esta onda delta representa la fase de sueño profundo lo cual no concuerda con la actividad que está realizando el sujeto, que es realizar actividades matemáticas complejas. Viendo la señal en función del tiempo se detectaron anomalías (señales en función del tiempo que parecen ondas cuadradas), recordando que las ondas cuadras (función rect(t)), en función del tiempo, se representa como función sinc(f), cuando se representa en frecuencias; teniendo en cuenta que la función Sinc(f) presenta una gran cantidad de frecuencias bajas, esto se vería reflejado como si fuera onda delta.
</p>  
  
<div align="center">
   <img src="./Imagenes/anomalias.png" alt="Anomalías durante lectura" width="500">

**fig x.  Señal con anemias similar a ondas cuadradas** 
</div>
<br> 
  
<p align="justify">
Para corregir esto se realizó otro filtrado a partir de 5 hz - 50 hz , con el fin de disminuir el sesgo de la señal causa por las anomalías obteniendo el siguiente gráfico de barras.
</p>
  
Se consideró el siguiente rango de frecuencias:
* **Delta**: 0.5 - 4 Hz *(amarillo)*  
* **Theta**: 4 - 8 Hz *(verde)*  
* **Alfa**: 8 - 13 Hz *(azul)*  
* **Beta**: 13 - 32 Hz *(anaranjado)*  
* **Gamma**: 32 - 50 Hz *(morado)*
  
  
<div align="center">
   <img src="./Imagenes/dificil3.png" alt="PSD en dificil por ondas" width="500">

**fig x.  Señal con anomalías similar a ondas cuadradas** 
</div>
<br>  
  
<p align="justify">
El gráfico de barras muestra la potencia de la señal en las distintas bandas de frecuencia durante la realización de operaciones aritméticas complejas. Se observa que la mayor potencia está en la banda beta (13 Hz - 32 Hz) lo cual es consistente con la literatura científica, el cual asocia las ondas Beta con actividades cognitivas intensas, así como el procesamiento de cálculos matemáticos. Esto confirma que, en esta instancia, la señal EEG del individuo refleja una alta actividad cognitiva en la banda Beta, que predomina sobre las otras bandas.
</p>  
  
<p align="justify">
También se realizó una comparación entre señales sin referencia y con referencia y se vio que si presenta una variación.
</p>  
  
<div align="center">
   <img src="./Imagenes/dificil4.png" alt="PSD en dificil - comparación" width="550">

**fig x. Gráficos de barras de la PSD** 
</div>
<br>  
  
<p align="justify">
A partir de las imágenes se observa que la principal diferencia es que en la onda theta (verde) hay una mayor intensidad sin tener como referencia a la señal basal. Pero si tomamos como referencia la señal basal se ve que las onda alpha (morada) presenta mayor intensidad.
</p>  
  
### Ultracortex Mark IV:
* **Cerrar los ojos**  

<div align="center">
   <img src="./Imagenes/ultracortex_aritmetica_facil.png" alt="Vista del GUI BCI en fácil" width="550">

**fig x. Open BCI 30 segundos** 
</div>
<br>  
  
<p align="justify">
Como se observa en la figura, durante los 30 segundos de respiración controlada, la actividad en la banda Alpha mostró una mayor potencia relativa en comparación con otras bandas de frecuencia. Este fenómeno es característico del estado de relajación que experimenta el sujeto cuando no se enfrenta a estímulos externos significativos y se encuentra en un estado de descanso con los ojos cerrados o en reposo mental.
</p>  
  
<div align="center">
   <img src="./Imagenes/tablas_psd.png" alt="Tablas de PSD en cerrar ojos" width="550">

**fig x. Gráficos de barras de la PSD** 
</div>
<br>  
  
* **Cerrar y abrir ojos**  
  
<p align="justify">
Durante la prueba, el sujeto alterna entre abrir y cerrar los ojos en intervalos regulares de 5 segundos. Este tipo de actividad constante provoca que las ondas Alpha (relajación con ojos cerrados) y Beta (alerta con ojos abiertos) se activen de manera intermitente y casi simultánea. El cerebro no tiene suficiente tiempo para reducir completamente una banda antes de que la otra vuelva a activarse.
</p>  

<div align="center">
   <img src="./Imagenes/abrir_cerrar_bci.png" alt="Abrir y cerrar ojos usando BCI" width="500">

**fig x. Open BCI abrir y cerrar ojos** 
</div>
<br>  

<div align="center">
   <img src="./Imagenes/psd_abrir_cerrar_bci.png" alt="Tabla psd en abrir y cerrar ojo" width="550">

**fig x. Gráficos de barras por canal de abrir y cerrar ojos** 
</div>
<br> 

<p align="justify">
EWONWEIOFNWEFW
EFNWIOFNWIOEFOWF
WEFNIWFNOWEIFW
WEFIWFNOWEIFN
WEFIWONF
WNFEIOWNFE
</p>
  
  
* **Operaciones matemáticas fácil**  
  
<div align="center">
   <img src="./Imagenes/matematica_facil_bci.png" alt="BCI: actividad de cálculo sencillo" width="550">

**Figura F5: Datos visualizados en OpenBCI** 
</div>
<br> 
  
<p align="justify">
En cuanto a los resultados para operaciones matemáticas fáciles usando el Ultracortex, se obtienen resultados similares a los vistos para el BITalino en el mismo caso de pruebas. Se percibe una activación tanto de beta como gamma, lo que implica que se están llevando a cabo procesos cognitivos más complejos, lo que a su vez va de la mano del contexto de la prueba. No obstante, gracias al Ultracortex también podemos ver las zonas de activación gracias al apartado Head Plot. En este caso, vemos que existe mayor activación alrededor de la zona parietal, frontal e incluso occipital.
</p>
  
<p align="justify">
Si bien el participante realizó la prueba con ojos cerrados, lo que implicaría una poca activación occipital, es posible que para resolver las preguntas haya optado por imágenes mentales para representar operaciones. Se ha encontrado evidencia de que la imaginería visual de una persona puede llegar a activar la región occipital [A4], lo cual puede explicar la activación percibida.
</p>  
  
<p align="justify">
Por otro lado, la activación parietal puede deberse al procesamiento del estímulo auditivo de la pregunta, ya que estudios acerca de lesiones en el área parietal derecha mostraron que esta zona es crítica para el reconocimiento de la voz [A5]. Finalmente, la activación frontal era esperada, ya que esta zona está involucrada en el procesamiento y resolución de problemas. Además, la poca activación de esta zona va de la mano con la complejidad de la tarea, ya que si bien es necesaria por la naturaleza racional, tampoco es muy demandante.
</p>  
<br>  

* **Operaciones matemáticas difícil**
  
<p align="justify">
A partir de los resultados obtenidos, se observa que la amplitud en el canal 2 tiene un valor constante de 0, lo que sugiere una posible mala colocación del electrodo o que este se desprendió, impidiendo la recepción de señal en ese canal.  
</p>  
  
<div align="center">
   <img src="./Imagenes/dificil_bci_interfaz.png" alt="BCI: cálculo complejo" width="550">

**fig x. Open BCI canal 2** 
</div>
<br>  
  
<p align="justify">
En cuanto al análisis de las bandas de frecuencia de las ondas cerebrales, se observa que las ondas beta y gamma son las más prominentes, mientras que la onda delta muestra la menor actividad. Este patrón es coherente con la actividad realizada, ya que las ondas beta están asociadas con procesos mentales activos y concentración, mientras que las ondas gamma suelen aparecer en actividades cognitivas de alto nivel.  
</p>  
  
<p align="justify">
Además, el gráfico de barras revela que las intensidades de las ondas theta y alpha también son elevadas, especialmente durante la resolución de problemas simples. Esto indica una mayor activación cerebral durante la tarea matemática, ya que dichas ondas están asociadas con la coordinación de procesos de atención y la relajación mental necesaria para resolver problemas.
</p>  
  
<div align="center">
   <img src="./Imagenes/BCI_complejo_2.png" alt="BCI: cálculo complejo 2" width="550">

**fig x. Open BCI** 
</div>
<br>  
  
<p align="justify">
Por último, se analizó el canal 1, observando que este muestra la mayor activación en el lóbulo frontal, lo cual es consistente con el tipo de actividad cognitiva llevada a cabo, dado que el lóbulo frontal es clave en el procesamiento de tareas complejas y toma de decisiones.
</p>  
  
<div align="center">
   <img src="./Imagenes/tabla_psd_complejo.png" alt="tablas de psd en cálculo complejo" width="550">

**fig x. Gráficos de barras por canal en resolución de problemas complejos** 
</div>
<br>   
  

## **6) Conclusiones:**  
<p align="justify"> 

* FALTAAAAAA
</p>  
<p align="justify"> 

* FALTAAAAA
</p>  
<p align="justify">  

* Se observó que durante la resolución de problemas matemáticos, la intensidad de las ondas cerebrales varía en función de si se usa el estado basal como referencia. Con referencia, la onda beta (azul) muestra mayor intensidad, mientras que sin referencia, aumenta la intensidad de la onda theta.
</p>  
  
<p align="justify"> 

* Se concluye que a partir de la actividad realizada, se obtiene una diferente potencia de las bandas de frecuencia de las ondas cerebrales.
</p>  
<p align="justify"> 

* Se concluye que para la actividad donde se realizó preguntas complejas, se obtienen ondas beta y gamma más prominentes debido a que estas están asociadas a la actividad mental, concentración y procesos cognitivos complejos.  
</p>  

## **7) Referencias:**

[A6] A. Rayi y N. I. Murr, “Electroencephalogram”, en StatPearls, Treasure Island (FL): StatPearls Publishing, 2024. Disponible en: http://www.ncbi.nlm.nih.gov/books/NBK563295/.