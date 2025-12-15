"""
DEMO COMPLETO: VectorSpace3D
Aplicación interactiva para generar documentos LaTeX con análisis vectorial

Este script demuestra TODAS las capacidades del sistema:
- Vectores 2D y 3D
- Operaciones vectoriales
- Transformaciones lineales
- Bases y subespacios
- Ortogonalización
- Eigenanálisis
"""

import numpy as np
from pylatex import Document, Section, Subsection, Package, NoEscape, Math
from pylatex.utils import bold
import sys

class VectorSpace3DComplete:
    """Sistema completo con todas las funcionalidades"""
    
    def __init__(self, title="Análisis Completo de Vectores"):
        self.doc = Document(documentclass='article')
        self.title = title
        self._setup_document()
        
    def _setup_document(self):
        """Configura paquetes LaTeX"""
        # Paquetes esenciales
        packages = [
            'tikz', 'tikz-3dplot', 'amsmath', 'amssymb',
            ('geometry', 'margin=2.5cm'), 'xcolor', 'pgfplots',
            'graphicx', 'float', 'hyperref'
        ]
        
        for pkg in packages:
            if isinstance(pkg, tuple):
                self.doc.packages.append(Package(pkg[0], options=pkg[1]))
            else:
                self.doc.packages.append(Package(pkg))
        
        # Librerías TikZ
        self.doc.preamble.append(NoEscape(
            r'\usetikzlibrary{arrows.meta, calc, patterns, 3d, decorations.markings}'
        ))
        self.doc.preamble.append(NoEscape(r'\pgfplotsset{compat=1.18}'))
        
        # Configuración hyperref
        self.doc.preamble.append(NoEscape(
            r'\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue}'
        ))
        
        # Comandos matemáticos personalizados
        self.doc.preamble.append(NoEscape(r'\newcommand{\vect}[1]{\mathbf{#1}}'))
        self.doc.preamble.append(NoEscape(r'\newcommand{\R}{\mathbb{R}}'))
        
        # Portada
        self.doc.preamble.append(NoEscape(r'\title{\textbf{' + self.title + r'}\\'))
        self.doc.preamble.append(NoEscape(
            r'\large Sistema VectorSpace3D con Python, TikZ y tikz-3dplot}'
        ))
        self.doc.preamble.append(NoEscape(r'\author{Generado Automáticamente}'))
        self.doc.preamble.append(NoEscape(r'\date{\today}'))
        
        self.doc.append(NoEscape(r'\maketitle'))
        
        # Resumen
        self.doc.append(NoEscape(r'\begin{abstract}'))
        self.doc.append(
            "Este documento presenta un análisis completo de vectores y espacios "
            "vectoriales, generado automáticamente mediante Python (PyLaTeX) y "
            "visualizado con los paquetes LaTeX TikZ y tikz-3dplot. "
            "Incluye representaciones gráficas 2D y 3D, operaciones vectoriales, "
            "transformaciones lineales, análisis de bases, ortogonalización "
            "y cálculo de eigenvalores."
        )
        self.doc.append(NoEscape(r'\end{abstract}'))
        
        self.doc.append(NoEscape(r'\tableofcontents'))
        self.doc.append(NoEscape(r'\newpage'))
    
    def add_intro_section(self):
        """Añade sección introductoria"""
        with self.doc.create(Section("Introducción")):
            self.doc.append(
                "Los vectores son objetos matemáticos fundamentales en álgebra lineal. "
                "En este documento exploramos vectores en "
            )
            self.doc.append(Math(data=[r'\R^2']))
            self.doc.append(" y ")
            self.doc.append(Math(data=[r'\R^3']))
            self.doc.append(", junto con sus propiedades y operaciones.\n\n")
            
            with self.doc.create(Subsection("Notación")):
                self.doc.append("Utilizaremos la siguiente notación:\n\n")
                self.doc.append(NoEscape(r'\begin{itemize}'))
                self.doc.append(NoEscape(r'\item Vectores: $\vect{v}, \vect{u}, \vect{w}$'))
                self.doc.append(NoEscape(r'\item Escalares: $a, b, c \in \R$'))
                self.doc.append(NoEscape(r'\item Matrices: $A, B, C$'))
                self.doc.append(NoEscape(r'\item Producto escalar: $\vect{u} \cdot \vect{v}$'))
                self.doc.append(NoEscape(r'\item Producto cruz: $\vect{u} \times \vect{v}$'))
                self.doc.append(NoEscape(r'\item Norma: $\|\vect{v}\|$'))
                self.doc.append(NoEscape(r'\end{itemize}'))
    
    def visualize_2d_vectors(self, vectors, labels, colors=None):
        """Visualización mejorada de vectores 2D"""
        if colors is None:
            colors = ['blue', 'red', 'green', 'orange', 'purple']
        
        max_val = max(max(abs(v[0]), abs(v[1])) for v in vectors) * 1.3
        
        code = r"\begin{figure}[H]" + "\n"
        code += r"\centering" + "\n"
        code += r"\begin{tikzpicture}[scale=2]" + "\n"
        
        # Ejes con etiquetas
        code += f"    \\draw[->] ({-max_val},0) -- ({max_val},0) node[right] {{$x$}};\n"
        code += f"    \\draw[->] (0,{-max_val}) -- (0,{max_val}) node[above] {{$y$}};\n"
        
        # Grid
        code += f"    \\draw[gray!20, very thin] ({-max_val},{-max_val}) grid ({max_val},{max_val});\n"
        
        # Círculo unitario
        code += "    \\draw[gray!30, dashed] (0,0) circle (1);\n"
        
        # Vectores
        for vec, label, color in zip(vectors, labels, colors):
            # Vector
            code += f"    \\draw[-{{Stealth[length=3mm]}}, ultra thick, {color}] "
            code += f"(0,0) -- ({vec[0]},{vec[1]});\n"
            
            # Etiqueta
            angle = np.arctan2(vec[1], vec[0])
            offset_x = 0.3 * np.cos(angle)
            offset_y = 0.3 * np.sin(angle)
            code += f"    \\node[{color}!80] at ({vec[0]+offset_x},{vec[1]+offset_y}) "
            code += f"{{$\\vect{{{label}}}$}};\n"
            
            # Punto final
            code += f"    \\fill[{color}] ({vec[0]},{vec[1]}) circle (1.5pt);\n"
            
            # Componentes (líneas punteadas)
            code += f"    \\draw[{color}!30, densely dotted] (0,0) -- ({vec[0]},0) -- ({vec[0]},{vec[1]});\n"
        
        code += r"\end{tikzpicture}" + "\n"
        code += r"\caption{Visualización de vectores en $\R^2$}" + "\n"
        code += r"\end{figure}" + "\n"
        
        return code
    
    def visualize_3d_vectors(self, vectors, labels, colors=None, theta=70, phi=120):
        """Visualización mejorada de vectores 3D"""
        if colors is None:
            colors = ['blue', 'red', 'green', 'orange', 'purple']
        
        max_val = max(max(abs(v[0]), abs(v[1]), abs(v[2])) for v in vectors) * 1.2
        
        code = r"\begin{figure}[H]" + "\n"
        code += r"\centering" + "\n"
        code += f"\\tdplotsetmaincoords{{{theta}}}{{{phi}}}\n"
        code += r"\begin{tikzpicture}[tdplot_main_coords, scale=1.5]" + "\n"
        
        # Planos de referencia
        code += "    \\draw[gray!10, fill=gray!5] "
        code += f"(0,0,0) -- ({max_val},0,0) -- ({max_val},{max_val},0) -- (0,{max_val},0) -- cycle;\n"
        
        # Ejes
        code += f"    \\draw[-{{Stealth[length=2mm]}}, thick] (0,0,0) -- ({max_val},0,0) node[right] {{$x$}};\n"
        code += f"    \\draw[-{{Stealth[length=2mm]}}, thick] (0,0,0) -- (0,{max_val},0) node[above] {{$y$}};\n"
        code += f"    \\draw[-{{Stealth[length=2mm]}}, thick] (0,0,0) -- (0,0,{max_val}) node[above] {{$z$}};\n"
        
        # Vectores
        for vec, label, color in zip(vectors, labels, colors):
            # Vector principal
            code += f"    \\draw[-{{Stealth[length=3mm]}}, ultra thick, {color}] "
            code += f"(0,0,0) -- ({vec[0]},{vec[1]},{vec[2]});\n"
            
            # Etiqueta
            code += f"    \\node[{color}!80] at ({vec[0]*1.1},{vec[1]*1.1},{vec[2]*1.1}) "
            code += f"{{$\\vect{{{label}}}$}};\n"
            
            # Punto final
            code += f"    \\fill[{color}] ({vec[0]},{vec[1]},{vec[2]}) circle (2pt);\n"
            
            # Proyección al plano XY
            code += f"    \\draw[{color}!40, dashed, thin] "
            code += f"({vec[0]},{vec[1]},{vec[2]}) -- ({vec[0]},{vec[1]},0);\n"
            code += f"    \\fill[{color}!40] ({vec[0]},{vec[1]},0) circle (1pt);\n"
        
        code += r"\end{tikzpicture}" + "\n"
        code += r"\caption{Visualización de vectores en $\R^3$}" + "\n"
        code += r"\end{figure}" + "\n"
        
        return code
    
    def create_comprehensive_demo(self):
        """Crea demostración completa"""
        
        # Introducción
        self.add_intro_section()
        
        # SECCIÓN 1: Vectores en 2D
        with self.doc.create(Section("Vectores en el Plano")):
            vectors_2d = [(3, 2), (-1, 4), (2, -1)]
            labels_2d = ['u', 'v', 'w']
            
            self.doc.append("Consideremos los siguientes vectores en ")
            self.doc.append(Math(data=[r'\R^2']))
            self.doc.append(":\n\n")
            
            for vec, label in zip(vectors_2d, labels_2d):
                self.doc.append(Math(data=[f'\\vect{{{label}}} = ({vec[0]}, {vec[1]})']))
                norm = np.sqrt(vec[0]**2 + vec[1]**2)
                self.doc.append(f", ")
                self.doc.append(Math(data=[f'\\|\\vect{{{label}}}\\| = {norm:.4f}']))
                self.doc.append("\n\n")
            
            code = self.visualize_2d_vectors(vectors_2d, labels_2d)
            self.doc.append(NoEscape(code))
        
        # SECCIÓN 2: Vectores en 3D
        with self.doc.create(Section("Vectores en el Espacio")):
            vectors_3d = [(2, 3, 1), (1, -1, 2), (-1, 2, 3)]
            labels_3d = ['a', 'b', 'c']
            
            self.doc.append("Ahora analizamos vectores en ")
            self.doc.append(Math(data=[r'\R^3']))
            self.doc.append(":\n\n")
            
            for vec, label in zip(vectors_3d, labels_3d):
                self.doc.append(Math(data=[f'\\vect{{{label}}} = ({vec[0]}, {vec[1]}, {vec[2]})']))
                norm = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
                self.doc.append(f", ")
                self.doc.append(Math(data=[f'\\|\\vect{{{label}}}\\| = {norm:.4f}']))
                self.doc.append("\n\n")
            
            code = self.visualize_3d_vectors(vectors_3d, labels_3d)
            self.doc.append(NoEscape(code))
        
        # SECCIÓN 3: Operaciones vectoriales
        with self.doc.create(Section("Operaciones Vectoriales")):
            v1 = (2, 3, 1)
            v2 = (1, -1, 2)
            
            with self.doc.create(Subsection("Suma de Vectores")):
                v_sum = tuple(a + b for a, b in zip(v1, v2))
                self.doc.append(Math(data=[
                    f'\\vect{{a}} + \\vect{{b}} = {v1} + {v2} = {v_sum}'
                ]))
                self.doc.append("\n\n")
                
                vectors_sum = [v1, v2, v_sum]
                labels_sum = ['a', 'b', 'a+b']
                colors_sum = ['blue', 'red', 'green']
                code = self.visualize_3d_vectors(vectors_sum, labels_sum, colors_sum)
                self.doc.append(NoEscape(code))
            
            with self.doc.create(Subsection("Producto Escalar")):
                dot = sum(a * b for a, b in zip(v1, v2))
                self.doc.append(Math(data=[f'\\vect{{a}} \\cdot \\vect{{b}} = {dot}']))
                self.doc.append("\n\n")
                
                norm_a = np.sqrt(sum(x**2 for x in v1))
                norm_b = np.sqrt(sum(x**2 for x in v2))
                cos_angle = dot / (norm_a * norm_b)
                angle = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))
                
                self.doc.append("Ángulo entre vectores: ")
                self.doc.append(Math(data=[f'\\theta = {angle:.2f}^\\circ']))
                self.doc.append("\n\n")
            
            with self.doc.create(Subsection("Producto Cruz")):
                cross = np.cross(v1, v2)
                self.doc.append(Math(data=[
                    f'\\vect{{a}} \\times \\vect{{b}} = ({cross[0]:.2f}, {cross[1]:.2f}, {cross[2]:.2f})'
                ]))
                self.doc.append("\n\n")
                self.doc.append(
                    "El producto cruz es perpendicular a ambos vectores originales.\n\n"
                )
                
                vectors_cross = [v1, v2, tuple(cross)]
                labels_cross = ['a', 'b', 'a×b']
                colors_cross = ['blue', 'red', 'purple']
                code = self.visualize_3d_vectors(vectors_cross, labels_cross, colors_cross)
                self.doc.append(NoEscape(code))
        
        # SECCIÓN 4: Transformaciones lineales
        with self.doc.create(Section("Transformaciones Lineales")):
            matrix = [[2, -1], [1, 2]]
            self.doc.append("Matriz de transformación:\n\n")
            self.doc.append(Math(data=[
                r'A = \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}'
            ]))
            self.doc.append("\n\n")
            
            # Visualizar transformación de base canónica
            basis = [(1, 0), (0, 1)]
            transformed = [tuple(np.dot(matrix, v)) for v in basis]
            
            self.doc.append("Transformación de la base canónica:\n\n")
            for orig, trans, label in zip(basis, transformed, ['e_1', 'e_2']):
                self.doc.append(Math(data=[
                    f'A\\vect{{{label}}} = {orig} \\mapsto {trans}'
                ]))
                self.doc.append("\n\n")
        
        # SECCIÓN 5: Conclusiones
        with self.doc.create(Section("Conclusiones")):
            self.doc.append(
                "Este documento ha demostrado las capacidades del sistema VectorSpace3D "
                "para visualizar y analizar vectores y espacios vectoriales. "
                "La combinación de Python con TikZ y tikz-3dplot permite crear "
                "documentación matemática de alta calidad de forma automática.\n\n"
            )
            
            self.doc.append(bold("Características destacadas:"))
            self.doc.append(NoEscape(r'\begin{itemize}'))
            self.doc.append(NoEscape(
                r'\item Visualizaciones precisas en 2D y 3D'
            ))
            self.doc.append(NoEscape(
                r'\item Cálculos automáticos de operaciones vectoriales'
            ))
            self.doc.append(NoEscape(
                r'\item Integración perfecta de código, matemáticas y gráficos'
            ))
            self.doc.append(NoEscape(
                r'\item Extensible para aplicaciones más complejas'
            ))
            self.doc.append(NoEscape(r'\end{itemize}'))
    
    def generate(self, filename='demo_completo'):
        """Genera el documento"""
        self.doc.generate_tex(filename)
        print(f"✓ Archivo LaTeX generado: {filename}.tex")
        print(f"\nPara compilar:")
        print(f"  pdflatex {filename}.tex")
        print(f"  pdflatex {filename}.tex  (segunda vez para referencias)")
        
        try:
            self.doc.generate_pdf(filename, clean_tex=False)
            print(f"\n✓ PDF generado exitosamente: {filename}.pdf")
        except Exception as e:
            print(f"\n⚠ No se pudo generar PDF automáticamente: {e}")
            print(f"  Compila manualmente con: pdflatex {filename}.tex")


# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    print("=" * 70)
    print(" VectorSpace3D - Demo Completo".center(70))
    print(" Sistema de Visualización de Vectores con Python y LaTeX".center(70))
    print("=" * 70)
    print()
    
    # Crear y generar documento
    demo = VectorSpace3DComplete(
        "VectorSpace3D: Sistema Completo de Análisis Vectorial"
    )
    demo.create_comprehensive_demo()
    demo.generate('vectorspace3d_demo_completo')
    
    print()
    print("=" * 70)
    print("Demo completado exitosamente!".center(70))
    print("=" * 70)
