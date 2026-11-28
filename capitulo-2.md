<!-- nav:start -->
<p align="center"><a href="capitulo-1.md">← Capítulo I</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-3.md">Capítulo III →</a></p>
<!-- nav:end -->

<a id="capítulo-ii-requirements-elicitation-analysis"></a>
# Capítulo II: Requirements Elicitation & Analysis

<a id="21-competidores"></a>
## 2.1. Competidores.

El análisis identifica a los competidores directos —soluciones digitales con modelos de negocio equivalentes— y a los indirectos, cuya oferta cubre parcialmente la misma necesidad.

**Airthings for Business**

Empresa noruega especializada en el monitoreo de calidad ambiental interior para el sector corporativo. Ofrece cinco modelos de monitor —Space Pro, Space Plus, Space Co2, Space Co2 Mini y Space Hub—, una plataforma de analítica y tres sensores virtuales: Virus Risk, Space Utilization y Ventilation Rate. Declara más de 10 000 edificios monitoreados y 150 000 dispositivos desplegados a nivel global (Airthings, 2026a).

Es el competidor más cercano a SenseWork, pues **sí incorpora un sensor de ruido ambiental**, y su enfoque de privacidad coincide con el de esta solución: el monitor muestrea 60 milisegundos de audio cada 6 segundos, calcula el nivel en decibelios dentro del propio dispositivo y descarta la muestra, de modo que resulta imposible reconstruir una conversación (Airthings, 2026b). El rango dinámico declarado es de 35 a 120 dBA SPL.

La diferencia se encuentra en la profundidad del tratamiento acústico. Airthings reporta el **nivel promedio en dBA a lo largo del tiempo**, sin aplicar las normas de confort acústico: no calcula el nivel continuo equivalente ponderado energéticamente ni los percentiles estadísticos L10, L50 y L90 de la norma ISO 1996, que son los que permiten distinguir un ruido de fondo permanente de picos intrusivos aislados. Tampoco calcula índices de confort térmico normalizados según ISO 7730, sino que reporta temperatura y humedad como valores independientes.

**Kaiterra**

Compañía enfocada en el sector B2B y la gestión de edificios inteligentes. Su línea de producto comprende monitores de interior —Sensedge, Sensedge Go y Sensedge Mini—, monitores de exterior y un modelo para instalación en conductos de climatización (Sensedge Duct), complementados por la Kaiterra Data Platform (Kaiterra, 2026).

Su ventaja competitiva reside en el cumplimiento normativo: sus dispositivos otorgan hasta 9 puntos en la certificación WELL y son compatibles con LEED, Fitwel, RESET y UL Verified Healthy Buildings. Se dirigen a desarrolladoras inmobiliarias y gestores de infraestructura de gran escala.

Su oferta **no contempla la dimensión acústica** —ninguno de sus monitores mide nivel sonoro— ni el confort térmico normalizado. Su unidad de gestión es el edificio y no la sala individual, lo que la aleja de la operación diaria de un espacio de trabajo compartido.

**Sonómetros profesionales (NTi Audio, Svantek)**

Instrumentos de medición acústica certificados según la norma IEC 61672, empleados en estudios acústicos, peritajes y verificación de cumplimiento normativo (NTi Audio, 2026). Ofrecen exactitud metrológica y validez legal de las mediciones, lo que los convierte en el referente técnico del sector. No obstante, se trata de instrumentos de medición puntual que requieren operador, no generan registro histórico continuo ni alertas, y su costo por unidad impide instrumentar de forma permanente todas las salas de un establecimiento.


<a id="211-análisis-competitivo"></a>
### 2.1.1. Análisis competitivo.

