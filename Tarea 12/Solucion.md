# HUMINT - Inteligencia en entornos corporativos

---

## 1. Test de HUMINT: Inteligencia en entornos corporativos

---

### Sección 1: Conceptos generales de HUMINT

**Pregunta 1. ¿Qué significa la sigla HUMINT?**  
Respuesta: **b) Human Intelligence**

**Pregunta 2. ¿Cuál de las siguientes actividades es típicamente exclusiva de la obtención de información de fuentes humanas?**  
Respuesta: **b) Interrogatorios**

**Pregunta 3. ¿Qué técnica busca obtener información sin que la fuente se dé cuenta de que está siendo cuestionada?**  
Respuesta: **a) Elicitación**

**Pregunta 4. ¿Cuál es una ventaja del HUMINT virtual frente al HUMINT tradicional?**  
Respuesta: **c) Permite acceder a información global sin restricciones geográficas**

**Pregunta 5. ¿Qué término describe el proceso de evaluar y seleccionar fuentes humanas para la recopilación de información?**  
Respuesta: **c) Screening**

**Pregunta 6. ¿Qué diferencia clave distingue HUMINT de las técnicas tradicionales de OSINT?**  
Respuesta: **c) HUMINT se centra en la interacción humana y la manipulación psicológica, mientras que OSINT se limita al análisis de información disponible públicamente**

---

### Sección 2: Credibilidad y fiabilidad

**Pregunta 7. ¿Qué elemento ayuda a determinar la fiabilidad de una fuente humana?**  
Respuesta: **a) La experiencia pasada del manejador con la fuente y la coherencia de su historial de aportaciones**

**Pregunta 8. ¿Qué estrategia permite al handler detectar posibles inconsistencias en la información de la fuente?**  
Respuesta: **b) Utilizar preguntas de control diseñadas para verificar la coherencia de las respuestas**

**Pregunta 9. ¿En qué dominios describe el FM 2.22-3 los criterios de evaluación de fiabilidad de la fuente?**  
Respuesta: **c) De la A a la F, donde A representa las fuentes más fiables**

---

### Sección 3: Insider threats

**Pregunta 10. ¿Cuál de las siguientes características define al insider bienintencionado?**  
Respuesta: **c) Ignora las reglas de seguridad para ser más eficiente**

**Pregunta 11. ¿Cuál de las siguientes combinaciones representa la aplicación conjunta de medidas preventivas y tecnológicas más efectivas para reducir el riesgo de amenazas internas en una organización?**  
Respuesta: **b) Control de acceso granular, principio de menor privilegio y autenticación multifactor (MFA)**

---

### Sección 4: Legalidad y ética

**Pregunta 12. ¿Qué normativa española regula la protección de datos personales?**  
Respuesta: **c) Ley Orgánica de Protección de Datos y Garantía de Derechos Digitales (LOPDGDD)**

**Pregunta 13. En el contexto ético, ¿qué principio debe guiar la selección de técnicas de HUMINT?**  
Respuesta: **a) El principio de proporcionalidad**

---

### Sección 5: Factores psicológicos

**Pregunta 14. ¿Qué modelo de personalidad utiliza las dimensiones Psicoticismo, Extraversión y Neuroticismo?**  
Respuesta: **b) Modelo PEN de Eysenck**

**Pregunta 15. ¿Qué principio de persuasión de Cialdini implica devolver un favor recibido?**  
Respuesta: **b) Reciprocidad**

**Pregunta 16. ¿Qué factor psicológico busca moldear comportamientos a través de refuerzos y castigos?**  
Respuesta: **b) Condicionamiento operante**

---

### Sección 6: UNVEIL Framework

**Pregunta 17. ¿Qué táctica del framework UNVEIL se encarga de estudiar el procedimiento de cierre de la relación con la fuente?**  
Respuesta: **d) EXIT**

**Pregunta 18. ¿Cuál de las siguientes no es una fuente de datos definida en el framework UNVEIL?**  
Respuesta: **d) CYBERSECURITY ALERTS**

**Pregunta 19. ¿Cuál de las siguientes técnicas encaja peor en la táctica EXTRACT, que tiene por definición como objetivo obtener información o acceso a información en el marco de una operación de inteligencia encauzada a través de HUMINT virtual?**  
Respuesta: **c) Manipular sentimientos de odio**

**Pregunta 20. ¿Cuál es el objetivo principal de las medidas técnicas en el marco UNVEIL?**  
Respuesta: **b) Asegurar la integridad operativa mediante cifrado, contravigilancia y Zero Trust**

**Pregunta 21. ¿Por qué las medidas técnicas dejaron de considerarse una táctica dentro de UNVEIL y pasaron a ser una categoría independiente?**  
Respuesta: **c) Porque son transversales y deben aplicarse en todas las fases y tácticas de una operación**

**Pregunta 22. ¿Cuál de los siguientes ejemplos se clasifica dentro de las medidas técnicas del modelo UNVEIL?**  
Respuesta: **b) Uso de comunicaciones cifradas, ocultamiento de ubicación técnica y sistemas operativos que preservan la privacidad**

---

### Sección 7: Aplicación en entornos corporativos

**Pregunta 23. ¿Cuál es la principal diferencia entre la vigilancia digital y la ciberinteligencia (CTI) aplicada con HUMINT en un SOC corporativo?**  
Respuesta: **b) La vigilancia digital genera alertas informativas, mientras que el HUMINT permite contextualizar, evaluar motivaciones y valorar la credibilidad de las fuentes**

