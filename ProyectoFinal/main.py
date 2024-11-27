import gym
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
    num_episodes = 100

    # Entrenar el agente
    print("Iniciando el entrenamiento...")
    q_table = train(env, n_bins, num_episodes, alpha, gamma, epsilon, epsilon_decay, epsilon_min)

    # Evaluar el agente
    print("\nIniciando la evaluación...")
    evaluar(env, q_table, n_bins)

    env.close()

if __name__ == "__main__":
    main()