<table>
  <thead>
    <tr>
      <th colspan="6">Competitive Analysis Landscape</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2"><strong>¿Por qué llevar a cabo este análisis?</strong></td>
      <td colspan="4">El objetivo es identificar las brechas tecnológicas y de experiencia de usuario en las plataformas actuales de monitoreo ambiental interior, para validar que la especialización en confort acústico y térmico normalizado, con operación garantizada sin conexión a internet, responde a una demanda insatisfecha en los espacios de trabajo compartidos de Lima Metropolitana.</td>
    </tr>
    <tr>
      <td colspan="2"><strong>Competidores</strong></td>
      <td><strong>SenseWork</strong> <img src="assets/brand/sensework-isotipo.svg" alt="SenseWork" width="34"></td>
      <td>Airthings for Business <img src="assets/competitors/airthings.svg" alt="Airthings for Business" width="110"></td>
      <td>Kaiterra <img src="assets/competitors/kaiterra.png" alt="Kaiterra" width="110"></td>
      <td>Sonómetros profesionales <img src="assets/competitors/nti.webp" alt="NTi Audio" width="70"></td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Perfil</strong></td>
      <td>Overview</td>
      <td>Plataforma IoT especializada en confort acústico y térmico para espacios de trabajo compartidos. Mide el nivel sonoro y las condiciones térmicas de cada sala, aplica las normas ISO 1996 e ISO 7730, y evalúa alertas en la capa Edge sin depender de la conexión a internet. El audio se procesa en el dispositivo y nunca se transmite.</td>
      <td>Plataforma noruega de monitoreo de calidad ambiental interior para el sector corporativo. Cinco modelos de monitor, panel en la nube y tres sensores virtuales. <strong>Mide nivel sonoro</strong> muestreando 60 ms cada 6 s y descartando el audio en el dispositivo, con un rango de 35 a 120 dBA SPL.</td>
      <td>Plataforma orientada a la gestión de edificios inteligentes y a la obtención de certificaciones. Línea Sensedge para interior, exterior y conductos de climatización, con analítica propia. Otorga hasta 9 puntos en la certificación WELL.</td>
      <td>Instrumentos de medición acústica de precisión certificados según IEC 61672, empleados en estudios acústicos, peritajes y verificación de cumplimiento normativo.</td>
    </tr>
    <tr>
      <td>Ventaja competitiva ¿Qué valor ofrece a los clientes?</td>
      <td><strong>Indicador interpretable sin formación técnica:</strong> expresa el confort como el porcentaje de personas que estaría insatisfecha, en lugar de valores crudos. <br><strong>Operación sin internet:</strong> las alertas se evalúan en el propio local, de modo que una caída del enlace no deja al operador sin vigilancia. <br><strong>Privacidad por diseño:</strong> el audio no abandona el dispositivo. <br><strong>Costo por sala</strong> compatible con instrumentar el local completo.</td>
      <td><strong>Amplitud de variables:</strong> cobertura de contaminantes que ningún competidor iguala, incluido el radón. <br><strong>Marca consolidada:</strong> más de 10 000 edificios y 150 000 dispositivos desplegados. <br><strong>Instalación autónoma:</strong> dispositivos inalámbricos que el propio cliente instala. <br><strong>Sensores virtuales</strong> derivados de los físicos: riesgo viral, uso del espacio y tasa de ventilación.</td>
      <td><strong>Cumplimiento normativo:</strong> hasta 9 puntos en WELL, más compatibilidad con LEED, Fitwel, RESET y UL Verified Healthy Buildings. <br><strong>Cobertura integral del edificio:</strong> monitores de interior, exterior y de conducto de climatización bajo una misma plataforma.</td>
      <td><strong>Exactitud certificada</strong> y trazabilidad metrológica. <br><strong>Validez legal</strong> de las mediciones para efectos normativos y periciales.</td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Perfil de Marketing</strong></td>
      <td>Mercado objetivo</td>
      <td><strong>Primario:</strong> operadores de espacios de trabajo compartidos en Lima Metropolitana, con entre uno y cinco locales en operación. <br><strong>Secundario:</strong> usuarios que reservan salas de forma recurrente para trabajo de concentración o videollamadas.</td>
      <td>Grandes corporaciones y administradores de edificios de oficinas en mercados desarrollados, con presupuestos de facilities consolidados.</td>
      <td>Desarrolladoras inmobiliarias y administradores de edificios corporativos que persiguen certificaciones de sostenibilidad.</td>
      <td>Consultoras de acústica, entidades de fiscalización ambiental y laboratorios de ensayo.</td>
    </tr>
    <tr>
      <td>Estrategias de marketing</td>
      <td><strong>Venta consultiva mediante diagnóstico:</strong> piloto gratuito que mide las salas del propio prospecto y entrega un informe con sus condiciones reales, convirtiendo la promesa comercial en evidencia. Presencia en asociaciones del sector inmobiliario corporativo.</td>
      <td>Marketing digital B2B, red de distribuidores e integración con plataformas de gestión de edificios.</td>
      <td><em>Account-Based Marketing</em> dirigido a arquitectos y gestores de infraestructura, para incorporar sus sensores desde la fase de diseño del proyecto.</td>
      <td>Venta especializada a través de distribuidores técnicos y presencia en el ámbito académico y profesional de la acústica.</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>Perfil de Producto</strong></td>
      <td>Productos &amp; Servicios</td>
      <td><strong>Hardware:</strong> módulo IoT por sala basado en ESP32, con micrófono MEMS y sensor de temperatura y humedad. <br><strong>Edge:</strong> servicio local que agrega por minuto, evalúa alertas y encola los datos ante la ausencia de conexión. <br><strong>Cloud:</strong> API con analítica de tendencias y correlaciones. <br><strong>Software:</strong> aplicación web adaptable, aplicación móvil de alertas y landing page.</td>
      <td><strong>Hardware:</strong> sensores de calidad del aire para interiores. <br><strong>Software:</strong> panel en la nube, API e integraciones con sistemas de gestión de edificios.</td>
      <td><strong>Hardware:</strong> sensores modulares calibrables. <br><strong>Software:</strong> panel de nivel industrial con reportes de cumplimiento. <br><strong>Servicio:</strong> consultoría para la obtención de certificaciones.</td>
      <td><strong>Hardware:</strong> sonómetros de clase 1 y clase 2, y calibradores acústicos. <br><strong>Software:</strong> herramientas de análisis de escritorio.</td>
    </tr>
    <tr>
      <td>Precios &amp; Costos</td>
      <td><strong>Modelo híbrido:</strong> venta del hardware a costo accesible por su base en ESP32, más suscripción mensual según el número de salas instrumentadas. El precio por sala se dimensiona por debajo del ingreso de unas pocas horas de reserva.</td>
      <td>Suscripción anual por dispositivo, con un costo de hardware por unidad que dificulta instrumentar todas las salas de un local.</td>
      <td>Presupuesto por proyecto para edificios completos, con planes de reemplazo periódico de los módulos de sensores.</td>
      <td>Compra del instrumento con costo elevado por unidad, más calibración periódica obligatoria.</td>
    </tr>
    <tr>
      <td>Canales de distribución (Web y/o Móvil)</td>
      <td><strong>Web:</strong> panel de gestión para el operador y el personal de recepción. <br><strong>Móvil:</strong> aplicación de atención de alertas mientras se recorre el local. <br><strong>Landing page:</strong> propuesta de valor para operadores que aún no son clientes.</td>
      <td><strong>Web:</strong> panel corporativo. <br><strong>Móvil:</strong> aplicación de consulta.</td>
      <td><strong>Web:</strong> panel empresarial compatible con protocolos industriales. <br><strong>API</strong> de integración.</td>
      <td><strong>Software de escritorio.</strong> El instrumento opera de forma autónoma.</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>Análisis SWOT</strong></td>
      <td>Fortalezas</td>
      <td>Aplicación de normas internacionales de confort, no de valores crudos. Cobertura simultánea de la dimensión acústica y la térmica. Operación garantizada sin conexión a internet. Privacidad verificable por diseño. Costo compatible con la instrumentación completa del local. Conocimiento del contexto operativo del coworking limeño.</td>
      <td>Marca consolidada con base instalada global. Amplitud de variables medidas. Es el único competidor que aborda simultáneamente aire y ruido. Enfoque de privacidad ya resuelto en el dispositivo. Instalación sin técnico especializado.</td>
      <td>Único que garantiza puntajes para certificaciones internacionales. Diseño modular que facilita el mantenimiento en grandes infraestructuras.</td>
      <td>Exactitud metrológica certificada. Validez legal de la medición.</td>
    </tr>
    <tr>
      <td>Debilidades</td>
      <td>Marca nueva, sin trayectoria comercial ni base instalada. Hardware sin certificación metrológica. Recursos de investigación y desarrollo limitados frente a competidores globales.</td>
      <td>Tratamiento acústico superficial: reporta el promedio en dBA sin percentiles ISO 1996, por lo que no distingue ruido de fondo de picos intrusivos. No calcula confort térmico normalizado (PMV/PPD). Orientado a grandes corporaciones, con costo por dispositivo elevado para instrumentar sala por sala. Dependencia de conexión permanente a internet.</td>
      <td>No incorpora la dimensión acústica en ninguno de sus modelos. No calcula confort térmico normalizado. Orientado al edificio como unidad y no a la gestión sala por sala. Complejidad y costo excesivos para un operador mediano.</td>
      <td>Medición puntual y no continua. Requiere operador presente. No genera registro histórico ni alertas. Costo prohibitivo para instrumentación permanente.</td>
    </tr>
    <tr>
      <td>Oportunidades</td>
      <td>Crecimiento sostenido del trabajo híbrido y de la demanda de espacios flexibles. Ausencia de una solución especializada en confort acústico para coworkings en el mercado peruano. Posibilidad de convertir la evidencia ambiental en argumento comercial del propio operador.</td>
      <td>Profundizar su tratamiento acústico incorporando percentiles normalizados, dado que ya cuenta con el hardware necesario. Expansión hacia mercados emergentes.</td>
      <td>Incorporación de indicadores de confort térmico normalizados a su oferta actual.</td>
      <td>Integración de sus instrumentos con plataformas de monitoreo continuo.</td>
    </tr>
    <tr>
      <td>Amenazas</td>
      <td>Entrada de un competidor establecido al segmento de espacios de trabajo compartidos. Comercialización de sensores genéricos de bajo costo percibidos como suficientes. Consideración de la medición ambiental como un gasto prescindible por parte del operador.</td>
      <td>Aparición de competidores de menor costo en el monitoreo de calidad del aire.</td>
      <td>Desarrollo de capacidades equivalentes por parte de los fabricantes de sistemas de climatización.</td>
      <td>Sustitución progresiva por redes de sensores continuos de menor costo.</td>
    </tr>
  </tbody>
</table>

*Nota.* Elaboración propia a partir de los sitios oficiales de cada competidor, consultados el 2 de septiembre de 2026 (Airthings, 2026a, 2026b; Kaiterra, 2026). Airthings y Kaiterra no publican sus precios y los gestionan mediante contacto comercial directo, de modo que las cifras corresponden a órdenes de magnitud obtenidos a partir de fuentes secundarias.


<a id="212-estrategias-y-tácticas-frente-a-competidores"></a>
### 2.1.2. Estrategias y tácticas frente a competidores.

Para afrontar de manera estratégica el panorama competitivo en Lima Metropolitana, SenseWork implementará una serie de tácticas ofensivas y defensivas orientadas a capitalizar las brechas de servicio de los actores globales y a mitigar las amenazas del mercado local.

**1. Profundidad acústica frente a amplitud de variables**

La verificación de los sitios oficiales muestra que Airthings **sí mide nivel sonoro**, por lo que la diferenciación no puede sustentarse en medir algo que el competidor no mide. La brecha real es de **profundidad en el tratamiento del dato**: Airthings reporta el promedio en dBA a lo largo del tiempo, mientras que Kaiterra no aborda la acústica en absoluto.

Nuestra estrategia consiste en aplicar las normas de confort —ISO 1996 e ISO 7730— sobre las mismas magnitudes físicas que el competidor ya captura, evitando la dispersión hacia el monitoreo de contaminantes donde ellos están consolidados.

*Táctica:* incorporar al panel los percentiles estadísticos L10, L50 y L90. Un promedio en dBA no distingue una sala con ruido de fondo permanente de otra con picos intrusivos aislados, aunque ambas registren el mismo promedio; sin embargo, la intervención correctiva es distinta en cada caso —aislamiento acústico en el primero, gestión de la actividad adyacente en el segundo—. Esa distinción es la que convierte el dato en una decisión.

