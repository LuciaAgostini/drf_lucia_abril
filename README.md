# API de Saludos — Primer Práctico DRF

Proyecto para el Primer Práctico de "Ingeniería de Software" (ITEC).
Temática elegida: **saludos** (mensajes de saludo en distintos idiomas).

## Contenido

- Modelo `Saludo` (mensaje, autor, idioma, fecha de creación)
- Serializer `SaludoSerializer` (ModelSerializer)
- Vistas funcionales de CRUD con `@api_view`:
  - `GET   /api/saludos/`            -> listar saludos
  - `POST  /api/saludos/`            -> crear saludo
  - `GET   /api/saludos/<id>/`       -> ver detalle
  - `PUT   /api/saludos/<id>/`       -> actualizar completo
  - `PATCH /api/saludos/<id>/`       -> actualizar parcial
  - `DELETE /api/saludos/<id>/`      -> eliminar

## Cómo correr el proyecto

### 1. Instalar dependencias con uv

```
uv sync
```

### 2. Entrar en src y migrar

```
cd src
uv run manage.py makemigrations saludos
uv run manage.py migrate
```

### 3. (Opcional) Crear superusuario para el admin

```
uv run manage.py createsuperuser
```

### 4. Levantar el servidor

```
uv run manage.py runserver
```

La API queda disponible en:

```
http://127.0.0.1:8000/api/saludos/
```

El panel de administración en:

```
http://127.0.0.1:8000/admin/
```

## Ejemplo de body para crear un saludo (POST)

```json
{
  "mensaje": "Hola mundo",
  "autor": "Lucia",
  "idioma": "es"
}
```

## Probar los endpoints

Se recomienda usar Postman, Bruno o ThunderClient para probar los endpoints.
