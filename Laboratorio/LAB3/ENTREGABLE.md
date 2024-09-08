# Desarrollar o mejorar un algoritmo capaz de diferenciar entre movimientos rutinarios, como rascarse el pecho o cepillarse los dientes, y las arritmias cardíacas 

## Introducción
Actualmente, para el diagnóstico de enfermedades cardiacas y/o arritmias, se utilizan diferentes dispositivos. Entre los más reconocidos se encuentran ECG (electrocardiograma) [1], Holters [2], Ecocardiograma [3], Tomografía Computarizada [4], entre otros. Lo que tienen en común es que el médico especialista requiere de las señales e imágenes generadas por estos dispositivos para realizar el diagnóstico.

En el caso de los ECG o Holters, se encargan de detectar los impulsos eléctricos del corazón mediante la inervación del órgano [1]. En el caso del ECG, es fundamental una correcta colocación de los electrodos en posiciones específicas del tórax para obtener un registro adecuado (en el caso de las derivaciones precordiales). Además, en el caso de los Holters, que registran la actividad cardíaca durante un período prolongado (generalmente 24 a 48 horas [2]), se requiere que el paciente mantenga un nivel de actividad controlado y evite movimientos bruscos que puedan interferir con la calidad de los datos obtenidos.

Un ejemplo notable de cómo los movimientos pueden afectar la señal del ECG es el fenómeno conocido como "taquicardia por cepillado de dientes" [5]. Este fenómeno ocurre cuando el movimiento al cepillarse los dientes genera interferencias que simulan actividad cardíaca rápida en los registros del ECG. Con el surgimiento de dispositivos wearables que buscan realizar funciones similares a los software que utilizan Holters y ECG, se ha notado que algunos de estos dispositivos alertan erróneamente a los pacientes sobre una enfermedad debido a parámetros ineficientes o movimientos espontáneos, lo que genera falsos positivos [6].

Para ilustrar este fenómeno, se presenta el caso de un paciente con fibrilación auricular paroxística, quien había comenzado el tratamiento con flecainida tres semanas antes de someterse a un examen de ECG Holter. La grabación mostró dos breves episodios de actividad cardíaca rápida, uno antes de acostarse y otro por la mañana. Tras una investigación más detallada, se descubrió que estos episodios coincidían con la rutina de cepillado de dientes del paciente. Actualmente, el único método confiable para confirmar o refutar esta observación es mediante la comparación cruzada con el diario del paciente, un detalle que los médicos no siempre tienen disponible [5].

## Estado del arte
### BeamO  
Este es un dispositivo comercial multifuncional para el monitoreo en casa. Se basa en la combinación de un ECG de una derivación, un oxímetro de pulso, un termómetro inalámbrico y un estetoscopio digital, lo que permite el diagnóstico de problemas cardíacos como arritmias. Además, la app permite compartir los datos con un médico, mejorando el seguimiento y diagnóstico [7].

![Fig. 1 Dispositivo BeamO](#) [7]

### Apple Watch  
Este es un dispositivo comercial que consta de un sensor de ECG de una derivación, lo que permite un monitoreo continuo. Además, este dispositivo presenta algoritmos que correlacionan los datos obtenidos con otros sensores como acelerómetro y giroscopio, de modo que se puedan distinguir las variaciones normales causadas por las actividades cotidianas de posibles patologías cardíacas [8].

![Fig. 2 Dispositivo Apple Watch](#) [8]

## Estadísticas

Al usar los ECG, estos dispositivos generalmente cuentan con software como herramienta para detectar anomalías en los trazos del ECG. Sin embargo, estos software no logran ser completamente fiables debido a errores. En un estudio se observó que el software malinterpretó infartos de miocardio (STEMI) con condiciones como el bloqueo de rama derecha, hipertrofia ventricular y el patrón de Brugada. Esto se debe a la incapacidad de interpretar correctamente los complejos QRS y las ondas ST [7R]. Esto indica fallas en estos dispositivos, en particular al interpretar las bioseñales, lo que no solo confunde enfermedades, sino que puede llegar a notificar una enfermedad cuando el paciente no la posee.

### Estadísticas de falsos positivos 
#### Evaluation of Atrial Fibrillation using Wearable Device Signals and Home Blood Pressure Data in the MIPACT Study (MIPACT-AFib) [8A]

Con el auge de los dispositivos wearables, comenzó a surgir evidencia de que algunos con capacidades de detección de arritmias generan falsos positivos. Este estudio evaluó la detección de fibrilación atrial (AF) en dispositivos wearables, incluyendo el Apple Watch y el OmronBP. De 2615 participantes evaluados, solo 5 de los 86 notificados con irregularidades en el ritmo cardíaco fueron confirmados con fibrilación auricular, lo que implica que el 93% de las alarmas no correspondían a arritmias.

#### Pulsewatch Study [9A]

Este estudio basado en el ensayo clínico Pulsewatch (NCT03761394) evaluó el uso de un sistema basado en un smartwatch y un monitor de parche ECG. En un grupo de 85 participantes, 15 recibieron alertas de AF, de las cuales el 67% fueron falsos positivos. Los falsos positivos fueron causados por interferencias o arritmias menores.

## Problemática detectada

Existe una carencia de software especializados para dispositivos cardíacos wearables que permitan distinguir las diferencias entre actividades rutinarias y patologías a nivel de bioseñal.

## Bases de datos

El objetivo es desarrollar o mejorar un algoritmo que sea capaz de diferenciar los movimientos rutinarios, como rascarse el pecho o cepillarse los dientes, de las arritmias cardíacas.

- **A large scale 12-lead electrocardiogram database for arrhythmia study** [R1]  
  Esta base de datos proporciona registros de ECG de personas con arritmias cardíacas, junto con sus respectivos diagnósticos.

- **Base de datos de personas sanas realizando actividades cotidianas**  
  Esta base de datos recopila ECG de personas sanas realizando actividades rutinarias, proporcionando una referencia más extensa.

## Propuesta frente a la problemática

Desarrollar y entrenar un modelo de Machine Learning capaz de diferenciar entre un trazado de ECG afectado por un movimiento rutinario y un trazado de ECG con una arritmia.
