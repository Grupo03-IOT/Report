<!-- nav:start -->
<p align="center"><a href="README.md">← Inicio</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-2.md">Capítulo II →</a></p>
<!-- nav:end -->

<a id="capítulo-i-introducción"></a>
# Capítulo I: Introducción

Este capítulo introduce la visión general del proyecto, detallando el perfil de la startup emergente y la problemática que motiva la solución. Se plantea el diseño inicial siguiendo un enfoque estructurado para el desarrollo de la arquitectura IoT y los productos digitales asociados

<a id="11-startup-profile"></a>
## 1.1. Startup Profile

Esta sección describe la identidad de la organización responsable del proyecto, abarcando su propósito fundamental en la industria tecnológica y la composición del talento técnico encargado de la creación de la plataforma B2B.

<a id="111-descripción-de-la-startup"></a>
### 1.1.1. Descripción de la Startup

SenseWork es una startup tecnológica dedicada a optimizar el confort ambiental en espacios de coworking y oficinas compartidas a través de una solución innovadora de Internet de las Cosas (IoT). Nuestra plataforma mide en tiempo real los niveles de ruido y las condiciones térmicas de las diferentes salas, alertando sobre inconvenientes de climatización o excesos de decibelios sin vulnerar en ningún momento la privacidad de los usuarios.

A través de nuestra aplicación móvil, los miembros del espacio de trabajo pueden visualizar y filtrar las salas disponibles utilizando un semáforo interactivo que califica el ambiente como óptimo, moderado o ruidoso, asegurando el lugar ideal para sus llamadas o trabajo enfocado. Por otro lado, ofrecemos a los administradores un dashboard web integral con mapas de calor y analíticas históricas que permite gestionar proactivamente las alertas, establecer umbrales de confort personalizados y evaluar el aislamiento de sus instalaciones.

SenseWork combina hardware IoT altamente accesible basado en Edge Computing con plataformas digitales intuitivas, logrando que los coworkings mejoren la retención de sus clientes al garantizar espacios de alta ergonomía ambiental, y que los usuarios maximicen su productividad sin fricciones.

**Misión** <br>
Conectar a los trabajadores y administradores de espacios compartidos mediante un ecosistema IoT accesible y 100% seguro. Buscamos empoderar a los usuarios para que encuentren el ambiente de trabajo perfecto de manera rápida, mientras facilitamos a las administraciones B2B la gestión proactiva de sus instalaciones, protegiendo siempre la privacidad de las conversaciones.

**Visión** <br>
Consolidarse como el estándar tecnológico B2B de referencia en el monitoreo del confort acústico y térmico corporativo en Latinoamérica, transformando la manera en que se auditan y habitan los coworkings a través de soluciones IoT escalables, precisas y preventivas.

<a id="112-perfiles-de-integrantes-del-equipo"></a>
### 1.1.2. Perfiles de integrantes del equipo

El equipo desarrollador está conformado por estudiantes de la carrera de Ingeniería de Software de la Universidad Peruana de Ciencias Aplicadas. A continuación, se detallan los perfiles de los miembros de la startup:

