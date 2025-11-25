#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def obtener_datos_regulaciones_final():
    """Devuelve una lista ampliada con 36 entradas, incluyendo el campo 'Categoría'."""
    # Categorías: 
    # R (Regulación Legal/Contractual), E (Estándar Técnico/Seguridad), 
    # A (Auditoría/Evaluación), M (Marco de Gestión/Gobierno)
    return [
        {"Valor": 1, "Regulación": "PCI DSS", "Alcance": "United States", "Categoría": "R", "Descripción": "Seguridad de datos de tarjetas de pago."},
        {"Valor": 2, "Regulación": "HIPAA", "Alcance": "United States", "Categoría": "R", "Descripción": "Protección de información de salud (PHI)."},
        {"Valor": 3, "Regulación": "FERPA", "Alcance": "United States", "Categoría": "R", "Descripción": "Privacidad de registros educativos."},
        {"Valor": 4, "Regulación": "SOX", "Alcance": "United States", "Categoría": "R", "Descripción": "Responsabilidad financiera corporativa."},
        {"Valor": 5, "Regulación": "GLBA", "Alcance": "United States", "Categoría": "R", "Descripción": "Protege información financiera personal."},
        {"Valor": 6, "Regulación": "PIPEDA", "Alcance": "Canada", "Categoría": "R", "Descripción": "Regula el uso de información personal."},
        {"Valor": 7, "Regulación": "DPA", "Alcance": "United Kingdom", "Categoría": "R", "Descripción": "Estándares para el procesamiento de datos personales."},
        {"Valor": 8, "Regulación": "COPPA", "Alcance": "United States", "Categoría": "R", "Descripción": "Privacidad online de niños."},
        {"Valor": 9, "Regulación": "CA SB-1386", "Alcance": "US (California)", "Categoría": "R", "Descripción": "Requisitos de notificación de violación de datos."},
        {"Valor": 10, "Regulación": "OPPA", "Alcance": "US (California)", "Categoría": "R", "Descripción": "Requisitos de política de privacidad online."},
        {"Valor": 11, "Regulación": "Directive 95/46/EC", "Alcance": "European Union", "Categoría": "A", "Descripción": "Marco original de protección de datos de la UE."},
        {"Valor": 12, "Regulación": "Directive 2002/58/EC", "Alcance": "European Union", "Categoría": "R", "Descripción": "Privacidad en comunicaciones electrónicas (e-Privacy)."},
        {"Valor": 13, "Regulación": "GDPR", "Alcance": "EU & Global", "Categoría": "R", "Descripción": "Marco estricto de privacidad y control de datos."},
        {"Valor": 14, "Regulación": "SOC2", "Alcance": "United States", "Categoría": "A", "Descripción": "Auditoría de controles para organizaciones de servicios."},
        {"Valor": 15, "Regulación": "ISO 27001", "Alcance": "International", "Categoría": "E", "Descripción": "Sistema de gestión de seguridad de la información (SGSI)."},
        {"Valor": 16, "Regulación": "CISA-SSDA", "Alcance": "United States", "Categoría": "E", "Descripción": "Seguridad en ciclo de vida de desarrollo de software."},
        {"Valor": 17, "Regulación": "FEDRAMP", "Alcance": "US (Federal)", "Categoría": "R", "Descripción": "Autorización de seguridad para servicios en la nube federales."},
        {"Valor": 18, "Regulación": "SLSA", "Alcance": "International", "Categoría": "E", "Descripción": "Seguridad para integridad de software (Supply Chain)."},
        {"Valor": 19, "Regulación": "SSDF", "Alcance": "United States", "Categoría": "E", "Descripción": "Marco para la creación de software seguro."},
        {"Valor": 20, "Regulación": "CIS Benchmark", "Alcance": "United States", "Categoría": "E", "Descripción": "Guías de configuración de seguridad para sistemas."},
        {"Valor": 21, "Regulación": "CSF (NIST)", "Alcance": "United States", "Categoría": "E", "Descripción": "Marco de ciberseguridad para gestionar riesgos."},
        {"Valor": 22, "Regulación": "ASVS (OWASP)", "Alcance": "International", "Categoría": "E", "Descripción": "Estándar para la verificación de seguridad de aplicaciones."},
        {"Valor": 23, "Regulación": "OWASP T10", "Alcance": "International", "Categoría": "E", "Descripción": "Las 10 principales vulnerabilidades de seguridad web."},
        {"Valor": 24, "Regulación": "OWASP API T10", "Alcance": "International", "Categoría": "E", "Descripción": "Las 10 principales vulnerabilidades de seguridad de API."},
        {"Valor": 25, "Regulación": "CCPA", "Alcance": "US (California)", "Categoría": "R", "Descripción": "Derechos de privacidad y control sobre datos personales de consumidores."},
        {"Valor": 26, "Regulación": "CPRA", "Alcance": "US (California)", "Categoría": "R", "Descripción": "Expansión y fortalecimiento de los derechos de privacidad de CCPA."},
        {"Valor": 27, "Regulación": "NIST 800-53", "Alcance": "US (Federal)", "Categoría": "E", "Descripción": "Controles de seguridad y privacidad para sistemas de información federales."},
        {"Valor": 28, "Regulación": "CMMC", "Alcance": "US (DoD)", "Categoría": "R", "Descripción": "Requisitos de ciberseguridad para contratistas del Departamento de Defensa."},
        {"Valor": 29, "Regulación": "LGPD", "Alcance": "Brazil", "Categoría": "R", "Descripción": "Marco de protección de datos personales brasileño."},
        {"Valor": 30, "Regulación": "APRA", "Alcance": "Australia", "Categoría": "R", "Descripción": "Estándares de seguridad para entidades financieras y de seguros."},
        {"Valor": 31, "Regulación": "PCI DSS v4.0", "Alcance": "International", "Categoría": "R", "Descripción": "Última versión del estándar de seguridad para la industria de tarjetas de pago."},
        # --- Entradas de Auditoría (NIA/NOGAI) ---
        {"Valor": 32, "Regulación": "NIA (Internacional)", "Alcance": "International", "Categoría": "A", "Descripción": "Auditoría Externa. Evalúa controles de TI. **No regula pentest, pero es base para la evidencia.**"},
        {"Valor": 33, "Regulación": "NOGAI (Internacional)", "Alcance": "International", "Categoría": "A", "Descripción": "Auditoría Interna Global. Exige enfoque en riesgos de TI. **No regula pentest, pero es base para la evidencia.**"},
        # --- Entradas de Marcos de Gestión (ITIL/COBIT/MAGERIT) ---
        {"Valor": 34, "Regulación": "COBIT", "Alcance": "International", "Categoría": "M", "Descripción": "Marco de GOBIERNO y gestión de TI. Define objetivos de control de ciberseguridad."},
        {"Valor": 35, "Regulación": "ITIL", "Alcance": "International", "Categoría": "M", "Descripción": "Marco de GESTIÓN de servicios de TI. Provee el proceso para la gestión de incidentes y cambios."},
        {"Valor": 36, "Regulación": "MAGERIT", "Alcance": "Spain/EU", "Categoría": "M", "Descripción": "Metodología de ANÁLISIS y gestión de riesgos de seguridad de la información."},
    ]

