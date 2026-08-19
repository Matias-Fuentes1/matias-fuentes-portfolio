# projects.py
# -----------------------------------------------------------------
# Mi Centro de Control: Acá centralizo toda la información de mis proyectos.
# Si quiero agregar o editar un caso de estudio, solo toco este archivo.
# Dejo app.py intacto, salvo que decida cambiar la lógica del diseño.
# -----------------------------------------------------------------
 
PROJECTS = [
    {
        "titulo": "Brechas de Ahorro e Inclusión Financiera en Brasil",
        "categoria": "BI",
        "resumen": (
            "Análisis de 144.000+ encuestas del Global Findex (Banco Mundial) sobre inclusión "
            "financiera en Brasil, aplicando ponderación poblacional y controles de calidad sobre los datos."
        ),
        "hallazgo_clave": (
        "La brecha de ahorro por género alcanza el 28,3%, casi el mismo impacto que la brecha por ingreso. "
        "Además, quienes tienen acceso a billeteras digitales ahorran 42 puntos porcentuales más."
        ),
        "imagen": "assets/Interseccionalidad.png",
        "stack": ["Python", "Pandas", "Matplotlib/Seaborn"],
        "github_url": "https://github.com/Matias-Fuentes1/behavioral-data-audit-brazi-py", 
        "dashboard_url": "", 
    },
    {
        "titulo": "Modelo Predictivo de Propensión de Compra",
        "categoria": "Data Science",
        "imagen": "assets/propension_compra.png",  
        "resumen": (
            "Pipeline de Random Forest sobre 300K+ usuarios de e-commerce para predecir "
            "probabilidad de compra, con prevención estricta de data leakage."
        ),
        "hallazgo_clave": (
            "El modelo redujo un 89% los falsos positivos y mantuvo la detección del 47% de los "
            "compradores reales dentro de un umbral operativo para el equipo comercial."
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
            "Se detectaron $1.39M en pérdidas sobre $64.9M de revenue, concentradas en tres "
            "subcategorías con márgenes de hasta -14%; el revenue creció 33% mientras el profit cayó 75%."
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
            "Cerca del 80% de los usuarios abandona antes de llegar al carrito, mientras Paid Search "
            "rinde 27% por debajo del promedio del sitio."
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
            "La retención cae del 100% a cerca del 20% en el primer mes. Aunque las cancelaciones "
            "representan el 17% de los pedidos, explican solo el 2% de la pérdida de ingresos: "
            "el foco debe estar en los clientes de mayor valor."
        ),
        "stack": ["BigQuery", "SQL", "Power BI"],
        "github_url": "https://github.com/Matias-Fuentes1/ecommerce-data-warehouse-sql",  
        "dashboard_url": "",  
    },
]
