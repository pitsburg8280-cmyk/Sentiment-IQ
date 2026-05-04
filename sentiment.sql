-- Script SQL para Sentiment-IQ
-- Crea las tablas necesarias para usuarios y reseñas

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    contraseña TEXT NOT NULL
);

-- Tabla de reseñas
CREATE TABLE IF NOT EXISTS reseñas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    sentimiento TEXT NOT NULL
);

-- Ejemplo de inserción de usuario administrador
INSERT INTO usuarios (nombre, rol, contraseña)
VALUES ('admin', 'admin', '1234');

-- Ejemplo de reseñas iniciales
INSERT INTO reseñas (texto, sentimiento)
VALUES ('El producto es excelente', 'Positivo'),
       ('El producto es malo', 'Negativo');