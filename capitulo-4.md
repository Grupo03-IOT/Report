<!-- nav:start -->
<p align="center"><a href="capitulo-3.md">← Capítulo III</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-5.md">Capítulo V →</a></p>
<!-- nav:end -->

<a id="capítulo-iv-solution-software-design"></a>
# Capítulo IV: Solution Software Design

<a id="41-strategic-level-domain-driven-design"></a>
## 4.1. Strategic-Level Domain-Driven Design.

En esta sección se describe el procedimiento con el que el equipo identificó y delimitó los bounded contexts de la plataforma. Partiendo del Big Picture EventStorming de la sección 2.4, se aplicaron el EventStorming a nivel de diseño, el Candidate Context Discovery, el modelado de los flujos de mensajes y el Bounded Context Canvas de cada contexto. El resultado se recoge en el context map y se traduce en la arquitectura de la solución.


<a id="411-design-level-eventstorming"></a>
### 4.1.1. Design-Level EventStorming.

El equipo trabajó sobre un único board, añadiendo una capa por paso y dejando constancia de cada una antes de continuar. La secuencia recorrió nueve pasos.

**Paso 1: Collect Domain Events**

Se recogieron treinta eventos del dominio sobre post-its naranjas, desde la captura de una muestra en el sensor hasta la revocación de una credencial.

<p align="center"><em>Figura 11.</em> Los treinta domain events recogidos sin orden.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-1-collect-domain-events.png" alt="Paso 1. Collect Domain Events" width="1000"></p>

**Paso 2: Timeline**

Los eventos se ordenaron cronológicamente y quedaron agrupados en cuatro tramos: la estructura del local y su telemetría, la política de alertas, la analítica y la identidad.

<p align="center"><em>Figura 12.</em> Línea temporal del área de Monitoring, que concentra la estructura del local y la telemetría.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-2a-timeline-monitoring.png" alt="Timeline del area de Monitoring" width="1000"></p>

<p align="center"><em>Figura 13.</em> Línea temporal del área de Alerting.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-2b-timeline-alerting.png" alt="Timeline del area de Alerting" width="1000"></p>

<p align="center"><em>Figura 14.</em> Línea temporal de Insights e IAM.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-2c-timeline-insights-iam.png" alt="Timeline de Insights e IAM" width="1000"></p>

**Paso 3: Pain and Pivotal Points**

Se marcaron cuatro pivotal events: Minute aggregated, Threshold exceeded, Room classified y Trend analyzed. Los pain points detectados fueron seis: no se distingue una sala silenciosa de un dispositivo caído, el reintento del Edge puede duplicar un agregado, una sala nueva sin clasificar quedaría sin vigilancia, un miembro puede reportar disconfort con la medición dentro de rango, el reloj sin sincronizar desordena el minuto y la privacidad del audio debe poder demostrarse.

<p align="center"><em>Figura 15.</em> Pivotal events y pain points del área de Monitoring.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-3a-pain-pivotal-monitoring.png" alt="Pain y pivotal points en Monitoring" width="1000"></p>

<p align="center"><em>Figura 16.</em> Pivotal events y pain points de Alerting, Insights e IAM.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-3b-pain-pivotal-resto.png" alt="Pain y pivotal points en el resto" width="1000"></p>

**Paso 4: Commands**

Se incorporaron los comandos sobre post-its azules, cada uno junto al evento que produce. El dispositivo IoT aparece como actor no humano: ejecuta Send measurement batch sin intervención de nadie, de modo que su autenticación no puede ser la de una persona.

<p align="center"><em>Figura 17.</em> Cada comando junto al evento que produce, y los actores que los ejecutan.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-4-commands.png" alt="Paso 4. Commands" width="1000"></p>

<p align="center"><em>Figura 18.</em> Detalle del área de Monitoring, donde se aprecia el emparejamiento entre cada comando y su evento.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-4a-commands-monitoring.png" alt="Detalle del emparejamiento entre comandos y eventos" width="1000"></p>

<p align="center"><em>Figura 19.</em> Detalle de Alerting, Insights e IAM con el mismo emparejamiento.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-4b-commands-resto.png" alt="Comandos de Alerting, Insights e IAM" width="1000"></p>

**Paso 5: Policies**

Se establecieron las políticas sobre post-its morados. Cuatro de ellas resuelven un pain point del paso anterior: el cierre por marca de agua corrige el reloj sin sincronizar, la entrega at-least-once absorbe la duplicación del reintento, el umbral por defecto cubre la sala recién registrada y el descarte del audio en el propio dispositivo sostiene la garantía de privacidad.

<p align="center"><em>Figura 20.</em> Políticas de Monitoring, intercaladas entre el evento que las dispara y el que producen.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-5a-policies-monitoring.png" alt="Politicas del area de Monitoring" width="1000"></p>

<p align="center"><em>Figura 21.</em> Políticas de Alerting, entre el evento que las dispara y el que producen.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-5b-policies-alerting.png" alt="Politicas de Alerting" width="1000"></p>

<p align="center"><em>Figura 22.</em> Políticas de Insights e IAM.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-5c-policies-insights-iam.png" alt="Politicas de Insights e IAM" width="1000"></p>

**Paso 6: Read Models**

Se identificaron seis read models sobre post-its verdes, desde el semáforo que consulta el miembro antes de reservar hasta el reporte histórico que sustenta una decisión de inversión. Cada uno tiene un actor que lo mira y una decisión que depende de él.

<p align="center"><em>Figura 23.</em> Read models de Monitoring, bajo los eventos que los alimentan.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-6a-read-models-monitoring.png" alt="Read models de Monitoring" width="1000"></p>

<p align="center"><em>Figura 24.</em> Read models de Alerting e Insights.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-6b-read-models-resto.png" alt="Read models de Alerting e Insights" width="1000"></p>

**Paso 7: External Systems**

Se señalaron tres sistemas externos sobre post-its rosados: el proveedor meteorológico, el broker MQTT y el servicio de notificaciones. Cada uno marca un punto de la frontera donde hará falta un adaptador que traduzca su lenguaje al propio.

<p align="center"><em>Figura 25.</em> Sistemas externos en los puntos de integración de Monitoring.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-7a-external-monitoring.png" alt="Sistemas externos de Monitoring" width="1000"></p>

<p align="center"><em>Figura 26.</em> Sistemas externos de Alerting e Insights.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-7b-external-resto.png" alt="Sistemas externos de Alerting e Insights" width="1000"></p>

**Paso 8: Aggregates**

Resultaron ocho agregados sobre post-its amarillos: Site, Room, Device, RoomReading, Threshold, Alert, Analysis y Account. Los cuatro primeros comparten la estructura física del local como raíz, y por eso terminan juntos en el paso siguiente.

<p align="center"><em>Figura 27.</em> Los agregados de Monitoring rotulando los eventos que encapsulan.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-8a-aggregates-monitoring.png" alt="Agregados de Monitoring" width="1000"></p>

<p align="center"><em>Figura 28.</em> Los agregados de Alerting, Insights e IAM.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-8b-aggregates-resto.png" alt="Agregados del resto de contextos" width="1000"></p>

**Paso 9: Bounded Contexts**

Por último se trazaron las fronteras sobre los agregados, siguiendo los pivotal events del paso 3, y se unieron los contextos que dependen entre sí. El resultado son cuatro bounded contexts: Monitoring e Insights como núcleo, Alerting como soporte e IAM como subdominio genérico. Alerting e Insights dependen de Monitoring a través de una capa anticorrupción, los tres aceptan el modelo de autorización de IAM, y los sistemas externos quedan fuera de toda frontera.

<p align="center"><em>Figura 29.</em> Los cuatro bounded contexts con su clasificación estratégica y las relaciones que los unen.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-9-bounded-contexts.png" alt="Paso 9. Bounded Contexts" width="1000"></p>

<p align="center"><em>Figura 30.</em> Detalle del bounded context Monitoring con los agregados, comandos, eventos, políticas y read models que encierra.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-9a-monitoring.png" alt="Detalle del bounded context Monitoring" width="1000"></p>

<p align="center"><em>Figura 31.</em> Detalle del bounded context Alerting.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-9b-alerting.png" alt="Detalle del bounded context Alerting" width="1000"></p>

<p align="center"><em>Figura 32.</em> Detalle del bounded context Insights.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-9c-insights.png" alt="Detalle del bounded context Insights" width="1000"></p>

<p align="center"><em>Figura 33.</em> Detalle del bounded context IAM.</p>

<p align="center"><img src="assets/event-storming/design-level/paso-9d-iam.png" alt="Detalle del bounded context IAM" width="1000"></p>

<a id="4111-candidate-context-discovery"></a>
#### <i>**4.1.1.1 Candidate Context Discovery.**</i>

A partir del EventStorming refinado, el equipo realizó una sesión de Candidate Context Discovery aplicando las tres técnicas de forma encadenada, de modo que las tres coincidieran antes de dar una frontera por buena.

La identificación empezó revisando el modelo de la sección anterior, con la atención puesta en los pivotal events y en los agregados, y sobre esa base se detectaron las agrupaciones naturales de comandos, eventos y políticas que operan sobre la misma entidad.

<p align="center"><em>Figura 34.</em> Agrupaciones naturales: los comandos, eventos y políticas que operan sobre cada entidad.</p>

<p align="center"><img src="assets/event-storming/design-level/ccd-1-agrupaciones-naturales.png" alt="Agrupaciones naturales por entidad" width="1000"></p>

**1. Start-with-Value**

Se empezó clasificando por aporte al negocio. Monitoring es core porque sin medición objetiva no hay producto que vender, e Insights también lo es porque es lo que separa la solución de un termómetro con memoria. Alerting es supporting, ya que resulta necesario para que la medición sirva de algo pero no es donde reside la ventaja competitiva. IAM es un subdominio genérico, con el problema ya resuelto en la industria. Esa clasificación es la que rotula cada frontera en la Figura 29.

**2. Start-with-Simple**

Para no perderse en la complejidad se descompuso el recorrido en seis pasos secuenciales, que son medir, agregar, comparar con la política, avisar, responder y explicar, y se preguntó a quién corresponde cada uno. Medir y agregar pertenecen a quien posee la estructura del local; comparar y avisar dependen de una política que alguien configura por separado; explicar necesita historia acumulada y no el instante. Son tres responsabilidades que no cambian por las mismas razones, y en las Figuras 11, 12 y 13 ya aparecen separadas por áreas.

**3. Look-for-Pivotal-Events**

Los pivotal events marcados en el paso 3 se leyeron como fronteras, citando en cada caso los dos lados que separan:

- Minute aggregated es la frontera entre el Edge y Monitoring: antes es muestra cruda y después es telemetría del dominio.
- Room classified es la frontera entre Monitoring y Alerting, porque la sala pasa a tener una política aplicable.
- Threshold exceeded es la frontera entre Alerting y Monitoring, ya que la medición pasa a ser política incumplida.
- Trend analyzed es la frontera entre Monitoring e Insights: la serie deja de ser dato y pasa a ser conclusión.

Los cuatro quedan marcados sobre la línea temporal en la Figura 15. Para decidir si cada uno separa de verdad dos contextos, se comprobó cómo se llama el dato a cada lado de la frontera.

<p align="center"><em>Figura 35.</em> Cada pivotal event con el nombre que recibe el dato antes y después de cruzar la frontera.</p>

<p align="center"><img src="assets/event-storming/design-level/ccd-2-pivotal-events.png" alt="Pivotal events leidos como frontera" width="1000"></p>

El evento Aggregate uploaded to cloud se descartó como frontera de modelo. Separa dos zonas de despliegue del mismo contexto y no dos lenguajes distintos, de modo que tratarlo como bounded context habría creado uno que el nivel táctico no necesita desarrollar.

**Agrupamientos y consolidación**

El primer agrupamiento reunió lo evidente: IAM alrededor de Account, y Alerting alrededor de Threshold y Alert. Son los dos contextos cuya responsabilidad no se discute, y cerrarlos primero deja a la vista lo que todavía falta por repartir.

<p align="center"><em>Figura 36.</em> Primer agrupamiento: IAM y Alerting cerrados, y los agregados que quedan sin repartir.</p>

<p align="center"><img src="assets/event-storming/design-level/ccd-3-primer-agrupamiento.png" alt="Primer agrupamiento" width="1000"></p>

El segundo aisló los contextos centrales y fue el que más discusión costó, porque Monitoring e Insights hablan ambos de lecturas. Se separaron por dos razones: cambian por motivos distintos, uno por cómo se captura el dato y otro por cómo se interpreta, y además Insights puede estar caído sin que la medición se detenga.

<p align="center"><em>Figura 37.</em> Segundo agrupamiento: Monitoring e Insights separados pese a compartir el vocabulario de las lecturas.</p>

<p align="center"><img src="assets/event-storming/design-level/ccd-4-segundo-agrupamiento.png" alt="Segundo agrupamiento" width="1000"></p>

El resultado de ambas rondas es el que encierra cada frontera en la Figura 29.

La consolidación final deja cuatro bounded contexts, que son Monitoring, Insights, Alerting e IAM, y coinciden exactamente con los que desarrolla el nivel táctico en la sección 4.2.

<a id="4112-domain-message-flows-modeling"></a>
#### <i>**4.1.1.2 Domain Message Flows Modeling.**</i>

La colaboración entre los cuatro contextos se modeló con Domain Storytelling, en tres escenarios: el principal de operación, el de instalación y el de fallo. Cada diagrama lleva su propia leyenda de notación.

**Escenario 1. Disconfort acústico en una sala**

<p align="center"><em>Figura 38.</em> Domain Storytelling del escenario de disconfort acústico.</p>

<p align="center"><img src="assets/domain-storytelling/ds-1-disconfort-acustico.png" alt="Domain Storytelling del escenario de disconfort acústico" width="1000"></p>

El flujo deja ver tres decisiones de reparto. La primera es que el Edge evalúa los umbrales y no el cloud: consulta los límites y decide localmente, de modo que una caída de internet no deja la sala sin vigilancia. La segunda es que Monitoring es el único que recibe telemetría y el único al que los demás preguntan, lo que lo convierte en el proveedor del que dependen Alerting e Insights. La tercera es que el administrador recorre tres contextos en una sola tarea, porque ve el estado, entiende la causa y ajusta la política, y esa continuidad obliga a que las fronteras sean invisibles para él aunque sean estrictas por dentro.

**Escenario 2. Alta de un local y sus salas**

