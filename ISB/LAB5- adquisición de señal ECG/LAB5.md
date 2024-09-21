LABORATORIO 5: Uso de BITalino para ECG

1. **Introducción**  
   Un electrocardiograma (ECG) es una técnica no invasiva que permite registrar la actividad eléctrica del corazón \[A6\], y es una herramienta de uso ampliamente extendido en lo que respecta a monitoreo y diagnóstico cardiaco. Una señal de ECG es captada por electrocardiografos, los cuales entregan/muestran la señal al usuario mediante papel milimetrado para ECG o en algunos casos de forma digital. Mediante esta técnica, es posible el diagnosticar distintos tipos de cardiopatías como lo son los distintos tipos de arritmias, infarto de miocardio, miocardiopatías, entre otras \[A7\]. Estas enfermedades pueden identificarse analizando las distintas ondas que posee un ECG: la onda P, Q, R, S y T, y la manera en la que estas se agrupan. Por ejemplo, un complejo QRS más ancho de lo esperado puede significar un engrosamiento ventricular \[A8\].   
     
   ![][image1]  
   **Figura 1: Imágen referencial de los componentes de una señal de ECG**  
     
   Para poder captar estas señales, se hace uso de las derivaciones de ECG. Estas son, en esencia, distintas “vistas” desde donde se capta la actividad eléctrica cardiaca. Estas perspectivas se logran gracias a la colocación de electrodos, los cuales se disponen de distinta manera dependiendo de la derivación de interés. Lo común en el campo médico es encontrar ECG que usen hasta 12 derivaciones, las cuales son:  
     
* Tres derivadas bipolares (DI, DII, DIII)  
* Tres derivadas unipolares (aVR, aVF, aVL)  
* Seis derivadas precordiales (V1, V2, V3, V4, V5, V6)

![][image2]  
**Figura 2: Representación de las derivaciones cardiacas**  
 

2. **Objetivos**

   

* Sensar las señales de ECG usando el Bitalino  
* Adquirir la señales del ECG usando Open Signals  
* Obtener la derivada 1, derivada 2 y derivada 3 del ECG  
* Obtener cada derivada variando entre estado basal, aguantando la respiración 20 segundos y después de realizar ejercicio  
* Analizar el ECG obtenido, respecto derivada y de acuerdo a la actividad realizada  
    
    
3. **Materiales y equipos**  
* Kit BITalino (placa y 3 cables para electrodos)  
* 3 electrodos  
* Laptop  
* Cronómetro  
* Software *Open Signals*  
    
4. **Procedimiento**

Para todas las actividaes se usó el Bitalino como sensor y el Open Signals como el dispositivo que recolecta la información. Para esto primero se realizó la correcta conexión del Bitalino  con los cables de los electrodos y también la conexión con el software Open Signals. A la par también se colocaron los electrodos en la persona que se realizó la prueba. Para la colocación de los electrodos nos basamos respecto a esta imagen   
![][image3]

**Figura 3:Posición de electrodos\[R1\]** 

| ![][image4]  | ![][image5]  | ![][image6]  |
| :---: | :---: | :---: |
| Conexión cables de los electrodos con el BITalino  | Conexión del BITalino con el Open Signals | Prueba1 |
| ![][image7]  | ![][image8]  | ![][image9]  |
| Conexión del BITanilo y cables de electrodos con los electrodos en la persona | Conexión del BITanilo y cables de electrodos con los electrodos en la persona | Prueba 2 |

**Figura 4:Tabla de imágenes sobre el procedimiento**  
**Elaboración propia**  

- ***Estado basal***

La primera actividad consiste en realizar la medición del electrocardiograma en el estado de reposo( cuando la persona no ha realizado ninguna actividad que requiera algún esfuerzo).  
Para la medición a la persona se la sentó en una silla y se mantuvo en reposo durante 1 min.  
Este procedimiento se realizó tanto para la primera derivada,segunda derivada y tercera derivada.  
Para las deriva se intercambió las posiciones de los cables(positivo,negativo y neutro) del ECG    
1ra derivada \= brazo izquierdo positivo , brazo derecho negativo, cresta iliaca positivo  
2da derivada= brazo izquierdo neutro , brazo derecho negativo, cresta iliaca positivo     
3ra derivada \= brazo izquierdo negativo , brazo derecho neutro, cresta iliaca positivo  

![][image10]

**Figura 5:Persona sentada en estado basal**

- ***Mantener respiración***

La segunda fase consistió en realizar la medición del electrocardiograma durante el reposo después de mantener la respiración durante 20 segundos. …\[DP1\]

- ***Actividad física***

La tercera fase consistió en la medición del electrocardiograma, luego de la realización de 5 minutos de actividad física. En el presente laboratorio, la actividad consistió:

| *Jumping jacks(*2 min y 50 s*)* | *![][image11]* |
| :---- | ----- |
| *Burpees(*2 minutos  *)* | ![][image12] |
| *Push-ups(*10 segundos*)* | ![][image13] |

**Figura 6: Tabla de los ejercicios realizados**  
Todo lo anterior da un total de 5 minutos de actividad física por parte del participante.

5. **Resultados**  
     
- ***Estado basal***

