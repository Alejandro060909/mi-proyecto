# 📊 Diferencias entre repositorios

| | Repositorio 1 | Repositorio 2 |
|---|---|---|
| **Repo** | `Proyecto1` | `mi-proyecto` |
| **Tecnología** | HTML/CSS puro — sitio estático | FastAPI (Python) — app con servidor |

> El contenido del tutorial (textos, imágenes, estilos) es **idéntico** en ambos. El cambio principal es **cómo se sirve el sitio**.

---

## 🗂️ Archivos: Estructura general

| Estado | Archivo | Descripción |
|---|---|---|
| ❌ Solo en repo1 | `index.html` | Página de inicio (HTML puro, en raíz) |
| ❌ Solo en repo1 | `static/css/style.css` | CSS en subcarpeta `css/` |
| ❌ Solo en repo1 | `static/images/image.png` | Imagen en subcarpeta `images/` |
| ✅ Solo en repo2 | `main.py` | Servidor FastAPI |
| ✅ Solo en repo2 | `requirements.txt` | Dependencias Python (`fastapi[standard]`) |
| ✅ Solo en repo2 | `vercel.json` | Config de despliegue Vercel para Python |
| ✅ Solo en repo2 | `.gitignore` | Exclusiones de git |
| ✅ Solo en repo2 | `static/style.css` | CSS movido a la raíz de `/static/` |
| ✅ Solo en repo2 | `static/image.png` | Imagen movida a la raíz de `/static/` |
| ✅ Solo en repo2 | `templates/base.html` | Plantilla base Jinja2 compartida |
| ✅ Solo en repo2 | `templates/index.html` | Template Jinja2 de inicio |
| 🔄 Modificado | `templates/primeraEtapa.html` | Convertido de HTML puro a Jinja2 |
| 🔄 Modificado | `templates/segundaEtapa.html` | Convertido de HTML puro a Jinja2 |
| 🔄 Modificado | `templates/terceraEtapa.html` | Convertido de HTML puro a Jinja2 |

---

## 🏗️ Cambio de arquitectura

### Repo 1 — `Proyecto1` (HTML estático)
```
Proyecto1/
├── index.html               ← Página completa (sin servidor)
├── static/
│   ├── css/
│   │   └── style.css        ← CSS en subcarpeta
│   └── images/
│       └── image.png        ← Imagen en subcarpeta
└── templates/
    ├── primeraEtapa.html    ← HTML completo independiente
    ├── segundaEtapa.html    ← HTML completo independiente
    └── terceraEtapa.html    ← HTML completo independiente
```

### Repo 2 — `mi-proyecto` (FastAPI)
```
mi-proyecto/
├── main.py                  ← Servidor Python
├── requirements.txt
├── vercel.json
├── .gitignore
├── static/
│   ├── style.css            ← CSS en raíz de /static/
│   └── image.png            ← Imagen en raíz de /static/
└── templates/
    ├── base.html            ← Plantilla Jinja2 compartida (nueva)
    ├── index.html           ← Hereda base.html (nuevo)
    ├── primeraEtapa.html    ← Hereda base.html
    ├── segundaEtapa.html    ← Hereda base.html
    └── terceraEtapa.html    ← Hereda base.html
```

---

## 📄 Templates: de HTML puro a Jinja2

Los tres templates compartían el mismo patrón de cambio:

### Repo 1 (HTML puro — abre directo en navegador)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/style.css">
    <title>Primera Etapa</title>
</head>
<body>
    <nav>
        <a href="../index.html">INICIO</a>
        ...
    </nav>
    <main>
        ...contenido...
        <img src="../static/images/image.png" alt="">
        <a href="segundaEtapa.html" class="btn">proximo</a>
    </main>
</body>
</html>
```

### Repo 2 (Jinja2 — requiere servidor FastAPI)
```html
{% extends "base.html" %}

{% block main %}
    ...contenido...
    <img src="{{ url_for('static', path='image.png') }}" alt="icono">
    <a href="/primeraEtapa" class="btn">proximo</a>
{% endblock %}
```

### Diferencias específicas por template

| Elemento | Repo 1 | Repo 2 |
|---|---|---|
| Estructura | HTML completo e independiente | Hereda `base.html` con `{% extends %}` |
| Nav incluida | Repetida en cada archivo | En `base.html` (compartida) |
| Imagen | `../static/images/image.png` | `{{ url_for('static', path='image.png') }}` |
| Links internos | Rutas de archivo (`primeraEtapa.html`, `../index.html`) | Rutas del servidor (`/primeraEtapa`, `/`) |
| CSS | `../static/css/style.css` relativo | `/static/style.css` vía servidor |

---

## 🎨 `style.css` — Sin cambios de contenido, solo reubicación

El CSS es **exactamente igual** en ambos repos. Solo cambió su ubicación:

| | Repo 1 | Repo 2 |
|---|---|---|
| **Ruta** | `static/css/style.css` | `static/style.css` |
| **Contenido** | Idéntico | Idéntico |

---

## 🖼️ `image.png` — Solo reubicación

| | Repo 1 | Repo 2 |
|---|---|---|
| **Ruta** | `static/images/image.png` | `static/image.png` |

---

## ✅ Archivos nuevos en repo 2

### `main.py`
Servidor FastAPI con 4 rutas: `/`, `/primeraEtapa`, `/segundaEtapa`, `/terceraEtapa`, cada una sirviendo su template Jinja2 correspondiente.

### `requirements.txt`
```
fastapi[standard]
```

### `vercel.json`
```json
{
  "version": 2,
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```

### `templates/base.html`
Plantilla Jinja2 nueva con navbar compartida, `{% block main %}` y link al CSS. Permite que los demás templates hereden su estructura sin repetirla.

---

## 🔁 Resumen ejecutivo

El proyecto es el **mismo tutorial de Main Storage en Minecraft**, pero migrado de un **sitio HTML estático** (repo 1) a una **app web con servidor FastAPI** (repo 2). Esto implica:

- ✅ Se introduce un servidor Python con rutas limpias (`/primeraEtapa` en vez de `primeraEtapa.html`)
- ✅ Se crea `base.html` como plantilla compartida, eliminando el `<nav>` repetido en cada página
- ✅ Se prepara el proyecto para despliegue en Vercel con `vercel.json`
- ✅ Se añade `.gitignore` para control de versiones
- ⚠️ El sitio ya no se puede abrir directo desde el explorador de archivos — requiere servidor
- ⚠️ Los assets se "aplanan" de subcarpetas (`css/`, `images/`) a la raíz de `/static/`