def imprimir_tabla(regulaciones, titulo, key_sort, key_group=None):
    """
    Función genérica para imprimir la tabla. Permite ordenamiento (key_sort)
    y, opcionalmente, agrupación por categoría (key_group).
    """
    import itertools
    
    # 1. Definir anchos de columna 
    ancho_val = 7
    ancho_reg = 22
    ancho_alcance = 18
    ancho_desc = 65 
    
    # 2. Mapeo de Categorías para el título
    mapa_cat = {
        'R': 'REGULACIÓN OBLIGATORIA (R)', 
        'E': 'ESTÁNDAR/CONTROL TÉCNICO (E)', 
        'A': 'AUDITORÍA/EVALUACIÓN (A)', 
        'M': 'MARCO DE GESTIÓN/GOBIERNO (M)'
    }

    print(f"\n{titulo}")
    
    # 3. Impresión del encabezado (igual para ambos modos)
    header = (
        f"{'ID':<{ancho_val}} | " 
        f"{'REGULACIÓN':<{ancho_reg}} | "
        f"{'ALCANCE':<{ancho_alcance}} | "
        f"{'DESCRIPCIÓN BREVE':<{ancho_desc}}"
    )
    separator = "=" * len(header)
    
    print(separator)
    print(header)
    print(separator)

    # 4. Impresión Agrupada por Categoría
    if key_group:
        lista_ordenada = sorted(regulaciones, key=lambda x: (x[key_group], x[key_sort]))
        
        for category, group in itertools.groupby(lista_ordenada, key=lambda x: x[key_group]):
            print(f"\n--- {mapa_cat.get(category, 'OTRAS')} ---")
            for reg in group:
                linea = (
                    f"{reg['Valor']:<{ancho_val}} | " 
                    f"{reg['Regulación']:<{ancho_reg}} | "
                    f"{reg['Alcance']:<{ancho_alcance}} | "
                    f"{reg['Descripción']:<{ancho_desc}}"
                )
                print(linea)
    
    # 5. Impresión Lineal (Modos ID, Regulación, Alcance)
    else:
        lista_ordenada = sorted(regulaciones, key=lambda x: x[key_sort])
        for reg in lista_ordenada:
            linea = (
                f"{reg['Valor']:<{ancho_val}} | " 
                f"{reg['Regulación']:<{ancho_reg}} | "
                f"{reg['Alcance']:<{ancho_alcance}} | "
                f"{reg['Descripción']:<{ancho_desc}}"
            )
            print(linea)
    
    print(separator)

if __name__ == "__main__":
    datos = obtener_datos_regulaciones_final()
    
    print("--- INICIO DE SALIDAS DEL SCRIPT (36 Entradas) ---")
    print("\n" + "="*80)
    print("### TABLAS DE ORDENAMIENTO (Sin Agrupación)")
    print("="*80)

    # 1. TABLA ORDENADA POR ID
    imprimir_tabla(
        datos,
        "🔢 TABLA ORDENADA POR ID (Valor de Opción)",
        "Valor" 
    )

    # 2. TABLA ORDENADA POR REGULACIÓN (Alfabético)
    imprimir_tabla(
        datos,
        "🔠 TABLA ORDENADA ALFABÉTICAMENTE POR REGULACIÓN",
        "Regulación" 
    )

    # 3. TABLA ORDENADA POR JURISDICCIÓN/ALCANCE
    imprimir_tabla(
        datos,
        "🌎 TABLA ORDENADA POR JURISDICCIÓN/ALCANCE",
        "Alcance"
    )
    
    print("\n" + "="*80)
    print("### TABLA DE CLASIFICACIÓN (Agrupada por Categoría)")
    print("="*80)
    
    # 4. TABLA CLASIFICADA POR CATEGORÍA
    imprimir_tabla(
        datos,
        "⭐ CLASIFICACIÓN POR TIPO (Regulación, Estándar, Auditoría, Gestión)",
        "Valor", # Orden secundario (por ID)
        "Categoría" # Agrupación principal
    )
    
    print("\n--- FIN DE SALIDAS DEL SCRIPT ---")