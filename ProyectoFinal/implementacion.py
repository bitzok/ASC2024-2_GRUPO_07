import gym
import numpy as np
import random


env = gym.make('CartPole-v1')

#Ajuste de variables

env.length = 100  
env.force_mag = 1

# Parámetros necesarios para el algoritmo Q-learning
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.99  # Descuento
epsilon = 1.0  # Probabilidad de exploración (comienza alta)
epsilon_decay = 0.995  # Decaimiento de epsilon por episodio
epsilon_min = 0.1  # Valor mínimo de epsilon
num_episodes = 100  # Cantidad de episodios o steps

# Inicializar la tabla Q
n_bins = 10  # Número de bins (intervalos) para cada dimensión del estado
q_table = np.zeros((n_bins, n_bins, n_bins, n_bins, env.action_space.n))  # Tabla Q con 4 dimensiones de estado

def discretize_state(state):
    state_bins = [
        np.digitize(state[0], np.linspace(-2.4, 2.4, n_bins - 1)),  # Posición 
        np.digitize(state[1], np.linspace(-3.0, 3.0, n_bins - 1)),  # Velocidad 
        np.digitize(state[2], np.linspace(-0.5, 0.5, n_bins - 1)),  # Ángulo 
        np.digitize(state[3], np.linspace(-2.0, 2.0, n_bins - 1))   # Velocidad angular 
    ]
    return tuple(state_bins) 

def epsilon_greedy(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Exploración: elige una acción aleatoria
    else:
        return np.argmax(q_table[state])  # Explotación: elige la mejor acción según la tabla Q

# Entrenamiento del agente con Q-learning
for episode in range(num_episodes):
    state = env.reset()  
    state = discretize_state(state) 
    done = False
    total_reward = 0
    
    while not done:
        action = epsilon_greedy(state, epsilon)  # Elegir acción usando epsilon-greedy
        next_state, reward, done, info = env.step(action)  # Tomar un paso en el entorno
        next_state = discretize_state(next_state)  

        # Actualizar la tabla Q
        best_next_action = np.argmax(q_table[next_state])  # Mejor acción en el siguiente estado
        q_table[state][action] += alpha * (reward + gamma * q_table[next_state][best_next_action] - q_table[state][action]) 
        
        state = next_state  # Actualizar el estado actual
        total_reward += reward
        
        env.render() 

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # Imprimir el progreso del entrenamiento
    
    print(f'Episodio {episode}/{num_episodes} - Recompensa total: {total_reward}')
    print(env.length)


# Evaluación del agente
state = env.reset() 
state = discretize_state(state)  
done = False
total_reward = 0

# Realizar una evaluación del agente
while not done:
    action = np.argmax(q_table[state])  
    next_state, reward, done, info = env.step(action)
    state = discretize_state(state)  
    total_reward += reward


    env.render()  # Mostrar el gráfico del péndulo

print(f'Recompensa total en la evaluación: {total_reward}')

env.close()
