#!/usr/bin/env python3
"""
VectorSpace3D - QUICK START
===========================

Ejemplo ejecutable mínimo para empezar rápidamente.
Genera un documento completo con visualizaciones 2D y 3D.

INSTALACIÓN:
    pip install numpy pylatex

USO:
    python quick_start.py

OUTPUT:
    - quick_start_demo.tex  (código LaTeX)
    - quick_start_demo.pdf  (documento compilado)
"""

import numpy as np
from pylatex import (Document, Section, Subsection, Package, 
                     NoEscape, Math, Command)
import sys
import os

def create_quick_demo():
    """Crea documento de demostración rápida"""
    
    print("=" * 70)
    print(" VectorSpace3D - Quick Start Demo".center(70))
    print("=" * 70)
    print()
    
    # Crear documento
    doc = Document(documentclass='article')
    
    # Paquetes
    print("📦 Configurando paquetes LaTeX...")
    for pkg in ['tikz', 'tikz-3dplot', 'amsmath', 
                ('geometry', 'margin=2cm'), 'xcolor']:
        if isinstance(pkg, tuple):
            doc.packages.append(Package(pkg[0], options=pkg[1]))
        else:
            doc.packages.append(Package(pkg))
    
    # Librerías
    doc.preamble.append(NoEscape(
        r'\usetikzlibrary{arrows.meta, calc}'
    ))
    doc.preamble.append(NoEscape(
        r'\newcommand{\vect}[1]{\mathbf{#1}}'
    ))
    
    # Título
    doc.preamble.append(Command('title', 
        'VectorSpace3D - Demostración Rápida'))
    doc.preamble.append(Command('author', 'Quick Start'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    
    doc.append(NoEscape(r'\maketitle'))
    
    print("✓ Documento inicializado")
    
    # SECCIÓN 1: Vectores 2D
    print("📐 Generando vectores 2D...")
    with doc.create(Section('Vectores en 2D')):
        doc.append("Tres vectores en el plano:\n\n")
        
        vectors = [(3, 2), (-1, 4), (2, -1)]
        labels = ['u', 'v', 'w']
        colors = ['blue', 'red', 'green']
        
        # Mostrar vectores
        for vec, label in zip(vectors, labels):
            doc.append(Math(data=[f'\\vect{{{label}}} = {vec}']))
            doc.append('\n\n')
        
        # Gráfico
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\begin{tikzpicture}[scale=1.5]'))
        doc.append(NoEscape(r'    \draw[->] (-4,0) -- (4,0) node[right] {$x$};'))
        doc.append(NoEscape(r'    \draw[->] (0,-2) -- (0,5) node[above] {$y$};'))
        doc.append(NoEscape(r'    \draw[gray!20] (-4,-2) grid (4,5);'))
        
        for vec, label, color in zip(vectors, labels, colors):
            doc.append(NoEscape(
                f'    \\draw[-{{Stealth[length=3mm]}}, ultra thick, {color}] '
                f'(0,0) -- ({vec[0]},{vec[1]}) '
                f'node[midway, above] {{$\\vect{{{label}}}$}};'
            ))
            doc.append(NoEscape(
                f'    \\fill[{color}] ({vec[0]},{vec[1]}) circle (2pt);'
            ))
        
        doc.append(NoEscape(r'\end{tikzpicture}'))
        doc.append(NoEscape(r'\end{center}'))
    
    print("✓ Sección 2D completada")
    
    # SECCIÓN 2: Vectores 3D
    print("🎲 Generando vectores 3D...")
    with doc.create(Section('Vectores en 3D')):
        doc.append("Tres vectores en el espacio:\n\n")
        
        vectors_3d = [(2, 3, 1), (1, -1, 2), (-1, 2, 2)]
        labels_3d = ['a', 'b', 'c']
        colors_3d = ['blue', 'red', 'green']
        
        # Mostrar vectores
        for vec, label in zip(vectors_3d, labels_3d):
            doc.append(Math(data=[f'\\vect{{{label}}} = {vec}']))
            norm = np.sqrt(sum(x**2 for x in vec))
            doc.append(f", ")
            doc.append(Math(data=[f'\\|\\vect{{{label}}}\\| = {norm:.3f}']))
            doc.append('\n\n')
        
        # Gráfico 3D
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\tdplotsetmaincoords{70}{120}'))
        doc.append(NoEscape(
            r'\begin{tikzpicture}[tdplot_main_coords, scale=1.2]'
        ))
        
        # Ejes
        doc.append(NoEscape(
            r'    \draw[->] (0,0,0) -- (4,0,0) node[right] {$x$};'
        ))
        doc.append(NoEscape(
            r'    \draw[->] (0,0,0) -- (0,4,0) node[above] {$y$};'
        ))
        doc.append(NoEscape(
            r'    \draw[->] (0,0,0) -- (0,0,4) node[above] {$z$};'
        ))
        
        # Plano de referencia
        doc.append(NoEscape(
            r'    \draw[gray!10, fill=gray!5] '
            r'(0,0,0) -- (3,0,0) -- (3,3,0) -- (0,3,0) -- cycle;'
        ))
        
        # Vectores
        for vec, label, color in zip(vectors_3d, labels_3d, colors_3d):
            doc.append(NoEscape(
                f'    \\draw[-{{Stealth[length=3mm]}}, ultra thick, {color}] '
                f'(0,0,0) -- ({vec[0]},{vec[1]},{vec[2]}) '
                f'node[above right] {{$\\vect{{{label}}}$}};'
            ))
            doc.append(NoEscape(
                f'    \\fill[{color}] ({vec[0]},{vec[1]},{vec[2]}) '
                f'circle (2pt);'
            ))
            # Proyección
            doc.append(NoEscape(
                f'    \\draw[{color}!40, dashed] '
                f'({vec[0]},{vec[1]},{vec[2]}) -- ({vec[0]},{vec[1]},0);'
            ))
        
        doc.append(NoEscape(r'\end{tikzpicture}'))
        doc.append(NoEscape(r'\end{center}'))
    
    print("✓ Sección 3D completada")
    
    # SECCIÓN 3: Operaciones
    print("➕ Generando operaciones...")
    with doc.create(Section('Operaciones Vectoriales')):
        v1 = (2, 3, 1)
        v2 = (1, -1, 2)
        
        with doc.create(Subsection('Suma')):
            v_sum = tuple(a + b for a, b in zip(v1, v2))
            doc.append(Math(data=[
                f'\\vect{{a}} + \\vect{{b}} = {v1} + {v2} = {v_sum}'
            ]))
            doc.append('\n\n')
        
        with doc.create(Subsection('Producto Escalar')):
            dot = sum(a * b for a, b in zip(v1, v2))
            doc.append(Math(data=[f'\\vect{{a}} \\cdot \\vect{{b}} = {dot}']))
            doc.append('\n\n')
            
            # Ángulo
            norm1 = np.sqrt(sum(x**2 for x in v1))
            norm2 = np.sqrt(sum(x**2 for x in v2))
            cos_angle = dot / (norm1 * norm2)
            angle = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))
            
            doc.append("Ángulo: ")
            doc.append(Math(data=[f'\\theta = {angle:.2f}^\\circ']))
            doc.append('\n\n')
        
        with doc.create(Subsection('Producto Cruz')):
            cross = np.cross(v1, v2)
            doc.append(Math(data=[
                f'\\vect{{a}} \\times \\vect{{b}} = '
                f'({cross[0]:.0f}, {cross[1]:.0f}, {cross[2]:.0f})'
            ]))
            doc.append('\n\n')
            doc.append("(Perpendicular a ambos vectores)\n\n")
    
    print("✓ Operaciones completadas")
    
    # Conclusión
    with doc.create(Section('Conclusión')):
        doc.append(
            "Este ejemplo demuestra las capacidades básicas de "
            "VectorSpace3D para visualización de vectores en 2D y 3D "
            "con TikZ y tikz-3dplot.\n\n"
        )
        doc.append(
            "Para funcionalidades avanzadas (bases, Gram-Schmidt, "
            "eigenvalores), consulta la documentación completa."
        )
    
    # Generar archivo
    filename = 'quick_start_demo'
    print()
    print("💾 Generando archivos...")
    
    try:
        doc.generate_tex(filename)
        print(f"✓ Archivo LaTeX generado: {filename}.tex")
        
        # Intentar compilar PDF
        try:
            doc.generate_pdf(filename, clean_tex=False)
            print(f"✓ PDF generado: {filename}.pdf")
            print()
            print("🎉 ¡Éxito total! Abre el PDF para ver el resultado.")
        except Exception as e:
            print(f"⚠ PDF no generado (compila manualmente):")
            print(f"   pdflatex {filename}.tex")
            print()
            print(f"Detalle del error: {e}")
        
        print()
        print("=" * 70)
        print(" Demo completada exitosamente".center(70))
        print("=" * 70)
        
        return True
        
    except Exception as e:
        print(f"❌ Error al generar archivos: {e}")
        return False


def print_usage():
    """Imprime instrucciones de uso"""
    print(__doc__)
    print("\nEJEMPLOS DE USO:")
    print("-" * 50)
    print("1. Ejecutar demo básico:")
    print("   python quick_start.py")
    print()
    print("2. Ver el resultado:")
    print("   open quick_start_demo.pdf  # macOS")
    print("   xdg-open quick_start_demo.pdf  # Linux")
    print("   start quick_start_demo.pdf  # Windows")
    print()
    print("3. Compilar manualmente si falla:")
    print("   pdflatex quick_start_demo.tex")
    print("   pdflatex quick_start_demo.tex  # 2 veces para refs")
    print("-" * 50)


if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)
    
    # Verificar dependencias
    try:
        import numpy
        from pylatex import Document
        print("✓ Dependencias encontradas")
    except ImportError as e:
        print(f"❌ Error: Falta instalar dependencias")
        print(f"   Ejecuta: pip install numpy pylatex")
        sys.exit(1)
    
    # Ejecutar demo
    success = create_quick_demo()
    
    sys.exit(0 if success else 1)
