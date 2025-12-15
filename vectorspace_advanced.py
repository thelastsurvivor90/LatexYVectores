"""
Módulo avanzado: Espacios vectoriales, bases, subespacios
"""

from vectorspace3d_main import VectorSpace3D
import numpy as np
from pylatex import Section, Subsection, Math, NoEscape

class AdvancedVectorSpace(VectorSpace3D):
    """Extensión con funcionalidades avanzadas"""
    
    def add_vector_space_basis(self, basis_vectors, title="Base del Espacio Vectorial"):
        """Analiza y visualiza una base de vectores"""
        with self.doc.create(Section(title)):
            dim = len(basis_vectors)
            n = len(basis_vectors[0])
            
            self.doc.append(f"Base del espacio vectorial ")
            self.doc.append(Math(data=[f'\\mathbb{{R}}^{n}']))
            self.doc.append(f" con dimensión {dim}:\n\n")
            
            # Mostrar vectores base
            for i, vec in enumerate(basis_vectors):
                vec_str = '(' + ', '.join(str(x) for x in vec) + ')'
                self.doc.append(Math(data=[f'\\vect{{e_{i+1}}} = {vec_str}']))
                self.doc.append('\n\n')
            
            # Verificar independencia lineal (determinante)
            if dim == n:
                det = np.linalg.det(basis_vectors)
                self.doc.append(f"Determinante de la matriz formada por los vectores: ")
                self.doc.append(Math(data=[f'\\det(A) = {det:.4f}']))
                self.doc.append('\n\n')
                
                if abs(det) > 1e-10:
                    self.doc.append("✓ Los vectores son linealmente independientes y forman una base.\n\n")
                else:
                    self.doc.append("✗ Los vectores son linealmente dependientes.\n\n")
            
            # Visualización
            if n == 2:
                self.add_vector_2d(basis_vectors, 
                                  labels=[f'e_{i+1}' for i in range(dim)],
                                  title="")
            elif n == 3:
                self.add_vector_3d(basis_vectors,
                                  labels=[f'e_{i+1}' for i in range(dim)],
                                  title="")
    
    def add_gram_schmidt(self, vectors, title="Proceso de Gram-Schmidt"):
        """Ortogonalización de Gram-Schmidt"""
        with self.doc.create(Section(title)):
            self.doc.append("Proceso de ortogonalización de Gram-Schmidt:\n\n")
            
            # Implementar Gram-Schmidt
            orthogonal = []
            for i, v in enumerate(vectors):
                v_array = np.array(v)
                # Restar proyecciones sobre vectores anteriores
                u = v_array.copy()
                for o in orthogonal:
                    o_array = np.array(o)
                    proj = (np.dot(v_array, o_array) / np.dot(o_array, o_array)) * o_array
                    u = u - proj
                
                # Normalizar
                u_norm = u / np.linalg.norm(u)
                orthogonal.append(tuple(u_norm))
                
                # Mostrar paso
                with self.doc.create(Subsection(f"Vector ortogonal {i+1}")):
                    vec_str = '(' + ', '.join(f'{x:.4f}' for x in u_norm) + ')'
                    self.doc.append(Math(data=[f'\\vect{{u_{i+1}}} = {vec_str}']))
                    self.doc.append('\n\n')
            
            # Visualizar conjunto ortogonal
            if len(vectors[0]) == 2:
                self.add_vector_2d(orthogonal,
                                  labels=[f'u_{i+1}' for i in range(len(orthogonal))],
                                  title="Base Ortonormal Resultante")
            elif len(vectors[0]) == 3:
                self.add_vector_3d(orthogonal,
                                  labels=[f'u_{i+1}' for i in range(len(orthogonal))],
                                  title="Base Ortonormal Resultante")
    
    def add_subspace_projection(self, vector, subspace_basis, 
                               title="Proyección sobre Subespacio"):
        """Proyecta un vector sobre un subespacio"""
        with self.doc.create(Section(title)):
            self.doc.append(f"Vector a proyectar: ")
            vec_str = '(' + ', '.join(str(x) for x in vector) + ')'
            self.doc.append(Math(data=[f'\\vect{{v}} = {vec_str}']))
            self.doc.append('\n\n')
            
            # Calcular proyección
            v = np.array(vector)
            projection = np.zeros_like(v)
            
            for basis_vec in subspace_basis:
                b = np.array(basis_vec)
                proj = (np.dot(v, b) / np.dot(b, b)) * b
                projection += proj
            
            proj_str = '(' + ', '.join(f'{x:.4f}' for x in projection) + ')'
            self.doc.append("Proyección sobre el subespacio:\n\n")
            self.doc.append(Math(data=[f'\\text{{proj}}_W(\\vect{{v}}) = {proj_str}']))
            self.doc.append('\n\n')
            
            # Componente ortogonal
            orthogonal_comp = v - projection
            orth_str = '(' + ', '.join(f'{x:.4f}' for x in orthogonal_comp) + ')'
            self.doc.append("Componente ortogonal:\n\n")
            self.doc.append(Math(data=[f'\\vect{{v}}^\\perp = {orth_str}']))
            self.doc.append('\n\n')
            
            # Visualización
            if len(vector) == 2:
                vectors = [vector, tuple(projection), tuple(orthogonal_comp)]
                labels = ['v', 'proj', 'v⊥']
                colors = ['blue', 'green', 'red']
                tikz_code = self._generate_2d_plot(vectors, labels, colors, True)
                self.doc.append(NoEscape(tikz_code))
            elif len(vector) == 3:
                vectors = [vector, tuple(projection), tuple(orthogonal_comp)]
                labels = ['v', 'proj', 'v⊥']
                colors = ['blue', 'green', 'red']
                tikz_code = self._generate_3d_plot(vectors, labels, colors, (70, 120))
                self.doc.append(NoEscape(tikz_code))
    
    def add_eigenanalysis(self, matrix, title="Análisis de Valores y Vectores Propios"):
        """Calcula y visualiza valores y vectores propios"""
        with self.doc.create(Section(title)):
            self.doc.append("Matriz a analizar:\n\n")
            
            # Mostrar matriz
            mat_str = r'\begin{bmatrix} '
            for i, row in enumerate(matrix):
                mat_str += ' & '.join(f'{x:.2f}' for x in row)
                if i < len(matrix) - 1:
                    mat_str += r' \\ '
            mat_str += r' \end{bmatrix}'
            self.doc.append(Math(data=[f'A = {mat_str}']))
            self.doc.append('\n\n')
            
            # Calcular eigenvalores y eigenvectores
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            
            with self.doc.create(Subsection("Valores Propios")):
                for i, eigenval in enumerate(eigenvalues):
                    if np.isreal(eigenval):
                        self.doc.append(Math(data=[f'\\lambda_{i+1} = {eigenval.real:.4f}']))
                    else:
                        self.doc.append(Math(data=[f'\\lambda_{i+1} = {eigenval.real:.4f} + {eigenval.imag:.4f}i']))
                    self.doc.append('\n\n')
            
            with self.doc.create(Subsection("Vectores Propios")):
                vectors_list = []
                for i, eigenvec in enumerate(eigenvectors.T):
                    if np.all(np.isreal(eigenvec)):
                        vec_str = '(' + ', '.join(f'{x.real:.4f}' for x in eigenvec) + ')'
                        self.doc.append(Math(data=[f'\\vect{{v_{i+1}}} = {vec_str}']))
                        self.doc.append('\n\n')
                        vectors_list.append(tuple(eigenvec.real))
                
                # Visualizar vectores propios
                if len(matrix) == 2 and len(vectors_list) == 2:
                    self.add_vector_2d(vectors_list,
                                      labels=[f'v_{i+1}' for i in range(len(vectors_list))],
                                      title="Visualización de Vectores Propios")
                elif len(matrix) == 3 and len(vectors_list) == 3:
                    self.add_vector_3d(vectors_list,
                                      labels=[f'v_{i+1}' for i in range(len(vectors_list))],
                                      title="Visualización de Vectores Propios")