<p align="center"><em>Figura 39.</em> Domain Storytelling del escenario de instalación de un local.</p>

<p align="center"><img src="assets/domain-storytelling/ds-2-alta-de-local.png" alt="Domain Storytelling del escenario de instalación" width="1000"></p>

La instalación recorre los tres contextos que el administrador toca: IAM para las credenciales propias y la clave de máquina del dispositivo, Monitoring para la estructura del local y Alerting para la política. El paso de clasificar cada sala es el que evita el pain point de la sala sin vigilancia, y si se omite la política de umbral por defecto la cubre igualmente, lo que hace que el sistema nunca quede ciego por un olvido durante la instalación.

**Escenario 3. Pérdida de conexión del Edge**

<p align="center"><em>Figura 40.</em> Domain Storytelling del escenario de pérdida de conexión del Edge.</p>

<p align="center"><img src="assets/domain-storytelling/ds-3-perdida-de-conexion.png" alt="Domain Storytelling del escenario de pérdida de conexión" width="1000"></p>

Este escenario justifica tres decisiones de diseño a la vez. El Edge conserva los umbrales en caché y mantiene la vigilancia local mientras no hay internet; el agregado que no consigue subir se encola en lugar de descartarse; y, como la entrega es at-least-once, la deduplicación por sala y minuto corresponde a quien recibe. El testamento de desconexión del broker es lo que permite distinguir una sala silenciosa de un dispositivo caído, que era el primero de los pain points sin resolver.


<a id="4113-bounded-context-canvases"></a>
#### <i>**4.1.1.3 Bounded Context Canvases.**</i>

Cada contexto se diseñó con su propio Bounded Context Canvas. Los cuatro se presentan por orden de importancia para el negocio, primero como canvas y después como tabla de detalle.

**Bounded Context: Monitoring** (core domain)

<p align="center"><em>Figura 41.</em> Bounded Context Canvas de Monitoring.</p>

<p align="center"><img src="assets/bounded-context-canvas/canvas-1-monitoring.png" alt="Bounded Context Canvas de Monitoring" width="1000"></p>

| Elemento | Contenido |
|---|---|
| **Propósito** | Saber cómo está cada sala ahora mismo, y conservar el registro de cómo ha estado. |
| **Clasificación estratégica** | Core domain. Es la razón por la que el producto existe: sin medición objetiva no hay nada que vender. |
| **Rol de dominio** | Proveedor de la estructura del local y de la telemetría. Todos los demás contextos dependen de él; él no depende de ninguno. |
| **Lenguaje ubicuo** | Site, Room, Room Type, Device, Room Reading, LAeq, L10, L90, PMV, PPD, ocupación, calidad del dato. |
| **Reglas de negocio** | Una lectura se identifica por sala y minuto, y el mismo minuto no se registra dos veces. Una sala desconocida se da de alta sola cuando un dispositivo reporta por ella. Un minuto incompleto se guarda, pero no es fiable para promediar. Sustituir un dispositivo no altera el historial de la sala. |
| **Capacidades** | Alta y clasificación de locales, tipos y salas · ingesta de telemetría · consulta del estado actual y de series históricas. |
| **Estratificación de capacidades** | Estructura del local por debajo y telemetría por encima: cambian a ritmos distintos, de modo que la ingesta puede evolucionar sin tocar el alta de salas. |
| **Dependencias entrantes** | Edge API (telemetría) · Web App y Mobile App (consulta) · Alerting e Insights (a través de la fachada). |
| **Dependencias salientes** | Ninguna. |
| **Crítica del diseño** | Al ser el proveedor del que dependen todos, concentra el riesgo: un cambio en su modelo de sala obliga a revisar las dos capas anticorrupción que lo traducen. El autoprovisionamiento facilita la instalación, pero genera salas sin clasificar que solo una persona puede resolver, de modo que el sistema acumula trabajo pendiente si nadie lo atiende. La tabla de lecturas crece un registro por sala y minuto, y su política de retención está sin decidir. |

**Bounded Context: Insights** (core domain)

<p align="center"><em>Figura 42.</em> Bounded Context Canvas de Insights.</p>

<p align="center"><img src="assets/bounded-context-canvas/canvas-2-insights.png" alt="Bounded Context Canvas de Insights" width="1000"></p>

| Elemento | Contenido |
|---|---|
| **Propósito** | Explicar por qué una sala se comporta como lo hace, a lo largo de semanas. |
| **Clasificación estratégica** | Core domain. Es lo que diferencia el producto de un termómetro con memoria. |
| **Rol de dominio** | Analítico. Consume series ajenas y produce conclusiones, sin poseer telemetría propia. |
| **Lenguaje ubicuo** | Correlación, tendencia, deriva térmica, anomalía, tamaño de muestra, fiabilidad, observación meteorológica. |
| **Reglas de negocio** | Ninguna conclusión se emite sin el tamaño de muestra que la respalda. Por debajo de treinta observaciones el resultado se declara insuficiente en lugar de estimarse. Si el servicio meteorológico externo no responde, el resto del análisis se entrega igual. |
| **Capacidades** | Correlación entre variables · ajuste de tendencias · detección de anomalías · acumulación del histórico climático exterior. |
| **Estratificación de capacidades** | La acumulación del histórico va por debajo y el análisis bajo demanda por encima, lo que permite cambiar el cálculo sin rehacer lo ya acumulado. |
| **Dependencias entrantes** | Web App (panel de diagnóstico). |
| **Dependencias salientes** | Monitoring (series de lecturas) · OpenWeather (clima exterior). |
| **Crítica del diseño** | No aporta valor hasta que existe historia suficiente, por lo que un local recién instalado ve el contexto vacío durante semanas. La correlación con el exterior depende de que el muestreo periódico haya venido acumulando observaciones: si el proveedor estuvo caído, el hueco no se recupera hacia atrás. Correlación no es causa, y los resultados deben presentarse como indicios y no como diagnósticos. |

**Bounded Context: Alerting** (supporting)

<p align="center"><em>Figura 43.</em> Bounded Context Canvas de Alerting.</p>

<p align="center"><img src="assets/bounded-context-canvas/canvas-3-alerting.png" alt="Bounded Context Canvas de Alerting" width="1000"></p>

| Elemento | Contenido |
|---|---|
| **Propósito** | Convertir la política de confort del negocio en límites que una máquina pueda evaluar. |
| **Clasificación estratégica** | Supporting. Necesario para que la medición sirva de algo, pero no es donde reside la ventaja competitiva. |
| **Rol de dominio** | Definidor de política. Publica umbrales y los resuelve por sala; no observa la telemetría. |
| **Lenguaje ubicuo** | Umbral, valor de aviso, valor crítico, minutos sostenidos, métrica, tipo de sala. |
| **Reglas de negocio** | El valor de aviso siempre es inferior al crítico. Un umbral se configura por tipo de sala, nunca por sala individual. Superar el límite un instante no basta: debe sostenerse el tiempo configurado. La configuración es idempotente. |
| **Capacidades** | Configuración de umbrales por tipo · resolución de umbrales aplicables a cada sala. |
| **Estratificación de capacidades** | Definir la política va por debajo y resolverla para cada sala por encima, de forma que el catálogo de umbrales evoluciona sin tocar la evaluación. |
| **Dependencias entrantes** | Web App (configuración) · Edge API (consulta para evaluar). |
| **Dependencias salientes** | Monitoring (qué salas existen y de qué tipo son). |
| **Crítica del diseño** | El contexto está incompleto: hoy define y publica umbrales, pero no evalúa ni emite alertas, de modo que su nombre promete más de lo que cumple. Al no existir clave foránea hacia Monitoring, borrar un tipo de sala dejaría umbrales huérfanos, y corresponde al caso de uso de borrado cubrirlo. Configurar solo por tipo de sala es lo que el negocio pide hoy, pero impide la excepción de una sala concreta. |

**Bounded Context: IAM** (generic subdomain)

<p align="center"><em>Figura 44.</em> Bounded Context Canvas de IAM.</p>

<p align="center"><img src="assets/bounded-context-canvas/canvas-4-iam.png" alt="Bounded Context Canvas de IAM" width="1000"></p>

| Elemento | Contenido |
|---|---|
| **Propósito** | Decidir quién entra y qué puede hacer, distinguiendo personas de máquinas. |
| **Clasificación estratégica** | Generic subdomain. El problema está resuelto en la industria; no se innova aquí. |
| **Rol de dominio** | Guardián. Ningún otro contexto implementa autorización por su cuenta. |
| **Lenguaje ubicuo** | Cuenta, credencial de máquina, rol, alcance, token, revocación. |
| **Reglas de negocio** | El correo identifica una cuenta sin distinguir mayúsculas. El registro público siempre crea cuentas con el rol de menor privilegio. La clave de una máquina se muestra una sola vez y no vuelve a ser recuperable. Una credencial revocada se rechaza indicando la revocación, no como si no existiera. |
| **Capacidades** | Registro y autenticación de personas · emisión y verificación de credenciales de máquina · concesión de roles y alcances. |
| **Estratificación de capacidades** | Autenticar va por debajo y autorizar por encima, lo que permite cambiar el mecanismo de acceso sin rehacer el modelo de roles. |
| **Dependencias entrantes** | Todos los contextos, a través de la cadena de filtros de seguridad. |
| **Dependencias salientes** | Ninguna. |
| **Crítica del diseño** | No contempla recuperación de contraseña ni rotación de credenciales de máquina, dos necesidades que aparecerán en cuanto el sistema salga de pruebas. El catálogo de alcances es cerrado y ampliarlo exige modificar código, lo que basta con dos alcances pero no escalaría. Al ser un subdominio genérico, conviene vigilar que no absorba reglas que pertenecen a otros contextos. |


<a id="412-context-mapping"></a>
### 4.1.2. Context Mapping.

El context map recoge las relaciones estructurales entre los cuatro bounded contexts y con el servicio externo, indicando para cada una el patrón de Domain-Driven Design que la gobierna y quién manda en el contrato.

<p align="center"><em>Figura 45.</em> Context map de la solución, con el patrón que gobierna cada relación.</p>

```mermaid
flowchart TB
    subgraph nube["cloud-api"]
        mon["monitoring<br/>[core]<br/>Upstream"]
        ins["insights<br/>[core]<br/>Downstream"]
        ale["alerting<br/>[supporting]<br/>Downstream"]
        iam["iam<br/>[generic]"]
        sha["shared<br/>Shared Kernel"]
    end
    ow(["OpenWeather<br/>[servicio externo]"])
    edge["Edge API<br/>[Flask]"]

    ins -->|"ACL: ReadingSeriesProvider"| mon
    ale -->|"ACL: RoomProfileProvider"| mon
    ins -->|"ACL: OutdoorWeatherProvider"| ow
    edge -->|"Customer/Supplier"| mon
    edge -->|"Customer/Supplier"| ale
    iam -.->|"Conformist: autorización"| mon
    iam -.->|"Conformist: autorización"| ins
    iam -.->|"Conformist: autorización"| ale
    mon --- sha
    ins --- sha
    ale --- sha
    iam --- sha
```

**Anti-corruption Layer.** Es el patrón que protege las tres dependencias salientes. Insights y Alerting no conocen el modelo de Monitoring: declaran puertos con su propio vocabulario —`ReadingSeriesProvider` pide una serie de `ReadingPoint`, `RoomProfileProvider` pide una lista de `RoomProfile`— y un único componente traduce. La sala de Monitoring tiene aforo, planta, superficie y última lectura; en Alerting una sala es un código y un tipo, y nada más. Esa reducción es la que impide que un cambio en el modelo del proveedor se propague a sus consumidores. El mismo patrón aísla a Insights de OpenWeather: `OutdoorWeatherProvider` expresa la necesidad de clima exterior, y el adaptador absorbe el formato del proveedor.

**Customer/Supplier.** La relación entre el Edge y el cloud es de cliente y proveedor con contrato negociado: el Edge consume los umbrales que publica Alerting y entrega telemetría a Monitoring en un formato acordado. Monitoring es el *upstream* de toda la solución —quien define el contrato— y tanto el Edge como los dos contextos analíticos son *downstream*.

**Conformist.** Los contextos de negocio no negocian con IAM: aceptan su modelo de roles y alcances tal como es, aplicado por la cadena de filtros de seguridad antes de que la petición llegue a un controlador. Ninguno implementa autorización propia ni traduce el modelo de identidad, y por eso la relación es de conformidad y no de anti-corrupción: aquí no hay nada de lo que protegerse, porque IAM es un subdominio genérico cuyo modelo no aporta ambigüedad al dominio.

**Shared Kernel.** El paquete `shared` es el único código que los cuatro contextos comparten deliberadamente, y se mantiene reducido a propósito: el catálogo de errores, la excepción de dominio, la clasificación de errores en tipos, la base de auditoría de las entidades y el manejador global de excepciones. Es un núcleo compartido y no una biblioteca de utilidades, lo que significa que modificarlo obliga a comprobar los cuatro contextos, y por eso todo lo que puede vivir en un solo contexto vive allí.

**Alternativas consideradas y por qué se descartaron.** El reparto actual no fue el primero: se llegó a él descartando otros tres, y conviene dejar constancia de cada uno porque las razones siguen vigentes.

*¿Y si Monitoring e Insights fueran un solo contexto?* Ambos trabajan sobre las mismas lecturas, de modo que unirlos evitaría la capa anticorrupción y una traducción. Se descartó porque responden a preguntas con horizontes distintos —una es el estado de ahora, la otra el patrón de tres semanas— y esa diferencia arrastra todo lo demás: Monitoring optimiza la escritura continua y la consulta del último minuto, mientras que Insights recorre series largas y tolera latencia. Unirlos obligaría a un solo modelo a servir a dos cargas opuestas, y el producto vende las dos cosas por separado.

*¿Y si `Threshold` viviera en Monitoring?* Fue así al principio. Se movió a Alerting porque un umbral existe únicamente para disparar una alerta: sin ese contexto no significa nada, y tenerlo junto a la telemetría mezclaba la medición con la política sobre la medición. El cambio se hizo cuando todavía era barato —nada lo usaba, ni caso de uso ni endpoint—; con la pantalla de administración ya construida encima habría costado mucho más.

*¿Y si se duplicara el tipo de sala en Alerting para romper la dependencia?* Eliminaría la única dependencia saliente del contexto y lo dejaría autónomo. Se descartó porque obligaría a mantener sincronizadas dos copias de la misma clasificación, y una discrepancia entre ellas se manifestaría como umbrales que no se aplican, un fallo silencioso y difícil de diagnosticar. Se prefirió pagar la dependencia y aislarla con la capa anticorrupción, que es reducida: un puerto con un solo método.

