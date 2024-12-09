from train import discretize_state
import numpy as np

def evaluar(env, q_table, n_bins, num_episodios=10):
    total_rewards = []
    for _ in range(num_episodios):
        state = env.reset()
        state = discretize_state(state, n_bins)
        done = False
        total_reward = 0

        while not done:
            action = np.argmax(q_table[state])
            next_state, reward, done, _ = env.step(action)
            state = discretize_state(next_state, n_bins)
            total_reward += reward
            env.render()

        total_rewards.append(total_reward)

    avg_reward = np.mean(total_rewards)
    print(f'Recompensa promedio tras {num_episodios} episodios: {avg_reward}')