# Ejemplo completo de uso
if __name__ == "__main__":
    # Crear sistema avanzado
    avs = AdvancedVectorSpace("Análisis Completo de Espacios Vectoriales")
    
    # 1. Análisis de base
    basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    avs.add_vector_space_basis(basis, "Base Canónica de R³")
    
    # 2. Base no ortogonal
    non_orthogonal = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    avs.add_vector_space_basis(non_orthogonal, "Base No Ortogonal")
    
    # 3. Gram-Schmidt
    vectors_gs = [[3, 1], [2, 2]]
    avs.add_gram_schmidt(vectors_gs, "Ortogonalización en R²")
    
    # 4. Proyección sobre subespacio
    vector_to_project = [5, 3, 1]
    subspace = [[1, 0, 0], [0, 1, 0]]
    avs.add_subspace_projection(vector_to_project, subspace,
                                "Proyección sobre el Plano XY")
    
    # 5. Análisis de eigenvalores
    matrix_2d = [[2, 1], [1, 2]]
    avs.add_eigenanalysis(matrix_2d, "Valores Propios de Matriz Simétrica")
    
    # 6. Ejemplos adicionales 3D
    vectors_3d = [(2, 3, 1), (1, -1, 2)]
    avs.add_vector_3d(vectors_3d, labels=['u', 'v'],
                     title="Vectores en R³")
    
    # Operaciones vectoriales
    avs.add_vector_operations((1, 2, 3), (4, -1, 2), 'a', 'b')
    
    # Transformación lineal 3D
    matrix_3d = [[1, 0, 0], [0, np.cos(np.pi/4), -np.sin(np.pi/4)], 
                 [0, np.sin(np.pi/4), np.cos(np.pi/4)]]
    vectors_transform = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    avs.add_linear_transformation(matrix_3d, vectors_transform,
                                  "Rotación en torno al eje X")
    
    # Generar documento
    avs.generate('analisis_completo_vectorial')
