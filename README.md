# Proyecto Final - Péndulo Invertido  

**Grupo 7**  
**Integrantes:**  
- Ames Camayo, Daniel Vides
- Cjumo Chumbes, Jose Carlos
- Ortiz Quispe, Akcel Eduardo
- Ramirez Alvarado, Piero Jaime
- Santa Cruz Pachas Edward Grover

---

## Descripción del Proyecto  
Este proyecto aborda el control del péndulo invertido, un sistema dinámico no lineal que representa un desafío clásico en la ingeniería de control. Se desarrollan e implementan dos enfoques principales:  
1. **Control moderno:** Diseño y simulación de un controlador PID, incluyendo su optimización con algoritmos genéticos.  
2. **Control inteligente:** Implementación de un agente basado en aprendizaje por refuerzo clásico (*Q-learning* o *SARSA*) para estabilizar el péndulo en el entorno simulado *CartPole-v1* de Gym.  

El objetivo es analizar y comparar ambos enfoques, destacando sus ventajas, limitaciones y aplicaciones prácticas.

---

## Estructura del Repositorio  
El repositorio está organizado de la siguiente manera:  

```plaintext
ASC2024-2_GRUPO_07/
├───Artículos
├───ProyectoFinal        # código del proyecto
│   ├── evaluar.py
│   ├── main.py          # código para ejecutar el proyecto
│   └── train.py
│   .gitignore
│   README.md
│   requirements.txt
│   setup.bat            # script instalación Windows
└───setup.sh             # script instalación Unix

```

---

## Instalación

### Opción 1: Instalación Manual

Pasos para configurar el entorno manualmente.

1. **Crear un entorno virtual**:
   - En terminal, crear un entorno virtual ejecutando:

     ```bash
     python -m venv venv
     ```

2. **Activar el entorno virtual**:
   - **En Unix**:

     ```bash
     source venv/bin/activate
     ```

   - **En Windows**:

     ```batch
     .\venv\Scripts\activate
     ```

3. **Instalar las dependencias**:
   Luego de activar el entorno, instalar las dependencias desde `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Opción 2: Instalación Automática con Scripts

Para instalación automática, se puede usar los scripts para simplificar la configuración del entorno.

1. **Ejecutar el script en Unix**:
   - Dar permisos de ejecución al script `setup.sh`:

     ```bash
     chmod +x setup.sh  # por única vez
     ```

   - Luego, ejecuta el script:

     ```bash
     ./setup.sh
     ```

2. **Ejecutar el script en Windows**:
   - En la terminal de Windows, ejecuta el script `setup.bat`:

     ```batch
     setup.bat
     ```

Ambos scripts actualizarán `pip` y `setuptools` a las versiones correctas, instalarán las dependencias desde `requirements.txt`, y configurarán el entorno virtual automáticamente.

---

