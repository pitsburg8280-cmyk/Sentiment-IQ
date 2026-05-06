Sentiment-IQ

📖 Descripción
Sentiment-IQ es un sistema de análisis de sentimientos desarrollado en Python.  
Permite a los usuarios ingresar reseñas de productos, clasificarlas automáticamente como Positivas o Negativas utilizando técnicas de Machine Learning (Naive Bayes), y almacenar los resultados en una base de datos SQLite.  
Además, genera reportes en formato CSV con timestamp para evidenciar el funcionamiento del sistema y la trazabilidad de los accesos.


📂 Estructura del proyecto

Sentiment-IQ/
│── sentiment.py          # Código principal en Python (POO + menú interactivo)
│── sentiment.sql         # Script SQL corregido para la base de datos
│── requirements.txt      # Dependencias necesarias
│── README.md             # Documentación del proyecto
│── docs/
│   └── Proyecto_SentimentIQ.pdf   # Documento académico (portada, UML, DER, reflexión, referencias)
│── data/
│   └── dataset.csv       # Dataset dinámico de reseñas
│── logs/
│   └── system.log        # Ejemplo de archivo de logs
│── reports/
│   └── reseñas.csv       # Reportes generados automáticamente con fecha/hora


⚙️ Instalación y ejecución

1. Clonar el repositorio
  git clone https://github.com/pitsburg8280-cmyk/Sentiment-IQ.git
   cd Sentiment-IQ

2. Instalar dependencias
Ejecuta en la terminal:
pip install -r requirements.txt

3. Ejecutar el programa
  python sentiment.py


🖥️ Uso del sistema

1. Al iniciar, el sistema solicita usuario y contraseña.  
   - Si el usuario no existe, se crea automáticamente en la base de datos.  

2. Menú interactivo:
   - 1. Agregar reseña → El usuario escribe una reseña, el sistema la clasifica y la guarda en la BD.  
   - 2. Ver reseñas → Muestra todas las reseñas almacenadas.  
   - 3. Exportar reporte → Genera un archivo reports/reseñas.csv con las reseñas clasificadas y la fecha/hora.  
   - 4. Salir → Finaliza el programa.  


🧠 Tecnologías utilizadas
- Python 3.10+
- SQLite3 (base de datos embebida)
- Scikit-learn (clasificación de sentimientos con Naive Bayes)
- Pandas (carga dinámica del dataset)
- Hashlib (encriptación de contraseñas)
- CSV (exportación de reportes)
- Logging (registro de eventos del sistema)


📊 Ejemplo de reporte CSV generado
ID,Texto,Sentimiento,FechaHora
1,El producto es excelente,Positivo,2026-05-07 06:15:00
2,No me gustó,Negativo,2026-05-07 06:16:12
3,Funciona bien,Positivo,2026-05-07 06:17:45


🎯 Objetivo académico
Este proyecto integra:
- Programación Orientada a Objetos (POO).  
- Persistencia en base de datos con SQL.  
- Machine Learning aplicado a reseñas.  
- Generación de reportes con trazabilidad.  
- Documentación profesional (README.md, UML, DER, PDF académico).  


👤 Autor
Proyecto desarrollado por Alvaro Moreno  
Módulo integrador de programación y ciencia de datos.  
Instituto Profesional de Líderes – Licenciatura en Inteligencia Artificial.