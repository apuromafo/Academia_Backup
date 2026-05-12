
# 🛡️ Burp Suite Certified Practitioner (BSCP) - Apuntes de Preparación

## 📋 ¿Qué es un Profesional Certificado de Burp Suite?

El **Profesional Certificado de Burp Suite (BSCP)** es una certificación oficial para profesionales de la seguridad web, de los creadores de **Burp Suite**.

Convertirse en un Profesional Certificado de Burp Suite demuestra:

* Un profundo conocimiento de las vulnerabilidades de seguridad web.
* La mentalidad correcta para explotarlas.
* Las habilidades de Burp Suite necesarias para llevarlo a cabo.

## 🚀 ¿Por qué convertirse en un practicante certificado?

Aprobar el examen indica un alto nivel de competencia en pruebas de seguridad web. Está dirigido tanto a pentesters como a las organizaciones que los emplean.

### Beneficios Principales:

* **Demuestra tu competencia:**
* Conocimiento profundo de las últimas clases de vulnerabilidades y su explotación.
* Muestra tus habilidades con Burp Suite Professional.
* Demuestra tu capacidad de hacking ante empleadores y la comunidad.


* **Mejora las habilidades de tu equipo:**
* Demuestra la competencia del equipo ante clientes potenciales.
* Identifica el mejor talento para unirse a tu equipo.
* Desarrolla experiencia con el conocimiento de las últimas vulnerabilidades.


---

## 🛠️ Información y Recursos Útiles

### Preparación para el Examen

Antes de realizar el examen, es fundamental seguir los pasos de preparación y leer los consejos oficiales:

* [Cómo prepararse para su examen](https://portswigger.net/web-security/certification/how-to-prepare)
* [Consejos y orientación](https://portswigger.net/web-security/certification/exam-hints-and-guidance)
* [Requisitos técnicos](https://www.google.com/search?q=https://portswigger.net/web-security/certification/technical-requirements)

### Proceso de Certificación

1. **Requisitos del sistema:** Asegura que tu máquina tenga las especificaciones correctas.
2. **Compra de examen:** Puedes comprar créditos cuando estés listo.
3. **Suscripción activa:** Es obligatorio tener acceso a **Burp Suite Professional**.

 

## 🎓 Sobre la Certificación

El **BSCP** es una certificación oficial que valida conocimientos avanzados en seguridad web, capacidad de explotación de vulnerabilidades y dominio de **Burp Suite Professional**.

* **Costo del Examen:** $99 USD.
* **Requisito:** Suscripción activa a Burp Suite Professional ($475 USD) aprox.
* **Enfoque:** Pruebas de penetración reales, mentalidad de ataque y uso eficiente del Scanner.

 ---

## 🛠️ Recursos de Estudio y Repositorios

| Recurso | Descripción | Link |
| --- | --- | --- |
| **Guía Oficial** | Preparación, consejos y guía oficial. | [PortSwigger Prep](https://portswigger.net/web-security/certification/how-to-prepare) |
| **CheatSheet 2025** | Recomendaciones actualizadas para el examen. | [JFOZ1010 GitHub](https://github.com/JFOZ1010/CheatSheet-BSCP-2025) |
| **WSAAR** | Scripts de apoyo para reconocimiento inicial. | [Nishacid GitHub](https://github.com/Nishacid/WSAAR) |
| **Exam Study** | Repositorio completo de metodología de examen. | [botesjuan GitHub](https://github.com/botesjuan/Burp-Suite-Certified-Practitioner-Exam-Study) |
| **DingyShark Guide** | Notas detalladas y estrategias de resolución. | [DingyShark GitHub](https://github.com/DingyShark/BurpSuiteCertifiedPractitioner) |
| **GitBook CheatSheet** | Laboratorios recomendados y técnicas. | [BSCP GitBook](https://bscpcheatsheet.gitbook.io/exam/recommended_labs) |

---

## 🔑 Diccionarios y Listas (PortSwigger)

Es fundamental tener estas listas a mano para ataques de fuerza bruta durante el examen:

* [Candidate Usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
* [Candidate Passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

---

## 🚀 Tips Técnicos y "Pwn" Techniques

### SSRF (Server-Side Request Forgery)

Durante el examen, es común que necesites interactuar con servicios internos. Ten siempre presente el puerto específico que suele utilizarse en el entorno del examen.

> **Tip Pro:** Si encuentras un vector SSRF, intenta apuntar al puerto **6566**.

```bash
# Payload común para SSRF en entornos BSCP
http://localhost:6566
http://192.168.0.[intruder_payload]:6566

```

### Escaneo y Metodología

* **Manual + Automated:** No dependas solo del scanner. Utiliza el Scanner de Burp sobre peticiones específicas mientras realizas pruebas manuales.
* **Guía de Errores:** Revisa los [Exam Hints](https://portswigger.net/web-security/certification/exam-hints-and-guidance) para evitar bloqueos comunes durante la prueba.
* **Skills Esenciales:** [Uso del Scanner en pruebas manuales](https://portswigger.net/web-security/essential-skills/using-burp-scanner-during-manual-testing).

---

## 📋 Requisitos Previos

1. **Suscripción:** Burp Suite Professional (Obligatorio).
2. **Sistema:** Cumplir con los [Requisitos Técnicos](https://www.google.com/search?q=https://portswigger.net/web-security/certification/technical-requirements).
3. **Preparación:** Completar los niveles "Practitioner" de la Web Security Academy.
4. ** si no apruebas:  ** recomiendan lo siguiente https://portswigger.net/web-security/certification/exam-hints-and-guidance/retaking-your-exam

---


#BSCP