*¿Y si se añadieran más contextos?* Cuatro es el techo que el equipo consideró sensato. Cada bounded context obliga a repetir por completo el diseño táctico —cuatro capas, tres diagramas y su esquema propio—, de modo que dividir más aumenta el coste de documentación y de mantenimiento sin que el dominio lo pida. Un quinto contexto tendría que justificarse por una frontera de negocio real, no por conveniencia técnica.

**La frontera es física, no solo conceptual.** Cada contexto tiene su propio esquema de PostgreSQL y su propia migración de Flyway con historial independiente, de modo que todos empiezan por `V1` y evolucionan sin coordinarse. No existe ninguna clave foránea que cruce de un esquema a otro: los contextos se referencian por identificador y cada uno responde de su integridad. La contrapartida queda anotada como deuda: borrar un tipo de sala dejaría umbrales huérfanos en Alerting, y es el caso de uso de borrado el que deberá cubrirlo.


<a id="413-software-architecture"></a>
### 4.1.3. Software Architecture.

La arquitectura de software se representa aplicando el modelo C4, que describe el sistema en niveles de detalle decrecientes: el panorama de sistemas, el contexto del sistema con sus usuarios y sistemas externos, la descomposición en containers desplegables y, por último, el despliegue sobre la infraestructura. El nivel de componentes se presenta dentro de cada bounded context, en la sección 4.2.

La solución es distribuida por exigencia del problema, no por elección de estilo: el procesamiento se reparte entre el dispositivo, una capa de borde dentro del local y la nube, porque el micrófono muestrea a 16 kHz y transmitir esas muestras sería, además de inviable en ancho de banda, grabar conversaciones de personas que no han dado su consentimiento.


<a id="4131-software-architecture-system-landscape-diagram"></a>
#### <i>**4.1.3.1. Software Architecture System Landscape Diagram.**</i>

El panorama sitúa la solución entre los actores del negocio y los sistemas con los que convive.

<p align="center"><em>Figura 46.</em> System Landscape Diagram de la solución ZenRoom.</p>

```mermaid
flowchart TB
    miembro["<b>Miembro del coworking</b><br/>[Persona]<br/>Reserva salas y necesita<br/>condiciones adecuadas"]
    admin["<b>Administrador de sede</b><br/>[Persona]<br/>Gestiona el local y<br/>responde por el confort"]
    visitante["<b>Visitante</b><br/>[Persona]<br/>Evalúa contratar la solución"]

    sistema["<b>ZenRoom</b><br/>[Sistema de software]<br/>Mide el confort acústico y térmico<br/>de cada sala y lo hace accionable"]

    ow(["<b>OpenWeather</b><br/>[Sistema externo]<br/>Condiciones meteorológicas<br/>del exterior"])
    stores(["<b>Tiendas de aplicaciones</b><br/>[Sistema externo]<br/>Distribución de la app móvil"])

    miembro -->|"consulta el estado de una sala<br/>y reporta molestias"| sistema
    admin -->|"supervisa, diagnostica<br/>y ajusta umbrales"| sistema
    visitante -->|"conoce la propuesta<br/>y solicita contacto"| sistema
    sistema -->|"obtiene temperatura<br/>y humedad exteriores"| ow
    sistema -->|"se distribuye a través de"| stores
```

Los tres actores se corresponden con los segmentos objetivo del capítulo I. El visitante no es un usuario del producto sino del Landing Page, y se incluye porque la conversión forma parte del alcance evaluado. OpenWeather es el servicio externo de terceros que la arquitectura de la solución exige consumir, y sostiene la correlación entre temperatura interior y exterior.


<a id="4132-software-architecture-context-level-diagrams"></a>
#### <i>**4.1.3.2. Software Architecture Context Level Diagrams.**</i>

El diagrama de contexto muestra el sistema como una única caja, rodeado de quienes lo usan y de aquello con lo que se comunica, sin revelar todavía su estructura interna.

<p align="center"><em>Figura 47.</em> Software Architecture Context Level Diagram.</p>

```mermaid
flowchart TB
    miembro["<b>Miembro del coworking</b><br/>[Persona]"]
    admin["<b>Administrador de sede</b><br/>[Persona]"]
    visitante["<b>Visitante</b><br/>[Persona]"]

    subgraph limite[" "]
        sistema["<b>ZenRoom</b><br/>[Sistema de software]<br/><br/>Mide de forma continua el nivel sonoro,<br/>la temperatura y la ocupación de cada sala;<br/>calcula indicadores normalizados de confort<br/>y los presenta al miembro y al administrador"]
    end

    ow(["<b>OpenWeather</b><br/>[Sistema externo]"])

    visitante -->|"consulta la propuesta de valor<br/>[HTTPS]"| sistema
    miembro -->|"consulta el confort de una sala<br/>y reporta molestias [HTTPS]"| sistema
    admin -->|"supervisa el local, diagnostica causas<br/>y configura umbrales [HTTPS]"| sistema
    sistema -->|"solicita las condiciones exteriores<br/>[HTTPS/JSON]"| ow
```

Desde fuera, el sistema es una sola cosa que responde a tres preguntas: si una sala está en condiciones ahora, por qué no lo está cuando falla, y qué hay que cambiar para que deje de fallar. El único sistema externo del que depende es el proveedor meteorológico, y esa dependencia es degradable: si no responde, la solución sigue funcionando y solo pierde la correlación con el exterior.


<a id="4132-software-architecture-container-level-diagrams"></a>
#### <i>**4.1.3.2. Software Architecture Container Level Diagrams.**</i>

El diagrama de containers descompone el sistema en las unidades que se despliegan por separado, con la tecnología de cada una y el protocolo por el que se comunican.

<p align="center"><em>Figura 48.</em> Software Architecture Container Level Diagram.</p>

```mermaid
flowchart TB
    miembro["<b>Miembro</b><br/>[Persona]"]
    admin["<b>Administrador</b><br/>[Persona]"]
    visitante["<b>Visitante</b><br/>[Persona]"]

    subgraph local["Dentro del coworking"]
        disp["<b>Dispositivo IoT</b><br/>[ESP32 DEVKIT V1]<br/>INMP441 · SHT31 · LD2410C"]
        emb["<b>Embedded Application</b><br/>[C++]<br/>Muestrea, calcula LAeq y percentiles,<br/>y descarta el audio"]
        broker["<b>Broker MQTT</b><br/>[Mosquitto]<br/>Transporta las muestras"]
        edge["<b>Edge API</b><br/>[Python, Flask, Peewee]<br/>Agrega por minuto, evalúa umbrales<br/>sin internet y encola si se cae la red"]
        sqlite[("<b>Almacén del borde</b><br/>[SQLite]<br/>Crudo 14 días, agregados y cola")]
    end

    subgraph cloud["En la nube"]
        api["<b>Cloud API</b><br/>[Spring Boot 4, Java 21]<br/>RESTful documentado con OpenAPI.<br/>monitoring · insights · alerting · iam"]
        db[("<b>Base de datos</b><br/>[PostgreSQL 18]<br/>Un esquema por bounded context")]
        web["<b>Web Application</b><br/>[Angular o Vue]<br/>Panel del administrador"]
        mobile["<b>Mobile Application</b><br/>[por decidir]<br/>Consulta y reporte del miembro"]
        landing["<b>Landing Page</b><br/>[HTML5, CSS3, JavaScript]<br/>Propuesta de valor y CTA"]
    end

    ow(["<b>OpenWeather</b><br/>[Sistema externo]"])

    disp --> emb
    emb -->|"publica muestras<br/>[MQTT]"| broker
    broker -->|"entrega<br/>[MQTT]"| edge
    emb -.->|"alternativa<br/>[HTTP/JSON]"| edge
    edge --> sqlite
    edge -->|"sube agregados por minuto<br/>[HTTPS/JSON, API key]"| api
    edge -->|"consulta umbrales<br/>[HTTPS/JSON, API key]"| api
    api --> db
    api -->|"obtiene el clima exterior<br/>[HTTPS/JSON]"| ow
    web -->|"[HTTPS/JSON, JWT]"| api
    mobile -->|"[HTTPS/JSON, JWT]"| api
    admin --> web
    miembro --> mobile
    visitante --> landing
    landing -.->|"deriva por segmento"| web
    landing -.->|"deriva por segmento"| mobile
```

El reparto entre las tres capas responde a tres restricciones distintas. El **dispositivo** calcula los indicadores acústicos en el propio microcontrolador porque el audio no puede salir de la sala. El **Edge** agrega por minuto y evalúa los umbrales localmente, de modo que una caída de internet no deja el local sin vigilancia, y encola lo que no ha podido subir. El **cloud** guarda la historia larga y resuelve lo que exige varias salas o varias semanas, que es donde vive la analítica.

La entrega entre el Edge y el cloud es *at-least-once*: la cola reintenta hasta confirmar, de modo que el mismo minuto puede llegar repetido y el cloud lo deduplica por sala e instante. Esa decisión traslada la complejidad al servidor a cambio de que el borde pueda ser simple y tolerante a fallos.

El transporte entre el dispositivo y el Edge admite MQTT a través de Mosquitto y, como alternativa, HTTP directo. La segunda vía existe porque el simulador del dispositivo la usa y porque permite depurar sin levantar el broker.


<a id="4133-software-architecture-deployment-diagrams"></a>
#### <i>**4.1.3.3. Software Architecture Deployment Diagrams.**</i>

El diagrama de despliegue muestra sobre qué infraestructura se ejecuta cada container en el entorno de desarrollo y pruebas, tal como lo define la composición de contenedores del repositorio `cloud-api`.

<p align="center"><em>Figura 49.</em> Software Architecture Deployment Diagram del entorno de desarrollo.</p>

```mermaid
flowchart TB
    subgraph sala["Nodo: sala del coworking"]
        esp["<b>ESP32 DEVKIT V1</b><br/>[Dispositivo, 30 pines]<br/>Embedded Application"]
    end

    subgraph servidor["Nodo: equipo del local"]
        mosq["<b>Mosquitto</b><br/>[Broker MQTT]"]
        flask["<b>Edge API</b><br/>[Flask]<br/>edge.db (SQLite)"]
    end

    subgraph host["Nodo: servidor de aplicación — Docker"]
        cont_api["<b>Contenedor comfort-api</b><br/>[eclipse-temurin:21-jre-alpine]<br/>cloud-api, puerto 8080"]
        cont_db["<b>Contenedor comfort-db</b><br/>[postgres:18-alpine]<br/>puerto 5433 → 5432<br/>volumen pgdata"]
        cont_adm["<b>Contenedor comfort-pgadmin</b><br/>[dpage/pgadmin4]<br/>puerto 5050, perfil tools"]
    end

    subgraph cdn["Nodo: alojamiento estático"]
        land["<b>Landing Page</b><br/>[HTML5, CSS3, JavaScript]"]
        webapp["<b>Web Application</b><br/>[bundle estático]"]
    end

    nav["<b>Navegador</b><br/>[del administrador]"]
    disp_mov["<b>Dispositivo móvil</b><br/>[del miembro]"]

    esp -->|"WiFi, MQTT"| mosq
    mosq --> flask
    flask -->|"HTTPS"| cont_api
    cont_api -->|"JDBC"| cont_db
    cont_adm -.->|"administración"| cont_db
    nav --> land
    nav --> webapp
    webapp -->|"HTTPS/JSON"| cont_api
    disp_mov -->|"HTTPS/JSON"| cont_api
```

La aplicación se empaqueta con un `Dockerfile` de dos etapas: la primera compila con el JDK 21 y resuelve las dependencias en una capa separada del código fuente, de modo que un cambio en el código no obliga a volver a descargarlas; la segunda parte de una imagen de solo ejecución y copia únicamente el artefacto, ejecutándolo con un usuario sin privilegios. La memoria se limita por porcentaje del contenedor en lugar de por un valor fijo, para que la misma imagen sirva en máquinas distintas.

La base de datos expone el puerto 5433 en la máquina anfitriona para no chocar con una instalación local de PostgreSQL, y persiste en un volumen con nombre. El contenedor de administración queda tras un perfil de Docker Compose, de modo que no se levanta salvo que se pida expresamente. El arranque de la aplicación depende de que la base de datos supere su comprobación de salud, porque Flyway aplica las migraciones de los cuatro esquemas antes de que la aplicación acepte peticiones.


<a id="42-tactical-level-domain-driven-design"></a>
## 4.2. Tactical-Level Domain-Driven Design

El diseño táctico desarrolla cada bounded context por dentro: las clases que representan su modelo, la organización en capas y los diagramas que las describen. La solución aplica una arquitectura por capas con inversión de dependencias, de modo que el dominio no conoce ni la persistencia ni el transporte: declara puertos, y la infraestructura los implementa.

Cada contexto se presenta en su propia sección, en el orden de importancia establecido en el context map, y todas siguen la misma estructura: las cuatro capas, el diagrama de componentes y los diagramas de nivel de código.


<a id="421-bounded-context"></a>
### 4.2.1. Bounded Context: Alerting

Es el contexto encargado de traducir la política de confort en vigilancia accionable: administra los umbrales configurables por tipo de sala (nivel sonoro, temperatura, ocupación, PPD) y los resuelve sala por sala para que la capa Edge pueda evaluarlos sin conocer la taxonomía de tipos que maneja Monitoring. No almacena telemetría ni la interpreta; solo decide, a partir de un valor y de cuánto tiempo se sostiene, cuándo una condición deja de ser tolerable. El servicio en la nube registra además las alertas que la Edge API abre y cierra al evaluar esos umbrales, y la acción correctiva con la que el administrador las atiende.

<a id="4211-domain-layer"></a>
#### <i>**4.2.1.1. Domain Layer.**</i>

Este contexto concentra las reglas de configuración y evaluación de los umbrales que disparan alertas sobre la telemetría de las salas.

**Entities:**

* `Threshold`: Entidad raíz que representa un límite configurable para una métrica de un tipo de sala, con propiedades `id`, `roomTypeId`, `metric`, `warnValue`, `criticalValue`, `sustainedMinutes` y `enabled`. Expone comportamiento de negocio propio: `isBreachedBy(value)` determina si una medida supera el valor de aviso, e `isCriticalFor(value)` si supera el valor crítico.

**Value Objects:**

