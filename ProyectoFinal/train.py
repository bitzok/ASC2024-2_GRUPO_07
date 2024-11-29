import numpy as np
import random


def initialize_q_table(n_bins, action_space_size):
    return np.zeros((n_bins, n_bins, n_bins, n_bins, action_space_size))


def discretize_state(state, n_bins):
    state_bins = [
        np.digitize(state[0], np.linspace(-2.4, 2.4, n_bins - 1)),  # Posición
        np.digitize(state[1], np.linspace(-3.0, 3.0, n_bins - 1)),  # Velocidad
        np.digitize(state[2], np.linspace(-0.5, 0.5, n_bins - 1)),  # Ángulo
        np.digitize(state[3], np.linspace(-2.0, 2.0, n_bins - 1))  # Velocidad angular
    ]
    return tuple(state_bins)


def epsilon_greedy(state, q_table, epsilon, action_space):
    if random.uniform(0, 1) < epsilon:
        return action_space.sample()  # Exploración: elige una acción aleatoria
    return np.argmax(q_table[state])  # Explotación: elige la mejor acción según la tabla Q


def train(env, n_bins, num_episodes, alpha, gamma, epsilon, epsilon_decay, epsilon_min):
    q_table = initialize_q_table(n_bins, env.action_space.n)
    rewards=[]

    for episode in range(num_episodes):
        state = env.reset()
        state = discretize_state(state, n_bins)
        done = False
        total_reward = 0

        while not done:
            action = epsilon_greedy(state, q_table, epsilon, env.action_space)
            next_state, reward, done, _ = env.step(action)
            next_state = discretize_state(next_state, n_bins)

            # Modificar recompensa
            #reward += 1.0 - (abs(state[2]) * 2.0) - (abs(state[0]) * 0.5)

            # Actualizar la tabla Q
            best_next_action = np.argmax(q_table[next_state])
            q_table[state][action] += alpha * (
                        reward + gamma * q_table[next_state][best_next_action] - q_table[state][action])

            state = next_state
            total_reward += reward

            env.render()

        # Guardar la recompensa total de este episodio
        rewards.append(total_reward)

        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

        print(f'Episodio {episode + 1}/{num_episodes} - Recompensa total: {total_reward}')

    return q_table, rewards