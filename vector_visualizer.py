#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VectorVisualizer - Sistema de Visualización de Vectores con PyLaTeX
Autor: Deyvi Samuel Barrera
Versión: 1.0
"""

import numpy as np
from pylatex import Document, Section, Subsection, TikZ, Math, Package
from pylatex.utils import NoEscape
import os

class Vector2D:
    """Clase para representar y operar con vectores en 2D"""
    
    def __init__(self, x, y, name="v"):
        self.x = float(x)
        self.y = float(y)
        self.name = name
    
    def __add__(self, other):
        """Suma de vectores"""
        return Vector2D(self.x + other.x, self.y + other.y, 
                       f"{self.name}+{other.name}")
    
    def __sub__(self, other):
        """Resta de vectores"""
        return Vector2D(self.x - other.x, self.y - other.y,
                       f"{self.name}-{other.name}")
    
    def __mul__(self, scalar):
        """Multiplicación por escalar"""
        return Vector2D(self.x * scalar, self.y * scalar,
                       f"{scalar}{self.name}")
    
    def dot(self, other):
        """Producto punto"""
        return self.x * other.x + self.y * other.y
    
    def magnitude(self):
        """Magnitud del vector"""
        return np.sqrt(self.x**2 + self.y**2)
    
    def angle(self):
        """Ángulo con respecto al eje x (en grados)"""
        return np.degrees(np.arctan2(self.y, self.x))
    
    def normalize(self):
        """Vector unitario"""
        mag = self.magnitude()
        if mag > 0:
            return Vector2D(self.x/mag, self.y/mag, f"\\hat{{{self.name}}}")
        return self
    
    def to_latex(self):
        """Representación LaTeX del vector"""
        return f"\\begin{{pmatrix}} {self.x:.2f} \\\\ {self.y:.2f} \\end{{pmatrix}}"


class Vector3D:
    """Clase para representar y operar con vectores en 3D"""
    
    def __init__(self, x, y, z, name="w"):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.name = name
    
    def __add__(self, other):
        """Suma de vectores"""
        return Vector3D(self.x + other.x, self.y + other.y, 
                       self.z + other.z, f"{self.name}+{other.name}")
    
    def __sub__(self, other):
        """Resta de vectores"""
        return Vector3D(self.x - other.x, self.y - other.y,
                       self.z - other.z, f"{self.name}-{other.name}")
    
    def __mul__(self, scalar):
        """Multiplicación por escalar"""
        return Vector3D(self.x * scalar, self.y * scalar, 
                       self.z * scalar, f"{scalar}{self.name}")
    
    def dot(self, other):
        """Producto punto"""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        """Producto cruz"""
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz, f"{self.name}\\times{other.name}")
    
    def magnitude(self):
        """Magnitud del vector"""
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        """Vector unitario"""
        mag = self.magnitude()
        if mag > 0:
            return Vector3D(self.x/mag, self.y/mag, self.z/mag,
                           f"\\hat{{{self.name}}}")
        return self
    
    def to_latex(self):
        """Representación LaTeX del vector"""
        return f"\\begin{{pmatrix}} {self.x:.2f} \\\\ {self.y:.2f} \\\\ {self.z:.2f} \\end{{pmatrix}}"


class VectorDocument:
    """Clase para generar documentos LaTeX con visualizaciones de vectores"""
    
    def __init__(self, title="Visualizacion de Vectores"):
        # Configuración del documento
        self.doc = Document(documentclass='article')
        
        # Paquetes necesarios
        self.doc.packages.append(Package('babel', options=['spanish']))
        self.doc.packages.append(Package('inputenc', options=['utf8']))
        self.doc.packages.append(Package('amsmath'))
        self.doc.packages.append(Package('amssymb'))
        self.doc.packages.append(Package('tikz'))
        self.doc.packages.append(Package('tikz-3dplot'))
        self.doc.packages.append(Package('xcolor'))
        self.doc.packages.append(Package('geometry', options=['margin=2cm']))
        
        # Librerías TikZ
        self.doc.preamble.append(NoEscape(r'\usetikzlibrary{arrows.meta,calc}'))
        
        # Colores personalizados
        self.doc.preamble.append(NoEscape(r'\definecolor{vec1}{RGB}{220,50,50}'))
        self.doc.preamble.append(NoEscape(r'\definecolor{vec2}{RGB}{50,120,220}'))
        self.doc.preamble.append(NoEscape(r'\definecolor{vec3}{RGB}{50,180,100}'))
        self.doc.preamble.append(NoEscape(r'\definecolor{vec4}{RGB}{200,100,50}'))
        
        # Título
        self.doc.preamble.append(NoEscape(f'\\title{{{title}}}'))
        self.doc.preamble.append(NoEscape(r'\author{VectorVisualizer}'))
        self.doc.preamble.append(NoEscape(r'\date{\today}'))
        
        self.doc.append(NoEscape(r'\maketitle'))
    
    def add_vector_2d(self, vector, color='vec1', title=None):
        """Añade visualización de un vector 2D"""
        
        if title:
            self.doc.append(Subsection(title))
        
        # Información matemática del vector
        with self.doc.create(Math(data=['inline'])) as math:
            math.append(NoEscape(f'\\vec{{{vector.name}}} = {vector.to_latex()}'))
        
        self.doc.append(NoEscape(f'\\\\[0.3cm]'))
        self.doc.append(f'Magnitud: ${vector.magnitude():.3f}$')
        self.doc.append(NoEscape(f'\\\\'))
        self.doc.append(f'Angulo: ${vector.angle():.2f}^\\circ$')
        self.doc.append(NoEscape(f'\\\\[0.5cm]'))
        
        # Visualización TikZ
        scale = min(3.0, 4.0 / max(abs(vector.x), abs(vector.y), 1))
        max_coord = max(abs(vector.x), abs(vector.y)) * 1.2
        
        tikz_code = f"""
        \\begin{{center}}
        \\begin{{tikzpicture}}[scale={scale}]
            % Ejes
            \\draw[->,thick,gray] ({-max_coord*0.2},0) -- ({max_coord},0) node[right] {{$x$}};
            \\draw[->,thick,gray] (0,{-max_coord*0.2}) -- (0,{max_coord}) node[above] {{$y$}};
            
            % Cuadrícula
            \\draw[step=1,gray,very thin,opacity=0.3] ({-max_coord*0.2},{-max_coord*0.2}) grid ({max_coord},{max_coord});
            
            % Vector
            \\draw[->,ultra thick,{color},line width=1.5pt] (0,0) -- ({vector.x},{vector.y}) 
                node[midway,above left] {{$\\vec{{{vector.name}}}$}};
            
            % Componentes (líneas punteadas)
            \\draw[dashed,{color},opacity=0.5] ({vector.x},0) -- ({vector.x},{vector.y});
            \\draw[dashed,{color},opacity=0.5] (0,{vector.y}) -- ({vector.x},{vector.y});
            
            % Etiquetas de componentes
            \\node[below,{color}] at ({vector.x/2},0) {{${vector.name}_x={vector.x:.2f}$}};
            \\node[left,{color}] at (0,{vector.y/2}) {{${vector.name}_y={vector.y:.2f}$}};
            
            % Punto final
            \\fill[{color}] ({vector.x},{vector.y}) circle (2pt);
        \\end{{tikzpicture}}
        \\end{{center}}
        """
        
        self.doc.append(NoEscape(tikz_code))
    
    def add_vector_sum_2d(self, v1, v2, title="Suma de Vectores"):
        """Visualiza la suma de dos vectores 2D"""
        
        self.doc.append(Subsection(title))
        
        result = v1 + v2
        
        # Fórmula matemática
        formula = f"""
        $$\\vec{{{v1.name}}} + \\vec{{{v2.name}}} = {v1.to_latex()} + {v2.to_latex()} = {result.to_latex()}$$
        """
        self.doc.append(NoEscape(formula))
        
        # Visualización
        scale = min(2.5, 5.0 / max(abs(result.x), abs(result.y), 1))
        max_coord = max(abs(v1.x), abs(v1.y), abs(v2.x), abs(v2.y), 
                       abs(result.x), abs(result.y)) * 1.3
        
        tikz_code = f"""
        \\begin{{center}}
        \\begin{{tikzpicture}}[scale={scale}]
            % Ejes
            \\draw[->,thick,gray] ({-max_coord*0.2},0) -- ({max_coord},0) node[right] {{$x$}};
            \\draw[->,thick,gray] (0,{-max_coord*0.2}) -- (0,{max_coord}) node[above] {{$y$}};
            
            % Cuadrícula
            \\draw[step=1,gray,very thin,opacity=0.2] ({-max_coord*0.2},{-max_coord*0.2}) grid ({max_coord},{max_coord});
            
            % Vector v1
            \\draw[->,ultra thick,vec1,line width=1.2pt] (0,0) -- ({v1.x},{v1.y}) 
                node[midway,below left] {{$\\vec{{{v1.name}}}$}};
            
            % Vector v2 desde el origen
            \\draw[->,ultra thick,vec2,line width=1.2pt] (0,0) -- ({v2.x},{v2.y}) 
                node[midway,above right] {{$\\vec{{{v2.name}}}$}};
            
            % Vector v2 desde v1 (método del paralelogramo)
            \\draw[->,thick,vec2,dashed,opacity=0.7] ({v1.x},{v1.y}) -- ({result.x},{result.y});
            
            % Vector v1 desde v2 (método del paralelogramo)
            \\draw[->,thick,vec1,dashed,opacity=0.7] ({v2.x},{v2.y}) -- ({result.x},{result.y});
            
            % Vector resultado
            \\draw[->,ultra thick,vec3,line width=2pt] (0,0) -- ({result.x},{result.y}) 
                node[midway,above,yshift=5pt] {{$\\vec{{{v1.name}}}+\\vec{{{v2.name}}}$}};
            
            % Puntos
            \\fill[vec1] ({v1.x},{v1.y}) circle (2pt);
            \\fill[vec2] ({v2.x},{v2.y}) circle (2pt);
            \\fill[vec3] ({result.x},{result.y}) circle (3pt);
        \\end{{tikzpicture}}
        \\end{{center}}
        """
        
        self.doc.append(NoEscape(tikz_code))
    
    def add_vector_3d(self, vector, color='vec1', title=None):
        """Añade visualización de un vector 3D"""
        
        if title:
            self.doc.append(Subsection(title))
        
        # Información matemática
        with self.doc.create(Math(data=['inline'])) as math:
            math.append(NoEscape(f'\\vec{{{vector.name}}} = {vector.to_latex()}'))
        
        self.doc.append(NoEscape(f'\\\\[0.3cm]'))
        self.doc.append(f'Magnitud: ${vector.magnitude():.3f}$')
        self.doc.append(NoEscape(f'\\\\[0.5cm]'))
        
        # Visualización TikZ-3dplot
        scale = min(1.5, 4.0 / max(abs(vector.x), abs(vector.y), abs(vector.z), 1))
        
        tikz_code = f"""
        \\begin{{center}}
        \\tdplotsetmaincoords{{65}}{{115}}
        \\begin{{tikzpicture}}[tdplot_main_coords,scale={scale}]
            % Ejes
            \\draw[->,thick,gray] (0,0,0) -- (5,0,0) node[right] {{$x$}};
            \\draw[->,thick,gray] (0,0,0) -- (0,5,0) node[above] {{$y$}};
            \\draw[->,thick,gray] (0,0,0) -- (0,0,5) node[above] {{$z$}};
            
            % Plano xy
            \\draw[gray,very thin,opacity=0.2] (0,0,0) -- (5,0,0) -- (5,5,0) -- (0,5,0) -- cycle;
            
            % Vector 3D
            \\draw[->,ultra thick,{color},line width=1.5pt] (0,0,0) -- ({vector.x},{vector.y},{vector.z}) 
                node[above right] {{$\\vec{{{vector.name}}}$}};
            
            % Proyecciones
            \\draw[dashed,{color},opacity=0.5] ({vector.x},{vector.y},0) -- ({vector.x},{vector.y},{vector.z});
            \\draw[dashed,gray,opacity=0.3] ({vector.x},0,0) -- ({vector.x},{vector.y},0);
            \\draw[dashed,gray,opacity=0.3] (0,{vector.y},0) -- ({vector.x},{vector.y},0);
            
            % Componentes en el plano
            \\draw[->,{color},opacity=0.6] (0,0,0) -- ({vector.x},0,0) node[midway,below] {{${vector.name}_x$}};
            \\draw[->,{color},opacity=0.6] (0,0,0) -- (0,{vector.y},0) node[midway,left] {{${vector.name}_y$}};
            \\draw[->,{color},opacity=0.6] (0,0,0) -- (0,0,{vector.z}) node[midway,left] {{${vector.name}_z$}};
            
            % Punto final
            \\fill[{color}] ({vector.x},{vector.y},{vector.z}) circle (2pt);
        \\end{{tikzpicture}}
        \\end{{center}}
        """
        
        self.doc.append(NoEscape(tikz_code))
    
    def add_cross_product_3d(self, v1, v2, title="Producto Cruz"):
        """Visualiza el producto cruz de dos vectores 3D"""
        
        self.doc.append(Subsection(title))
        
        result = v1.cross(v2)
        
        # Fórmula
        formula = f"""
        $$\\vec{{{v1.name}}} \\times \\vec{{{v2.name}}} = {result.to_latex()}$$
        \\\\[0.3cm]
        El vector resultante es perpendicular a ambos vectores.
        """
        self.doc.append(NoEscape(formula))
        
        # Visualización
        tikz_code = f"""
        \\begin{{center}}
        \\tdplotsetmaincoords{{70}}{{120}}
        \\begin{{tikzpicture}}[tdplot_main_coords,scale=1.2]
            % Ejes
            \\draw[->,thick,gray] (0,0,0) -- (4,0,0) node[right] {{$x$}};
            \\draw[->,thick,gray] (0,0,0) -- (0,4,0) node[above] {{$y$}};
            \\draw[->,thick,gray] (0,0,0) -- (0,0,4) node[above] {{$z$}};
            
            % Vector v1
            \\draw[->,ultra thick,vec1,line width=1.2pt] (0,0,0) -- ({v1.x},{v1.y},{v1.z}) 
                node[below right] {{$\\vec{{{v1.name}}}$}};
            
            % Vector v2
            \\draw[->,ultra thick,vec2,line width=1.2pt] (0,0,0) -- ({v2.x},{v2.y},{v2.z}) 
                node[above left] {{$\\vec{{{v2.name}}}$}};
            
            % Plano formado por v1 y v2 (semi-transparente)
            \\fill[gray,opacity=0.15] (0,0,0) -- ({v1.x},{v1.y},{v1.z}) -- 
                ({v1.x+v2.x},{v1.y+v2.y},{v1.z+v2.z}) -- ({v2.x},{v2.y},{v2.z}) -- cycle;
            
            % Vector producto cruz (perpendicular)
            \\draw[->,ultra thick,vec3,line width=1.8pt] (0,0,0) -- ({result.x},{result.y},{result.z}) 
                node[above,xshift=5pt] {{$\\vec{{{v1.name}}}\\times\\vec{{{v2.name}}}$}};
            
            % Puntos
            \\fill[vec1] ({v1.x},{v1.y},{v1.z}) circle (2pt);
            \\fill[vec2] ({v2.x},{v2.y},{v2.z}) circle (2pt);
            \\fill[vec3] ({result.x},{result.y},{result.z}) circle (3pt);
        \\end{{tikzpicture}}
        \\end{{center}}
        """
        
        self.doc.append(NoEscape(tikz_code))
    
    def generate_pdf(self, filename='vector_output'):
        """Genera el archivo PDF"""
        
        # Crear directorio de salida si no existe
        os.makedirs('output', exist_ok=True)
        
        filepath = os.path.join('output', filename)
        
        try:
            self.doc.generate_pdf(filepath, clean_tex=False, compiler='pdflatex')
            print(f"✓ PDF generado exitosamente: {filepath}.pdf")
            print(f"✓ Archivo .tex guardado en: {filepath}.tex")
            return True
        except Exception as e:
            print(f"✗ Error al generar PDF: {e}")
            return False


# ============================================================================
# EJEMPLOS DE USO
# ============================================================================

def ejemplo_vectores_2d():
    """Ejemplo completo con vectores 2D"""
    
    print("Generando documento de vectores 2D...")
    
    doc = VectorDocument(title="Vectores en el Plano - Ejemplos")
    
    # Sección 1: Vector individual
    doc.doc.append(Section("Vector Individual en 2D"))
    v1 = Vector2D(3, 2, "u")
    doc.add_vector_2d(v1, color='vec1', title="Vector $\\vec{u}$")
    
    # Sección 2: Otro vector
    v2 = Vector2D(1, 3, "v")
    doc.add_vector_2d(v2, color='vec2', title="Vector $\\vec{v}$")
    
    # Sección 3: Suma de vectores
    doc.doc.append(Section("Operaciones Vectoriales"))
    doc.add_vector_sum_2d(v1, v2, title="Suma: $\\vec{u} + \\vec{v}$")
    
    # Sección 4: Producto punto
    doc.doc.append(Subsection("Producto Punto"))
    dot_product = v1.dot(v2)
    doc.doc.append(NoEscape(f"$$\\vec{{u}} \\cdot \\vec{{v}} = {dot_product:.2f}$$"))
    
    # Generar PDF
    doc.generate_pdf('vectores_2d')


def ejemplo_vectores_3d():
    """Ejemplo completo con vectores 3D"""
    
    print("Generando documento de vectores 3D...")
    
    doc = VectorDocument(title="Vectores en el Espacio 3D")
    
    # Sección 1: Vectores individuales
    doc.doc.append(Section("Vectores en el Espacio"))
    
    w1 = Vector3D(3, 2, 2, "a")
    doc.add_vector_3d(w1, color='vec1', title="Vector $\\vec{a}$")
    
    w2 = Vector3D(1, 3, 1, "b")
    doc.add_vector_3d(w2, color='vec2', title="Vector $\\vec{b}$")
    
    # Sección 2: Producto cruz
    doc.doc.append(Section("Producto Cruz"))
    doc.add_cross_product_3d(w1, w2)
    
    # Sección 3: Información adicional
    doc.doc.append(Section("Propiedades"))
    dot_prod = w1.dot(w2)
    cross = w1.cross(w2)
    
    info = f"""
    \\textbf{{Producto punto:}} $\\vec{{a}} \\cdot \\vec{{b}} = {dot_prod:.2f}$
    \\\\[0.3cm]
    \\textbf{{Magnitud del producto cruz:}} $|\\vec{{a}} \\times \\vec{{b}}| = {cross.magnitude():.2f}$
    \\\\[0.3cm]
    \\textbf{{Verificacion de perpendicularidad:}}
    \\\\
    $(\\vec{{a}} \\times \\vec{{b}}) \\cdot \\vec{{a}} = {cross.dot(w1):.6f} \\approx 0$
    \\\\
    $(\\vec{{a}} \\times \\vec{{b}}) \\cdot \\vec{{b}} = {cross.dot(w2):.6f} \\approx 0$
    """
    
    doc.doc.append(NoEscape(info))
    
    # Generar PDF
    doc.generate_pdf('vectores_3d')


def ejemplo_completo():
    """Ejemplo que combina 2D y 3D"""
    
    print("Generando documento completo...")
    
    doc = VectorDocument(title="Sistema Completo de Visualizacion Vectorial")
    
    # Tabla de contenidos
    doc.doc.append(NoEscape(r'\tableofcontents'))
    doc.doc.append(NoEscape(r'\newpage'))
    
    # PARTE 1: VECTORES 2D
    doc.doc.append(Section("Algebra Vectorial en 2D"))
    
    # Vectores básicos
    doc.doc.append(Subsection("Vectores Fundamentales"))
    u = Vector2D(4, 2, "u")
    v = Vector2D(-1, 3, "v")
    
    doc.add_vector_2d(u, 'vec1', title="Primer Vector")
    doc.add_vector_2d(v, 'vec2', title="Segundo Vector")
    
    # Operaciones
    doc.add_vector_sum_2d(u, v)
    
    # Producto escalar
    doc.doc.append(Subsection("Multiplicacion por Escalar"))
    u2 = u * 1.5
    doc.add_vector_2d(u2, 'vec4', title="$1.5\\vec{u}$")
    
    # PARTE 2: VECTORES 3D
    doc.doc.append(NoEscape(r'\newpage'))
    doc.doc.append(Section("Algebra Vectorial en 3D"))
    
    # Vectores 3D
    a = Vector3D(2, 3, 1, "a")
    b = Vector3D(1, -1, 2, "b")
    
    doc.add_vector_3d(a, 'vec1', title="Vector $\\vec{a}$ en 3D")
    doc.add_vector_3d(b, 'vec2', title="Vector $\\vec{b}$ en 3D")
    
    # Producto cruz
    doc.add_cross_product_3d(a, b)
    
    # PARTE 3: APLICACIONES
    doc.doc.append(NoEscape(r'\newpage'))
    doc.doc.append(Section("Aplicaciones Practicas"))
    
    doc.doc.append(Subsection("Fisica: Vectores de Fuerza"))
    f1 = Vector2D(3, 4, "F_1")
    f2 = Vector2D(-2, 1, "F_2")
    doc.doc.append("Consideremos dos fuerzas actuando sobre un objeto:")
    doc.add_vector_sum_2d(f1, f2, title="Fuerza Resultante")
    
    # Generar PDF
    doc.generate_pdf('sistema_completo')


if __name__ == "__main__":
    print("=" * 60)
    print("VectorVisualizer - Sistema de Visualizacion de Vectores")
    print("=" * 60)
    print()
    
    print("Seleccione el ejemplo a generar:")
    print("1. Vectores en 2D")
    print("2. Vectores en 3D")
    print("3. Sistema Completo (2D + 3D)")
    print("4. Generar todos")
    print()
    
    opcion = input("Opcion (1-4): ").strip()
    
    if opcion == "1":
        ejemplo_vectores_2d()
    elif opcion == "2":
        ejemplo_vectores_3d()
    elif opcion == "3":
        ejemplo_completo()
    elif opcion == "4":
        ejemplo_vectores_2d()
        print()
        ejemplo_vectores_3d()
        print()
        ejemplo_completo()
    else:
        print("Opcion no valida. Generando ejemplo completo...")
        ejemplo_completo()
    
    print()
    print("=" * 60)
    print("Proceso completado!")
    print("Los archivos PDF se encuentran en la carpeta 'output/'")
    print("=" * 60)
    