* `ThresholdMetric`: Enum cerrado de las magnitudes sobre las que se puede configurar un umbral (`LAEQ`, `L10`, `PPD`, `OCCUPIED_PCT`, `TEMP_C`), con conversión a/desde su representación persistida en minúsculas.
* `RoomProfile`: Representación mínima de una sala (código y tipo) usada exclusivamente dentro de este contexto; es la traducción anticorrupción de lo que Monitoring expone como sala.

**Aggregates:**

* `Threshold` actúa a la vez como entidad y como raíz de agregado, porque no tiene entidades hijas que requieran una consistencia transaccional adicional.
* `Alert`: agregado que representa una alerta de una sala, identificada por la clave de origen (`sourceKey`) que envía la Edge API. Guarda la regla, la severidad, el mensaje, el valor medido, los instantes de apertura y cierre, y el responsable, el instante y la acción correctiva del reconocimiento. Sus reglas son que solo se reconoce una alerta abierta, que la acción correctiva tiene entre 3 y 500 caracteres, que un evento repetido no crea otra alerta y que el cierre es idempotente.

**Value Objects de las alertas:** `AlertStatus` (`OPEN`, `ACKNOWLEDGED`, `CLOSED`), `AlertSeverity` (`INFO`, `WARNING`, `CRITICAL`) y `AlertClosure` (`AUTO`, `MANUAL`).

**Domain Services:**

* No se define ningún servicio de dominio propio; la lógica de evaluación vive en los métodos del propio `Threshold`.

**Repositories (Interfaces):**

* `ThresholdRepository`: Puerto de persistencia con `save`, `findEnabledByRoomTypeId` y `findByRoomTypeIdAndMetric`.
* `RoomProfileProvider`: Puerto de salida que declara la necesidad de conocer las salas y su tipo, sin saber que quien la satisface es Monitoring (capa anticorrupción).

* `AlertRepository`: Puerto de persistencia de las alertas con `save`, `findById`, `findBySourceKey` y `search`.
* `RoomDirectory`: Puerto de salida que traduce el código del local y de la sala que envía la Edge API al identificador de la sala.

**Domain Errors:**

* `AlertingError`: Catálogo de errores del contexto (`UNKNOWN_THRESHOLD_METRIC`, `INVALID_THRESHOLD_RANGE`, `ALERT_NOT_FOUND`, `ALERT_NOT_OPEN`, `CORRECTIVE_ACTION_REQUIRED`, `ALERT_BATCH_EMPTY`, `ALERT_CLOSED_BEFORE_OPENED`, `UNKNOWN_ALERT_SEVERITY`, `UNKNOWN_ALERT_STATUS`, `INVALID_ALERT_RULE`, `RANGE_INVERTED`).

<a id="4212-interface-layer"></a>
#### <i>**4.2.1.2. Interface Layer.**</i>

Controllers:

* `ThresholdsController`: Expone `/api/v1/room-types/{roomTypeId}/thresholds` para configurar (`PUT /{metric}`, protegido a `ADMIN`) y listar (`GET`, `ADMIN`/`MEMBER`) los umbrales de un tipo de sala.
* `RoomThresholdsController`: Expone `GET /api/v1/room-thresholds`, resuelto por sala (no por tipo) para que el Edge pueda consultar sin conocer la taxonomía de tipos; protegido con el scope de máquina `SCOPE_thresholds:read`.
* `AlertEventsController`: Expone `POST /api/v1/alerts/events`, por el que la Edge API informa las alertas que abre y cierra, protegido con el scope de máquina `SCOPE_alerts:write`.
* `AlertsController`: Expone `GET /api/v1/alerts`, `GET /api/v1/alerts/{alertId}` y `PATCH /api/v1/alerts/{alertId}/acknowledge`, reservados a `ADMIN`.

<a id="4213-application-layer"></a>
#### <i>**4.2.1.3. Application Layer.**</i>

**Command Services:**

* `ConfigureThresholdUseCaseImpl`: Crea o reajusta el umbral de una métrica para un tipo de sala; la operación es idempotente.
* `RecordAlertEventsUseCaseImpl`: Registra el lote de eventos de la Edge API. Un evento con una clave conocida actualiza la alerta, y un evento con instante de cierre la cierra. Si una sala del lote no existe, no se guarda ningún evento.
* `AcknowledgeAlertUseCaseImpl`: Reconoce una alerta abierta con su acción correctiva y toma el responsable del token del usuario.

**Query Services:**

* `ListThresholdsUseCaseImpl`: Lista los umbrales activos de un tipo de sala.
* `ListAlertsUseCaseImpl` y `GetAlertUseCaseImpl`: Listan las alertas con filtros por estado, sala, fechas y presencia de acción correctiva, y consultan una alerta.
* `ResolveRoomThresholdsUseCaseImpl`: Traduce los umbrales configurados por tipo a los umbrales aplicables por sala concreta, cacheando por tipo para no repetir consultas.

**Outbound Services (ACL):**

* `ExternalMonitoringService`: Único punto del contexto que conoce a Monitoring; implementa `RoomProfileProvider` traduciendo las salas del otro contexto a `RoomProfile`.

<a id="4214-infrastructure-layer"></a>
#### <i>**4.2.1.4. Infrastructure Layer.**</i>

**Persistence/Repositories:**

* `ThresholdRepositoryImpl`: Implementación JPA de `ThresholdRepository`, apoyada en `ThresholdEntity`, `ThresholdMapper` y `ThresholdJpaRepository`.
* `AlertRepositoryImpl`: Implementación JPA de `AlertRepository`, apoyada en `AlertEntity`, `AlertMapper` y `AlertJpaRepository`.

**Configuration:**

* `AlertingErrorCatalogConfiguration`: Publica el catálogo `AlertingError` como bean `ErrorCatalogSource` para que los códigos de error del contexto sean resolubles globalmente.

<a id="4215-bounded-context-software-architecture-component-level-diagrams"></a>
#### <i>**4.2.1.5. Bounded Context Software Architecture Component Level Diagrams.**</i>

La solución despliega un único container para los servicios en la nube —la aplicación `cloud-api`, construida con Spring Boot 4 sobre Java 21—, dentro del cual cada bounded context ocupa su propio paquete y no comparte clases con los demás. El diagrama descompone ese container en los componentes de Alerting, agrupados por la capa a la que pertenecen, e indica para cada uno su tecnología y su responsabilidad.

<p align="center"><em>Figura 50.</em> Diagrama de componentes del bounded context Alerting dentro del container cloud-api.</p>

```mermaid
flowchart TB
    admin["Administrador<br/>[Web App]"]
    edge["Edge API<br/>[Flask, en el local]"]

    subgraph cont["Container: cloud-api — Spring Boot 4, Java 21"]
        direction TB
        subgraph il["Interface Layer"]
            tc["ThresholdsController<br/>[Spring MVC]<br/>Configura y lista umbrales por tipo de sala"]
            rtc["RoomThresholdsController<br/>[Spring MVC]<br/>Resuelve umbrales por sala concreta"]
        end
        subgraph al["Application Layer"]
            cfg["ConfigureThresholdUseCaseImpl<br/>[Spring Bean]<br/>Alta o reajuste idempotente"]
            lst["ListThresholdsUseCaseImpl<br/>[Spring Bean]<br/>Umbrales activos de un tipo"]
            rsv["ResolveRoomThresholdsUseCaseImpl<br/>[Spring Bean]<br/>Traduce de tipo a sala, cacheando por tipo"]
            acl["ExternalMonitoringService<br/>[Anti-corruption Layer]<br/>Implementa RoomProfileProvider"]
        end
        subgraph dl["Domain Layer"]
            th["Threshold<br/>[POJO]<br/>Decide si una medida incumple el límite"]
        end
        subgraph inf["Infrastructure Layer"]
            repo["ThresholdRepositoryImpl<br/>[Spring Data JPA]<br/>Persiste y consulta umbrales"]
        end
    end

    mon["MonitoringContextFacade<br/>[bounded context Monitoring]"]
    db[("PostgreSQL<br/>esquema alerting")]

    admin -->|"HTTPS/JSON, JWT rol ADMIN"| tc
    edge -->|"HTTPS/JSON, scope thresholds:read"| rtc
    tc --> cfg
    tc --> lst
    rtc --> rsv
    cfg --> th
    rsv --> th
    rsv --> acl
    acl -->|"solo lectura"| mon
    cfg --> repo
    lst --> repo
    rsv --> repo
    repo -->|"JDBC"| db
```

El contexto expone dos controladores porque atiende a dos consumidores con necesidades distintas. El administrador configura umbrales **por tipo de sala**, que es como se razona el negocio: todas las cabinas de llamadas comparten límite. El Edge, en cambio, evalúa **por sala concreta** y no conoce la taxonomía de tipos, de modo que `ResolveRoomThresholdsUseCaseImpl` hace la traducción y cachea por tipo para no repetir la consulta una vez por sala. `ExternalMonitoringService` es el único componente que conoce la existencia de Monitoring, y lo hace a través de su fachada, nunca de sus repositorios.


<a id="4216-bounded-context-software-architecture-code-level-diagrams"></a>
#### <i>**4.2.1.6. Bounded Context Software Architecture Code Level Diagrams.**</i>

El nivel de código detalla la implementación del contexto en dos diagramas: el de clases del Domain Layer, que describe el modelo y sus relaciones, y el de base de datos, que describe cómo se persiste.


<a id="42161-bounded-context-domain-layer-class-diagrams"></a>
##### <i>**4.2.1.6.1. Bounded Context Domain Layer Class Diagrams.**</i>

El diagrama recoge las clases del Domain Layer de Alerting, con sus atributos, sus métodos y el ámbito de cada miembro. La entidad `Threshold` concentra el comportamiento —decidir si una medida incumple— y el resto del modelo son value objects, comandos y los puertos que el dominio declara para no depender de la infraestructura ni de otros contextos.

<p align="center"><em>Figura 51.</em> Diagrama de clases del Domain Layer del bounded context Alerting.</p>

```mermaid
classDiagram
    direction LR

    class Threshold {
        -UUID id
        -UUID roomTypeId
        -ThresholdMetric metric
        -float warnValue
        -Float criticalValue
        -int sustainedMinutes
        -boolean enabled
        +Threshold(ConfigureThresholdCommand command)
        +handle(ConfigureThresholdCommand command) void
        +isBreachedBy(Float value) boolean
        +isCriticalFor(Float value) boolean
    }

    class ThresholdMetric {
        <<enumeration>>
        LAEQ
        L10
        PPD
        OCCUPIED_PCT
        TEMP_C
        +toCode() String
        +fromCode(String code)$ ThresholdMetric
    }

    class RoomProfile {
        <<value object>>
        +String code
        +UUID roomTypeId
        +isClassified() boolean
    }

    class ConfigureThresholdCommand {
        <<command>>
        +UUID roomTypeId
        +ThresholdMetric metric
        +float warnValue
        +Float criticalValue
        +int sustainedMinutes
        +boolean enabled
    }

    class ListThresholdsQuery {
        <<query>>
        +UUID roomTypeId
    }

    class AlertingError {
        <<enumeration>>
        UNKNOWN_THRESHOLD_METRIC
        INVALID_THRESHOLD_RANGE
        +code() String
        +kind() ErrorKind
        +messageTemplate() String
    }

    class ThresholdRepository {
        <<interface>>
        +save(Threshold threshold) Threshold
        +findEnabledByRoomTypeId(UUID roomTypeId) List~Threshold~
        +findByRoomTypeIdAndMetric(UUID roomTypeId, ThresholdMetric metric) Optional~Threshold~
    }

    class RoomProfileProvider {
        <<interface>>
        +rooms() List~RoomProfile~
    }

    Threshold "0..*" --> "1" ThresholdMetric : se configura sobre
    ConfigureThresholdCommand "1" --> "1" ThresholdMetric : indica
    Threshold ..> ConfigureThresholdCommand : se crea y reajusta con
    ConfigureThresholdCommand ..> AlertingError : valida el rango con
    ThresholdMetric ..> AlertingError : rechaza códigos desconocidos con
    ThresholdRepository ..> Threshold : persiste
    RoomProfileProvider ..> RoomProfile : entrega
```

`Threshold` es a la vez entidad y raíz de agregado: no contiene entidades hijas, y su identidad y su tipo de sala son inmutables, porque cambiar cualquiera de los dos significa que el umbral es otro. Los métodos `isBreachedBy` e `isCriticalFor` responden únicamente por el valor; la comprobación de que el incumplimiento se sostenga durante `sustainedMinutes` no vive en la entidad, ya que un umbral conoce su propio límite pero no la serie temporal que lo pone a prueba.

Los dos puertos de salida separan responsabilidades distintas. `ThresholdRepository` abstrae la persistencia del propio contexto. `RoomProfileProvider`, en cambio, declara una necesidad que satisface otro contexto: Alerting necesita saber qué salas existen y de qué tipo son, y lo expresa con `RoomProfile`, un vocabulario reducido a lo que aquí significa algo. La sala de Monitoring tiene aforo, planta y superficie; ninguno de esos atributos interviene en la evaluación de un umbral, y copiarlos convertiría la capa anticorrupción en un trámite.


<a id="42162-bounded-context-database-design-diagram"></a>
##### <i>**4.2.1.6.2. Bounded Context Database Design Diagram.**</i>

El bounded context persiste en el esquema Alerting de PostgreSQL, con dos tablas, `threshold` y `alert`. Los umbrales viven en la base de datos y no en el código para que la administración pueda ajustarlos desde la aplicación web sin volver a desplegar el servicio.

<p align="center"><em>Figura 52.</em> Diagrama de base de datos del bounded context Alerting.</p>

```mermaid
erDiagram
    ROOM_TYPE ||--o{ THRESHOLD : "room_type_id"

    ROOM_TYPE {
        uuid id PK "esquema monitoring, fuera de este bounded context"
    }

    THRESHOLD {
        uuid id PK
        uuid room_type_id "NOT NULL, referencia lógica, sin clave foránea"
        varchar metric "NOT NULL, 24, valor persistido en minúsculas"
        real warn_value "NOT NULL"
        real critical_value "NULL, opcional"
        integer sustained_minutes "NOT NULL, DEFAULT 2"
        boolean enabled "NOT NULL, DEFAULT TRUE"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    ALERT {
        uuid id PK
        varchar source_key UK "NOT NULL, 120"
        uuid room_id "NOT NULL, referencia lógica"
        varchar rule "NOT NULL, 40"
        varchar severity "NOT NULL, 16"
        varchar message "NOT NULL, 200"
        double value "NULL"
        varchar status "NOT NULL, 16"
        timestamptz opened_at "NOT NULL"
        timestamptz closed_at "NULL"
        varchar closed_by "NULL, 8"
        timestamptz acknowledged_at "NULL"
        uuid acknowledged_by "NULL"
        varchar corrective_action "NULL, 500"
    }
```

