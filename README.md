
# BGColorGenerator

BGColorGenerator es una biblioteca de Python que predice el color de fondo ideal basado en un color de texto dado, utilizando un modelo de red neuronal preentrenado. Es una herramienta perfecta para diseñadores, desarrolladores web y cualquiera que necesite generar combinaciones de colores visualmente atractivas y accesibles de manera automática.

## Instalación

Puedes instalar esta biblioteca directamente desde PyPI:

```bash
pip install bg_color_generator
```

## Uso

### Predicción del Color de Fondo

El paquete incluye una función clave `get_bg_color` que te permite predecir el color de fondo ideal dado un color de texto en formato RGBA. También puedes visualizar el contraste entre el color de texto y el color de fondo predicho.

```python
from utils.colorgenerator import get_bg_color

# Definir el color del texto en formato RGBA
text_color = [255, 255, 255, 1]  # Blanco opaco

# Obtener el color de fondo recomendado y visualizar el contraste
bg_color = get_bg_color(text_color)
print(f'Predicted background color: {bg_color}')
```

### Funciones Clave

- **`get_bg_color(rgba_array, turn_off_visualization=False)`**: Predice el color de fondo ideal basado en un color de texto dado en formato RGBA. Opcionalmente, permite desactivar la visualización del contraste entre el color de texto y el color de fondo predicho. Devuelve un array de forma `[R, G, B, A]` representando el color de fondo recomendado.

- **`plot_contrast(color1, color2)`**: Visualiza el contraste entre dos colores en formato RGBA. Útil para evaluar visualmente cómo se verá el texto sobre el fondo.

## Requisitos

Este paquete requiere las siguientes bibliotecas de Python:

- `tensorflow>=2.0.0`
- `matplotlib`
- `pandas`

Estas dependencias se instalarán automáticamente cuando uses `pip` para instalar `bg_color_generator`.

## Ejemplos

### Predicción y Visualización

Aquí hay un ejemplo completo de cómo predecir un color de fondo y visualizarlo junto al color de texto:

```python
from utils.colorgenerator import get_bg_color
from utils.visualization import plot_contrast

# Color del texto en RGBA (Rojo, Verde, Azul, Alpha)
text_color = [255, 255, 255, 1]  # Blanco opaco

# Predicción del color de fondo y visualización del contraste
bg_color = get_bg_color(text_color)

# Mostrar los colores
print(f'Text color: {text_color}')
print(f'Predicted background color: {bg_color}')
```

### Contribuyendo

Si te gustaría contribuir a este proyecto, siéntete libre de hacer un fork del repositorio, crear una rama (`git checkout -b feature/nueva-feature`), hacer tus cambios y enviar un pull request. Apreciamos cualquier contribución que pueda mejorar el proyecto.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo [LICENSE](LICENSE).

---

**BGColorGenerator** - Facilita la elección de colores de fondo, mejorando la estética y accesibilidad de tus proyectos.