**Pregunta 24. ¿Cuál de las siguientes técnicas del ciclo de HUMINT virtual resulta útil para la creación de perfiles de investigación que faciliten la exploración de comunidades o espacios virtuales?**  
Respuesta: **b) UTA02 - Prepare**

**Pregunta 25. En el contexto de un SOC corporativo, ¿por qué no siempre se aplica el ciclo completo de HUMINT?**  
Respuesta: **b) Porque existen limitaciones legales y regulatorias que impiden interactuar directamente con actores en entornos clandestinos**

---

## 2. Ejercicio práctico

**Caso analizado:** _When the Hunter Becomes the Hunted: The Art and Risk of Threat Actor Engagement_, Analyst1.

---

### Sección 1: Preinteracción

**Técnica identificada:** **UTA01 - Plan Gathering**.

En el artículo puede identificarse una fase de **preinteracción** asociada a la planificación del **threat actor engagement**. Antes de establecer contacto directo con un actor de amenaza, el investigador debe valorar si la interacción está realmente justificada por los **requisitos de inteligencia** de la investigación y no solo por la posibilidad técnica de acceder al canal de comunicación.

Esta técnica parece emplearse cuando se plantea la necesidad de definir qué información se espera obtener, qué valor tendría para la investigación, qué riesgos asumiría el investigador y cuál podría ser el peor escenario si la interacción no se controla adecuadamente. En términos de **HUMINT virtual**, esta fase sitúa el trabajo del **handler** antes de la conversación con la **source**, permitiendo revisar canales, identidad operativa, medidas de **OPSEC** y límites de la interacción.

Por tanto, **UTA01 - Plan Gathering** permite decidir si el contacto directo aporta más valor que una recogida pasiva mediante **OSINT**, **SOCMINT** u otras fuentes indirectas. En un contexto corporativo, esta planificación resulta esencial para evitar una exposición innecesaria del investigador, del **SOC** o de la organización.

---

### Sección 2: Interacción

**Técnica identificada:** **UTA04 - Influence**.

En el artículo puede identificarse una técnica de **interacción** vinculada con **UTA04 - Influence**, especialmente a través de la construcción de **rapport**, la adaptación del tono y el manejo de las motivaciones del actor de amenaza. En el caso de Jon DiMaggio, la interacción no se presenta como una conversación espontánea, sino como un contacto directo gestionado con una estrategia clara de **HUMINT virtual**.

Esta técnica parece emplearse cuando el investigador adapta su forma de comunicarse según el perfil del actor, pero manteniendo siempre una posición transparente sobre su rol: es investigador y puede escribir sobre el actor. Esa claridad permite establecer límites y evita que la **source** interprete la relación como una amistad real o como una colaboración sin consecuencias.

Además, la influencia se apoya en elementos psicológicos observables en algunos **threat actors**, como el ego, la reputación, la búsqueda de notoriedad o el deseo de controlar el relato público sobre sus acciones. En este contexto, el **handler** puede aprovechar esos factores para facilitar la cooperación y obtener información útil, sin perder de vista que la fuente sigue teniendo intereses propios y potencialmente hostiles.

---

### Sección 3: Postinteracción

**Técnica identificada:** **UTA09 - Debrief and Archive**.

En la fase de **postinteracción** puede identificarse la técnica **UTA09 - Debrief and Archive**, aplicada al análisis posterior de la información obtenida durante el contacto con el actor de amenaza. El artículo deja claro que la conversación no termina cuando la **source** responde, ya que la información proporcionada puede contener datos ciertos, exageraciones, omisiones interesadas o incluso desinformación.

Esta técnica parece emplearse cuando se recomienda analizar por qué el actor puede estar mintiendo, qué intenta ocultar y qué objetivo persigue con su narrativa. Desde una perspectiva de **HUMINT virtual**, el valor de la interacción no está solo en obtener una respuesta, sino en convertir esa información en inteligencia útil, verificable y contextualizada.

Por ello, el **debriefing** posterior debe incluir el registro de la conversación, la selección de los datos relevantes, la evaluación de la credibilidad de la fuente y la **corroboración cruzada** con otros canales. Esta validación puede realizarse mediante fuentes indirectas, **OSINT**, **SOCMINT**, indicadores técnicos o incluso contraste con otros actores relacionados. Sin esta fase, el riesgo principal sería aceptar como inteligencia lo que en realidad podría ser manipulación, propaganda o una narrativa interesada del actor.

---

### Sección 4: Medidas técnicas

**Medida técnica identificada:** **TM0010 - Hide technical location**.

Una medida técnica adecuada para el caso analizado es **TM0010 - Hide technical location**, orientada a ocultar la ubicación técnica del investigador y reducir la exposición de la infraestructura utilizada durante el **threat actor engagement**. El artículo muestra que los investigadores también pueden convertirse en objetivo de vigilancia, intimidación, doxxing o represalias, por lo que la **OPSEC** debe considerarse una parte esencial de la operación.

Esta medida podría aplicarse mediante el uso de un entorno de investigación aislado de la red corporativa, cuentas separadas, dispositivos dedicados, **VPN**, proxies, máquinas virtuales o infraestructura compartimentada. El objetivo sería impedir que el actor de amenaza pueda vincular la interacción con la identidad real del investigador, con el **SOC** o con los activos técnicos de la organización.

También sería necesario controlar los metadatos, los patrones de conexión, la identidad operativa utilizada y los canales de comunicación. En operaciones de **HUMINT virtual**, esta medida no sustituye a la estrategia ni a la supervisión legal, pero reduce la posibilidad de atribución técnica inversa y limita el impacto si la interacción se vuelve hostil.
