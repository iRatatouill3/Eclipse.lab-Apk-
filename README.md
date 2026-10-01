# EclipseLab — APK Android

Aplicación educativa sobre eclipses solares creada en **Python + Kivy**.

**Autor:** Carlos Felipe Obando Latorre  
**Curso:** 10-2  
**Año:** 2026

## Qué incluye
- Explicación de qué es un eclipse solar.
- Tipos de eclipse: total, parcial, anular e híbrido.
- Simulador interactivo.
- Recomendaciones de seguridad.
- Mini quiz.
- Pantalla del autor.

---

# OPCIÓN RECOMENDADA: crear el APK desde GitHub sin instalar programas

## 1. Crear un repositorio
En GitHub pulsa **New repository** y llámalo, por ejemplo:

`EclipseLab-APK`

Puedes dejarlo público.

## 2. Subir los archivos
Sube todo el contenido de esta carpeta al repositorio.

IMPORTANTE: la carpeta:

`.github/workflows/`

también debe quedar subida con el archivo:

`android.yml`

## 3. Ejecutar la compilación
En tu repositorio entra en:

**Actions → Build Android APK → Run workflow**

GitHub empezará a compilar la aplicación.

La primera compilación puede tardar varios minutos porque descarga las herramientas de Android.

## 4. Descargar el APK
Cuando termine:

1. Abre la ejecución que aparezca en verde.
2. Baja hasta **Artifacts**.
3. Pulsa **EclipseLab-APK**.
4. Se descargará un ZIP.
5. Dentro estará el archivo `.apk`.

## 5. Instalarlo en Android
Pasa el APK a tu celular, ábrelo y Android te pedirá autorización para instalar aplicaciones desde esa fuente.

---

# Probar el código en computador

Si tienes Python instalado:

```bash
pip install kivy
python main.py
```

---

# Cómo explicarlo al profesor

“Mi proyecto es una aplicación Android educativa sobre los eclipses solares. La desarrollé en Python utilizando Kivy para crear la interfaz gráfica. La aplicación tiene varias pantallas, un simulador, información sobre los tipos de eclipses, recomendaciones para observarlos de forma segura y un quiz interactivo. Para convertir el proyecto de Python en un APK utilicé Buildozer mediante GitHub Actions.”