| Foto del estudiante                                                                       | Nombres y apellidos | Código de estudiante | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="assets/team/espino.png" alt="Alejandro Espino Flores" width="100">              | Espino Flores, Alejandro | U202122129 | Estudiante del octavo ciclo de Ingeniería de Software. Trabajo en el diseño e implementación de servicios backend con Java y Spring Boot aplicando diseño guiado por el dominio: separación en bounded contexts, arquitectura por capas con inversión de dependencias y un esquema de persistencia propio por contexto. Me interesa que la documentación y el código digan lo mismo, de modo que cualquier integrante pueda explicar el diseño sin haberlo escrito. En este proyecto aporto el servicio RESTful interno sobre el que se apoyan la capa de borde y las aplicaciones cliente, las convenciones técnicas que el equipo sigue en ese repositorio, y la revisión e integración de las incorporaciones mediante pull requests. |
| <img src="assets/team/huarcaya.png" alt="Gilbert Alonso Huarcaya Matias" width="100">     | Huarcaya Matias, Gilbert Alonso | U202322187 | Estudiante de séptimo ciclo de Ingeniería de Software. Trabajo en desarrollo backend con Java y Spring Boot, y en servicios de borde con Python, aplicando arquitectura por capas y separación entre el dominio y la infraestructura. Me interesa la calidad del software: automatización de pruebas, revisión de código y trazabilidad entre lo documentado y lo construido. Aporto al equipo en el diseño de los servicios cloud y edge de la plataforma, en la definición de los contratos de mensajería entre el dispositivo y la nube, y en la verificación de que los artefactos del informe correspondan con la solución implementada. |
| <img src="assets/team/lang.png" alt="Werner Khalil Lang Nassi" width="100">               | Lang Nassi, Werner Khalil | U202310003 |   Estudiante de la Universidad Peruana de Ciencias Aplicadas (UPC), cursando en 8.º ciclo. Tengo afinidad con la arquitectura de software y e desarollado habilidades con machine y deep learning. Ademas siempre estoy dispuesto a aprender nuevas metologias o habilidades que me ayuden a desarollarme en la carrera.   |
| <img src="assets/team/JuanArone_Photo.png" alt="Juan Paul Llamccaya Arone" width="100">           | Llamccaya Arone, Juan Paul | U201923571 | Estudiante de Ingeniería de Software cursando el 8 ciclo con experiencia en programación en C++ (CLI), programación orientada a objetos (POO) y desarrollo web con HTML, JavaScript y CSS. Cuenta con conocimientos en diseño UX, Packet Tracer, SQL y Python, además de experiencia en tecnologías de desarrollo frontend como Angular y React.                                                                                                                                                                                                                                                                                              |
| <img src="assets/team/SandraLuyo.png" alt="Sandra Paula Luyo Correa" width="100">         | Luyo Correa, Sandra Paula | U202314513 | Estudiante de 20 años del ectavo ciclo de la carrera de Ingeniería de Software en la UPC. Me considero una persona ordenada y responsable. Tengo conocimientos de C++, C#, JavaScript, Vue, Angular y base de datos en SQL y MongoDB. En este proyecto, me comprometo a gestionar, ayudar y motivar a mi equipo en todo lo que sea necesario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <img src="assets/team/FotoSolis.png" alt="Giancarlo Rafael Solis Santa Cruz" width="100"> | Solis Santa Cruz, Giancarlo Rafael | U202318615 | Estudiante de Ingeniería de Software cursando el octavo ciclo. Persona proactiva, intuitiva y enfocada en la eficiencia, con un enfoque preventivo frente a los problemas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

<a id="12-solution-profile"></a>
## 1.2. Solution Profile

En esta sección se expone la justificación de la propuesta tecnológica y el problema detectado en el mercado. Asimismo, se desarrolla el proceso Lean UX para validar las suposiciones e hipótesis que rigen la creación del modelo de negocio digital.

<a id="121-antecedentes-y-problemática"></a>
### 1.2.1 Antecedentes y problemática

El trabajo híbrido y remoto se ha consolidado, en los últimos años, como una modalidad estructural del mercado laboral peruano. Según registros del Ministerio de Trabajo y Promoción del Empleo [MTPE], mientras en 2019 solo 1 040 empresas formales declararon contar con al menos un teletrabajador, en 2022 la cifra se multiplicó hasta las 12 766 compañías (MTPE, 2023). Esta transformación ha impulsado el crecimiento sostenido de los espacios de trabajo compartido en Lima, donde ya operan 86 sedes de coworking concentradas en los distritos de mayor actividad corporativa, con operadores expandiéndose hacia nuevas zonas y grandes empresas y no únicamente startups o freelancers como principal motor de demanda (Binswanger, 2026). En un mercado de estas características, la competencia ha dejado de librarse por precio o ubicación: se disputa en la calidad de la experiencia de trabajo, dentro de la cual el confort ambiental la combinación del confort acústico y el térmico resulta determinante.

La gravedad de esta condición radica en los efectos documentados de ambos factores sobre el desempeño cognitivo. Las directrices de la Organización Mundial de la Salud sobre ruido ambiental reconocen que la exposición al ruido interfiere en la comunicación hablada, perturba la concentración y degrada el desempeño en tareas cognitivas (Berglund et al., 1999). Este problema se acentúa en una de las capitales más ruidosas de la región: la red de monitoreo de la Autoridad de Transporte Urbano para Lima y Callao [ATU], que opera 50 sensores en 22 distritos, registró promedios de hasta 70.5 dB en la estación Angamos, superando de forma holgada el límite diurno de 60 dB(A) que el Estándar de Calidad Ambiental para Ruido, aprobado por la Presidencia del Consejo de Ministros [PCM], fija para zonas residenciales (ATU, 2024; PCM, 2003). Se trata, además, de mediciones exteriores que no reflejan el ambiente interior, donde se suman el ruido de los equipos de climatización, las conversaciones simultáneas de un plan abierto y el sonido que se infiltra desde la vía pública. En la dimensión térmica, la norma de confort de la International Organization for Standardization [ISO] define como confortable aquel entorno en el que menos del 10 % de los ocupantes estaría insatisfecho, condición que solo se garantiza cuando la temperatura de operación se mantiene dentro de los rangos de referencia para trabajo de oficina (ISO, 2005).

