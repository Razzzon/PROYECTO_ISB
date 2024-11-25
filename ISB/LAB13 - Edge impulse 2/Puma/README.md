# LAB13: Extracción de características *Edge Impulse* 

<br>

## Lista de contenidos:
1. **Creación de impulso**  
2. **Características espectrales**
3. **Clasificador**
4. **Link al Edge Impulse creado**

## **Creación del impulso**
<div align="justify">
A partir del laboratorio anterior, donde se creó un proyecto para la importación de data en Edge Impulse, se va a realizar la extracción de características. Entonces, el primer paso a realizar es la creación del impulso, por lo que se selecciona la opción de Impulse design.
</div>

<div align="center">
  <img src="./imagenes/ImpulseDesign.PNG" alt="ImpulseDesign" width="450">
  <p>

  **Figura 1: Creación del impulso**
  </p>
</div> <br>

<div align="justify">
En la ventana para la creación del impulso, se debe añadir los bloques de procesamiento y aprendizaje. En el caso del bloque de procesamiento, se selecciona la opción de Spectral Analysis. Por otro lado, en el caso del bloque de aprendizaje se selecciona la opción de Classification. Después de realizar estos ajustes, se guarda el impulso.
</div>

<div align="center">
   <img src="./imagenes/SpectralAnalysis.PNG" alt="SpectralAnalysis" width="350">
   <img src="./imagenes/Classification.PNG" alt="Classification" width="350">

**Figura 2: Selección de los bloques de procesamiento y aprendizaje**  
</div>
<br>

## **Características espectrales**
<div align="justify">
El segundo paso a realizar son las características espectrales. Se selecciona esta opción y se nos muestra una ventana donde se observan la configuración de parámetros y el resultado del filtro.
</div>  <br>

<div align="center">
  <img src="./imagenes/SpecialFeatures.PNG" alt="SpecialFeatures" width="450">
  <p>

  **Figura 3: Características espectrales**
  </p>
</div> <br>

<div align="justify">
Entonces, en la configuración de parámetros, se selecciona el filtro pasa bajas con una frecuencia de corte de 150 Hz y orden 6. Después, se realiza el guardado de los parámetros y se observa el resultado del filtro realizado.
</div>  <br>

<div align="center">
  <img src="./imagenes/Parameters.PNG" alt="Parameters" width="450">
  <p>

  **Figura 4: Ajuste de parámetros**
  </p>
</div> <br>

<div align="justify">
Después, se selecciona la opción de Generate features y se observa el siguiente resultado:
</div>  <br>

<div align="center">
   <img src="./imagenes/GenerateFeatures.PNG" alt="GenerateFeatures" width="350">
   <img src="./imagenes/Resultado.PNG" alt="Resultado" width="350">

**Figura 5: Generación de funciones**  
</div>
<br>

## **Clasificador**
<div align="justify">
El último paso a realizar es el clasificador. Se selecciona esta opción y se nos muestra una ventana donde se debe realizar la configuración de la red neuronal.
</div> <br>

<div align="center">
  <img src="./imagenes/Classifier.PNG" alt="Classifier" width="450">
  <p>

  **Figura 6: Ventana para importar los datos**
  </p>
</div> <br>

<div align="justify">
Después de realizar la configuración de la red neuronal, se guarda y entrena para obtener los resultados del modelo. Los resultados obtenidos fueron los siguientes:
</div> <br>

<div align="center">
   <img src="./imagenes/Modelo1.PNG" alt="Modelo1" width="350">
   <img src="./imagenes/Modelo2.PNG" alt="Modelo2" width="350">

**Figura 7: Resultados del modelo**
</div> <br>

<div align="justify">
Finalmente, se realiza la discusión de los resultados obtenidos.  
</div> <br>

- **Desempeño General del Modelo**:  
  - Se obtuvo una precisión global del 73.5%, lo que indica un desempeño aceptable pero que puede ser mejorable.
  - El valor de pérdida de 0.46 sugiere que el modelo no está sobreajustado.

- **Análisis de la Matriz de Confusión**:  
  - Se observa que la clase Ejercicio se clasifica correctamente en el 100% de los casos, por lo que se podría decir que es el punto fuerte del modelo.
  - Se observa una alta confusión entre las clase de Basal y Respiración. El 58.8% de las muestras de Basal se clasifican incorrectamente como Respiración y el 15% de las muestras de Respiración se clasifican incorrectamente como Basal.
  - Esta confusión puede deberse a características compartidas entre las dos categorías de Basal y Respiración, lo que limita la capacidad discriminante del modelo. Por otro lado, la clase Ejercicio presenta características que permite diferenciarle fácilmente de las otras dos categorías.

- **Métricas Adicionales**:  
  - Se observa un valor de 0.91 para el área bajo la curva ROC, lo que sugiere un buen balance entre sensibilidad y especificidad.   
  - Respecto a las métricas del F1-Score, estas evidencian que la clase Ejercicio presenta un desempeño perfecto (1.00). Mientras que las clases Basal (0.52) y Respiración (0.72) muestran necesidad de mejora en la clasificación.

- **Distribución de los Datos (Explorador de Datos)**:  
  - El gráfico muestra que las muestras se agrupan en ciertas regiones del espacio de características. Por un lado, la clase Ejercicio está separada de las otras dos categorías. Por otro lado, hay traslapes significativos entre "Basal" y "Respiración", lo que confirma la confusión observada en la matriz de confusión.


## **Link al Edge Impulse creado**
<div align="justify">
Link: https://studio.edgeimpulse.com/public/558232/live
</div> <br>