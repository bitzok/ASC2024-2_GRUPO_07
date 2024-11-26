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

📂 ProyectoFinal-PenduloInvertido
├── 📁 control_moderno
│ ├── PID_manual.ipynb # Diseño y simulación del controlador PID manual.
│ ├── PID_optimizacion_genetica.ipynb # Optimización del PID con algoritmos genéticos.
│ └── resultados_graficos # Gráficos comparativos entre PID manual y optimizado.
├── 📁 control_inteligente
│ ├── agente_qlearning.py # Implementación del agente basado en Q-learning.
│ ├── agente_sarsa.py # Implementación del agente basado en SARSA.
│ ├── configuraciones_cartpole # Parámetros y configuraciones del entorno.
│ └── resultados_graficos # Gráficos de recompensas y desempeño del agente.
├── README.md # Descripción del proyecto y pasos para ejecutarlo.
└── requerimientos.txt # Dependencias necesarias para ejecutar el código.

---