La columna `room_type_id` es la única referencia de la tabla y **no lleva clave foránea**, a diferencia del resto del modelo de datos de la solución. La tabla a la que apunta, `room_type`, pertenece al esquema Monitoring, y declarar una restricción física entre ambos esquemas ataría los dos bounded contexts a nivel de base de datos: cualquier cambio en la estructura de salas obligaría a coordinar un despliegue conjunto, y el límite entre contextos dejaría de ser real. La integridad se mantiene en la capa de aplicación, a través del puerto `RoomProfileProvider` descrito en el Domain Layer, que es la única vía por la que este contexto conoce las salas.

El par `room_type_id` y `metric` identifica un umbral de forma única en la práctica: el caso de uso de configuración es idempotente y reajusta el umbral existente en lugar de crear uno nuevo. Las columnas de auditoría —`created_at`, `updated_at`, `deleted_at`, `created_by` y `updated_by`— las gestiona Spring Data JPA Auditing, razón por la cual no llevan valor por defecto en el esquema, y `deleted_at` implementa el borrado lógico que preserva el histórico de configuración.


<a id="422-bounded-context"></a>

La tabla `alert` tiene una restricción de unicidad sobre `source_key`, que evita duplicados cuando la Edge API reintenta el envío, y dos índices, por sala y fecha de apertura y por estado y fecha de apertura. Su columna `room_id` tampoco lleva clave foránea, porque la sala pertenece al esquema Monitoring y se valida a través de su fachada.


### 4.2.2. Bounded Context: IAM

Gestiona la identidad y el acceso de los dos tipos de consumidores de la plataforma: las personas (administradores y miembros del coworking, autenticados por email y contraseña con emisión de JWT) y las máquinas (el Edge de cada local, autenticado mediante API keys con *scopes* como `readings:write` o `thresholds:read`). Es el contexto que hace cumplir la separación de responsabilidades entre quien configura el sistema y quien únicamente sube o consume telemetría.

<a id="4221-domain-layer"></a>
#### <i>**4.2.2.1. Domain Layer.**</i>

Contiene las reglas de identidad, autenticación y credenciales de acceso, tanto para personas como para máquinas (el Edge).

**Aggregates:**

* `User`: Representa una persona con acceso al sistema, con `id`, `email`, `passwordHash`, `displayName`, `active` y `roles`. Encapsula `ensureCanSignIn()`, que lanza error de negocio si la cuenta está desactivada.
* `ApiCredential`: Representa la credencial de una máquina (el Edge), con `id`, `code`, `tokenHash`, `active` y `scopes`. Encapsula `ensureUsable()`, que rechaza credenciales revocadas.

**Value Objects:**

* `Role`: Enum de lo que puede hacer una persona (`MEMBER`, `ADMIN`).
* `Scope`: Enum de lo que puede hacer una máquina (`READINGS_WRITE`, `THRESHOLDS_READ`).
* `IssuedToken`: Token recién emitido junto a su tiempo de expiración en segundos.

**Domain Services (Ports out):**

* `PasswordHasher`: Contrato para cifrar y comparar contraseñas en tiempo constante.
* `ApiKeyHasher`: Contrato para generar claves de máquina y reducirlas a un hash determinista (indexable, sin sal).
* `TokenIssuer`: Contrato para emitir la credencial (JWT) con la que un usuario demuestra su identidad en peticiones subsecuentes.

**Repositories (Interfaces):**

* `UserRepository`: `save`, `findById`, `findByEmail`, `existsByEmail`.
* `ApiCredentialRepository`: `save`, `findByTokenHash`, `existsByCode`.

**Domain Errors:**

* `IamError`: Catálogo de errores (`EMAIL_ALREADY_USED`, `USER_NOT_FOUND`, `INVALID_CREDENTIALS`, `ACCOUNT_DISABLED`, `CREDENTIAL_CODE_ALREADY_USED`, `CREDENTIAL_REVOKED`, `UNKNOWN_SCOPE`).

<a id="4222-interface-layer"></a>
#### <i>**4.2.2.2. Interface Layer.**</i>

**Controllers:**

* `AuthController`: Expone `POST /api/v1/auth/login`; el mismo error de credenciales cubre email inexistente o contraseña incorrecta, para no revelar qué cuentas existen.
* `UsersController`: Expone `POST /api/v1/users` para el registro público, que siempre crea la cuenta con rol `MEMBER`, `GET /api/v1/users` y `PATCH /api/v1/users/{userId}`, con el que un `ADMIN` desactiva o reactiva una cuenta.
* `CredentialsController`: Expone `POST /api/v1/credentials`, protegido a `ADMIN`, para emitir credenciales de máquina; la clave en claro se devuelve una única vez.

<a id="4223-application-layer"></a>
#### <i>**4.2.2.3. Application Layer.**</i>

**Command Services:**

* `RegisterUserUseCaseImpl`: Registra una cuenta, validando unicidad de correo y delegando el hash de la contraseña.
* `CreateApiCredentialUseCaseImpl`: Genera y persiste una credencial de máquina con sus scopes.

**Query/Authentication Services:**

* `AuthenticateUserUseCaseImpl`: Valida email y contraseña y emite el `IssuedToken` (login).
* `AuthenticateApiKeyUseCaseImpl`: Resuelve el dueño de una API key a partir de su hash, filtrando credenciales inactivas.

<a id="4224-infrastructure-layer"></a>
#### <i>**4.2.2.4. Infrastructure Layer.**</i>

**Persistence/Repositories:**

* `UserRepositoryImpl` / `ApiCredentialRepositoryImpl`: Implementaciones JPA sobre `UserEntity`/`ApiCredentialEntity`, con sus respectivos mappers y repositorios Spring Data.

**External/Security Services:**

* `BCryptPasswordHasher`: Implementación de `PasswordHasher` sobre BCrypt.
* `Sha256ApiKeyHasher`: Implementación determinista de `ApiKeyHasher` para claves de máquina.
* `ActiveAccountJwtConverter` y `UserStatusCache`: Comprueban en cada petición que la cuenta del token sigue activa y responden 401 `IAM_ACCOUNT_DISABLED` en caso contrario. El estado se guarda en caché durante 30 segundos.
* `JwtTokenIssuer`: Implementación de `TokenIssuer`, emite JWT firmados (RS256) con claims de email, nombre y roles.
* `ApiKeyAuthenticationFilter`, `SecurityConfiguration`, `JwtConfiguration`: Configuración de Spring Security para autenticar tanto usuarios (JWT) como máquinas (API key) sobre la misma cadena de filtros.

**Configuration:**

* `IamErrorCatalogConfiguration`: Publica el catálogo `IamError`.

<a id="4225-bounded-context-software-architecture-component-level-diagrams"></a>
#### <i>**4.2.2.5. Bounded Context Software Architecture Component Level Diagrams.**</i>

La solución despliega un único container para los servicios en la nube —la aplicación `cloud-api`, construida con Spring Boot 4 sobre Java 21—, dentro del cual cada bounded context ocupa su propio paquete y no comparte clases con los demás. El diagrama descompone ese container en los componentes de IAM, agrupados por la capa a la que pertenecen, e indica para cada uno su tecnología y su responsabilidad.

<p align="center"><em>Figura 53.</em> Diagrama de componentes del bounded context IAM dentro del container cloud-api.</p>

```mermaid
flowchart TB
    persona["Persona<br/>[Web App o Mobile App]"]
    maquina["Edge API<br/>[Flask, en el local]"]

    subgraph cont["Container: cloud-api — Spring Boot 4, Java 21"]
        direction TB
        subgraph sec["Cadena de filtros de seguridad"]
            filt["ApiKeyAuthenticationFilter<br/>[Spring Security]<br/>Autentica máquinas por API key"]
            cfgsec["SecurityConfiguration + JwtConfiguration<br/>[OAuth2 Resource Server]<br/>Valida el JWT de las personas"]
        end
        subgraph il["Interface Layer"]
            auth["AuthController<br/>[Spring MVC]<br/>Inicio de sesión"]
            users["UsersController<br/>[Spring MVC]<br/>Registro público de cuentas"]
            creds["CredentialsController<br/>[Spring MVC]<br/>Emite credenciales de máquina"]
        end
        subgraph al["Application Layer"]
            reg["RegisterUserUseCaseImpl<br/>[Spring Bean]<br/>Alta con correo único"]
            autu["AuthenticateUserUseCaseImpl<br/>[Spring Bean]<br/>Verifica contraseña y emite token"]
            autk["AuthenticateApiKeyUseCaseImpl<br/>[Spring Bean]<br/>Resuelve la credencial por su hash"]
            crea["CreateApiCredentialUseCaseImpl<br/>[Spring Bean]<br/>Genera clave y alcances"]
        end
        subgraph dl["Domain Layer"]
            usr["User / ApiCredential<br/>[POJO]<br/>Deciden si la identidad puede operar"]
        end
        subgraph inf["Infrastructure Layer"]
            bcrypt["BCryptPasswordHasher<br/>[Spring Security Crypto]<br/>Hash lento con sal"]
            sha["Sha256ApiKeyHasher<br/>[SHA-256]<br/>Hash determinista, indexable"]
            jwt["JwtTokenIssuer<br/>[Nimbus JOSE]<br/>Firma el token de sesión"]
            repos["UserRepositoryImpl / ApiCredentialRepositoryImpl<br/>[Spring Data JPA]<br/>Persisten identidades"]
        end
    end

    db[("PostgreSQL<br/>esquema iam")]

    persona -->|"HTTPS/JSON"| auth
    persona -->|"HTTPS/JSON"| users
    persona -->|"HTTPS/JSON, JWT rol ADMIN"| creds
    maquina -->|"cabecera con API key"| filt
    persona -.->|"cabecera Authorization"| cfgsec
    filt --> autk
    auth --> autu
    users --> reg
    creds --> crea
    reg --> usr
    autu --> usr
    autk --> usr
    reg --> bcrypt
    autu --> bcrypt
    autu --> jwt
    crea --> sha
    autk --> sha
    reg --> repos
    autu --> repos
    autk --> repos
    crea --> repos
    repos -->|"JDBC"| db
```

Los dos caminos de autenticación conviven en la misma cadena de filtros y terminan en el mismo modelo de dominio, pero no comparten mecanismo de verificación. La persona presenta correo y contraseña una vez y recibe un token firmado que acompaña a las peticiones siguientes; la máquina presenta su clave en cada petición, y por eso su hash debe ser determinista e indexable. Esa asimetría es la que justifica que `BCryptPasswordHasher` y `Sha256ApiKeyHasher` sean componentes distintos y no dos usos de uno solo.


<a id="4226-bounded-context-software-architecture-code-level-diagrams"></a>
#### <i>**4.2.2.6. Bounded Context Software Architecture Code Level Diagrams.**</i>

El nivel de código detalla la implementación del contexto en dos diagramas: el de clases del Domain Layer, que describe el modelo y sus relaciones, y el de base de datos, que describe cómo se persiste.


<a id="42261-bounded-context-domain-layer-class-diagrams"></a>
##### <i>**4.2.2.6.1. Bounded Context Domain Layer Class Diagrams.**</i>

El Domain Layer de IAM modela dos identidades que el sistema trata por separado: la persona, representada por `User`, y la máquina, representada por `ApiCredential`. Cada una tiene su propio catálogo de permisos —`Role` para lo que puede hacer una persona, `Scope` para lo que puede hacer el Edge— y su propio mecanismo de verificación, declarado como puerto para que el dominio no dependa de una biblioteca criptográfica concreta.

<p align="center"><em>Figura 54.</em> Diagrama de clases del Domain Layer del bounded context IAM.</p>

```mermaid
classDiagram
    direction LR

    class User {
        -UUID id
        -String email
        -String passwordHash
        -String displayName
        -boolean active
        -Set~Role~ roles
        +User(String email, String passwordHash, String displayName, Set~Role~ roles)
        +hasRole(Role role) boolean
        +ensureCanSignIn() void
    }

    class ApiCredential {
        -UUID id
        -String code
        -String tokenHash
        -boolean active
        -Set~Scope~ scopes
        +ApiCredential(String code, String tokenHash, Set~Scope~ scopes)
        +ensureUsable() void
    }

    class Role {
        <<enumeration>>
        MEMBER
        ADMIN
        +toCode() String
        +fromCode(String code)$ Role
    }

    class Scope {
        <<enumeration>>
        READINGS_WRITE
        THRESHOLDS_READ
        -String code
        +toCode() String
        +fromCode(String code)$ Scope
    }

    class IssuedToken {
        <<value object>>
        +String value
        +long expiresInSeconds
    }

    class RegisterUserCommand {
        <<command>>
        +String email
        +String plainPassword
        +String displayName
        +Set~Role~ roles
    }

    class IamError {
        <<enumeration>>
        EMAIL_ALREADY_USED
        USER_NOT_FOUND
        INVALID_CREDENTIALS
        ACCOUNT_DISABLED
        CREDENTIAL_CODE_ALREADY_USED
        CREDENTIAL_REVOKED
        UNKNOWN_SCOPE
        +code() String
        +kind() ErrorKind
        +messageTemplate() String
    }

    class UserRepository {
        <<interface>>
        +save(User user) User
        +findById(UUID id) Optional~User~
        +findByEmail(String email) Optional~User~
        +existsByEmail(String email) boolean
    }

    class ApiCredentialRepository {
        <<interface>>
        +save(ApiCredential credential) ApiCredential
        +findByTokenHash(String tokenHash) Optional~ApiCredential~
        +existsByCode(String code) boolean
    }

    class PasswordHasher {
        <<interface>>
        +hash(String plainPassword) String
        +matches(String plainPassword, String hash) boolean
    }

    class ApiKeyHasher {
        <<interface>>
        +generate() String
        +hash(String apiKey) String
    }

    class TokenIssuer {
        <<interface>>
        +issueFor(User user) IssuedToken
    }

    User "1" --> "1..*" Role : tiene concedidos
    ApiCredential "1" --> "1..*" Scope : tiene concedidos
    RegisterUserCommand "1" --> "1..*" Role : solicita
    User ..> RegisterUserCommand : se crea con
    User ..> IamError : rechaza el acceso con
    ApiCredential ..> IamError : rechaza la credencial con
    Scope ..> IamError : rechaza códigos desconocidos con
    TokenIssuer ..> IssuedToken : emite
    TokenIssuer ..> User : acredita a
    UserRepository ..> User : persiste
    ApiCredentialRepository ..> ApiCredential : persiste
    PasswordHasher ..> User : verifica la contraseña de
    ApiKeyHasher ..> ApiCredential : verifica la clave de
```