*Para la obtención de las gráficas se realizó un filtrado de 0.5hz hasta 55 hz(señal original) y otro filtrador de 65 hz hasta 100 hz(señal original), para disminuir el ruido electrónico que es de 60 hz y también tomando en cuenta que el rango de la frecuencia de la señal de ECG está entre 0 hz \-100 hz.*  
*Posterior se sumó las dos señales filtradas para obtener los gráficos*

| *Derivada I* | *![][image14]* | *![][image15]* |
| :---- | :---- | :---- |
| ***Derivada II*** | ***![][image16]*** | ***![][image17]*** |
| ***Derivada III*** | ***![][image18]*** | ***![][image19]*** |

**Figura 7: Tabla de ECG(Derivada I,II,III ) y FFT estado basal**

Posterior al registro electrocardiográfico en estado basal ,se obtuvieron 3 trazos correspondientes a las Derivadas I, II y III respectivamente como se muestran en los gráficos anteriores, los cuales muestran una buena calidad de la señal y una interferencia de ruido  baja tras la aplicación de la Trasnformda de Fourier, es así que permite de forma adecuada identificar  las ondas P, QRS y T en cada derivada. 

Es importante resaltar que BItalino ha demostrado evidenciar un ECG al cual el profesional en salud puede dar lectura, en este caso tenemos un sujeto estable en estado basal sin patologías subyacetes , por ende la descripción de este ECG se rige a la literatura \[R2\]como :

| Ritmo cardiaco sinusal porque presenta onda P positiva. | ![][image20] |
| :---- | :---- |
| Ritmo regular porque presenta intervalos R-R idénticos,en cuanto a la Frecuencia cardiaca se evidencia en 1 minuto 78 latidos (normal de 60-100 latidos). | ***![][image21]*** |
| Ondas onda P  100 mseg (normal : menos de 100 mseg ), complejo QRS 65 mseg (normal: entre 60-100 mseg) , intervalo QT  350 mseg (normal de 350 a 450 mseg) | ***![][image22]*** |

**Figura 8: Tabla de ECG(Derivada II ), onda P, lpm y duración de los tramos(onda p,complejo QRS e intervalo QT)**

- ***Mantener respiración***

| *Derivada I* | ![][image23] | ![][image24] |
| :---- | :---- | :---- |
| ***Derivada II*** | ![][image25] | ![][image26] |
| ***Derivada III*** | ![][image27] | ![][image28] |

**Figura 9: Tabla de ECG(Derivada I,II,III ) y FFT estado basal**

- ***Actividad física***


***![][image29]***  
![][image30]  

**Figura 10: Tabla de ECG(Derivada I,II,III ) y FFT ejercicio**  
Se muestran los resultados de la señal de ECG para el participante luego de 5 minutos de ejercicio aeróbico y anaeróbico, con énfasis en los primeros. Visualmente, si bien se conserva de manera general el patrón en las derivadas, destaca un comportamiento errático en la primera derivada en comparación a la señal adquirida para esta misma pero en reposo. Sumado a esto, mediante la transformada de Fourier apreciamos que la señal contiene varios componentes con distintas frecuencias, lo que se puede ver de forma más prominente en la transformada de la tercera derivada. Todos estos cambios en la señal y por consecuente su transformada podrían atribuirse en primera instancia al ruido muscular. El tejido muscular, con énfasis en el estriado, puede llegar a tener altas demandas energéticas a causa de distintos tipos de estrés \[A1\]. Al momento de realizar ejercicio, los músculos se activan en mayor medida debido a el aumento en la tasa de impulsos enviados. Esto desemboca en la liberación de iones de calcio en el tejido muscular, lo que induce más contracción y por tanto mayor liberación de ATP por parte de las mitocondrias para satisfacer la demanda \[A1\]. El factor clave en este caso son los impulsos eléctricos enviados, ya que existen diversidad de manifestaciones mioeléctricas ocasionadas por la fatiga muscular del estrés mecánico \[A2\] de eventos como hacer ejercicio. Esta señalización puede llegar a interferir en el ECG, en concreto por la actividad residual: incluso si la persona ya no está en movimiento, los músculos que han sido activados pueden continuar generando impulsos que interfieren con la señal. 

Existe evidencia de que la contracción de los músculos estriados contamina en gran medida la señal de ECG \[A3\]. Esta contaminación por artefactos musculares puede acentuarse por el hecho de que el rango de frecuencias del músculo estriado (2 \- 500 Hz) engloba al del ECG (0.5 \- 100 Hz) \[A4\], lo que se presta a que se infiltren las señales musculares a la lectura ya que no pueden ser filtradas en su totalidad.  Entonces, la aparición de más componentes de frecuencia en la transformada puede explicarse por este último punto: la mayor tasa de actividad mioeléctrica ocasiona que se infiltren señales musculares durante la medición del ECG. Por otro lado, vemos que en las distintas derivaciones, la señal cardiaca parece oscilar de forma más frecuente que en otros estados, es decir, visualmente luce más comprimida. Se ha encontrado que en actividad y post actividad, elementos de la señal como el complejo QRS y el intervalo QT se vuelven más cortos \[A5\], lo cual va de la mano con los resultados obtenidos en el escenario de ejercicio.

6. **Conclusiones**  
     
     
     
7. **Referencias**  