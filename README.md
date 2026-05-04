Sentiment-IQ

📖 Descripción
Sentiment-IQ es un sistema de análisis de sentimientos desarrollado en Python.  
Permite a los usuarios ingresar reseñas de productos, clasificarlas automáticamente como Positivas o Negativas utilizando técnicas de Machine Learning, y almacenar los resultados en una base de datos SQLite.  
Además, genera reportes en formato CSV para evidenciar el funcionamiento del sistema.


📂 Estructura del proyecto

Sentiment-IQ/
│── sentiment.py          # Código principal en Python (POO + menú interactivo)
│── sentiment.sql         # Script SQL para la base de datos
│── requirements.txt      # Dependencias necesarias
│── README.md             # Documentación del proyecto
│── docs/
│   └── Proyecto_SentimentIQ.pdf   # Documento académico (portada, UML, DER, reflexión, referencias)
│── data/
│   └── dataset.csv       # Dataset de reseñas (opcional)
│── logs/
│   └── system.log        # Ejemplo de archivo de logs
│── reports/
│   └── reseñas.csv       # Reportes generados automáticamente


⚙️ Instalación y ejecución

1. Clonar o descargar el proyecto
Descarga la carpeta Sentiment-IQ y ábrela en Visual Studio Code.

2. Instalar dependencias
Ejecuta en la terminal:
pip install -r requirements.txt
3. Ejecutar el programa
  python sentiment.py


🖥️ Uso del sistema

1. Al iniciar, el sistema solicita usuario y contraseña.  
   - Si el usuario no existe, se crea automáticamente.  
2. Menú interactivo:
   - 1. Agregar reseña → El usuario escribe una reseña, el sistema la clasifica y la guarda en la BD.  
   - 2. Ver reseñas → Muestra todas las reseñas almacenadas.  
   - 3. Exportar reporte → Genera un archivo reports/reseñas.csv con las reseñas clasificadas.  
   - 4. Salir → Finaliza el programa.  


🧠 Tecnologías utilizadas
- Python 3.10+
- SQLite3 (base de datos embebida)
- Scikit-learn (clasificación de sentimientos con Naive Bayes)
- Hashlib (encriptación de contraseñas)
- CSV (exportación de reportes)


📊 Ejemplo de reporte CSV generado
ID,Texto,Sentimiento
1,El producto es excelente,Positivo
2,No me gustó,Negativo
3,Funciona bien,Positivo
4,Defectuoso,Negativo


🎯 Objetivo académico
Este proyecto integra:
- Programación Orientada a Objetos (POO).
- Persistencia en base de datos.
- Machine Learning aplicado a reseñas.
- Generación de reportes.
- Documentación profesional (README.md, UML, DER, PDF académico).


👤 Autor
Proyecto desarrollado por Alvaro Moreno como parte del módulo integrador de programación y ciencia de datos.