A pesar de contar con marcos normativos maduros para caracterizar ambas dimensiones la norma ISO 1996 define el nivel sonoro continuo equivalente y los percentiles estadísticos que distinguen un ruido de fondo permanente de picos intrusivos aislados (ISO, 2016), mientras que la ISO 7730 traduce la condición térmica a índices normalizados (ISO, 2005), estos se aplican casi exclusivamente en estudios puntuales a cargo de consultoras especializadas con instrumentos certificados, y no como información de la operación diaria. Las ofertas tecnológicas disponibles, por su parte, se han enfocado en otras variables: las plataformas corporativas de monitoreo ambiental se orientan al edificio como unidad de gestión y a la calidad del aire como métrica central Airthings reporta el promedio del nivel sonoro sin percentiles normalizados ni indicadores térmicos (Airthings, 2026a, 2026b), y Kaiterra no contempla la dimensión acústica (Kaiterra, 2026), mientras que los sonómetros profesionales son instrumentos de medición puntual que requieren un operador y no generan registro histórico ni alertas. El mercado peruano aún no ofrece una solución tecnológica especializada en el confort acústico y térmico sala por sala para espacios de trabajo compartidos.

El problema central radica en la imposibilidad de los operadores y de los miembros de los espacios de trabajo compartidos de Lima Metropolitana para conocer y gestionar las condiciones acústicas y térmicas reales de cada sala. Ante la ausencia de una medición objetiva y continua, el administrador actúa de forma reactiva, descubriendo los problemas a través de quejas tardías y sin detalle o de salas que dejan de reservarse, mientras que el miembro descubre las condiciones del ambiente cuando ya reservó y ocupó el espacio, con el consiguiente deterioro de su concentración, de sus videollamadas y de la renovación de su membresía. Para estructurar y delimitar la problemática, se aplicó el marco analítico de las 5W y 2 Hs:

* **What (Qué):** Existe una carencia de sistemas de monitoreo de confort acústico y térmico por sala, en tiempo real y asequibles para el sector. Esto convierte al problema en una condición invisible: salas cuyos niveles sonoros superan el umbral de referencia para el trabajo de concentración (45 dB) o cuya temperatura se aparta del rango de confort (20 °C a 23 °C), sin que ni el usuario ni el operador puedan verificarlo antes de la reserva.
* **Who (Quién):** Los segmentos directamente afectados son los miembros del coworking profesionales remotos e híbridos y freelancers que reservan salas para concentración o videollamadas y los administradores y gestores de los espacios, responsables de la operación del local y de la satisfacción de sus clientes.
* **Where (Dónde):** El problema ocurre en las salas de los espacios de trabajo compartidos de Lima Metropolitana —cabinas de llamadas, salas de reuniones y áreas abiertas—, concentrados en distritos corporativos como San Isidro, Miraflores, Surco y Barranco.
* **When (Cuándo):** La condición es continua durante la jornada laboral y se acentúa en las horas pico de reserva. El intervalo crítico transcurre entre la aparición del problema y su manifestación como queja o como caída de reservas, lapso durante el cual el administrador lo desconoce por completo.
* **Why (Por qué):** Existe, primero, una alta barrera de entrada tecnológica: las redes de sensores industriales son costosas y ajenas a la operación del coworking, y los sonómetros profesionales solo permiten mediciones puntuales, sin registro histórico ni alertas. Segundo, no existe un mecanismo comercial que obligue a transparentar las condiciones de las salas, y el miembro tiende a no formalizar la queja: abandona la sala o deja de volver, de modo que la causa permanece invisible para el operador.
* **How (Cómo):** La problemática se manifiesta de forma silente y retrospectiva. El miembro descubre las condiciones al ocupar la sala, cuando ya no puede cambiarla; el administrador inspecciona a mano, ajusta la climatización por percepción e interviene sin evidencia, sin saber si su acción mejora o empeora la condición, por lo que el problema tiende a repetirse.
* **How Much (Cuánto):** Las videollamadas se ven interrumpidas por ruido externo superior a los 55 dB, y una sala fuera del rango de confort térmico presenta, conforme a ISO 7730, más de un 10 % de ocupantes potencialmente insatisfechos (ISO, 2005). Para el operador, el costo del hardware industrial impide instrumentar todas las salas, y las pérdidas se materializan en salas infrautilizadas y membresías no renovadas; la inversión resulta asumible solo si el costo por sala se mantiene por debajo del ingreso de unas pocas horas de reserva.

