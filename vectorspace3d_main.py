"""
VectorSpace3D: Sistema de Visualización de Vectores con Python y LaTeX
Utiliza PyLaTeX, TikZ y tikz-3dplot para crear documentos matemáticos avanzados
"""

import numpy as np
from pylatex import Document, Section, Subsection, Math, TikZ, Axis, Plot
from pylatex import Package, NoEscape, Figure, Command
from pylatex.utils import bold
import os

class VectorSpace3D:
    """Clase principal para manejo de vectores y espacios vectoriales"""
    
    def __init__(self, title="Análisis de Vectores y Espacios Vectoriales"):
        self.doc = Document(documentclass='article')
        self.title = title
        self._setup_document()
        
    def _setup_document(self):
        """Configura paquetes y preámbulo del documento"""
        # Paquetes esenciales
        self.doc.packages.append(Package('tikz'))
        self.doc.packages.append(Package('tikz-3dplot'))
        self.doc.packages.append(Package('amsmath'))
        self.doc.packages.append(Package('amssymb'))
        self.doc.packages.append(Package('geometry', options='margin=2cm'))
        self.doc.packages.append(Package('xcolor'))
        self.doc.packages.append(Package('pgfplots'))
        
        # Librerías TikZ
        self.doc.preamble.append(NoEscape(r'\usetikzlibrary{arrows.meta, calc, patterns, decorations.markings}'))
        self.doc.preamble.append(NoEscape(r'\pgfplotsset{compat=1.18}'))
        
        # Comandos personalizados
        self.doc.preamble.append(NoEscape(r'\newcommand{\vect}[1]{\mathbf{#1}}'))
        
        # Título
        self.doc.preamble.append(Command('title', self.title))
        self.doc.preamble.append(Command('author', 'Sistema VectorSpace3D'))
        self.doc.preamble.append(Command('date', NoEscape(r'\today')))
        self.doc.append(NoEscape(r'\maketitle'))
        self.doc.append(NoEscape(r'\tableofcontents'))
        self.doc.append(NoEscape(r'\newpage'))
    
    def add_vector_2d(self, vectors, labels=None, title="Vectores en 2D", 
                      colors=None, show_grid=True):
        """
        Añade visualización de vectores en 2D
        
        Args:
            vectors: Lista de tuplas (x, y)
            labels: Lista de etiquetas para cada vector
            title: Título de la sección
            colors: Lista de colores para cada vector
        """
        with self.doc.create(Section(title)):
            # Descripción matemática
            self.doc.append("Visualización de vectores en el espacio ")
            self.doc.append(Math(data=[r'\mathbb{R}^2']))
            self.doc.append(":\n\n")
            
            # Listar vectores
            if labels is None:
                labels = [f'v_{i+1}' for i in range(len(vectors))]
            if colors is None:
                colors = ['blue', 'red', 'green', 'orange', 'purple']
            
            for i, (vec, label) in enumerate(zip(vectors, labels)):
                self.doc.append(Math(data=[f'\\vect{{{label}}} = ({vec[0]}, {vec[1]})']))
                self.doc.append('\n\n')
            
            # Crear figura TikZ
            tikz_code = self._generate_2d_plot(vectors, labels, colors, show_grid)
            self.doc.append(NoEscape(tikz_code))
    
    def _generate_2d_plot(self, vectors, labels, colors, show_grid):
        """Genera código TikZ para gráfico 2D"""
        # Calcular límites del gráfico
        max_val = max(max(abs(v[0]), abs(v[1])) for v in vectors) * 1.2
        
        code = r"\begin{center}" + "\n"
        code += r"\begin{tikzpicture}[scale=1.5]" + "\n"
        
        # Ejes
        code += f"    \\draw[->] ({-max_val},0) -- ({max_val},0) node[right] {{$x$}};\n"
        code += f"    \\draw[->] (0,{-max_val}) -- (0,{max_val}) node[above] {{$y$}};\n"
        
        # Grid opcional
        if show_grid:
            code += f"    \\draw[gray!30, very thin] ({-max_val},{-max_val}) grid ({max_val},{max_val});\n"
        
        # Dibujar vectores
        for i, (vec, label, color) in enumerate(zip(vectors, labels, colors)):
            code += f"    \\draw[->, thick, {color}!80] (0,0) -- ({vec[0]},{vec[1]}) "
            code += f"node[midway, above left] {{$\\vect{{{label}}}$}};\n"
            code += f"    \\fill[{color}] ({vec[0]},{vec[1]}) circle (2pt);\n"
        
        code += r"\end{tikzpicture}" + "\n"
        code += r"\end{center}" + "\n"
        
        return code
    
    def add_vector_3d(self, vectors, labels=None, title="Vectores en 3D",
                      colors=None, view_angle=(70, 120)):
        """
        Añade visualización de vectores en 3D usando tikz-3dplot
        
        Args:
            vectors: Lista de tuplas (x, y, z)
            labels: Lista de etiquetas
            colors: Lista de colores
            view_angle: (theta, phi) ángulos de visualización
        """
        with self.doc.create(Section(title)):
            self.doc.append("Visualización de vectores en el espacio ")
            self.doc.append(Math(data=[r'\mathbb{R}^3']))
            self.doc.append(":\n\n")
            
            if labels is None:
                labels = [f'v_{i+1}' for i in range(len(vectors))]
            if colors is None:
                colors = ['blue', 'red', 'green', 'orange', 'purple']
            
            # Listar vectores
            for i, (vec, label) in enumerate(zip(vectors, labels)):
                self.doc.append(Math(data=[f'\\vect{{{label}}} = ({vec[0]}, {vec[1]}, {vec[2]})']))
                self.doc.append('\n\n')
            
            # Generar gráfico 3D
            tikz_code = self._generate_3d_plot(vectors, labels, colors, view_angle)
            self.doc.append(NoEscape(tikz_code))
    
    def _generate_3d_plot(self, vectors, labels, colors, view_angle):
        """Genera código tikz-3dplot para gráfico 3D"""
        max_val = max(max(abs(v[0]), abs(v[1]), abs(v[2])) for v in vectors) * 1.3
        theta, phi = view_angle
        
        code = r"\begin{center}" + "\n"
        code += f"\\tdplotsetmaincoords{{{theta}}}{{{phi}}}\n"
        code += r"\begin{tikzpicture}[tdplot_main_coords, scale=1.2]" + "\n"
        
        # Ejes coordenados
        code += f"    \\draw[->] (0,0,0) -- ({max_val},0,0) node[right] {{$x$}};\n"
        code += f"    \\draw[->] (0,0,0) -- (0,{max_val},0) node[above] {{$y$}};\n"
        code += f"    \\draw[->] (0,0,0) -- (0,0,{max_val}) node[above] {{$z$}};\n"
        
        # Planos de referencia (opcional)
        code += f"    \\draw[gray!20, fill=gray!5] (0,0,0) -- ({max_val*0.8},0,0) -- "
        code += f"({max_val*0.8},{max_val*0.8},0) -- (0,{max_val*0.8},0) -- cycle;\n"
        
        # Dibujar vectores
        for vec, label, color in zip(vectors, labels, colors):
            code += f"    \\draw[->, ultra thick, {color}] (0,0,0) -- ({vec[0]},{vec[1]},{vec[2]}) "
            code += f"node[above right] {{$\\vect{{{label}}}$}};\n"
            code += f"    \\fill[{color}] ({vec[0]},{vec[1]},{vec[2]}) circle (2pt);\n"
            
            # Líneas proyección (ayuda visual)
            code += f"    \\draw[dashed, {color}!40] ({vec[0]},{vec[1]},{vec[2]}) -- ({vec[0]},{vec[1]},0);\n"
        
        code += r"\end{tikzpicture}" + "\n"
        code += r"\end{center}" + "\n"
        
        return code
    
    def add_vector_operations(self, v1, v2, label1='u', label2='v'):
        """Añade sección con operaciones vectoriales"""
        with self.doc.create(Section("Operaciones Vectoriales")):
            
            # Suma de vectores
            with self.doc.create(Subsection("Suma de Vectores")):
                v_sum = tuple(a + b for a, b in zip(v1, v2))
                self.doc.append(Math(data=[f'\\vect{{{label1}}} + \\vect{{{label2}}} = {v_sum}']))
                self.doc.append('\n\n')
                
                if len(v1) == 2:
                    vectors = [v1, v2, v_sum]
                    labels = [label1, label2, f'{label1}+{label2}']
                    colors = ['blue', 'red', 'green']
                    tikz_code = self._generate_2d_plot(vectors, labels, colors, True)
                    self.doc.append(NoEscape(tikz_code))
            
            # Producto escalar
            with self.doc.create(Subsection("Producto Escalar")):
                dot_product = sum(a * b for a, b in zip(v1, v2))
                self.doc.append(Math(data=[f'\\vect{{{label1}}} \\cdot \\vect{{{label2}}} = {dot_product:.4f}']))
                self.doc.append('\n\n')
                
                # Ángulo entre vectores
                norm1 = np.sqrt(sum(x**2 for x in v1))
                norm2 = np.sqrt(sum(x**2 for x in v2))
                cos_angle = dot_product / (norm1 * norm2)
                angle = np.arccos(np.clip(cos_angle, -1, 1))
                
                self.doc.append(f"Ángulo entre vectores: ")
                self.doc.append(Math(data=[f'\\theta = {np.degrees(angle):.2f}^\\circ']))
                self.doc.append('\n\n')
            
            # Producto cruz (solo 3D)
            if len(v1) == 3 and len(v2) == 3:
                with self.doc.create(Subsection("Producto Cruz")):
                    cross = np.cross(v1, v2)
                    self.doc.append(Math(data=[f'\\vect{{{label1}}} \\times \\vect{{{label2}}} = ({cross[0]:.4f}, {cross[1]:.4f}, {cross[2]:.4f})']))
                    self.doc.append('\n\n')
                    self.doc.append("El producto cruz es perpendicular a ambos vectores.\n\n")
                    
                    # Visualización
                    vectors = [v1, v2, tuple(cross)]
                    labels_viz = [label1, label2, f'{label1}×{label2}']
                    colors = ['blue', 'red', 'purple']
                    tikz_code = self._generate_3d_plot(vectors, labels_viz, colors, (70, 120))
                    self.doc.append(NoEscape(tikz_code))
    
    def add_linear_transformation(self, matrix, vectors, title="Transformación Lineal"):
        """Visualiza transformación lineal"""
        with self.doc.create(Section(title)):
            self.doc.append("Matriz de transformación:\n\n")
            
            # Mostrar matriz
            mat_str = r'\begin{bmatrix} '
            for i, row in enumerate(matrix):
                mat_str += ' & '.join(str(x) for x in row)
                if i < len(matrix) - 1:
                    mat_str += r' \\ '
            mat_str += r' \end{bmatrix}'
            
            self.doc.append(Math(data=[f'A = {mat_str}']))
            self.doc.append('\n\n')
            
            # Transformar vectores
            transformed = [tuple(np.dot(matrix, v)) for v in vectors]
            
            if len(vectors[0]) == 2:
                # Gráfico comparativo 2D
                code = r"\begin{center}" + "\n"
                code += r"\begin{tikzpicture}[scale=1.5]" + "\n"
                
                # Vectores originales
                for i, v in enumerate(vectors):
                    color = ['blue', 'red'][i]
                    code += f"    \\draw[->, thick, {color}!60] (0,0) -- ({v[0]},{v[1]});\n"
                
                # Vectores transformados
                for i, v in enumerate(transformed):
                    color = ['blue', 'red'][i]
                    code += f"    \\draw[->, ultra thick, {color}] (0,0) -- ({v[0]},{v[1]});\n"
                
                code += r"\end{tikzpicture}" + "\n"
                code += r"\end{center}" + "\n"
                self.doc.append(NoEscape(code))
    
    def generate(self, filename='vectorspace3d_output', compile_pdf=True):
        """Genera el documento LaTeX"""
        self.doc.generate_tex(filename)
        if compile_pdf:
            try:
                self.doc.generate_pdf(filename, clean_tex=False)
                print(f"✓ Documento generado: {filename}.pdf")
            except Exception as e:
                print(f"⚠ PDF no generado (requiere LaTeX instalado): {e}")
                print(f"✓ Archivo .tex generado: {filename}.tex")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear sistema
    vs = VectorSpace3D("Análisis Avanzado de Vectores y Espacios Vectoriales")
    
    # Ejemplo 2D
    vectors_2d = [(3, 2), (-1, 4), (2, -3)]
    vs.add_vector_2d(vectors_2d, labels=['u', 'v', 'w'], 
                     title="Vectores en el Plano")
    
    # Ejemplo 3D
    vectors_3d = [(2, 3, 1), (1, -1, 2), (-2, 1, 3)]
    vs.add_vector_3d(vectors_3d, labels=['a', 'b', 'c'],
                     title="Vectores en el Espacio Tridimensional")
    
    # Operaciones
    vs.add_vector_operations((3, 4, 2), (1, -2, 5), 'p', 'q')
    
    # Transformación lineal
    matrix = [[2, -1], [1, 3]]
    vectors_transform = [(1, 0), (0, 1)]
    vs.add_linear_transformation(matrix, vectors_transform)
    
    # Generar documento
    vs.generate('mi_analisis_vectorial')
