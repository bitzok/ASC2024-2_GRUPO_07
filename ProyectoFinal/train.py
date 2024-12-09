import numpy as np
import random

def initialize_q_table(n_bins, action_space_size):
    return np.random.uniform(low=-1, high=1, size=(n_bins, n_bins, n_bins, n_bins, action_space_size))


def discretize_state(state, n_bins):
    state_bounds = [
        (-4.8, 4.8),        # Posición del carro
        (-5.0, 5.0),        # Velocidad del carro
        (-0.418, 0.418),    # Ángulo del péndulo
        (-5.0, 5.0)         # Velocidad angular del péndulo
    ]
    ratios= [(state[i] + abs(state_bounds[i][0])) / (state_bounds[i][1] - state_bounds[i][0]) for i in range(len(state))]
    
    new_state = [int(round((n_bins - 1) * ratios[i])) for i in range(len(state))]
    new_state = [min(n_bins - 1, max(0, s)) for s in new_state]
    return tuple(new_state)

def epsilon_greedy(state, q_table, epsilon, action_space):
    if random.uniform(0, 1) < epsilon:
        return action_space.sample()  # Exploración
    return np.argmax(q_table[state])  # Explotación


def train(env, n_bins, num_episodes, alpha, gamma, epsilon, epsilon_decay, epsilon_min):
    q_table = initialize_q_table(n_bins, env.action_space.n)
    rewards = []
    max_steps = 200

    for episode in range(num_episodes):
        state = env.reset()
        state = discretize_state(state, n_bins)
        done = False
        total_reward = 0
        steps = 0

        while not done and steps < max_steps:
            action = epsilon_greedy(state, q_table, epsilon, env.action_space)
            next_state, reward, done, _ = env.step(action)
            next_state = discretize_state(next_state, n_bins)

            reward = 1.0 - abs(state[2]) * 1.5 - abs(state[0]) * 0.2
            if done:
                reward = -200
            else:
                reward = 1

            best_next_action = np.argmax(q_table[next_state])
            q_table[state][action] += alpha * (
                        reward + gamma * q_table[next_state][best_next_action] - q_table[state][action])

            state = next_state
            total_reward += reward
            #env.render()
            steps += 1

        rewards.append(total_reward)

        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

        if len(rewards) > 10:
            avg_reward = np.mean(rewards[-10:])
            print(f'Episodio {episode + 1}/{num_episodes} - Recompensa total: {total_reward} - Promedio (últimos 10): {avg_reward}')

    return q_table, rewards