<a id="122-lean-ux-process"></a>
### 1.2.2 Lean UX Process.

El marco de Lean UX Process abarca la visión del modelo de negocio que será soportado por el producto de software. Mediante iteraciones rápidas, se formulan declaraciones de problemas y suposiciones clave para dirigir el diseño de la solución hacia la entrega de valor tangible.

<a id="1221-lean-ux-problem-statements"></a>
#### <i>**1.2.2.1. Lean UX Problem Statements.**</i>

Hemos observado que los administradores de coworkings y oficinas compartidas operan de manera reactiva ante las quejas ambientales, ya que carecen de herramientas de monitoreo de confort en tiempo real.
<br>¿Cómo podemos proveerles un panel web (Dashboard) centralizado que les permita anticiparse a los problemas térmicos y de ruido en sus instalaciones?

Hemos observado que los trabajadores remotos e híbridos se sienten frustrados al ocupar cabinas o salas que resultan ser excesivamente ruidosas o calurosas, lo cual afecta severamente su concentración y productividad.
<br>¿Cómo podemos ofrecerles una aplicación móvil intuitiva con indicadores visuales que les permita encontrar el espacio de trabajo ideal de manera rápida?

Hemos observado que los usuarios de oficinas compartidas desconfían de los sistemas de monitoreo acústico tradicionales por el temor legítimo a que sus conversaciones privadas sean grabadas o vulneradas.
<br>¿Cómo podemos garantizar la medición precisa de decibelios en las salas sin capturar, almacenar ni transmitir audios crudos en ningún momento?

Hemos observado que la implementación de redes de sensores industriales resulta demasiado costosa y requiere instalaciones eléctricas complejas que los espacios B2B evitan realizar.
<br>
¿Cómo podemos diseñar un ecosistema de dispositivos IoT de bajo costo, basado en Edge Computing, que sea escalable, económico y totalmente seguro de implementar?

<a id="1222-lean-ux-assumptions"></a>
#### <i>**1.2.2.2. Lean UX Assumptions.**</i>

**Business Assumptions**

* El hardware IoT económico (~S/ 65 por nodo) facilitará la escalabilidad y adopción masiva en infraestructuras B2B frente a soluciones industriales costosas.
* El procesamiento *Edge* que elimina el audio instantáneamente superará las barreras de privacidad y legalidad, siendo un diferenciador clave de venta.

**Business Outcome Assumptions**

* Los coworkings incrementarán su retención de clientes corporativos en un 20% al poder garantizar y certificar ambientes ergonómicos.
* Se reducirán en un 40% los costos operativos derivados del uso ineficiente del aire acondicionado gracias al monitoreo térmico focalizado.

**User Assumptions**

* Los trabajadores remotos e híbridos se sienten profundamente frustrados al tener videollamadas interrumpidas por ruido externo superior a 55 dB.
* Los administradores de *facility management* operan a ciegas; solo descubren fallas de climatización cuando un cliente se queja formalmente.

**User Outcome and Benefit Assumptions**

* Los usuarios ahorrarán tiempo y reducirán su estrés al encontrar una sala óptima en menos de 60 segundos desde su móvil.
* Los administradores obtendrán tranquilidad y control predictivo, previniendo crisis ambientales en las instalaciones.

**Feature Assumptions**

* Un semáforo visual (Verde, Amarillo, Rojo) es la forma más rápida para que el usuario entienda el estado de una sala sin leer métricas complejas.
* El cruce de datos internos con la API de OpenWeatherMap permitirá a los administradores evaluar qué salas tienen fallas reales de aislamiento.

<a id="1223-lean-ux-hypothesis-statements"></a>
#### <i>**1.2.2.3. Lean UX Hypothesis Statements.**</i>

* **Hypothesis 1:**
  <br> Creemos que lograremos un incremento del 30% en las renovaciones de membresías corporativas. Si los administradores de instalaciones B2B. Alcanzan un control proactivo sobre los problemas de climatización (HVAC) y aislamiento acústico. Con el mapa de calor del *Web Dashboard* y el centro de alertas automatizado.
* **Hypothesis 2:**
  <br> Creemos que lograremos una alta tasa de usuarios activos diarios. Si los trabajadores híbridos miembros del coworking. Alcanzan la capacidad de encontrar al instante un espacio tranquilo y cómodo sin vulnerar su privacidad. Con el mapa móvil en vivo de las salas, el sistema inteligente de filtrado y los indicadores visuales tipo semáforo.
* **Hypothesis 3:**
  <br> Creemos que lograremos una reducción del 40% en los costos de ancho de banda de hardware en la nube. Si nuestra arquitectura IoT. Alcanza el procesamiento local de las señales de audio. Con un enfoque de *Edge Computing* (Flask/ESP32) que calcula el $V_{RMS}$ y elimina los audios crudos de manera instantánea.