La separación entre persona y máquina no es cosmética: determina cómo se guarda cada secreto. La contraseña de una persona se cifra con un algoritmo lento y con sal, de modo que dos cuentas con la misma contraseña producen hashes distintos; la clave del Edge, en cambio, se reduce a un hash determinista, porque el sistema necesita localizar la credencial a partir de la clave que llega en cada petición, y eso exige una columna indexable. Esa diferencia justifica que existan dos puertos, `PasswordHasher` y `ApiKeyHasher`, en lugar de uno solo.

Ambos agregados guardan su identificador y su código de forma inmutable y exponen un método que decide si la credencial sirve: `ensureCanSignIn` en el caso de la persona y `ensureUsable` en el de la máquina. La comprobación vive en el dominio y no en la capa de seguridad para que una cuenta desactivada o una credencial revocada se rechacen por la misma regla, con independencia de por dónde llegue la petición.


<a id="42262-bounded-context-database-design-diagram"></a>
##### <i>**4.2.2.6.2. Bounded Context Database Design Diagram.**</i>

El bounded context persiste en el esquema IAM, con cuatro tablas: una por cada identidad y una tabla de unión por cada catálogo de permisos, ya que tanto los roles de una persona como los alcances de una máquina son conjuntos.

<p align="center"><em>Figura 55.</em> Diagrama de base de datos del bounded context IAM.</p>

```mermaid
erDiagram
    USER_ACCOUNT ||--o{ USER_ROLE : "concede"
    API_CREDENTIAL ||--o{ API_CREDENTIAL_SCOPE : "concede"

    USER_ACCOUNT {
        uuid id PK
        varchar email "NOT NULL, 160, único por LOWER(email) si no está borrada"
        varchar password_hash "NOT NULL, 72, BCrypt"
        varchar display_name "NOT NULL, 128"
        boolean active "NOT NULL, DEFAULT TRUE"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    USER_ROLE {
        uuid user_id PK, FK "NOT NULL, ON DELETE CASCADE"
        varchar role PK "NOT NULL, 32"
    }

    API_CREDENTIAL {
        uuid id PK
        varchar code "NOT NULL, 64, único por LOWER(code) si no está borrada"
        varchar token_hash "NOT NULL, 64, único, SHA-256"
        boolean active "NOT NULL, DEFAULT TRUE"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    API_CREDENTIAL_SCOPE {
        uuid credential_id PK, FK "NOT NULL, ON DELETE CASCADE"
        varchar scope PK "NOT NULL, 48"
    }
```

Las dos tablas de unión llevan clave primaria compuesta —`(user_id, role)` y `(credential_id, scope)`—, lo que impide conceder dos veces el mismo permiso sin necesidad de una restricción adicional, y se borran en cascada con su identidad: un rol sin persona a la que pertenecer no significa nada.

Los índices únicos son parciales y merecen atención. `ux_user_account_email` se declara sobre `LOWER(email)` y solo sobre las filas cuyo `deleted_at` es nulo: el correo no distingue mayúsculas a efectos de identidad, y una cuenta dada de baja no debe bloquear el alta de otra con el mismo correo. `ux_api_credential_token`, en cambio, es total y sin condición, porque el hash del token se consulta en cada petición del Edge y debe resolverse por índice aunque la credencial esté revocada; solo así el rechazo de una credencial revocada puede explicarse con el error correspondiente en lugar de confundirse con una clave inexistente.

El tamaño de `password_hash` está fijado en 72 caracteres, que es la longitud de un hash BCrypt, y el de `token_hash` en 64, la de un SHA-256 en hexadecimal. Ninguna de las dos columnas guarda el secreto en claro: la clave de máquina se muestra una sola vez, en la respuesta a su creación, y no vuelve a ser recuperable.


<a id="423-bounded-context"></a>
### 4.2.3. Bounded Context: Insights

Es el contexto analítico: no captura telemetría, sino que la recibe ya calculada desde Monitoring a través de una capa anticorrupción y le aplica estadística (correlación de Pearson, regresión lineal, detección de anomalías por z-score) para responder preguntas que requieren historia larga, como si el ruido de una sala proviene de la ocupación o del ambiente, o si su temperatura sigue a la del exterior por un mal aislamiento. Complementa esa serie con observaciones periódicas del clima externo (OpenWeather) para poder correlacionar interior y exterior, y siempre acompaña cada conclusión con el tamaño de muestra que la respalda, rechazando períodos con datos insuficientes.

<a id="4231-domain-layer"></a>
#### <i>**4.2.3.1. Domain Layer.**</i>

Este contexto no gestiona telemetría cruda; consume series ya calculadas y produce conclusiones estadísticas sobre el confort de una sala.

**Aggregates:**

* `WeatherObservation`: Medición histórica del clima exterior, con `observedAt`, `tempC`, `rhPct` y `condition`.

**Value Objects:**

* `ReadingPoint`: Un punto reducido de la serie temporal de una sala (`ts`, `laeq`, `backgroundNoise`, `tempC`, `ppd`, `occupiedPct`); es el vocabulario propio del contexto, independiente del agregado `RoomReading` de Monitoring.
* `Correlation`: Coeficiente de Pearson entre dos series junto al tamaño de muestra, con `isReliable()` y `strength()` (negligible/weak/moderate/strong).
* `Trend`: Recta ajustada por mínimos cuadrados (`slopePerHour`, `rSquared`, `sampleSize`), con criterio propio de fiabilidad.
* `RoomAnalytics`: Resultado agregado del análisis de una sala en un periodo (ruido vs. ocupación, deriva térmica, interior vs. exterior, anomalías de ruido).

**Domain Services:**

* `ComfortAnalyticsService`: Servicio de dominio puro (sin persistencia) que calcula correlaciones de Pearson, regresión lineal simple y detección de anomalías por z-score sobre una serie de `ReadingPoint`.

**Repositories/Ports (Interfaces):**

* `WeatherObservationRepository`: Persistencia del histórico de clima exterior.
* `ReadingSeriesProvider`: Puerto de salida (ACL) que declara la necesidad de series de lecturas, sin saber que las provee Monitoring.
* `OutdoorWeatherProvider`: Puerto de salida (ACL) que declara la necesidad del clima actual, sin saber que lo sirve OpenWeather.

**Domain Errors:**

* `InsightsError`: Catálogo de errores (`RANGE_INVERTED`, `RANGE_TOO_SHORT`).

<a id="4232-interface-layer"></a>
#### <i>**4.2.3.2. Interface Layer.**</i>

**Controllers:**

* `RoomAnalyticsController`: Expone `GET /api/v1/insights/rooms/{roomId}`, con rango `from`/`to` obligatorio; responde `422` cuando no hay suficientes datos para un análisis confiable.

<a id="4233-application-layer"></a>
#### <i>**4.2.3.3. Application Layer.**</i>

**Query Services:**

* `AnalyzeRoomUseCaseImpl`: Orquesta la obtención de la serie de lecturas y del clima exterior, y delega el cálculo estadístico en `ComfortAnalyticsService`; rechaza rangos con muestra insuficiente.

**Command/Scheduled Services:**

* `SampleOutdoorWeatherUseCaseImpl`: Toma una muestra puntual del proveedor de clima y la persiste, construyendo el histórico necesario para correlacionar hacia atrás.

**Outbound Services (ACL):**

* `ExternalMonitoringService`: Único punto del contexto que conoce a Monitoring; implementa `ReadingSeriesProvider` traduciendo `RoomReading` a `ReadingPoint`.

<a id="4234-infrastructure-layer"></a>
#### <i>**4.2.3.4. Infrastructure Layer.**</i>

**Persistence/Repositories:**

* `WeatherObservationRepositoryImpl`: Implementación JPA de `WeatherObservationRepository`.

**External Services:**

* `OpenWeatherAdapter` / `OpenWeatherClient`: Implementan `OutdoorWeatherProvider` consumiendo la API de OpenWeather, con DTOs de respuesta (`CurrentWeatherResponse`, `MainResponse`, `WeatherResponse`).
* `OutdoorWeatherSampler`: Tarea programada que invoca periódicamente `SampleOutdoorWeatherUseCase`.

**Configuration:**

* `InsightsErrorCatalogConfiguration`: Publica el catálogo `InsightsError`.

<a id="4235-bounded-context-software-architecture-component-level-diagrams"></a>
#### <i>**4.2.3.5. Bounded Context Software Architecture Component Level Diagrams.**</i>

La solución despliega un único container para los servicios en la nube —la aplicación `cloud-api`, construida con Spring Boot 4 sobre Java 21—, dentro del cual cada bounded context ocupa su propio paquete y no comparte clases con los demás. El diagrama descompone ese container en los componentes de Insights, agrupados por la capa a la que pertenecen, e indica para cada uno su tecnología y su responsabilidad.

<p align="center"><em>Figura 56.</em> Diagrama de componentes del bounded context Insights dentro del container cloud-api.</p>

```mermaid
flowchart TB
    admin["Administrador<br/>[Web App]"]
    reloj["Planificador<br/>[Spring Scheduling]"]

    subgraph cont["Container: cloud-api — Spring Boot 4, Java 21"]
        direction TB
        subgraph il["Interface Layer"]
            rac["RoomAnalyticsController<br/>[Spring MVC]<br/>Analítica de una sala en un rango"]
        end
        subgraph al["Application Layer"]
            ana["AnalyzeRoomUseCaseImpl<br/>[Spring Bean]<br/>Orquesta series, clima y cálculo"]
            smp["SampleOutdoorWeatherUseCaseImpl<br/>[Spring Bean]<br/>Toma y guarda una muestra de clima"]
            acl["ExternalMonitoringService<br/>[Anti-corruption Layer]<br/>Implementa ReadingSeriesProvider"]
        end
        subgraph dl["Domain Layer"]
            cas["ComfortAnalyticsService<br/>[Apache Commons Math 3.6.1]<br/>Pearson, regresión lineal y z-score"]
        end
        subgraph inf["Infrastructure Layer"]
            sampler["OutdoorWeatherSampler<br/>[Spring Scheduling]<br/>Dispara el muestreo periódico"]
            ow["OpenWeatherAdapter + OpenWeatherClient<br/>[Spring Cloud OpenFeign]<br/>Implementa OutdoorWeatherProvider"]
            repo["WeatherObservationRepositoryImpl<br/>[Spring Data JPA]<br/>Persiste el histórico de clima"]
        end
    end

    mon["MonitoringContextFacade<br/>[bounded context Monitoring]"]
    db[("PostgreSQL<br/>esquema insights")]
    api(["OpenWeather<br/>[servicio externo de terceros]"])

    admin -->|"HTTPS/JSON, JWT"| rac
    reloj --> sampler
    rac --> ana
    sampler --> smp
    ana --> acl
    acl -->|"solo lectura"| mon
    ana --> cas
    ana --> repo
    smp --> ow
    smp --> repo
    ow -->|"HTTPS/JSON"| api
    repo -->|"JDBC"| db
```

Este contexto es el que consume el **servicio externo de terceros** exigido por la arquitectura de la solución. La correlación entre temperatura interior y exterior solo puede calcularse hacia atrás si el histórico exterior existe, y OpenWeather sirve el clima actual, no el pasado; por eso `OutdoorWeatherSampler` acumula observaciones periódicamente en lugar de consultarlas en el momento del análisis. Si el servicio externo no responde, la analítica se degrada de forma controlada: el resto de indicadores se calcula igual y solo la correlación interior-exterior se declara sin datos suficientes.


<a id="4236-bounded-context-software-architecture-code-level-diagrams"></a>
#### <i>**4.2.3.6. Bounded Context Software Architecture Code Level Diagrams.**</i>

El nivel de código detalla la implementación del contexto en dos diagramas: el de clases del Domain Layer, que describe el modelo y sus relaciones, y el de base de datos, que describe cómo se persiste.


<a id="42361-bounded-context-domain-layer-class-diagrams"></a>
##### <i>**4.2.3.6.1. Bounded Context Domain Layer Class Diagrams.**</i>

El Domain Layer de Insights no contiene telemetría, sino los resultados de interpretarla. Su única pieza persistente es `WeatherObservation`; todo lo demás son value objects que expresan una conclusión estadística junto con la evidencia que la sostiene, y un servicio de dominio puro que los calcula.

<p align="center"><em>Figura 57.</em> Diagrama de clases del Domain Layer del bounded context Insights.</p>

