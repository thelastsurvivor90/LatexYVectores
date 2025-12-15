# 🎯 VectorSpace3D

## Sistema Avanzado de Visualización de Vectores y Espacios Vectoriales

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-TikZ-green.svg)](https://tikz.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Descripción

**VectorSpace3D** es un sistema innovador que combina la potencia computacional de Python con la elegancia tipográfica de LaTeX para crear visualizaciones matemáticas profesionales de vectores y espacios vectoriales en 2D y 3D.

### Características Principales

✨ **Visualización Automática**: Genera gráficos TikZ de alta calidad  
🔢 **Cálculos Precisos**: Operaciones vectoriales con NumPy  
📐 **Geometría 3D**: Utiliza tikz-3dplot para representaciones tridimensionales  
📊 **Análisis Completo**: Bases, ortogonalización, eigenvalores  
📄 **Documentación Automática**: Genera PDFs profesionales  

---

## 🚀 Instalación

### Requisitos Previos

**Python 3.8 o superior:**
```bash
python --version
```

**Distribución LaTeX completa:**
- **Linux**: `sudo apt-get install texlive-full`
- **macOS**: Instalar [MacTeX](https://www.tug.org/mactex/)
- **Windows**: Instalar [MiKTeX](https://miktex.org/)

### Instalar Dependencias Python

```bash
# Clonar repositorio
git clone https://github.com/usuario/vectorspace3d.git
cd vectorspace3d

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate  # Windows

# Instalar paquetes
pip install numpy pylatex
```

### Verificar Paquetes LaTeX

Asegúrate de tener instalados:
- `tikz`
- `tikz-3dplot`
- `pgfplots`
- `amsmath`
- `geometry`

---

## 📁 Estructura del Proyecto

```
VectorSpace3D/
├── README.md                      # Este archivo
├── requirements.txt               # Dependencias Python
├── LICENSE                        # Licencia MIT
│
├── src/
│   ├── __init__.py
│   ├── vectorspace3d_main.py     # Módulo principal
│   └── vectorspace_advanced.py   # Funciones avanzadas
│
├── examples/
│   ├── ejemplo_basico_2d.py      # Ejemplo simple 2D
│   ├── ejemplo_basico_3d.py      # Ejemplo simple 3D
│   ├── ejemplo_operaciones.py    # Operaciones vectoriales
│   ├── ejemplo_transformaciones.py
│   ├── ejemplo_gram_schmidt.py
│   └── demo_completo.py          # Demo con todas las funciones
│
├── docs/
│   ├── manual_usuario.tex        # Manual en LaTeX
│   ├── tutorial.md               # Tutorial paso a paso
│   └── api_reference.md          # Referencia de la API
│
├── output/                        # Archivos generados
│   ├── *.tex                     # Código LaTeX
│   └── *.pdf                     # PDFs compilados
│
└── tests/
    └── test_vectorspace.py       # Tests unitarios
```

---

## 🎓 Uso Básico

### Ejemplo 1: Vectores en 2D

```python
from vectorspace3d_main import VectorSpace3D

# Crear sistema
vs = VectorSpace3D("Mi Primer Análisis Vectorial")

# Definir vectores
vectors = [(3, 2), (-1, 4), (2, -3)]
labels = ['u', 'v', 'w']

# Visualizar
vs.add_vector_2d(vectors, labels=labels, 
                 title="Vectores en el Plano")

# Generar documento
vs.generate('mi_analisis_2d')
```

### Ejemplo 2: Vectores en 3D

```python
# Vectores tridimensionales
vectors_3d = [(2, 3, 1), (1, -1, 2), (-2, 1, 3)]

vs.add_vector_3d(vectors_3d, 
                 labels=['a', 'b', 'c'],
                 view_angle=(70, 120))

vs.generate('analisis_3d')
```

### Ejemplo 3: Operaciones Vectoriales

```python
# Suma, producto escalar, producto cruz
vs.add_vector_operations(
    v1=(3, 4, 2), 
    v2=(1, -2, 5),
    label1='p', 
    label2='q'
)

vs.generate('operaciones')
```

---

## 🔬 Funcionalidades Avanzadas

### Análisis de Bases

```python
from vectorspace_advanced import AdvancedVectorSpace

avs = AdvancedVectorSpace("Análisis de Espacios")

# Verificar base
basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
avs.add_vector_space_basis(basis, "Base Canónica")
```

### Ortogonalización de Gram-Schmidt

```python
# Vectores no ortogonales
vectors = [[3, 1, 0], [2, 2, 1], [1, 0, 2]]

# Ortogonalizar
avs.add_gram_schmidt(vectors)
```

### Proyección sobre Subespacios

```python
# Proyectar vector sobre subespacio
vector = [5, 3, 1]
subspace = [[1, 0, 0], [0, 1, 0]]  # Plano XY

avs.add_subspace_projection(vector, subspace)
```

### Análisis de Eigenvalores

```python
# Matriz simétrica
matrix = [[2, 1], [1, 2]]

avs.add_eigenanalysis(matrix)
```

---

## 🌐 Proyecto Overleaf

### Opción 1: Subir Archivos Generados

1. Ejecuta el script Python para generar `.tex`
2. Sube el archivo a [Overleaf](https://www.overleaf.com/)
3. Compila en Overleaf

### Opción 2: Template Overleaf

Hemos creado un template público en Overleaf:

🔗 **[VectorSpace3D Template](https://www.overleaf.com/read/xxxxx)**

Para usar:
1. Abre el link
2. Click en "Copy Project"
3. Modifica los vectores y parámetros
4. Compila

### Estructura del Template Overleaf

```
proyecto_overleaf/
├── main.tex                  # Documento principal
├── preamble.tex             # Preámbulo con paquetes
├── sections/
│   ├── intro.tex
│   ├── vectores_2d.tex
│   ├── vectores_3d.tex
│   ├── operaciones.tex
│   └── conclusiones.tex
└── figures/
    ├── vector_2d_1.tex
    ├── vector_3d_1.tex
    └── transformacion.tex
```

---

## 🎥 Video Tutorial

📺 **Ver video explicativo completo**: [YouTube Link](#)

El video cubre:
- 00:00 - Introducción y motivación
- 02:30 - Instalación y configuración
- 05:00 - Ejemplos básicos 2D
- 10:00 - Visualización 3D con tikz-3dplot
- 15:00 - Operaciones vectoriales
- 20:00 - Funciones avanzadas
- 25:00 - Integración con Overleaf
- 30:00 - Casos de uso prácticos

---

## 📖 Documentación Completa

### Manual de Usuario

Ver [`docs/manual_usuario.tex`](docs/manual_usuario.tex) para:
- Guía completa de todas las funciones
- Ejemplos detallados
- Solución de problemas
- Mejores prácticas

### API Reference

Ver [`docs/api_reference.md`](docs/api_reference.md) para:
- Documentación de cada función
- Parámetros y tipos
- Valores de retorno
- Ejemplos de código

---

## 🎨 Personalización

### Colores

```python
# Personalizar colores de vectores
colors = ['blue!80', 'red!80', 'green!70', 'orange!90']
vs.add_vector_2d(vectors, colors=colors)
```

### Ángulos de Vista 3D

```python
# Cambiar perspectiva
vs.add_vector_3d(vectors, view_angle=(45, 135))
```

### Escala

```python
# Ajustar escala del gráfico
# Modificar en el código generado TikZ
```

---

## 🧪 Ejemplos Completos

### Demo Interactivo

```bash
# Ejecutar demo completo
python examples/demo_completo.py
```

Genera un documento con:
- ✅ Vectores 2D y 3D
- ✅ Todas las operaciones
- ✅ Transformaciones lineales
- ✅ Análisis de bases
- ✅ Ortogonalización
- ✅ Eigenanálisis

### Casos de Uso

**1. Material Educativo**
```python
# Crear material para clase de álgebra lineal
vs = VectorSpace3D("Clase 05: Espacios Vectoriales")
# ... agregar contenido
vs.generate('clase_05')
```

**2. Investigación**
```python
# Documentar resultados de investigación
avs = AdvancedVectorSpace("Análisis de Datos Multidimensionales")
# ... análisis específico
avs.generate('paper_figuras')
```

**3. Presentaciones**
```python
# Generar figuras para presentación
vs = VectorSpace3D("Presentación Proyecto")
# ... crear visualizaciones
vs.generate('presentacion_figuras')
```

---

## 🛠️ Solución de Problemas

### Error: "Module not found: pylatex"

```bash
pip install pylatex numpy
```

### Error: "pdflatex command not found"

Instala una distribución completa de LaTeX:
- Ubuntu/Debian: `sudo apt-get install texlive-full`
- macOS: Instalar MacTeX
- Windows: Instalar MiKTeX

### Los PDF no se generan automáticamente

```python
# Solo generar .tex sin compilar
vs.generate('archivo', compile_pdf=False)

# Luego compilar manualmente
# pdflatex archivo.tex
```

### Gráficos 3D no se ven correctamente

Verifica que tikz-3dplot esté instalado:
```bash
kpsewhich tikz-3dplot.sty
```

---

## 📊 Comparación con Otras Herramientas

| Característica | VectorSpace3D | Matplotlib | Mathematica | GeoGebra |
|----------------|---------------|------------|-------------|----------|
| Calidad tipográfica | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Integración LaTeX | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Vectores 3D | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Automatización | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Gratis/Open Source | ✅ | ✅ | ❌ | ✅ |

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver [`LICENSE`](LICENSE) para más detalles.

---

## 👥 Autores

- **Desarrollador Principal** - *Concepto y desarrollo* - [@usuario](https://github.com/usuario)

---

## 🙏 Agradecimientos

- Equipo de TikZ por el increíble sistema de gráficos
- Desarrolladores de tikz-3dplot
- Comunidad de PyLaTeX
- Todos los contribuidores

---

## 📞 Contacto

- **Email**: contacto@vectorspace3d.com
- **GitHub**: [github.com/usuario/vectorspace3d](https://github.com/usuario/vectorspace3d)
- **Documentación**: [vectorspace3d.readthedocs.io](https://vectorspace3d.readthedocs.io)

---

## 🔄 Actualizaciones

### v1.0.0 (2025-01-16)
- ✨ Lanzamiento inicial
- 📊 Visualización 2D y 3D
- 🔢 Operaciones vectoriales básicas
- 📐 Transformaciones lineales

### Roadmap v2.0.0
- [ ] Interfaz gráfica (GUI)
- [ ] Animaciones con TikZ
- [ ] Soporte para más operaciones
- [ ] Exportación a múltiples formatos
- [ ] Integración con Jupyter Notebooks

---

⭐ **Si este proyecto te es útil, no olvides darle una estrella en GitHub!** ⭐
