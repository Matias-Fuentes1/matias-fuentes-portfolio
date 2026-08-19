# projects.py
# -----------------------------------------------------------------
# Mi Centro de Control: Acá centralizo toda la información de mis proyectos.
# Si quiero agregar o editar un caso de estudio, solo toco este archivo.
# Dejo app.py intacto, salvo que decida cambiar la lógica del diseño.
# -----------------------------------------------------------------
 
PROJECTS = [
    {
        "titulo": "Barreras de Ahorro en la Juventud Brasileña",
        "categoria": "BI",
        "resumen": (
            "Análisis de 144.000+ encuestas individuales del Global Findex (Banco Mundial) "
            "sobre inclusión financiera en Brasil, con ponderación poblacional."
        ),
        "hallazgo_clave": (
        "El género es una barrera más pesada que la pobreza: un hombre joven en vulnerabilidad "
        "extrema (Q1) ahorra el 63.9%, superando a la mujer del estrato más rico (Q5), "
        "quien alcanza solo el 53.2% debido a penalizaciones por Sobrecarga Cognitiva."
        ),
        "imagen": "assets/Interseccionalidad.png",
        "stack": ["Python", "Pandas", "Matplotlib/Seaborn"],
        "github_url": "https://github.com/Matias-Fuentes1/behavioral-data-audit-brazi-py", 
        "dashboard_url": "", 
    },
    {
        "titulo": "Modelo Predictivo de Propensión de Compra",
        "categoria": "BI",
        "imagen": "assets/propension_compra.png",  
        "resumen": (
            "Pipeline de Random Forest sobre 300K+ usuarios de e-commerce para predecir "
            "probabilidad de compra, con prevención estricta de data leakage."
        ),
        "hallazgo_clave": (
            "ROC-AUC de 0.81 y reducción del 89% en falsos positivos mediante optimización "
            "del umbral de decisión."
        ),
        "stack": ["Python", "Scikit-learn", "Pandas"],
        "github_url": "https://github.com/Matias-Fuentes1/marketing-data-science-project",  
        "dashboard_url": "",
    },
    {
        "titulo": "Análisis de Rentabilidad Comercial",
        "categoria": "BI",
        "imagen": "assets/dashboard_analisis_rentabilidad.png",  
        "resumen": (
            "Dashboard ejecutivo en Power BI sobre rentabilidad por subcategoría, región "
            "y período en un negocio retail."
        ),
        "hallazgo_clave": (
            "El 98.3% del revenue se concentra en el Top 10 de productos; 3 subcategorías "
            "generan $1.39M en pérdidas con márgenes de hasta -14%."
        ),
        "stack": ["Microsoft Excel", "DAX", "SQL"],
        "github_url": "https://github.com/Matias-Fuentes1/sales-performance-excel-AdventureWorks",  
        "dashboard_url": "https://1drv.ms/x/c/e6bb2b6437ad3a02/IQCRO5eruw2_QK5wSJOR3IA3ARMHYr8bvef82a2T08fYxWY?e=m9peVe", 
    },
    {
        "titulo": "Performance de Canales y Embudo de Conversión — Google Merchandise Store",
        "categoria": "Marketing",
        "imagen": "assets/dashboard_funnel.png",
        "resumen": (
            "Pipeline de datos con GA4 + BigQuery para analizar el funnel de conversión "
            "y la performance de canales de adquisición sobre 360K+ sesiones."
        ),
        "hallazgo_clave": (
            "El 78% de los usuarios abandona antes de ver un producto; Referral es el "
            "canal más eficiente (1.66% CVR) frente a Paid Search, el menos eficiente (0.98%)."
        ),
        "stack": ["BigQuery", "SQL", "Looker Studio", "GA4"],
        "github_url": "https://github.com/Matias-Fuentes1/marketing-infrastructure-funnel-audit",  # TODO
        "dashboard_url": "https://datastudio.google.com/s/tKwvK5oybuA", 
    },
    {
        "titulo": "Retención de Clientes y Segmentación RFM",
        "categoria": "BI", 
        "imagen": "assets/dashboard_cohortes_recurrencia.png",
        "resumen": (
            "Modelo de datos en BigQuery (esquema estrella) + dashboard Power BI para "
            "analizar cohortes de retención sobre +500K transacciones."
        ),
        "hallazgo_clave": (
            "La retención cae del 100% al ~20% entre la primera y segunda compra: "
            "el primer mes es la ventana crítica."
        ),
        "stack": ["BigQuery", "SQL", "Power BI"],
        "github_url": "https://github.com/Matias-Fuentes1/ecommerce-data-warehouse-sql",  
        "dashboard_url": "📥 Descargar Reporte (.pbix) — requiere Power BI Desktop (gratis)",  
    },
]