*Táctica:* expresar el confort térmico como PPD, el porcentaje de personas que estaría insatisfecha, en lugar de reportar temperatura y humedad como valores independientes. Ningún competidor traduce ambas variables a un índice normalizado interpretable.

**2. Sustitución de la confianza en la marca por evidencia del propio local**

Como producto nuevo, SenseWork no puede apoyarse en referencias de clientes previos frente a marcas consolidadas como Airthings o Kaiterra.

*Táctica:* ofrecer un piloto gratuito de dos semanas instrumentando dos o tres salas del prospecto, cuyo resultado es un informe con las condiciones reales medidas en su establecimiento. El argumento comercial deja de ser una promesa y se convierte en un diagnóstico.

*Táctica:* documentar públicamente el método de cálculo y las normas aplicadas —ISO 1996 e ISO 7730—, de modo que la validez del indicador pueda verificarse con independencia de la reputación del proveedor.

**3. Delimitación del alcance frente a los instrumentos certificados**

Los sonómetros profesionales cuentan con certificación IEC 61672, de la que carece un módulo basado en ESP32. Competir en exactitud metrológica supondría una desventaja estructural.

*Táctica:* posicionar el producto de forma inequívoca como herramienta de gestión operativa y no de peritaje legal, delimitando explícitamente su alcance en la comunicación comercial.

*Táctica:* documentar el procedimiento de calibración del sensor contra un sonómetro de referencia y publicar el margen de error esperado, aportando trazabilidad sin pretender certificación.

**4. Construcción de ventaja en la operación sin conectividad**

Airthings o Kaiterra podrían incorporar indicadores de confort acústico normalizado a su oferta actual. La ventaja defendible se encuentra en una capa que un competidor global no replica con facilidad.

*Táctica:* consolidar la evaluación de alertas en la capa Edge como diferenciador central. En locales con infraestructura de red poco confiable, un sistema que deja de alertar cuando cae el enlace no resuelve el problema que dice atender.

*Táctica:* priorizar la profundidad de la integración con la operación diaria del coworking —asignación de salas y gestión de reservas— frente a la amplitud de variables medidas.

**5. Traducción del valor al lenguaje del negocio del operador**

El operador puede considerar que el problema no justifica una inversión recurrente.

*Táctica:* expresar el valor del producto en términos de reservas no renovadas y salas infrautilizadas, y no en términos técnicos de precisión de medición.

*Táctica:* dimensionar el precio por sala de modo que se mantenga por debajo del ingreso de unas pocas horas de reserva, situando la decisión en un umbral que no requiere aprobación presupuestaria formal.

**6. Anticipación de la objeción de privacidad**

La instalación de un micrófono en una sala ocupada genera resistencia inmediata, tanto en el operador como en sus clientes. Conviene señalar que Airthings ya resolvió esta objeción con un enfoque equivalente —procesamiento en el dispositivo y descarte del audio—, lo que confirma que es el estándar esperado del sector y no un diferenciador exclusivo.

*Táctica:* abordar la objeción en la primera conversación comercial, explicando que el audio se procesa en el propio dispositivo y que únicamente se transmite un valor numérico agregado, convirtiendo la restricción técnica en un argumento de confianza.

*Táctica:* documentar públicamente el diseño del pipeline acústico —de la muestra al indicador— de modo que la garantía de privacidad sea verificable y no una simple declaración comercial.

*Táctica:* habilitar la publicación del indicador de confort por sala en los canales de reserva del operador, de modo que la medición se transforme en un elemento de transparencia hacia el usuario final y no en un mecanismo de vigilancia.


<a id="22-entrevistas"></a>
## 2.2. Entrevistas.

La investigación se apoya en entrevistas a representantes de ambos segmentos objetivo, orientadas a recoger hechos verificables sobre su operación cotidiana antes que opiniones sobre la solución.

Las entrevistas se diseñaron siguiendo un enfoque **semiestructurado**: un guion base garantiza la comparabilidad entre sesiones, mientras que las preguntas de profundización permiten explorar los temas que cada participante identifique como relevantes. El principio rector del diseño es **preguntar por hechos y no por opiniones**: se indaga sobre lo que el participante hizo la última vez que enfrentó el problema, en lugar de pedirle que valore una solución hipotética. Las preguntas sobre el producto se reservan para el final de la sesión, de modo que no condicionen las respuestas previas.

| Aspecto | Definición |
| :---- | :---- |
| Modalidad | Presencial en el local del participante o videollamada, según su disponibilidad |
| Duración | Entre 20 y 30 minutos por sesión |
| Registro | Grabación de audio y video, previo consentimiento explícito del participante |
| Cantidad mínima | 3 entrevistas por segmento objetivo |
| Herramienta de registro | Microsoft Stream o Clipchamp |


<a id="221-diseño-de-entrevistas"></a>
### 2.2.1. Diseño de entrevistas.

| Segmento Objetivo #1: | Miembros y Usuarios del Coworking |
| :---- | :---- |
| **Datos Demográficos** | ¿Cuál es su nombre completo y edad?<br/>¿Cuál es su ocupación?<br/>¿En qué distrito suele trabajar? |
| **Ocupación y Background** | ¿Con qué frecuencia utiliza espacios de trabajo compartidos?<br/>¿Para qué tipo de actividad reserva una sala: concentración, reuniones, videollamadas?<br/>¿Suele volver al mismo espacio o los alterna? |
| **Perfil Psicográfico** | ¿Qué valora más al elegir un espacio de trabajo: el precio, la ubicación o las condiciones del ambiente?<br/>¿Qué tan dispuesto está a pagar más por un espacio que le garantice mejores condiciones de trabajo? |
| **Confort acústico** | Cuénteme sobre la última vez que trabajó en una sala y la experiencia no resultó como esperaba. ¿Qué ocurrió?<br/>¿Le ha sucedido que el ruido le impidiera concentrarse o dificultara una videollamada? ¿Qué hizo en ese momento?<br/>¿Ha tenido que elevar la voz o repetir lo dicho durante una llamada por el ruido de la sala?<br/>¿Ha abandonado una sala antes de tiempo por este motivo? |
| **Confort térmico** | ¿Le ha resultado alguna sala incómoda por temperatura? ¿Cómo lo resolvió?<br/>¿Ha tenido que abrigarse o quitarse ropa dentro de una sala para poder trabajar? |
| **Comportamiento ante el problema** | Cuando ocurre algo así, ¿lo comunica al personal del espacio? Si no lo hace, ¿por qué?<br/>¿Ha dejado de usar algún espacio por este motivo? ¿Llegó a explicarles la razón? |
| **Criterios de decisión** | Al reservar una sala, ¿qué información consulta previamente?<br/>¿Qué información sobre una sala le gustaría conocer antes de reservarla?<br/>¿Ha usado alguna aplicación para medir ruido o temperatura? ¿Con qué resultado? |
| **Tecnología y Canales** | ¿Esta información influiría en su elección de sala? ¿De qué manera?<br/>¿Cómo preferiría verla expresada: en decibelios, en una escala de colores o de otra forma?<br/>¿Desde qué dispositivo consultaría esta información al momento de reservar? |
| **Privacidad** | ¿Le generaría alguna inquietud saber que hay un sensor de sonido en la sala donde trabaja?<br/>¿Cambiaría su percepción saber que el dispositivo no graba audio y solo mide el nivel de ruido? |

