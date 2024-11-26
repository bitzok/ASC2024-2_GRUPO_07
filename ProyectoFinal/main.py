import gym

env = gym.make('CartPole-v1')  # Eliminar el parámetro render_mode

state = env.reset()

num_steps = 1000

for step in range(num_steps):
    env.render()  # Mostrar el entorno gráficamente

    # Elige una acción aleatoria: 0 = mover a la izquierda, 1 = mover a la derecha
    action = env.action_space.sample()  # Acción aleatoria

    # Hacer un paso en el entorno con la acción seleccionada
    next_state, reward, done, info = env.step(action)

    # Si el episodio ha terminado (el péndulo cae o el máximo de pasos es alcanzado), reiniciar el entorno
    if done:
        print(f'Episodio terminado en el paso {step+1}')
        state = env.reset()  # Resetear el entorno para iniciar un nuevo episodio

env.close()