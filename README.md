# LatexYVectores y Guia de Instalacion y Uso
🎯 Concepto de la Aplicación VectorVisualizer: Un sistema que permite crear documentos LaTeX profesionales con visualizaciones automáticas de operaciones vectoriales, transformaciones lineales y espacios vectoriales.
# 📦 VectorVisualizer - Guía de Instalación y Uso

## 🚀 Instalación

### Requisitos Previos

#### 1. Python 3.8 o superior
```bash
# Verificar versión de Python
python --version
# o
python3 --version
```

#### 2. Distribución LaTeX

**Windows:**
- Descargar e instalar [MiKTeX](https://miktex.org/download)
- O [TeX Live](https://tug.org/texlive/windows.html)

**macOS:**
```bash
# Usando Homebrew
brew install mactex-no-gui
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install texlive-full
# O instalación mínima:
sudo apt-get install texlive texlive-latex-extra texlive-lang-spanish
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install texlive-scheme-full
```

#### 3. Paquetes LaTeX Necesarios

Los siguientes paquetes deben estar instalados:
- `tikz`
- `tikz-3dplot`
- `babel` (con soporte español)
- `inputenc`
- `amsmath`
- `amssymb`
- `xcolor`
- `geometry`

MiKTeX y TeX Live completos incluyen estos paquetes por defecto.

### Instalación del Proyecto

#### Opción 1: Instalación Manual

```bash
# 1. Crear directorio del proyecto
mkdir VectorVisualizer
cd VectorVisualizer

# 2. Crear archivo vector_visualizer.py
# (copiar el código Python proporcionado)

# 3. Instalar dependencias Python
pip install pylatex numpy

# 4. Crear carpeta de salida
mkdir output
```

#### Opción 2: Usando requirements.txt

```bash
# 1. Clonar o descargar el proyecto
cd VectorVisualizer

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Verificar instalación
python -c "import pylatex; print('PyLaTeX instalado correctamente')"
```

#### Opción 3: Usando entorno virtual (Recomendado)

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## 🎮 Uso Básico

### Ejecución del Programa

```bash
python vector_visualizer.py
```

### Menú Interactivo

```
============================================================
VectorVisualizer - Sistema de Visualización de Vectores
============================================================

Seleccione el ejemplo a generar:
1. Vectores en 2D
2. Vectores en 3D
3. Sistema Completo (2D + 3D)
4. Generar todos

Opción (1-4): 
```

### Salida Generada

Los archivos se guardan en `output/`:
- `vectores_2d.pdf` - Documento con ejemplos 2D
- `vectores_2d.tex` - Código fuente LaTeX
- `vectores_3d.pdf` - Documento con ejemplos 3D
- `vectores_3d.tex` - Código fuente LaTeX
- `sistema_completo.pdf` - Documento integrado
- `sistema_completo.tex` - Código fuente completo

---

## 💡 Ejemplos de Uso Programático

### Ejemplo 1: Vector Simple en 2D

```python
from vector_visualizer import Vector2D, VectorDocument

# Crear documento
doc = VectorDocument(title="Mi Primer Vector")

# Crear vector
v = Vector2D(3, 4, "v")

# Añadir al documento
doc.add_vector_2d(v, color='vec1', title="Vector de Velocidad")

# Generar PDF
doc.generate_pdf('mi_vector')
```

### Ejemplo 2: Suma de Vectores

```python
from vector_visualizer import Vector2D, VectorDocument

doc = VectorDocument(title="Suma de Fuerzas")

# Dos fuerzas
f1 = Vector2D(5, 2, "F_1")
f2 = Vector2D(-2, 3, "F_2")

# Visualizar suma
doc.add_vector_sum_2d(f1, f2, title="Fuerza Resultante")

doc.generate_pdf('suma_fuerzas')
```

### Ejemplo 3: Producto Cruz en 3D

```python
from vector_visualizer import Vector3D, VectorDocument

doc = VectorDocument(title="Momento Angular")

# Vectores posición y momento lineal
r = Vector3D(2, 0, 0, "r")
p = Vector3D(0, 3, 1, "p")

# Calcular momento angular L = r × p
doc.add_cross_product_3d(r, p)

# Información adicional
L = r.cross(p)
doc.doc.append(f"Magnitud del momento: {L.magnitude():.2f}")

doc.generate_pdf('momento_angular')
```

### Ejemplo 4: Transformación Lineal

```python
from vector_visualizer import Vector2D, VectorDocument
import numpy as np

doc = VectorDocument(title="Rotación de Vector")

# Vector original
v = Vector2D(3, 0, "v")
doc.add_vector_2d(v, 'vec1', title="Vector Original")

# Rotación de 45 grados
theta = np.radians(45)
rot_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Aplicar rotación
v_rot_coords = rot_matrix @ np.array([v.x, v.y])
v_rot = Vector2D(v_rot_coords[0], v_rot_coords[1], "v'")

doc.add_vector_2d(v_rot, 'vec2', title="Vector Rotado 45°")

doc.generate_pdf('rotacion')
```

---

## 🎨 Personalización

### Cambiar Colores

```python
# En la clase VectorDocument, modificar el preamble:
doc.preamble.append(NoEscape(r'\definecolor{micolor}{RGB}{100,200,150}'))

# Usar el color personalizado
doc.add_vector_2d(v, color='micolor')
```

### Ajustar Escala

```python
# Modificar el parámetro scale en el código TikZ
scale = 2.0  # Mayor para vectores pequeños
scale = 0.5  # Menor para vectores grandes
```

### Cambiar Idioma

```python
# En Document initialization
doc.packages.append(Package('babel', options=['english']))
# o
doc.packages.append(Package('babel', options=['french']))
```

### Personalizar Estilo de Flechas

```python
# En el código TikZ, modificar:
\draw[->,ultra thick,vec1,line width=2pt,-{Stealth[length=5mm]}]
```

---

## 🔧 Solución de Problemas

### Error: "pdflatex not found"

**Solución:**
- Verificar que LaTeX esté instalado: `pdflatex --version`
- Agregar LaTeX al PATH del sistema
- Reiniciar terminal después de instalar LaTeX

### Error: "Package tikz-3dplot not found"

**Solución:**
```bash
# MiKTeX
mpm --install=tikz-3dplot

# TeX Live
tlmgr install tikz-3dplot
```

### Error: "UnicodeDecodeError"

**Solución:**
- Asegurar que los archivos Python usen codificación UTF-8
- Agregar al inicio del archivo:
```python
# -*- coding: utf-8 -*-
```

### PDFs se generan pero están en blanco

**Solución:**
- Verificar logs en archivos `.log` en carpeta `output/`
- Compilar manualmente el `.tex` para ver errores:
```bash
cd output
pdflatex sistema_completo.tex
```

### Error: "ImportError: No module named 'pylatex'"

**Solución:**
```bash
pip install --upgrade pylatex
# O con Python 3 específicamente:
pip3 install pylatex
```

---

## 📚 Uso en Overleaf

### Importar a Overleaf

1. Ejecutar el programa y generar archivos `.tex`
2. Ir a [Overleaf](https://www.overleaf.com)
3. Crear "New Project" → "Blank Project"
4. Copiar contenido del archivo `.tex` generado
5. Compilar en Overleaf

### Nota sobre Overleaf

Overleaf incluye todos los paquetes necesarios (tikz, tikz-3dplot, etc.), por lo que el código generado funcionará sin modificaciones.

---

## 🎓 Casos de Uso Educativos

### Para Profesores

```python
# Generar material de clase completo
doc = VectorDocument(title="Clase 5: Vectores en el Espacio")

# Agregar múltiples ejemplos
for i in range(1, 6):
    v = Vector3D(i, i*0.5, i*0.3, f"v_{i}")
    doc.add_vector_3d(v, f'vec{i%4+1}', 
                      title=f"Ejemplo {i}")

doc.generate_pdf('clase_5_vectores')
```

### Para Estudiantes

```python
# Resolver ejercicios con visualización
def resolver_problema(v1, v2):
    doc = VectorDocument(title="Solución del Ejercicio")
    
    # Datos del problema
    doc.doc.append(Section("Datos"))
    doc.add_vector_2d(v1, 'vec1', title="Vector A")
    doc.add_vector_2d(v2, 'vec2', title="Vector B")
    
    # Solución
    doc.doc.append(Section("Solución"))
    doc.add_vector_sum_2d(v1, v2, title="A + B")
    
    # Respuesta
    resultado = v1 + v2
    doc.doc.append(f"Magnitud resultante: {resultado.magnitude():.2f}")
    
    return doc

# Usar
v1 = Vector2D(3, 4, "A")
v2 = Vector2D(1, 2, "B")
solucion = resolver_problema(v1, v2)
solucion.generate_pdf('ejercicio_resuelto')
```

---

## 🚀 Extensiones Avanzadas

### Agregar Animaciones (opcional)

Usando el paquete `animate` de LaTeX:

```python
doc.packages.append(Package('animate'))

# Generar frames de animación
for angle in range(0, 360, 10):
    theta = np.radians(angle)
    v_rot = Vector2D(np.cos(theta)*3, np.sin(theta)*3, "v")
    # Agregar frame...
```

### Integración con Matplotlib

```python
import matplotlib.pyplot as plt

# Crear gráfico matplotlib
fig, ax = plt.subplots()
ax.quiver(0, 0, v.x, v.y, angles='xy', scale_units='xy', scale=1)
plt.savefig('vector_plot.png')

# Incluir en documento LaTeX
from pylatex import Figure
with doc.create(Figure()) as fig:
    fig.add_image('vector_plot.png', width='0.5\\textwidth')
```

---

## 📞 Soporte y Recursos

### Documentación Oficial

- **PyLaTeX**: https://jeltef.github.io/PyLaTeX/
- **TikZ Manual**: https://tikz.dev/
- **tikz-3dplot**: https://www.ctan.org/pkg/tikz-3dplot

### Comunidad

- Stack Overflow: Tag `pylatex` o `tikz`
- TeX Stack Exchange: https://tex.stackexchange.com
- GitHub Issues: (repositorio del proyecto)

### Mejores Prácticas

1. ✅ Siempre usar `try-except` para manejo de errores
2. ✅ Verificar instalación de LaTeX antes de ejecutar
3. ✅ Mantener archivos `.tex` para referencia
4. ✅ Usar nombres descriptivos para vectores
5. ✅ Comentar código personalizado
6. ✅ Crear backup de configuraciones personalizadas

---

## 📝 Licencia y Contribuciones

Este proyecto es de código abierto y puede ser modificado según sus necesidades.

Para contribuir:
1. Fork del repositorio
2. Crear branch para nueva funcionalidad
3. Commit cambios con mensajes descriptivos
4. Push y crear Pull Request

---

## 🎯 Próximos Pasos

Después de dominar lo básico, puedes:

1. Crear biblioteca personal de vectores comunes
2. Automatizar generación de exámenes
3. Integrar con sistemas LMS (Moodle, Canvas)
4. Desarrollar API REST para generación de PDFs
5. Crear interfaz gráfica con Tkinter o PyQt

¡Disfruta explorando el mundo de los vectores con VectorVisualizer! 🚀
