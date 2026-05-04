import sqlite3
import hashlib
import csv
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# --- Clase Usuario ---
class Usuario:
    def __init__(self, nombre, rol, password):
        self.__nombre = nombre
        self.__rol = rol
        self.__password = hashlib.sha256(password.encode()).hexdigest()

    def get_nombre(self):
        return self.__nombre

    def validar_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

class Administrador(Usuario):
    def __init__(self, nombre, password):
        super().__init__(nombre, "admin", password)

    def crear_usuario(self, nombre, rol, password, db):
        db.insertar_usuario(nombre, rol, password)

class Cliente(Usuario):
    def __init__(self, nombre, password):
        super().__init__(nombre, "cliente", password)

    def enviar_reseña(self, texto, analyzer, db):
        sentimiento = analyzer.predecir(texto)
        reseña = Reseña(texto, sentimiento)
        db.insertar_reseña(reseña)

# --- Clase Reseña ---
class Reseña:
    def __init__(self, texto, sentimiento=None):
        self.texto = texto
        self.sentimiento = sentimiento

# --- Base de Datos ---
class SentimentDB:
    def __init__(self, db_name="sentiment.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            rol TEXT,
            contraseña TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS reseñas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT,
            sentimiento TEXT)""")
        self.conn.commit()

    def insertar_usuario(self, nombre, rol, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("INSERT INTO usuarios (nombre, rol, contraseña) VALUES (?,?,?)",
                            (nombre, rol, hashed))
        self.conn.commit()

    def validar_login(self, nombre, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        user = self.cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND contraseña=?",
                                   (nombre, hashed)).fetchone()
        return user

    def insertar_reseña(self, reseña):
        self.cursor.execute("INSERT INTO reseñas (texto, sentimiento) VALUES (?,?)",
                            (reseña.texto, reseña.sentimiento))
        self.conn.commit()

    def leer_reseñas(self):
        return self.cursor.execute("SELECT * FROM reseñas").fetchall()

    def exportar_csv(self, archivo="reports/reseñas.csv"):
        reseñas = self.leer_reseñas()
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Texto", "Sentimiento"])
            writer.writerows(reseñas)

# --- ML: Clasificación ---
class SentimentAnalyzer:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def entrenar(self, textos, etiquetas):
        X = self.vectorizer.fit_transform(textos)
        self.model.fit(X, etiquetas)

    def normalizar(self, texto):
        texto = texto.lower()
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        return texto

    def predecir(self, texto):
        texto = self.normalizar(texto)
        X = self.vectorizer.transform([texto])
        return self.model.predict(X)[0]

# --- Menú Interactivo ---
def menu():
    db = SentimentDB()
    sa = SentimentAnalyzer()

    # Dataset ampliado: 20 positivas y 20 negativas
    textos = [
        "el producto es excelente", "me gusto mucho", "funciona bien", "muy rapido", "positivo",
        "gran calidad", "muy satisfecho", "lo recomiendo", "me encanto", "perfecto",
        "bueno", "maravilloso", "fantastico", "increible", "mejor de lo esperado",
        "muy util", "agradable", "eficiente", "vale la pena", "superior",
        "el producto es malo", "no me gusto", "defectuoso", "muy lento", "terrible",
        "negativo", "poca calidad", "muy insatisfecho", "no lo recomiendo", "horrible",
        "pesimo", "desastroso", "fallo", "inutil", "decepcionante",
        "muy caro", "molesto", "frustrante", "no funciona", "mala experiencia"
    ]
    etiquetas = [
        "Positivo","Positivo","Positivo","Positivo","Positivo",
        "Positivo","Positivo","Positivo","Positivo","Positivo",
        "Positivo","Positivo","Positivo","Positivo","Positivo",
        "Positivo","Positivo","Positivo","Positivo","Positivo",
        "Negativo","Negativo","Negativo","Negativo","Negativo",
        "Negativo","Negativo","Negativo","Negativo","Negativo",
        "Negativo","Negativo","Negativo","Negativo","Negativo",
        "Negativo","Negativo","Negativo","Negativo","Negativo"
    ]

    sa.entrenar(textos, etiquetas)

    print("=== Sentiment-IQ ===")
    nombre = input("Usuario: ")
    password = input("Contraseña: ")

    if not db.validar_login(nombre, password):
        print("Credenciales inválidas. Creando usuario nuevo...")
        db.insertar_usuario(nombre, "cliente", password)

    cliente = Cliente(nombre, password)

    while True:
        print("\n--- Menú ---")
        print("1. Agregar reseña")
        print("2. Ver reseñas")
        print("3. Exportar reporte")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            texto = input("Escribe tu reseña: ")
            cliente.enviar_reseña(texto, sa, db)
            print("Reseña guardada.")
        elif opcion == "2":
            reseñas = db.leer_reseñas()
            for r in reseñas:
                print(r)
        elif opcion == "3":
            db.exportar_csv()
            print("Reporte exportado en reports/reseñas.csv")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()