import pandas as pd
import math
import matplotlib.pyplot as plt


vg = pd.read_csv('VideoGames.csv', sep=',')

def graf2():
    generos = ['ACTION', 'ADVENTURE', 'FIGHTING', 'MISC', 'PLATFORM', 'PUZZLE', 'RACING', 'ROLE-PLAYING', 'SHOOTER', 'SIMULATION', 'SPORTS', 'STRATEGY']

    rodar = True
    while rodar is True:
        valido1 = False
        valido2 = False

        # Usuário fornece gênero
        print('= Opcoes de Genero =\nAction, Sports, Misc, Role-Playing, Shooter,', '\nAdventure, Racing, Platform, Simulation, Fighting, Strategy, Puzzle')
        while valido1 is False:
            gen = input('\nDigite um genero: ')
            try:
                str(gen)
                if gen.upper() in generos:
                    valido1 = True
                else:
                    print('Oops... esse nao e um genero valido!')
                    valido1 = False
            except ValueError:
                print('Oops... esse nao e um genero valido!')

        while valido1 is True:
            # Listas com valores
            n_critica   = []
            n_players = []

            for i in range(len(vg)):
                li = vg.iloc[i]

                genero = str(li['Genre'])
                cscore = li['Critic_Score']
                pscore = li['User_Score']

                # Se gênero = genero_fornecido:
                if genero.upper() == gen.upper():
                    if not math.isnan(float(cscore)):
                        n_critica.append(cscore/10)  # Adiciona 'Critic Score' à lista critic
                    if not math.isnan(float(pscore)):
                        n_players.append(pscore)  # Adiciona 'User Score' à lista player

            # Plot histograma barras agrupadas
            # Eixo X: nota
            # Eixo Y: frequência
            plt.style.use('dark_background')
            plt.rcParams['figure.facecolor'] = '#222831'
            plt.rcParams['axes.facecolor'] = '#222831'
            plt.rcParams['text.color'] = '#ececec'
            plt.rcParams['xtick.color'] = '#ececec'
            plt.rcParams['ytick.color'] = '#ececec'
            plt.rcParams['axes.labelcolor'] = '#ececec'
            fig, a = plt.subplots()

            a.hist([n_players, n_critica], rwidth=0.85, color=['#30475e', '#f2a365'], label=['Players', 'Critica'])

            a.set_xlabel('Nota Recebida', color='#ececec')
            a.set_ylabel('Ocorrencias da Nota', color='#ececec')
            a.set_title(f'Notas da Critica e dos Jogadores para o genero {gen.capitalize()}', fontweight='bold')

            plt.grid(True, which='both', axis='y', alpha=0.5, linestyle=':', color='#ececec')
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.tight_layout()
            plt.show()
            valido1=False
            rodar=False
graf2()
