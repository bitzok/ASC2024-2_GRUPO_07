import gym
import matplotlib.pyplot as plt
from train import train
from evaluar import evaluar

def smooth_rewards(rewards, window=50):
    """Calcula el promedio móvil de las recompensas."""
    import numpy as np
    return np.convolve(rewards, np.ones(window)/window, mode='valid')

def main():
    # Configuración de parámetros
    env = gym.make('CartPole-v1')
    n_bins = 10
    alpha = 0.01
    gamma = 0.95
    epsilon = 1.0
    epsilon_decay = 0.995
    epsilon_min = 0.01
    num_episodes = 30000

    # Entrenar el agente
    print("Iniciando el entrenamiento...")
    q_table, rewards = train(env, n_bins, num_episodes, alpha, gamma, epsilon, epsilon_decay, epsilon_min)

    print("\nGenerando gráfica de recompensas...")
    smoothed_rewards = smooth_rewards(rewards, window=100)
    plt.plot(smoothed_rewards)
    plt.xlabel('Episodios')
    plt.ylabel('Recompensa acumulada (promedio móvil)')
    plt.title('Progreso del entrenamiento del agente')
    plt.show()

    # Evaluar el agente
    print("\nIniciando la evaluación...")
    evaluar(env, q_table, n_bins)

    env.close()

if __name__ == "__main__":
    main()