<a id="1224-lean-ux-canvas"></a> 
#### <i>**1.2.2.4. Lean UX Canvas.**</i>

El Lean UX Canvas permite organizar y validar los principales elementos de la propuesta de solución de SenseWork y ZenRoom, relacionando el problema de negocio, los usuarios, los resultados esperados, las soluciones planteadas, las hipótesis, los supuestos y los experimentos necesarios para validar la propuesta de manera iterativa.

<div align="center">
  <img src="img/Lean UX Canvas (1).png" alt="Lean UX Canvas" width="1000">
  <br>
   <i>Figura 1. Lean UX Canvas de la propuesta de solución SenseWork y ZenRoom.</i>
</div>

<a id="13-segmentos-objetivo"></a>
## 1.3. Segmentos objetivo.

<u>**Segmento Objetivo #1: Miembros y Usuarios del Coworking**</u>

| Segmento Objetivo<br>#1: | Miembros y Usuarios del Coworking  |
| :--- | :--- |
| **Aspectos demográficos** | **Sexo:** Indistinto<br>**Edad:** 22 a 50 años<br>**Nivel socioeconómico:** Profesionales, freelancers, nómadas digitales y emprendedores que invierten en espacios de trabajo flexible  |
| **Aspectos geográficos** | **Nacionalidad:** Peruana y extranjeros residentes<br>**Zona geográfica:** Lima Metropolitana, especialmente en distritos con alta concentración de coworkings y centros empresariales (Miraflores, San Isidro, Surco, Barranco, San Borja) |
| **Aspectos psicográficos** | Profesionales enfocados en la alta concentración (*deep work*), la productividad y el bienestar durante su jornada laboral.<br>Valoran el confort acústico y térmico como factores esenciales para realizar llamadas sin interrupciones y trabajar sin fatiga.<br>Buscan herramientas digitales inmediatas, autónomas y transparentes que les eviten perder tiempo buscando salas adecuadas. |
| **Aspectos conductuales** | **Necesidad:** Encontrar rápidamente salas de concentración con bajo nivel de ruido (<45 dB) y temperatura óptima (20°C - 23°C) para llamadas importantes o trabajo enfocado.<br>**Uso de herramientas:** Consultan la App para revisar el mapa en vivo con semáforo visual (Verde, Amarillo, Rojo), filtrar por decibelios/temperatura y consultar el histórico de tranquilidad por hora.<br>**Respuesta:** Seleccionan la sala según las métricas en tiempo real y utilizan el botón de "Reporte de Disconfort" ante cualquier problema acústico o térmico en el espacio. |

<br>

<u>**Segmento Objetivo #2: Administradores y Gestores de Coworking**</u>

| Segmento Objetivo<br>#2: | Administradores y Gestores de Espacios de Coworking  |
| :--- | :--- |
| **Aspectos demográficos** | **Sexo:** Indistinto<br>**Edad:** 25 a 60 años<br>**Nivel socioeconómico:** Administradores de sede, Community Managers y Jefes de Operaciones / Facilities con manejo de presupuesto operativo (NSE A y B) |
| **Aspectos geográficos** | **Nacionalidad:** Peruana<br>**Zona geográfica:** Lima Metropolitana, en sedes corporativas, edificios comerciales y centros de coworking |
| **Aspectos psicográficos** | Gestores orientados a la eficiencia operativa, la satisfacción del cliente y la diferenciación competitiva de sus instalaciones.<br>Valoran la automatización y el uso de datos en tiempo real (*data-driven*) para mantener estándares de confort y prevenir quejas antes de que ocurran.<br>Muestran interés en soluciones que optimicen el uso de climatización y energía sin comprometer la experiencia ni la reputación del establecimiento. |
| **Aspectos conductuales** | **Necesidad:** Monitorear en tiempo real el confort ambiental integral (acústico y térmico) de todo el edificio y prevenir reclamos de los usuarios.<br>**Uso de herramientas:** Acceden al Dashboard Web para supervisar el plano interactivo (Heatmap), analizar promedios históricos cruzados con el clima exterior (API) y configurar umbrales tolerables según el tipo de sala.<br>**Respuesta:** Actúan inmediatamente ante alertas automáticas cuando una sala supera los límites de decibelios por más de 5 minutos o cuando la temperatura sale del rango de confort. |

<hr>

<!-- nav:start -->
<p align="center"><a href="README.md">← Inicio</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-2.md">Capítulo II →</a></p>
<!-- nav:end -->
