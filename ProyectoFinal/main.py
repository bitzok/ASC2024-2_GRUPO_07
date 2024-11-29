import gym
import matplotlib.pyplot as plt
from train import train
from evaluar import evaluar

def main():
    # Configuración de parámetros
    env = gym.make('CartPole-v1')
    n_bins = 10
    alpha = 0.1
    gamma = 0.99
    epsilon = 1.0
    epsilon_decay = 0.995
    epsilon_min = 0.1
    num_episodes = 200

    # Entrenar el agente
    print("Iniciando el entrenamiento...")
    q_table , rewards = train(env, n_bins, num_episodes, alpha, gamma, epsilon, epsilon_decay, epsilon_min)

    # Visualizar recompensas
    plt.plot(rewards)
    plt.xlabel('Episodios')
    plt.ylabel('Recompensa acumulada')
    plt.title('Progreso del entrenamiento')
    plt.show()

    # Evaluar el agente
    print("\nIniciando la evaluación...")
    evaluar(env, q_table, n_bins)

    env.close()

if __name__ == "__main__":
    main()