| Segmento Objetivo #2: | Administradores y Gestores de Espacios de Coworking |
| :---- | :---- |
| **Datos Demográficos** | ¿Cuál es su nombre completo y edad?<br/>¿En qué distrito se ubica su establecimiento?<br/>¿Cuál es su cargo actual? |
| **Ocupación y Background** | ¿Cuántas salas administra y qué tipo de clientes las utilizan?<br/>¿Cuántas personas frecuentan el local en un día típico?<br/>¿Cuánto tiempo lleva administrando este tipo de espacio? |
| **Perfil Psicográfico** | ¿Cómo toma decisiones cuando detecta un problema que afecta la experiencia de sus clientes?<br/>¿Qué herramientas digitales usa actualmente para gestionar el local y las reservas?<br/>¿Qué tan abierto se considera a adoptar nueva tecnología si resuelve un problema concreto? |
| **Confort acústico** | ¿Cuáles son las quejas más frecuentes que recibe sobre las salas?<br/>Cuénteme sobre la última vez que un cliente le manifestó una molestia por ruido. ¿Qué ocurrió y qué hizo usted?<br/>Si tuviera que señalar ahora mismo cuál es la sala más ruidosa de su local, ¿podría hacerlo? ¿En qué se basaría?<br/>¿Hay alguna sala que se reserve menos que las demás? ¿A qué lo atribuye?<br/>¿Sabía que en una sala de reuniones el ruido de fondo permanente y los picos aislados de voz requieren intervenciones distintas? |
| **Confort térmico** | ¿Cómo decide cuándo ajustar el aire acondicionado de una sala?<br/>¿Ha recibido quejas sobre sensación de frío, calor o aire viciado dentro de las salas?<br/>¿Cómo sabría hoy si la temperatura de una sala es adecuada para quienes la ocupan, más allá de lo que marca el termostato? |
| **Prácticas actuales de medición** | ¿Mide actualmente alguna condición ambiental de sus salas? ¿De qué manera?<br/>¿Ha realizado alguna inversión en acondicionamiento acústico o climatización? ¿Cómo decidió dónde intervenir?<br/>¿Qué información le habría resultado útil para tomar esa decisión?<br/>¿Ha tenido clientes que dejaron de renovar? ¿Llegó a conocer el motivo? |
| **Objetivos y Frustraciones** | ¿Qué tan importante considera el confort de las salas para la reputación de su negocio?<br/>¿Existe algún aspecto del ambiente interior que sienta que no puede controlar ni medir actualmente?<br/>¿Le resultaría útil poder demostrar a un cliente que una sala cumple condiciones adecuadas de trabajo? |
| **Tecnología y Canales** | ¿Qué dispositivos usa a diario para gestionar el local?<br/>¿Usaría una aplicación que le muestre en tiempo real el estado acústico y térmico de cada sala y le envíe alertas?<br/>¿Le resultaría útil generar reportes históricos por sala para sustentar decisiones de inversión?<br/>Si el sistema le avisara ahora que una sala presenta ruido elevado de forma sostenida, ¿qué haría usted? |
| **Privacidad** | ¿Qué preocupación le genera instalar un sensor de sonido en una sala ocupada por clientes?<br/>¿Cambiaría su percepción saber que el audio se procesa dentro del dispositivo y que solo se transmite un valor numérico, sin grabar conversaciones? |
| **Comportamiento de Decisión** | ¿Qué lo lleva a invertir en una mejora para el local?<br/>¿Quién más participa en las decisiones de equipamiento o tecnología?<br/>¿Qué tendría que costar mensualmente para que la decisión de contratarlo no requiera una aprobación mayor?<br/>¿Recomendaría a otros operadores una solución que le haya dado resultados concretos? |

<a id="222-registro-de-entrevistas"></a>
### 2.2.2. Registro de entrevistas.

**<ins>Segmento #1: Miembros y Usuarios del Coworking</ins>**

**Entrevista #1**

| Campo | Contenido                                                                                                  |
| :---- |:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos | Mathias Bueno                                                                                              |
| Edad | 20 años                                                                                                    |
| Cargo | Practicante de Product Manager                                                                             |
| Distrito | Miraflores / San Isidro                                                                                    |
| Fecha | 13/09/2026                                                                                                 |
| Duración | 08:03                                                                                                      |
| Captura de la sesión | <img src="./assets/entrevistas-needfinding/entrevista1-seg1.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |
| Inicio                 | 0:09                                                                                                       |
| Fin                    | 08:11                                                                                                      |

*Resumen:* Mathias es un practicante de Product Manager de 20 años que trabaja en modalidad remota y acude a espacios de coworking entre 3 y 4 veces por semana. Reserva salas principalmente para videollamadas importantes y demostraciones con clientes internacionales, priorizando el silencio y el confort ambiental al punto de estar dispuesto a pagar entre un 10% y 15% más por condiciones garantizadas. Ha experimentado problemas recurrentes de aislamiento acústico y mal control de temperatura (salas sin ventilación o aire acondicionado excesivo), llegando incluso a abandonar sesiones antes de tiempo. Aunque rara vez reclama en recepción por considerarlo ineficaz, manifiesta gran interés en consultar desde su celular el estado de ruido y temperatura en tiempo real antes de reservar, prefiriendo un indicador visual tipo semáforo. Respecto a los sensores IoT, aprueba su uso siempre que se garantice que solo monitorean niveles de ruido ambiental y no graban conversaciones.

**Entrevista #2**

| Campo                  | Contenido                                                                                                  |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos     | Daniela Gómez                                                                                              |
| Edad                   | 22                                                                                                         |
| Cargo                  | Diseñadora UX/UI freelance                                                                                 |
| Distrito               | Miraflores / Barranco                                                                                      |
| Fecha                  | 14/09/2026                                                                                                 |
| Captura de la sesión   | <img src="./assets/entrevistas-needfinding/entrevista2-seg1.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |
| Inicio                 | 08:12                                                                                                      |
| Fin                    | 17:47                                                                                                      |

*Resumen:* Daniela es una diseñadora UX/UI freelance de 22 años que trabaja de forma remota y utiliza espacios de coworking entre 3 y 4 veces por semana, principalmente para videollamadas con clientes y sesiones de concentración, priorizando el silencio y el confort térmico por encima del precio o la ubicación. Ha experimentado problemas recurrentes de ruido y temperatura, llegando a tener dificultades durante reuniones, sentirse incómoda e incluso abandonar una sala antes de terminar su reserva. Aunque rara vez reclama al personal porque considera que perdería tiempo, sí ha dejado de utilizar espacios con estas deficiencias. Le interesaría conocer desde su celular los niveles de ruido y temperatura en tiempo real antes de reservar, prefiriendo una escala visual tipo semáforo, y estaría dispuesta a pagar más por condiciones garantizadas. Respecto a los sensores IoT, aceptaría su uso siempre que se garantice que solo monitorean el nivel de ruido y no graban conversaciones.

**Entrevista #3**

| Campo                  | Contenido                                                                                                  |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos     | Franklin Segovia                                                                                           |
| Edad                   | 25                                                                                                         |
| Cargo                  | Desarrollador de software                                                                                  |
| Distrito               | Miraflores / San Isidro                                                                                    |
| Fecha                  | 18/09/2026                                                                                                 |
| Captura de la sesión   | <img src="./assets/entrevistas-needfinding/entrevista3-seg1.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |
| Inicio                 | 17:48                                                                                                      |
| Fin                    | 24:17                                                                                                      |

**Resumen:** Franklin Segovia es un desarrollador de software de 25 años que trabaja de forma híbrida y utiliza espacios de coworking aproximadamente tres veces por semana, principalmente para videollamadas, reuniones y actividades que requieren concentración, priorizando el silencio y el confort térmico. Ha experimentado problemas relacionados con el ruido y la temperatura que han afectado su concentración y sus reuniones, llegando incluso a retirarse de una sala antes de terminar su reserva. Aunque en algunas ocasiones comunica estos inconvenientes al personal, otras veces prefiere no hacerlo para evitar perder tiempo, y ha dejado de utilizar espacios que presentan estas deficiencias. Le interesaría conocer desde su celular los niveles de ruido y temperatura en tiempo real antes de reservar, prefiriendo una escala visual tipo semáforo para comparar rápidamente las salas. También estaría dispuesto a pagar un poco más por mejores condiciones de trabajo. Respecto a los sensores IoT, considera importante la privacidad y aceptaría su uso siempre que se garantice que solo miden el nivel de ruido y no graban ni almacenan conversaciones.


**<ins>Segmento #2: Administradores y Gestores de Coworking</ins>**

**Entrevista #4**

| Campo | Contenido                                                                                                  |
| :---- |:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos | Jaime Correa                                                                                               |
| Edad | 28                                                                                                         |
| Ocupación | Administrador de coworking                                                                                 |
| Distrito | San Isidro                                                                                                 |
| Fecha | 20/09/2026                                                                                                 |
| Captura de la sesión | <img src="./assets/entrevistas-needfinding/entrevista4-seg2.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |
| Inicio                 | 24:21                                                                                                      |
| Fin                    | 40:52                                                                                                      |