```mermaid
classDiagram
    direction LR

    class WeatherObservation {
        -OffsetDateTime observedAt
        -Float tempC
        -Float rhPct
        -String condition
    }

    class ReadingPoint {
        <<value object>>
        +OffsetDateTime ts
        +Float laeq
        +Float backgroundNoise
        +Float tempC
        +Float ppd
        +Float occupiedPct
    }

    class Correlation {
        <<value object>>
        +Double coefficient
        +int sampleSize
        -int MINIMUM_SAMPLE$
        +insufficientData(int sampleSize)$ Correlation
        +isReliable() boolean
        +strength() String
    }

    class Trend {
        <<value object>>
        +Double slopePerHour
        +Double rSquared
        +int sampleSize
        -int MINIMUM_SAMPLE$
        -double MINIMUM_FIT$
        +insufficientData(int sampleSize)$ Trend
        +isReliable() boolean
    }

    class RoomAnalytics {
        <<value object>>
        +UUID roomId
        +OffsetDateTime from
        +OffsetDateTime to
        +int sampleSize
        +Correlation noiseVsOccupancy
        +Trend thermalDrift
        +Correlation indoorVsOutdoor
        +List~OffsetDateTime~ noiseAnomalies
    }

    class ComfortAnalyticsService {
        <<domain service>>
        +int MINIMUM_SAMPLE$
        -double ANOMALY_Z_SCORE$
        +analyze(UUID roomId, OffsetDateTime from, OffsetDateTime to, List~ReadingPoint~ series, List~WeatherObservation~ outdoor) RoomAnalytics
        -noiseVsOccupancy(List~ReadingPoint~ series) Correlation
        -thermalDrift(List~ReadingPoint~ series) Trend
        -indoorVsOutdoor(List~ReadingPoint~ series, List~WeatherObservation~ outdoor) Correlation
        -noiseAnomalies(List~ReadingPoint~ series) List~OffsetDateTime~
    }

    class AnalyzeRoomQuery {
        <<query>>
        +UUID roomId
        +OffsetDateTime from
        +OffsetDateTime to
    }

    class InsightsError {
        <<enumeration>>
        RANGE_INVERTED
        RANGE_TOO_SHORT
        +code() String
        +kind() ErrorKind
        +messageTemplate() String
    }

    class WeatherObservationRepository {
        <<interface>>
        +save(WeatherObservation observation) void
        +findInRange(OffsetDateTime from, OffsetDateTime to) List~WeatherObservation~
    }

    class ReadingSeriesProvider {
        <<interface>>
        +seriesOf(UUID roomId, OffsetDateTime from, OffsetDateTime to) List~ReadingPoint~
    }

    class OutdoorWeatherProvider {
        <<interface>>
        +fetchCurrent() Optional~WeatherObservation~
    }

    RoomAnalytics "1" --> "2" Correlation : ruido-ocupación e interior-exterior
    RoomAnalytics "1" --> "1" Trend : deriva térmica
    ComfortAnalyticsService ..> RoomAnalytics : produce
    ComfortAnalyticsService "1" ..> "0..*" ReadingPoint : analiza
    ComfortAnalyticsService "1" ..> "0..*" WeatherObservation : contrasta con
    AnalyzeRoomQuery ..> InsightsError : valida el rango con
    ReadingSeriesProvider ..> ReadingPoint : entrega
    OutdoorWeatherProvider ..> WeatherObservation : entrega
    WeatherObservationRepository ..> WeatherObservation : persiste
```

`Correlation` y `Trend` comparten un rasgo que ordena todo el contexto: **ninguna conclusión viaja sin su tamaño de muestra**. Ambos exponen `isReliable()` y un constructor estático `insufficientData`, de modo que la falta de datos es un resultado legítimo y no una excepción. Un coeficiente de correlación calculado sobre cinco minutos de lecturas es aritméticamente válido y estadísticamente inútil; obligar a que el valor viaje acompañado del número de muestras impide presentarlo como si significara algo. Por eso `Correlation.strength()` devuelve `insufficient_data` antes que una etiqueta cualitativa cuando no se alcanza el mínimo de treinta observaciones.

`ReadingPoint` es la traducción anticorrupción de la lectura de Monitoring: seis campos frente a los más de veinte del agregado original, porque el análisis estadístico solo necesita el instante y las magnitudes que correlaciona. `ComfortAnalyticsService` es un servicio de dominio puro —no consulta repositorios ni conoce la persistencia— y recibe las dos series ya resueltas, lo que permite ejercitarlo con datos sintéticos sin levantar la infraestructura.


<a id="42362-bounded-context-database-design-diagram"></a>
##### <i>**4.2.3.6.2. Bounded Context Database Design Diagram.**</i>

El bounded context persiste en el esquema Insights una sola tabla, y no es telemetría propia: es el histórico del clima exterior que el sistema va acumulando para poder correlacionarlo hacia atrás con las lecturas de cada sala.

<p align="center"><em>Figura 58.</em> Diagrama de base de datos del bounded context Insights.</p>

```mermaid
erDiagram
    WEATHER_OBSERVATION {
        uuid id PK
        timestamptz observed_at "NOT NULL, instante que describe la observación"
        real temp_c "NULL, temperatura exterior"
        real rh_pct "NULL, humedad relativa exterior"
        varchar condition "NULL, 64, descripción del proveedor"
        timestamptz fetched_at "NOT NULL, DEFAULT now(), instante de la consulta"
    }
```

La tabla no guarda ninguna referencia a salas ni a locales, y es deliberado: el clima exterior no pertenece a ninguna sala en particular, sino al momento. La correlación entre temperatura interior y exterior se resuelve en la capa de aplicación, emparejando cada observación con la lectura más próxima en el tiempo a través del puerto `ReadingSeriesProvider`. Persistir aquí una clave de Monitoring ataría los dos contextos sin ganar nada.

`observed_at` y `fetched_at` responden a preguntas distintas y por eso conviven: la primera es el instante que la observación describe, la segunda el instante en que el sistema la pidió al proveedor externo. Cuando el servicio meteorológico devuelve un dato con retraso o repite la última medición disponible, la diferencia entre ambas columnas lo delata, y permite descartar observaciones obsoletas sin perderlas.

La tabla tampoco lleva columnas de auditoría, por el mismo criterio que la telemetría de Monitoring: nadie edita ni borra una observación meteorológica, de modo que `created_by` y `updated_by` estarían vacías en todas las filas. Su trazabilidad es precisamente el par de marcas de tiempo.


<a id="424-bounded-context"></a>
### 4.2.4. Bounded Context: Monitoring

Es el *core domain* de la plataforma: administra la estructura física del negocio (locales, salas y sus tipos), los dispositivos IoT que reportan por cada sala, y recibe la telemetría agregada por minuto que sube el Edge, deduplicándola y autoprovisionando salas y dispositivos desconocidos. Expone además una fachada de anticorrupción (`MonitoringContextFacade`) que es la única puerta por la que Alerting e Insights acceden a sus datos, de modo que ningún otro contexto conoce sus repositorios ni su modelo interno.

<a id="4241-domain-layer"></a>
#### <i>**4.2.4.1. Domain Layer.**</i>

**Aggregates:**

* `Site`: Local físico (coworking) donde se instalan los dispositivos; modelado desde el inicio para soportar múltiples locales aunque hoy exista uno solo.
* `RoomType`: Clasifica las salas por actividad (p. ej. cabina de llamadas, zona común), que es lo que da sentido a los umbrales de Alerting.
* `Room`: Sala instrumentada, identificada por el `code` que reporta el firmware; nace activa y sin clasificar, y se autorregistra la primera vez que un dispositivo desconocido reporta por ella.
* `RoomReading`: Agregado por minuto de una sala (acústica, clima, confort, ocupación y calidad del dato), con `isReliable()` para excluir minutos incompletos de los cálculos estadísticos.

**Entities:**

* `Device`: Módulo ESP32 que reporta por una sala, con `lastSeen`, `lastSeq` y `lostBatches`; se mantiene separado de `Room` para que sustituir un módulo no le cueste a la sala su historial.

**Value Objects:**

* `AcousticMetrics`: Niveles de presión sonora ISO 1996 (`laeq`, `l10`, `l50`, `l90`, `lmax`, `lmin`), con `backgroundNoise()` e `intrusivePeaks()`.
* `Climate`: Temperatura y humedad relativa del sensor SHT31.
* `ThermalComfort`: Confort térmico ISO 7730 / Fanger (`pmv`, `ppd`, `verdict`), con `isAcceptable()` según ASHRAE 55.
* `Occupancy`: Porcentaje de ocupación y transiciones detectadas por el sensor de presencia mmWave.
* `DataQuality`: Lotes recibidos vs. esperados, para distinguir un minuto sólido de uno construido con datos incompletos.

**Domain Services:**

* No se define un servicio de dominio propio: los cálculos acústicos y de confort ya llegan resueltos desde el Edge, y el cloud solo agrega lo que necesita historia larga o varias salas (eso vive en Insights).

**Repositories (Interfaces):**

* `SiteRepository`, `RoomTypeRepository`, `RoomRepository`, `RoomReadingRepository`, `DeviceRepository`.

**Domain Errors:**

* `MonitoringError`: Catálogo de errores del contexto (`ROOM_NOT_FOUND`, `SITE_NOT_FOUND`, `ROOM_TYPE_FROM_ANOTHER_SITE`, `READING_BATCH_EMPTY`, `NO_SITE_AVAILABLE`, entre otros).

**Reportes de incomodidad:**

* `DiscomfortReport`: agregado que registra la molestia de un miembro en una sala (`DiscomfortCategory`: `NOISE`, `WARM`, `COLD`), con un comentario opcional y una copia de la última lectura de la sala si no tiene más de diez minutos. El mismo usuario puede informar la misma categoría en la misma sala una vez cada diez minutos.
* `DiscomfortReportRepository`: puerto de persistencia con `save`, `findLatest`, `search` y `findByUserId`.

<a id="4242-interface-layer"></a>
#### <i>**4.2.4.2. Interface Layer.**</i>

**Controllers:**

* `SitesController`: Expone `/api/v1/sites` para dar de alta y listar locales y sus tipos de sala.
* `RoomsController`: Expone `/api/v1/rooms` para listar salas (incluyendo las no clasificadas), consultarlas, obtener su serie temporal o su última lectura, y clasificarlas.
* `ReadingsController`: Expone `POST /api/v1/readings`, único punto de entrada de la telemetría subida por el Edge, protegido con el scope de máquina `SCOPE_readings:write`.

**Anti-Corruption Layer (saliente, hacia otros contextos):**

* `MonitoringContextFacade` / `MonitoringContextFacadeImpl`: Única superficie pública de este contexto hacia Alerting e Insights; delega en los casos de uso, nunca en los repositorios directamente.
* `DiscomfortReportsController`: Expone `POST /api/v1/discomfort-reports` y `GET /api/v1/discomfort-reports/mine` para `ADMIN` y `MEMBER`, y `GET /api/v1/discomfort-reports` y `/summary` para `ADMIN`.

<a id="4243-application-layer"></a>
#### <i>**4.2.4.3. Application Layer.**</i>

**Command Services:**

* `CreateSiteUseCaseImpl`, `CreateRoomTypeUseCaseImpl`, `ClassifyRoomUseCaseImpl`: Altas y clasificación, validando pertenencia al mismo local.
* `IngestReadingsUseCaseImpl`: Procesa el lote del Edge con tres responsabilidades: deduplica lecturas (entrega *at-least-once*), autoprovisiona salas y dispositivos desconocidos, y refleja el estado del dispositivo sin recalcular sus contadores.

**Query Services:**

* `ListSitesUseCaseImpl`, `ListRoomTypesUseCaseImpl`, `ListRoomsUseCaseImpl`, `ListUnclassifiedRoomsUseCaseImpl`, `GetRoomUseCaseImpl`, `GetLatestReadingUseCaseImpl`, `GetReadingsInRangeUseCaseImpl`.

`FileDiscomfortReportUseCaseImpl` registra el reporte con la lectura del momento, y `ListDiscomfortReportsUseCaseImpl` lista los reportes y los cuenta por sala y categoría.

<a id="4244-infrastructure-layer"></a>
#### <i>**4.2.4.4. Infrastructure Layer.**</i>

**Persistence/Repositories:**

* `SiteRepositoryImpl`, `RoomTypeRepositoryImpl`, `RoomRepositoryImpl`, `RoomReadingRepositoryImpl`, `DeviceRepositoryImpl`: Implementaciones JPA con sus entidades (`SiteEntity`, `RoomEntity`, `RoomReadingEntity`, `RoomTypeEntity`, `DeviceEntity`), mappers y repositorios Spring Data correspondientes.

**Configuration:**

* `DiscomfortReportRepositoryImpl`: Implementación JPA de `DiscomfortReportRepository`, apoyada en `DiscomfortReportEntity`, `DiscomfortReportMapper` y `DiscomfortReportJpaRepository`.

* `MonitoringErrorCatalogConfiguration`: Publica el catálogo `MonitoringError`.

<a id="4245-bounded-context-software-architecture-component-level-diagrams"></a>
#### <i>**4.2.4.5. Bounded Context Software Architecture Component Level Diagrams.**</i>

La solución despliega un único container para los servicios en la nube —la aplicación `cloud-api`, construida con Spring Boot 4 sobre Java 21—, dentro del cual cada bounded context ocupa su propio paquete y no comparte clases con los demás. El diagrama descompone ese container en los componentes de Monitoring, agrupados por la capa a la que pertenecen, e indica para cada uno su tecnología y su responsabilidad.

<p align="center"><em>Figura 59.</em> Diagrama de componentes del bounded context Monitoring dentro del container cloud-api.</p>

```mermaid
flowchart TB
    admin["Administrador<br/>[Web App]"]
    edge["Edge API<br/>[Flask, en el local]"]

    subgraph cont["Container: cloud-api — Spring Boot 4, Java 21"]
        direction TB
        subgraph il["Interface Layer"]
            sites["SitesController<br/>[Spring MVC]<br/>Alta y listado de locales y tipos de sala"]
            rooms["RoomsController<br/>[Spring MVC]<br/>Salas, series, última lectura y clasificación"]
            reads["ReadingsController<br/>[Spring MVC]<br/>Única entrada de la telemetría"]
            facade["MonitoringContextFacade<br/>[Anti-corruption Layer]<br/>Única superficie hacia otros contextos"]
        end
        subgraph al["Application Layer"]
            ing["IngestReadingsUseCaseImpl<br/>[Spring Bean]<br/>Deduplica, autoprovisiona y sincroniza"]
            alta["CreateSite / CreateRoomType / ClassifyRoom<br/>[Spring Bean]<br/>Altas y clasificación"]
            qry["ListRooms / GetRoom / GetLatestReading / GetReadingsInRange<br/>[Spring Bean]<br/>Consultas del panel"]
        end
        subgraph dl["Domain Layer"]
            agg["Site · RoomType · Room · Device · RoomReading<br/>[POJO]<br/>Estructura del local y telemetría por minuto"]
        end
        subgraph inf["Infrastructure Layer"]
            repos["Site/RoomType/Room/Device/RoomReading RepositoryImpl<br/>[Spring Data JPA]<br/>Persisten estructura y lecturas"]
        end
    end

    otros["Alerting e Insights<br/>[bounded contexts]"]
    db[("PostgreSQL<br/>esquema monitoring")]

    admin -->|"HTTPS/JSON, JWT"| sites
    admin -->|"HTTPS/JSON, JWT"| rooms
    edge -->|"HTTPS/JSON, scope readings:write"| reads
    otros -->|"llamada en proceso"| facade
    reads --> ing
    sites --> alta
    rooms --> alta
    rooms --> qry
    facade --> qry
    ing --> agg
    alta --> agg
    qry --> agg
    ing --> repos
    alta --> repos
    qry --> repos
    repos -->|"JDBC"| db
```