*Resumen:* Jaime Correa, ingeniero industrial de 28 años y administrador de una sede de coworking en San Isidro, gestiona alrededor de diez salas utilizadas por profesionales, trabajadores híbridos y equipos empresariales. Durante la entrevista señaló que los principales problemas que enfrenta son el ruido y las variaciones de temperatura, los cuales actualmente se atienden de forma reactiva a partir de quejas de los clientes o de la percepción del personal, sin contar con mediciones objetivas ni registros históricos. También indicó que sería útil disponer de información en tiempo real para identificar qué salas presentan problemas, recibir alertas antes de que los usuarios se quejen y analizar datos históricos para sustentar inversiones en aislamiento acústico o climatización. Mostró una actitud favorable hacia una solución IoT como SenseWork, especialmente por su capacidad de centralizar el monitoreo acústico y térmico, siempre que se garantice la privacidad de los usuarios y que los sensores no graben ni almacenen conversaciones.

**Entrevista #5**

| Campo | Contenido                                                                                                  |
| :---- |:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos | Ayrton Briceño                                                                                             |
| Edad | 41                                                                                                         |
| Ocupación | Administrador de sede de coworking                                                                         |
| Distrito | San Isidro                                                                                                 |
| Fecha | 19/09/2026                                                                                                 |
| Captura de la sesión | <img src="./assets/entrevistas-needfinding/entrevista5-seg2.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |         
| Inicio                 | 40:53                                                                                                      |
| Fin                    | 48:59                                                                                                      |

*Resumen:* Ayrton es un administrador de sede de 41 años que gestiona doce salas (cabinas, salas de reuniones y áreas abiertas) con unas ochenta personas por día. Reconoce el ruido como la queja más frecuente y el frío o calor como la segunda, pero no dispone de ningún dato objetivo: identifica la sala más ruidosa por impresión propia y ajusta el aire acondicionado por sensación. Ante la última queja por ruido ofreció cambiar de sala al cliente y no intervino la sala, al atribuirla a un evento puntual. Invirtió unos siete mil soles en paneles acústicos en la sala más reclamada, sin poder verificar el resultado ni saber si era la más ruidosa o solo la más usada. Una cabina se reserva muy poco y nunca investigó la causa. Desconoce el motivo de la mayoría de las bajas de clientes. Probó una aplicación de decibeles que se abandonó por no tener referencia interpretativa. Usaría el sistema desde el celular para atender alertas y desde la computadora para reportes, y decidiría por su cuenta un costo cercano a 100 soles mensuales. Su principal preocupación es la privacidad: pediría garantía escrita de que no se graba audio. Exige instalación sencilla, sin obra ni técnico.

**Entrevista #6**

| Campo | Contenido                                                                                                  |
| :---- |:-----------------------------------------------------------------------------------------------------------|
| Nombre y apellidos | Fiorella Grisel Cordova Pinchi                                                                             |
| Edad | 29                                                                                                         |
| Ocupación | Coordinadora administrativa; evalúa la apertura de un espacio de oficinas compartidas                      |
| Distrito | Pueblo Libre                                                                                               |
| Fecha | 16/09/2026                                                                                                 |
| Captura de la sesión | <img src="./assets/entrevistas-needfinding/entrevista6-seg2.png" alt="Captura de la sesión" width="250" /> |
| Enlace de la grabación | [https://bit.ly/4yOxHbD](https://bit.ly/4yOxHbD)                                                           |
| Inicio                 | 49:00                                                                                                       |
| Fin                    | 56:31                                                                                                      |

*Resumen:* Fiorella es una coordinadora administrativa de 29 años que evalúa junto a su hermano convertir una casa familiar en oficinas y dos salas de alquiler por horas, con una remodelación cotizada entre 40 y 45 mil soles. Visitó cinco locales haciéndose pasar por clienta y halló precios equivalentes pero experiencias dispares: descartó uno por la transferencia de ruido entre salas contiguas, que el personal atribuyó a una reunión puntual. Admite que no reclama cuando algo no le gusta y que un operador habituado al local deja de percibir el problema, de modo que no espera enterarse por sus clientes. Descartó una aplicación de medición sonora porque el valor numérico carecía de referencia interpretativa y reclama un indicador tipo semáforo. Prioriza el diagnóstico durante la obra sobre el monitoreo posterior, pues permite dirigir la partida de aislamiento de 6 mil soles. Asumiría hasta 60 soles mensuales y exige una garantía escrita de no grabación, verificable por el cliente.


<a id="223-análisis-de-entrevistas"></a>
### 2.2.3. Análisis de entrevistas.

El análisis se realiza por segmento objetivo sobre la evidencia recogida en las seis entrevistas registradas (2.2.2), tres por segmento. Para cada segmento se identifican las características objetivas hechos verificables sobre demografía, operación y comportamiento y subjetivas percepciones, valoraciones y disposiciones que se repiten con mayor prevalencia, expresada esta como porcentaje de entrevistas del segmento que la evidencian.

**Segmento #1: Miembros y Usuarios del Coworking** *(E1: Mathias, E2: Daniela, E3: Franklin)*

*Características objetivas*

| Característica | Evidencia en entrevistas | Prevalencia |
| :---- | :---- | :----: |
| Jóvenes profesionales del sector digital, entre 20 y 25 años (promedio de 22) | E1 (20, practicante de Product Manager), E2 (22, diseñadora UX/UI), E3 (25, desarrollador de software) | 100 % |
| Trabaja en modalidad remota o híbrida | E1 y E2 en modalidad remota, E3 en modalidad híbrida | 100 % |
| Frequencia de uso intensiva del coworking: entre 3 y 4 veces por semana | E1, E2 y E3 | 100 % |
| Reserva salas principalmente para videollamadas y tareas de concentración | E1 (videollamadas con clientes internacionales y demos), E2 (videollamadas con clientes), E3 (videollamadas, reuniones y concentración) | 100 % |
| Trabaja en distritos corporativos de Lima Metropolitana | E1 y E3 (Miraflores / San Isidro), E2 (Miraflores / Barranco) | 100 % |
| Ha abandonado una sala antes de terminar su reserva por condiciones ambientales | E1, E2 y E3 | 100 % |
| Ha dejado de utilizar espacios de coworking por estas deficiencias | E2 y E3 | 67 % |

*Características subjetivas*

| Característica | Evidencia en entrevistas | Prevalencia |
| :---- | :---- | :----: |
| Prioriza el silencio y el confort térmico por encima del precio y la ubicación | E1, E2 y E3 | 100 % |
| Está dispuesto a pagar más por condiciones ambientales garantizadas | E1 (entre 10 % y 15 % más), E2 y E3 | 100 % |
| Prefiere consultar en tiempo real, desde el celular, el estado de la sala antes de reservar | E1, E2 y E3 | 100 % |
| Prefiere un indicador visual tipo semáforo antes que métricas numéricas | E1, E2 y E3 | 100 % |
| Rara vez formaliza la queja al personal del espacio | E1 (la considera ineficaz), E2 (perdería tiempo), E3 (solo algunas veces, para no perder tiempo) | 100 % |
| Acepta el uso de sensores IoT siempre que no graben ni almacenen conversaciones | E1, E2 y E3 | 100 % |

Los tres miembros coinciden en un patrón que ninguna solución actual atiende: sufren el problema ambiental después de haber reservado y pagado, y su única salida es abandonar la sala o dejar de volver, sin que la queja llegue a formalizarse. El arquetipo del Segmento 1 (Camila Rivas, 2.3.1) se construye sobre este patrón: una profesional digital de alta frecuencia de uso cuya elección de sala se decide por condiciones que hoy no puede verificar.

**Segmento #2: Administradores y Gestores de Coworking** *(E4: Jaime, E5: Ayrton, E6: Fiorella)*

*Características objetivas*

| Característica | Evidencia en entrevistas | Prevalencia |
| :---- | :---- | :----: |
| Adultos jóvenes entre 28 y 41 años (promedio de 33) | E4 (28), E5 (41), E6 (29) | 100 % |
| Responsables de la operación de un espacio de coworking en Lima Metropolitana | E4 y E5 (administradores en operación, San Isidro), E6 (coordinadora que evalúa la apertura, Pueblo Libre) | 100 % |
| Gestionan entre 2 y 12 salas de distintos tipos (cabinas, salas de reuniones, áreas abiertas) | E4 (≈10 salas), E5 (12 salas, ≈80 personas por día), E6 (2 salas proyectadas) | 100 % |
| No disponen de mediciones objetivas ni registros históricos de las condiciones ambientales | E4, E5 y E6 | 100 % |
| Han realizado o proyectado inversiones de acondicionamiento sin poder verificar su resultado | E5 (S/ 7 000 en paneles acústicos), E6 (partida de S/ 6 000 en aislamiento durante obra) | 67 % |
| Intentaron medir con aplicaciones de ruido y las abandonaron por falta de referencia interpretativa | E5 y E6 | 67 % |

*Características subjetivas*

| Característica | Evidencia en entrevistas | Prevalencia |
| :---- | :---- | :----: |
| Reconoce el ruido como el principal problema del negocio y la temperatura como el segundo | E4 (ambos como problemas principales), E5 (ruido como queja más frecuente, temperatura segunda), E6 (descartó un local por transferencia de ruido entre salas) | 100 % |
| Atiende los problemas de forma reactiva, a partir de quejas o de la percepción propia | E4 (quejas del cliente o percepción del personal), E5 (impresión propia para la sala más ruidosa, sensación para el aire acondicionado) | 67 % |
| Percibe que el operador habituado al local deja de notar el problema y no puede esperar que el cliente lo reporte | E6 (no reclama cuando algo no le gusta; el personal se habitúa) | 33 % |
| Decidiría la contratación de forma autónoma en un rango de S/ 60 a S/ 100 mensuales por sala | E5 (≈S/ 100), E6 (hasta S/ 60) | 67 % |
| Exige garantía escrita y verificable de que el sensor no graba conversaciones | E4 (garantía de privacidad), E5 (garantía escrita), E6 (garantía escrita verificable por el cliente) | 100 % |
| Usaría la solución desde el celular para alertas y desde la computadora para reportes e inversiones | E5 (celular para alertas, computadora para reportes), E4 (alertas anticipadas y datos históricos para sustentar inversiones) | 67 % |

Los tres administradores comparten la condición que define al segmento: toman decisiones de alto impacto dónde invertir, cómo asignar salas, cómo responder a un cliente sin ningún dato objetivo que las sustente. El arquetipo del Segmento 2 (Martín Salazar, 2.3.1) recoge este perfil: un operador que gestiona la experiencia de sus clientes a partir de quejas tardías e impresiones, y cuya disposición de adopción queda condicionada a un precio dentro del gasto operativo discrecional y a una garantía de privacidad verificable.

**Síntesis**

El contraste entre ambos segmentos confirma la asimetría que ordena el Needfinding (2.3): el miembro padece una condición que no puede consultar antes de reservar, y el administrador opera un espacio cuya condición no puede medir. La preferencia compartida por un indicador visual tipo semáforo manifestada de forma independiente por los tres miembros (E1–E3) y reforzada por el abandono de aplicaciones numéricas en el segmento opuesto (E5, E6) valida la Feature Assumption del semáforo (1.2.2.2) y la estrategia de traducir las magnitudes físicas a índices interpretables (2.1.2). Asimismo, el rango de precio declarado por los administradores (S/ 60–100 mensuales) es coherente con la táctica de fijar el precio por sala por debajo del ingreso de unas pocas horas de reserva (2.1.2), y la exigencia de garantías escritas de no grabación (E4–E6) ajusta la suposición de privacidad: el procesamiento del audio en el dispositivo es condición necesaria, pero la garantía debe además ser verificable por el cliente.


<a id="23-needfinding"></a>
## 2.3. Needfinding.

Dos necesidades no atendidas ordenan el análisis: el administrador no puede identificar objetivamente qué sala presenta problemas, y el miembro no dispone de información sobre las condiciones de la sala antes de reservarla.


<a id="231-user-personas"></a>
### 2.3.1. User Personas.

Cada segmento se representa mediante un arquetipo que reúne sus características recurrentes: del análisis competitivo provienen las expectativas que los productos existentes ya instalaron en el mercado; de las entrevistas, los comportamientos y frustraciones que ninguna solución atiende hoy.

<p align="center"><em>Figura 2.</em> User Persona del Segmento 1 — Camila Rivas, miembro del coworking.</p>

<p align="center">
  <img src="assets/user-persona/persona-camila-rivas.png" alt="User Persona: Camila Rivas — Miembro del coworking" width="720">
</p>

<p align="center"><em>Figura 3.</em> User Persona del Segmento 2 — Martín Salazar, administrador de sede de coworking.</p>

<p align="center">
  <img src="assets/user-persona/persona-martin-salazar.png" alt="User Persona: Martín Salazar — Administrador de sede" width="720">
</p>

Ambos arquetipos comparten el mismo entorno pero lo habitan desde posiciones opuestas: Camila padece una condición ambiental que no eligió y Martín administra un espacio cuya condición no puede medir. Esa asimetría define el alcance de la solución.

*Nota.* Elaboración propia.


<a id="232-user-task-matrix"></a>
### 2.3.2. User Task Matrix.

La User Task Matrix concentra las tareas que **miembros** y **administradores** ejecutan hoy para cumplir sus objetivos, con independencia de la plataforma.

| Tarea | Miembro/Usuario del coworking |  | Administrador/Gestor |  |
| :---- | :----: | :----: | :----: | :----: |
|  | **Frecuencia** | **Importancia** | **Frecuencia** | **Importancia** |
| Elegir una sala antes de reservar | Alta | Alta | — | — |
| Verificar las condiciones al ingresar a la sala | Alta | Media | — | — |
| Realizar trabajo de concentración o videollamadas | Alta | Alta | — | — |
| Cambiar de sala durante una sesión por disconfort | Baja | Alta | — | — |
| Reportar una molestia al personal del espacio | Baja | Media | — | — |
| Ajustar la climatización de una sala | Baja | Media | Alta | Media |
| Asignar una sala a un cliente según su actividad | — | — | Alta | Alta |
| Atender una queja sobre las condiciones de una sala | — | — | Media | Alta |
| Supervisar el estado ambiental de todas las salas | — | — | Alta | Alta |
| Identificar qué sala presenta problemas ambientales | — | — | Baja | Alta |
| Configurar los umbrales tolerables por tipo de sala | — | — | Baja | Alta |
| Decidir dónde invertir en acondicionamiento acústico | — | — | Baja | Alta |
| Revisar el histórico de condiciones de una sala | — | — | Baja | Media |

**Análisis de la matriz**

**Coincidencia principal.** Ambos segmentos ejecutan, desde lados opuestos de la relación comercial, una misma tarea de selección con alta frecuencia y alta importancia: el miembro **elige una sala antes de reservar** y el administrador **asigna una sala según la actividad del cliente**. Las dos dependen de un dato que hoy ninguno posee. Esta convergencia sugiere que un mismo indicador puede servir a ambos, y justifica exponerlo tanto en el panel de gestión como en el canal de reserva del miembro.

**Diferencia en el horizonte temporal.** El miembro opera en el **momento presente**: necesita saber si la sala sirve ahora para la llamada que tiene en diez minutos. El administrador opera en **dos horizontes simultáneos**: la supervisión continua de todas las salas —alta frecuencia— y las decisiones esporádicas de inversión en acondicionamiento —baja frecuencia, alta importancia—. Esa asimetría orienta el diseño hacia superficies distintas: una vista inmediata y ligera para el miembro, y para el administrador un panel de supervisión más un módulo de reportes históricos.

**Tareas de baja frecuencia y alta importancia.** Configurar umbrales por tipo de sala, identificar qué sala presenta problemas y decidir dónde invertir son decisiones esporádicas de alto impacto económico que hoy se toman sin evidencia. No requieren una interfaz de consulta continua, sino acceso al histórico acumulado.

**Hallazgo que condiciona el diseño.** La tarea **reportar una molestia al personal** registra baja frecuencia y solo media importancia para el miembro, lo que confirma cuantitativamente lo observado de forma cualitativa: el usuario tiende a no formalizar la queja, sino a no volver. Esperar a que el problema se reporte no es, por tanto, un mecanismo viable de detección, y refuerza la necesidad de una medición continua y automática.

**Tarea compartida con distinto peso.** Ajustar la climatización aparece en ambos segmentos, pero con frecuencias opuestas: alta para el administrador, que controla el sistema, y baja para el miembro, que rara vez tiene acceso a él. Esto indica que la acción correctiva debe dirigirse al administrador, mientras que al miembro le corresponde el canal de reporte.

*Nota.* Elaboración propia.


<a id="233-user-journey-mapping"></a>
### 2.3.3. User Journey Mapping.

Los User Journey Maps se presentan en su versión **As-Is**: el recorrido de cada segmento en la situación actual, antes de la intervención de la plataforma. El end-to-end journey que se ilustra abarca desde la operación normal del local, cuando ninguna condición ha sido detectada, hasta el seguimiento posterior a una intervención correctiva, pasando por la aparición silenciosa del problema y su manifestación tardía como queja o como pérdida de reservas. Cada mapa se vincula con la ficha de User Persona correspondiente, elaborada en la misma herramienta.

<p align="center"><em>Figura 4.</em> Journey Map As-Is del Segmento 2 — Administrador de sede de coworking.</p>

<p align="center">
  <img src="assets/journey-maps/journey-map-as-is-administrador.png" alt="Journey Map As-Is: Administrador de sede de coworking" width="900">
</p>

El recorrido evidencia el problema central que aborda la solución: entre la **aparición del problema** y su **manifestación** transcurre un intervalo durante el cual la condición ya afecta al miembro pero el administrador la desconoce por completo. Cuando finalmente se entera, lo hace a través de una queja tardía y sin detalle, o de una señal indirecta como la caída en las reservas de una sala.

La etapa de **diagnóstico e intervención** concentra las barreras de mayor impacto: sin medición, el administrador inspecciona a mano y ajusta la climatización por percepción, sin saber si su intervención mejora o empeora la condición. La etapa de **seguimiento** cierra el ciclo sin verificación, por lo que el problema tiende a repetirse.

<p align="center"><em>Figura 5.</em> Journey Map As-Is del Segmento 1 — Miembro del coworking.</p>

<p align="center">
  <img src="assets/journey-maps/journey-map-as-is-miembro.png" alt="Journey Map As-Is: Miembro del coworking" width="900">
</p>

En el recorrido del miembro el intervalo crítico se ubica entre la **llegada** y el **post-uso**. Descubre las condiciones de la sala cuando ya la reservó y no puede cambiarla, intenta trabajar en un entorno que no le sirve y, al no reportar la molestia, el operador nunca llega a conocer el motivo por el que esa sala deja de usarse.

Ambos recorridos convergen en el mismo punto ciego: el miembro sabe qué sala le falló pero no lo comunica, y el administrador percibe el efecto —una sala que se reserva menos— sin acceder a la causa. Esa asimetría de información es la que la solución busca cerrar.

*Nota.* Elaboración propia. Ambos recorridos corresponden a la versión **As-Is**: la situación actual, sin la solución implementada.

<a id="234-empathy-mapping"></a>
### 2.3.4. Empathy Mapping.

El equipo situó a cada User Persona en el centro del lienzo y fue completando, por turnos, lo que ese arquetipo dice, ve, hace y escucha en su jornada, junto con lo que necesita lograr y aquello que le duele o le beneficia. Las observaciones provienen del análisis competitivo y de la caracterización del problema, y se contrastarán con las entrevistas una vez completado el trabajo de campo.

<p align="center"><em>Figura 6.</em> Empathy Map del Segmento 1 — Camila Rivas, miembro del coworking.</p>

<p align="center">
  <img src="assets/empathy-maps/empathy-map-camila-rivas.png" alt="Empathy Map: Camila Rivas — Miembro del coworking" width="720">
</p>

<p align="center"><em>Figura 7.</em> Empathy Map del Segmento 2 — Martín Salazar, administrador de sede.</p>

<p align="center">
  <img src="assets/empathy-maps/empathy-map-martin-salazar.png" alt="Empathy Map: Martín Salazar — Administrador de sede" width="720">
</p>

Ambos lienzos convergen en un mismo hallazgo: lo que el miembro siente y lo que el administrador observa describen el mismo problema desde dos lados que hoy no se comunican entre sí.

*Nota.* Elaboración propia.


<a id="24-big-picture-eventstorming"></a>
## 2.4. Big Picture EventStorming.

El modelo recorre el flujo completo del dominio, desde la captura de una medición en el dispositivo instalado en la sala hasta la intervención del administrador sobre las condiciones detectadas.

El modelo se organiza en siete fases, que ordenan la línea temporal de izquierda a derecha:

| Fase | Alcance |
| :---- | :---- |
| 1. Captura en el dispositivo | El módulo IoT muestrea sonido, temperatura y humedad, y consolida las ventanas de medición |
| 2. Procesamiento en el borde | La capa Edge agrega por minuto y calcula los indicadores normalizados |
| 3. Alertas locales | Se evalúan los umbrales y se levantan las alertas sin depender de internet |
| 4. Sincronización con la nube | Los agregados se transmiten y, ante un fallo, quedan encolados |
| 5. Configuración y alta | Registro de locales, salas, dispositivos y umbrales |
| 6. Respuesta del administrador | Reconocimiento de la alerta, acción correctiva y cierre |
| 7. Analítica y participación del miembro | Tendencias, contexto meteorológico y reporte de disconfort |

*Nota.* Elaboración propia.

La notación del board emplea el siguiente código de color: **naranja** para los Domain Events, **azul** para los Commands, **amarillo** para los Actors, **rosa** para los External Systems, **morado** para las Policies, **verde** para los Read Models y **rojo** para los Hot Spots.

**Domain Events identificados**


| # | Domain Event | Descripción |
| :---- | :---- | :---- |
| 1 | `SensorMeasurementCaptured` | El dispositivo captura una muestra de nivel sonoro, temperatura y humedad |
| 2 | `AcousticWindowProcessed` | El dispositivo consolida las ventanas de muestreo en un nivel equivalente por segundo |
| 3 | `MeasurementBatchSent` | El dispositivo transmite un lote de mediciones agregadas a la capa Edge |
| 4 | `MeasurementBatchReceived` | La capa Edge recibe y valida el lote procedente del dispositivo |
| 5 | `MinuteAggregated` | La capa Edge consolida las mediciones del minuto para una sala |
| 6 | `AcousticIndicatorsCalculated` | Se calculan el nivel equivalente y los percentiles L10, L50 y L90 conforme a ISO 1996 |
| 7 | `ThermalComfortCalculated` | Se calculan los índices PMV y PPD conforme a ISO 7730 |
| 8 | `ThresholdExceeded` | Un indicador supera el umbral configurado para la sala |
| 9 | `AlertRaised` | Se genera una alerta asociada a la sala y al indicador afectado |
| 10 | `AggregateUploadedToCloud` | El agregado del minuto se transmite a la capa Cloud |
| 11 | `UploadQueuedForRetry` | La transmisión falla y el agregado queda encolado para reintento |
| 12 | `SiteRegistered` | Se registra un nuevo local en el sistema |
| 13 | `RoomRegistered` | Se registra una nueva sala dentro de un local |
| 14 | `RoomClassified` | Se asigna un tipo a la sala, lo que determina sus umbrales aplicables |
| 15 | `DeviceRegistered` | Se asocia un dispositivo a una sala |
| 16 | `DeviceWentOffline` | El broker notifica la desconexión del dispositivo mediante su testamento |
| 17 | `ThresholdConfigured` | El administrador define los umbrales de una sala |
| 18 | `ThresholdsSyncedToEdge` | La capa Edge descarga la configuración de umbrales vigente |
| 19 | `AlertAcknowledged` | El administrador toma conocimiento de una alerta |
| 20 | `CorrectiveActionTaken` | El administrador registra la intervención realizada sobre la sala |
| 21 | `AlertClosed` | La condición se normaliza y la alerta se cierra |
| 22 | `TrendAnalyzed` | Se calculan tendencias y correlaciones sobre el histórico de la sala |
| 23 | `WeatherObservationRetrieved` | Se obtiene la observación meteorológica externa para contextualizar las mediciones |
| 24 | `DiscomfortReported` | Un miembro reporta una molestia acústica o térmica desde la aplicación |
| 25 | `RoomComfortStateChanged` | La sala cambia de estado en el semáforo de confort (verde, amarillo o rojo) |

**Policies identificadas** — las reglas que gobiernan el dominio

| Policy | Regla |
| :---- | :---- |
| Cierre por marca de agua | *Cuando* llegan datos de un minuto posterior para esa sala, *entonces* se cierra el minuto anterior y se agrega. Nunca por reloj de pared. |
| Umbral por defecto | *Cuando* una sala no ha sido clasificada, *entonces* se le aplican los umbrales por defecto de una sala de concentración: por debajo de 45 dB y entre 20 °C y 23 °C. Una sala recién registrada nunca queda sin vigilancia. |
| Superación sostenida | *Cuando* un indicador permanece fuera del umbral durante 5 minutos continuos, *entonces* se levanta la alerta. Un pico momentáneo no alerta. |
| Reintento de subida | *Cuando* falla la transmisión al cloud, *entonces* el agregado queda encolado y se reintenta. Nunca se descarta. |
| Entrega at-least-once | *Cuando* la capa Edge no confirma la subida, *entonces* reintenta. La deduplicación es responsabilidad de quien recibe, por la pareja sala e instante. |
| Cierre de alerta | *Cuando* el indicador retorna al rango durante el tiempo sostenido, *entonces* la alerta se cierra automáticamente. |
| Descarte del audio | *Cuando* se calcula el nivel sonoro, *entonces* la muestra de audio se descarta en el propio dispositivo. Nunca se transmite. |

*Nota.* Elaboración propia.

**Read Models identificados** — la información que cada actor consulta

| Read Model | Consultado por |
| :---- | :---- |
| Semáforo de confort de la sala | Miembro, antes de reservar |
| Mapa de calor del local | Administrador, en supervisión continua |
| Serie por minuto de una sala | Administrador, durante el diagnóstico |
| Alertas abiertas | Administrador, en la operación diaria |
| Reporte histórico por sala | Administrador, para decidir inversiones |
| Estado de los dispositivos | Administrador y soporte técnico |

*Nota.* Elaboración propia.

**Hot Spots — puntos que requieren decisión de diseño**

| Hot Spot | Pregunta abierta |
| :---- | :---- |
| Cierre del minuto | ¿Cuándo se considera cerrado un minuto si el reloj del dispositivo no se ha sincronizado por NTP? |
| Duplicación de agregados | Si la capa Edge reintenta la subida ante un fallo, ¿quién asume la responsabilidad de deduplicar? |
| Umbrales por defecto | ¿Qué umbral se aplica a una sala recién registrada que aún no ha sido clasificada? |
| Ausencia de datos | ¿Cómo se distingue una sala genuinamente silenciosa de un dispositivo que dejó de reportar? |
| Privacidad | ¿Qué garantiza que el contenido de las conversaciones no pueda reconstruirse a partir de los datos transmitidos? |
| Alcance de la alerta | ¿Debe notificarse al miembro que ocupa la sala o únicamente al administrador del local? |
| Reporte subjetivo vs. medición | Si un miembro reporta disconfort pero la medición está dentro del umbral, ¿se descarta el reporte, se registra como discrepancia o se ajusta el umbral de esa sala? |

*Nota.* Elaboración propia. Cada hot spot marca una decisión que el modelo aún no resuelve y que condiciona el diseño de la solución.

<p align="center"><em>Figura 8.</em> Big Picture EventStorming del dominio, organizado en las siete fases de la línea temporal.</p>

<p align="center">
  <img src="assets/event-storming/big-picture-eventstorming.png" alt="Big Picture EventStorming — Plataforma de confort ambiental en coworking" width="960">
</p>

El modelo reúne 25 domain events distribuidos en las siete fases, junto con las policies que los gobiernan, los read models que cada actor consulta y los hot spots aún sin resolver.


<a id="25-ubiquitous-language"></a>
## 2.5. Ubiquitous Language.

Los siguientes términos se emplean de forma consistente en el informe, en las conversaciones con el cliente y en la implementación. La documentación técnica y las interfaces del producto los utilizan en inglés, de modo que el vocabulario del código coincida con el del dominio.

| Término (inglés) | Término (español) | Definición |
| :---- | :---- | :---- |
| **Site** | Local | Establecimiento físico del operador que agrupa un conjunto de salas. Un operador puede administrar varios locales. |
| **Room** | Sala | Espacio delimitado dentro de un local, comercializado de forma independiente y sujeto a medición. |
| **Room Type** | Tipo de sala | Clasificación de una sala según su uso previsto —cabina de llamadas, sala de reuniones, área abierta— que determina los umbrales de confort aplicables. |
| **Device** | Dispositivo | Módulo IoT instalado en una sala que captura las mediciones. Se registra de forma independiente de la sala para preservar el histórico ante su reemplazo. |
| **Reading** | Lectura | Conjunto de valores capturados por un dispositivo en un instante determinado. |
| **Minute Aggregate** | Agregado por minuto | Registro consolidado que resume las mediciones de una sala durante un minuto. Es la unidad de información que se transmite a la nube. |
| **LAeq** | Nivel sonoro continuo equivalente | Nivel de presión sonora promediado energéticamente durante un intervalo, expresado en dB(A) conforme a la norma ISO 1996. No equivale al promedio aritmético de los niveles. |
| **L10 / L50 / L90** | Percentiles de nivel sonoro | Nivel superado durante el 10 %, 50 % y 90 % del tiempo de medición. L90 representa el ruido de fondo y L10 los picos intrusivos. |
| **PMV** | Voto medio estimado | Índice de sensación térmica de la norma ISO 7730, en una escala de −3 (frío) a +3 (calor). |
| **PPD** | Porcentaje de personas insatisfechas | Proporción estimada de ocupantes que manifestaría insatisfacción con las condiciones térmicas. Nunca desciende por debajo del 5 %. |
| **Threshold** | Umbral | Valor límite configurado para un indicador en una sala, cuya superación sostenida origina una alerta. |
| **Alert** | Alerta | Notificación generada al superarse un umbral, con severidad, sala e indicador asociados. |
| **Edge** | Borde | Capa de procesamiento local, alojada en el propio establecimiento, que agrega mediciones y evalúa alertas sin depender de la conexión a internet. |
| **Trend** | Tendencia | Evolución de un indicador a lo largo del tiempo para una sala determinada. |
| **Correlation** | Correlación | Medida estadística de la relación entre dos indicadores, considerada confiable a partir de un tamaño mínimo de muestra. |
| **Occupancy** | Ocupación | Proporción del tiempo durante el cual se detecta presencia en una sala. |
| **Comfort Index** | Índice de confort | Indicador consolidado que resume la condición acústica y térmica de una sala, presentado al miembro como semáforo de tres estados: verde (adecuada), amarillo (aceptable) y rojo (no recomendada). |
| **Comfort Range** | Rango de confort | Intervalo objetivo de una sala de concentración: nivel sonoro por debajo de **45 dB** y temperatura entre **20 °C y 23 °C**. Es el rango declarado como referencia para el trabajo de concentración y las videollamadas. |
| **Sustained Breach** | Superación sostenida | Condición que origina una alerta: el indicador permanece fuera del umbral durante un tiempo mínimo continuo —**5 minutos** por defecto— para evitar alertas por picos momentáneos. |
| **Discomfort Report** | Reporte de disconfort | Aviso que el miembro emite desde la aplicación cuando percibe una molestia acústica o térmica, y que se contrasta con la medición registrada en ese instante. |
| **Heatmap** | Mapa de calor | Representación del plano del local que colorea cada sala según su condición ambiental actual, destinada al panel del administrador. |


<hr>

<!-- nav:start -->
<p align="center"><a href="capitulo-1.md">← Capítulo I</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-3.md">Capítulo III →</a></p>
<!-- nav:end -->