`ReadingsController` es el único punto por el que entra telemetría, y `IngestReadingsUseCaseImpl` concentra las tres responsabilidades que hacen tolerante la ingesta: deduplica por sala y minuto, porque el Edge entrega con garantía *at-least-once*; autoprovisiona la sala y el dispositivo cuando reportan por primera vez, de modo que instalar un módulo no exige configurar nada por adelantado; y refleja el estado del dispositivo descartando los lotes que llegan fuera de orden.

`MonitoringContextFacade` merece atención por su ubicación: vive en la Interface Layer, junto a los controladores REST, y no en la de aplicación. La razón es que cumple la misma función que un controlador —exponer el contexto al exterior— solo que su protocolo es una llamada en proceso en lugar de HTTP. Delega en los casos de uso y nunca en los repositorios, con lo que Alerting e Insights quedan sujetos a las mismas reglas de negocio que cualquier consumidor externo.


<a id="4246-bounded-context-software-architecture-code-level-diagrams"></a>
#### <i>**4.2.4.6. Bounded Context Software Architecture Code Level Diagrams.**</i>

El nivel de código detalla la implementación del contexto en dos diagramas: el de clases del Domain Layer, que describe el modelo y sus relaciones, y el de base de datos, que describe cómo se persiste.


<a id="42461-bounded-context-domain-layer-class-diagrams"></a>
##### <i>**4.2.4.6.1. Bounded Context Domain Layer Class Diagrams.**</i>

Monitoring es el bounded context más extenso de la solución, por lo que su Domain Layer se presenta en dos diagramas complementarios: el primero recoge los agregados, la entidad y los value objects que componen el modelo; el segundo, los puertos de persistencia que el dominio declara.

<p align="center"><em>Figura 60.</em> Modelo del Domain Layer del bounded context Monitoring.</p>

```mermaid
classDiagram
    direction TB

    class Site {
        -UUID id
        -String code
        -String name
        -String address
        -String timezone
        -String DEFAULT_TIMEZONE$
        +Site(CreateSiteCommand command)
    }

    class RoomType {
        -UUID id
        -UUID siteId
        -String code
        -String displayName
        -String description
        +RoomType(CreateRoomTypeCommand command)
    }

    class Room {
        -UUID id
        -UUID siteId
        -String code
        -UUID roomTypeId
        -String displayName
        -String floor
        -Integer capacity
        -Float areaM2
        -boolean active
        +Room(CreateRoomCommand command)
        +isClassified() boolean
        +handle(ClassifyRoomCommand command) void
    }

    class Device {
        -UUID id
        -String code
        -UUID roomId
        -String fwVersion
        -OffsetDateTime lastSeen
        -Long lastSeq
        -long lostBatches
        +Device(RegisterDeviceCommand command)
        +handle(SyncDeviceStateCommand command) void
        +hasEverReported() boolean
    }

    class RoomReading {
        -UUID id
        -UUID roomId
        -OffsetDateTime ts
        -int periodS
        -OffsetDateTime receivedAt
        +RoomReading(RecordRoomReadingCommand command)
        +isReliable() boolean
    }

    class AcousticMetrics {
        <<value object>>
        +Float laeq
        +Float l10
        +Float l50
        +Float l90
        +Float lmax
        +Float lmin
        +empty()$ AcousticMetrics
        +backgroundNoise() Float
        +intrusivePeaks() Float
        +exceeds(Float limit) boolean
    }

    class Climate {
        <<value object>>
        +Float tempC
        +Float rhPct
        +empty()$ Climate
    }

    class ThermalComfort {
        <<value object>>
        +Float pmv
        +Float ppd
        +String verdict
        -float ASHRAE_55_ACCEPTABLE_PPD$
        +empty()$ ThermalComfort
        +isAcceptable() boolean
    }

    class Occupancy {
        <<value object>>
        +Float occupiedPct
        +Integer transitions
        +vacant()$ Occupancy
        +isMostlyOccupied() boolean
    }

    class DataQuality {
        <<value object>>
        +Integer batches
        +Integer expected
        +unknown()$ DataQuality
        +isComplete() boolean
        +missingBatches() int
    }

    Site "1" --> "0..*" RoomType : clasifica sus salas con
    Site "1" --> "0..*" Room : alberga
    RoomType "1" --> "0..*" Room : tipifica
    Room "1" --> "0..*" Device : es reportada por
    Room "1" --> "0..*" RoomReading : acumula
    RoomReading "1" *-- "1" AcousticMetrics : acoustic
    RoomReading "1" *-- "1" Climate : climate
    RoomReading "1" *-- "1" ThermalComfort : comfort
    RoomReading "1" *-- "1" Occupancy : occupancy
    RoomReading "1" *-- "1" DataQuality : quality
```

<p align="center"><em>Figura 61.</em> Puertos de persistencia y catálogo de errores del bounded context Monitoring.</p>

```mermaid
classDiagram
    direction LR

    class SiteRepository {
        <<interface>>
        +save(Site site) Site
        +findById(UUID id) Optional~Site~
        +findByCode(String code) Optional~Site~
        +findAll() List~Site~
        +findDefault() Optional~Site~
    }

    class RoomTypeRepository {
        <<interface>>
        +save(RoomType roomType) RoomType
        +findById(UUID id) Optional~RoomType~
        +findBySiteIdAndCode(UUID siteId, String code) Optional~RoomType~
        +findAllBySiteId(UUID siteId) List~RoomType~
    }

    class RoomRepository {
        <<interface>>
        +save(Room room) Room
        +findById(UUID id) Optional~Room~
        +findByCode(String code) Optional~Room~
        +findBySiteIdAndCode(UUID siteId, String code) Optional~Room~
        +findActiveBySiteId(UUID siteId) List~Room~
        +findUnclassified() List~Room~
    }

    class DeviceRepository {
        <<interface>>
        +save(Device device) Device
        +findByCode(String code) Optional~Device~
        +findAllByRoomId(UUID roomId) List~Device~
        +findSilentSince(OffsetDateTime since) List~Device~
    }

    class RoomReadingRepository {
        <<interface>>
        +save(RoomReading reading) RoomReading
        +findByRoomIdAndTs(UUID roomId, OffsetDateTime ts) Optional~RoomReading~
        +findInRange(UUID roomId, OffsetDateTime from, OffsetDateTime to) List~RoomReading~
        +findLatest(UUID roomId) Optional~RoomReading~
    }

    class MonitoringError {
        <<enumeration>>
        ROOM_NOT_FOUND
        ROOM_HAS_NO_READINGS
        SITE_NOT_FOUND
        SITE_CODE_ALREADY_USED
        ROOM_TYPE_NOT_FOUND
        ROOM_TYPE_CODE_ALREADY_USED
        ROOM_TYPE_FROM_ANOTHER_SITE
        RANGE_INVERTED
        NO_SITE_AVAILABLE
        READING_BATCH_EMPTY
        READING_PERIOD_REQUIRED
        +code() String
        +kind() ErrorKind
        +messageTemplate() String
    }

    SiteRepository ..> Site : persiste
    RoomTypeRepository ..> RoomType : persiste
    RoomRepository ..> Room : persiste
    DeviceRepository ..> Device : persiste
    RoomReadingRepository ..> RoomReading : persiste
```

`RoomReading` compone cinco value objects en lugar de aplanar veinte campos sueltos, y cada uno responde por una dimensión del confort con su propio vocabulario: `AcousticMetrics` expone `backgroundNoise()` e `intrusivePeaks()`, que devuelven los percentiles L90 y L10 de la norma ISO 1996 bajo el nombre que usa el negocio; `ThermalComfort` conoce el umbral de PPD del 10 % que la norma ASHRAE 55 considera aceptable. Los cinco ofrecen un constructor estático para el caso vacío —`empty()`, `vacant()`, `unknown()`—, de modo que una lectura a la que le falta un sensor se representa sin recurrir a valores nulos dispersos por el agregado.

`DataQuality` merece mención aparte porque sostiene la fiabilidad de todo lo que se calcula después: compara los lotes recibidos con los esperados en el minuto, y `RoomReading.isReliable()` delega en él. Un minuto construido con la mitad de las muestras es un dato legítimo para mostrar en el panel, pero no para promediar en una serie histórica, y esa distinción se decide aquí y no en Insights.

La entidad `Device` se mantiene separada de `Room` con una razón concreta: sustituir un módulo ESP32 averiado no puede costarle a la sala su historial de lecturas. Su método `handle` descarta los lotes que llegan con un número de secuencia inferior al último visto, lo que hace idempotente la sincronización de estado ante los reenvíos de una entrega *at-least-once*.


<a id="42462-bounded-context-database-design-diagram"></a>
##### <i>**4.2.4.6.2. Bounded Context Database Design Diagram.**</i>

El bounded context persiste en el esquema Monitoring, con las tablas que reproducen la estructura física del negocio (local, tipos de sala, salas y dispositivos), la telemetría que estos reportan y los reportes de incomodidad de los miembros.

<p align="center"><em>Figura 62.</em> Diagrama de base de datos del bounded context Monitoring.</p>

```mermaid
erDiagram
    SITE ||--o{ ROOM_TYPE : "clasifica con"
    SITE ||--o{ ROOM : "alberga"
    ROOM_TYPE |o--o{ ROOM : "tipifica"
    ROOM |o--o{ DEVICE : "es reportada por"
    ROOM ||--o{ ROOM_READING : "acumula"
    ROOM ||--o{ DISCOMFORT_REPORT : "recibe"

    SITE {
        uuid id PK
        varchar code "NOT NULL, 64"
        varchar name "NOT NULL, 128"
        varchar address "NULL, 256"
        varchar timezone "NOT NULL, 64, DEFAULT America/Lima"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    ROOM_TYPE {
        uuid id PK
        uuid site_id FK "NOT NULL"
        varchar code "NOT NULL, 32"
        varchar display_name "NOT NULL, 128"
        varchar description "NULL, 256"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    ROOM {
        uuid id PK
        uuid site_id FK "NOT NULL"
        uuid room_type_id FK "NULL hasta que se clasifica"
        varchar code "NOT NULL, 64, el que reporta el firmware"
        varchar display_name "NOT NULL, 128"
        varchar floor "NULL, 32"
        integer capacity "NULL"
        real area_m2 "NULL"
        boolean active "NOT NULL, DEFAULT TRUE"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    DEVICE {
        uuid id PK
        uuid room_id FK "NULL hasta que se asigna"
        varchar code "NOT NULL, 64"
        varchar fw_version "NULL, 32"
        timestamptz last_seen "NULL"
        bigint last_seq "NULL, último número de secuencia visto"
        bigint lost_batches "NOT NULL, DEFAULT 0"
        timestamptz created_at "NOT NULL"
        timestamptz updated_at "NOT NULL"
        timestamptz deleted_at "NULL, borrado lógico"
        uuid created_by "NULL"
        uuid updated_by "NULL"
    }

    ROOM_READING {
        uuid id PK
        uuid room_id FK "NOT NULL"
        timestamptz ts "NOT NULL, minuto que describe"
        integer period_s "NOT NULL"
        real laeq "NULL, nivel continuo equivalente"
        real l10 "NULL, percentil de picos intrusivos"
        real l50 "NULL"
        real l90 "NULL, ruido de fondo"
        real lmax "NULL"
        real lmin "NULL"
        real temp_c "NULL"
        real rh_pct "NULL"
        real pmv "NULL, voto medio previsto ISO 7730"
        real ppd "NULL, porcentaje de insatisfechos"
        varchar thermal_verdict "NULL, 24"
        real occupied_pct "NOT NULL, DEFAULT 0"
        integer transitions "NOT NULL, DEFAULT 0"
        integer batches "NULL, lotes recibidos"
        integer expected "NULL, lotes esperados"
        timestamptz received_at "NOT NULL, DEFAULT now()"
    }
    DISCOMFORT_REPORT {
        uuid id PK
        uuid room_id FK "NOT NULL"
        uuid user_id "NOT NULL, referencia lógica"
        varchar category "NOT NULL, 8"
        varchar comment "NULL, 500"
        timestamptz created_at "NOT NULL"
        timestamptz reading_ts "NULL"
        real laeq "NULL"
        real temp_c "NULL"
        real rh_pct "NULL"
        real occupied_pct "NULL"
    }
```

Las cuatro tablas de estructura llevan auditoría completa y borrado lógico porque las edita una persona. **`room_reading` no lleva ninguna de esas columnas, y es deliberado**: es telemetría inmutable generada por máquina, nadie edita ni borra la lectura de un sensor, y esas cinco columnas estarían vacías en cientos de miles de filas. Su trazabilidad es el par `ts` y `received_at` —el minuto que describe frente al instante en que llegó—, cuya diferencia delata cortes de red y relojes desincronizados en el dispositivo.

Dos claves foráneas son deliberadamente opcionales. `room.room_type_id` nace nula porque la sala se da de alta sola la primera vez que un dispositivo desconocido reporta por ella, y es el administrador quien la clasifica después desde la aplicación web. `device.room_id` lo es por la misma razón: un módulo puede estar registrado antes de asignarse a una sala. Ambas nulabilidades sostienen el autoprovisionamiento descrito en el Application Layer, que permite instalar un dispositivo sin configurar nada por adelantado.

Los identificadores que maneja el firmware no son UUID: viajan en la columna `code` —`sala-01`, `esp32-sala-01`— y el dispositivo nunca ve la clave primaria. Las claves primarias son UUID versión 7, ordenados cronológicamente en sus 48 bits altos, de modo que ordenar por `id` equivale a ordenar por creación y las inserciones caen al final del índice en lugar de dispersarlo, lo que importa especialmente en `room_reading`, que crece un registro por sala y minuto.

El par `room_id` y `ts` identifica una lectura de forma única en la práctica, y es la base de la deduplicación: el Edge entrega con garantía *at-least-once*, de modo que el mismo minuto puede llegar más de una vez y el caso de uso de ingesta lo reconoce por esa pareja antes de insertarlo.

Los reportes de incomodidad se guardan en la tabla `discomfort_report`, con `room_id` como clave foránea hacia `room`, el identificador del usuario como referencia lógica a IAM, la categoría, el comentario, el instante del reporte y las columnas de la lectura copiada (`reading_ts`, `laeq`, `temp_c`, `rh_pct` y `occupied_pct`).

<hr>

<!-- nav:start -->
<p align="center"><a href="capitulo-3.md">← Capítulo III</a> · <a href="README.md#contenido">Contenido</a> · <a href="capitulo-5.md">Capítulo V →</a></p>
<!-- nav:end -->
