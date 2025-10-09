import time
import getpass
import os
import csv




# Dicionário de usuários
usuarios = {
    "admin": {"senha": "12345"},
    "funcionario": {"senha": "12345"},
    "cliente": {"senha": "12345"},
    "sócio": {"senha": "12345"}
}


# Login do usuario
tentativas = 3
acesso_liberado = False


print("="*30)
print("            LOGIN     ")
print("="*30 + "\n")


while tentativas > 0:
    login = input('Digite seu login: ').lower().strip()
    senha = getpass.getpass('Digite sua senha: ').strip()
    os.system("cls" if os.name == "nt" else "clear")


    if login in usuarios and usuarios[login]["senha"] == senha:
        time.sleep(0.5)
        print("\nVerificando...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print('\nLogin efetuado com sucesso!!!\n\n')
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        acesso_liberado = True


        # Informações necessárias
        time.sleep(1)
        print('Algumas informações são necessárias para continuar.')


        while True:
            time.sleep(0.7)
            responsavel = input('\nDigite o nome do responsável pelo laboratório: ').strip()
            time.sleep(0.5)


            if responsavel.replace(' ', '').isalpha():
                break
            else:
                print('\nDIGITE APENAS LETRAS.\n\nTente novamente.')


        # Máquinas disponíveis e escolhidas
        numero_de_maquinas = 65
        time.sleep(0.5)
        print(f'\n     {numero_de_maquinas} máquinas estão disponíveis.')


        while True:
            try:
                time.sleep(0.3)
                maquinas_escolhidas = int(input('\nNúmero de máquinas que serão utilizadas: '))


                if maquinas_escolhidas > numero_de_maquinas or maquinas_escolhidas < 1:
                    print(f'\n{numero_de_maquinas} MÁQUINAS ESTÃO DISPONÍVEIS!')
                else:
                    time.sleep(0.5)
                    print(f'\nForam escolhidas {maquinas_escolhidas} máquinas.\n')
                    break
            except ValueError:
                print('\nDIGITE APENAS NÚMEROS!')


        # Captura a data e hora
        data = time.strftime("%d/%m/%y")
        horario = time.strftime("%H:%M")


        # Cadastro dos alunos
        time.sleep(0.5)
        print('Para continuar é necessário cadastrar cada Aluno em uma máquina.\n')


        reservas = []
        maquinas_ocupadas = set()
        num_aluno_ocupado = set()


        for i in range(maquinas_escolhidas):
            print(f"\nCadastro do {i+1}º aluno:")


            # Nome do aluno
            while True:
                nome = input('Nome do aluno: ').lower().strip()
                if nome.replace(' ', '').isalpha():
                    break
                else:
                    time.sleep(0.5)
                    print("\nNome inválido!\n\nDigite apenas letras.\n")


            # Número do aluno
            while True:
                try:
                    num_aluno = int(input('N° do aluno: '))
                    if num_aluno in num_aluno_ocupado:
                        print("\nNúmero de chamada já escolhido!\n\nTente outro número.\n")
                    elif num_aluno > 0:
                        num_aluno_ocupado.add(num_aluno)
                        break
                    else:
                        time.sleep(0.5)
                        print("\nO número digitado deve ser maior que 0!\n")
                except ValueError:
                    time.sleep(0.5)
                    print("\nDigite apenas números inteiros!\n")


            # Número da máquina
            while True:
                try:
                    num_maquina = int(input('N° da máquina: '))
                    if num_maquina in maquinas_ocupadas:
                        time.sleep(0.5)
                        print("\nEssa máquina já foi ocupada!\n\nTente escolher outra.\n")
                    elif num_maquina < 1 or num_maquina > numero_de_maquinas:
                        time.sleep(0.5)
                        print(f"\nO número digitado deve estar entre 1 e {numero_de_maquinas}!\n\nTente outra.\n")
                    else:
                        maquinas_ocupadas.add(num_maquina)
                        break
                except ValueError:
                    time.sleep(0.5)
                    print("\nDigite apenas números inteiros!\n")


            reservas.append((nome, num_aluno, num_maquina))


        # Dados da reserva das máquinas
        time.sleep(0.3)
        print("\nPreenchendo dados da reserva...")
        time.sleep(0.7)
        os.system("cls" if os.name == "nt" else "clear")


        time.sleep(1)
        print("\n\n" + "="*90)
        print('                                    DADOS DA RESERVA')
        print("="*90)
        print(f"{'Nome do aluno':<30} | {'N° do aluno':<15} | {'N° da maquina':<15}")
        print("-" * 90)


        for aluno in reservas:
            print(f"{aluno[0]:<30} | {aluno[1]:<15} | {aluno[2]:<15}")
            print("-" * 90)


        print("="*90)
        print(f"Responsável: {responsavel}")
        print(f"Máquinas escolhidas: {maquinas_escolhidas}")
        print(f"Data da reserva: {data}")
        print(f"Horário da reserva: {horario}")
        print("="*90)


        #Salvando dados em .csv no exel


        # Ajustando nome do arquivo com data e hora
        nome_arquivo = f"reserva_{data.replace('/', '-')}_{horario.replace(':', '-')}.csv"


        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')  # Usando ; para Excel PT-BR
            escritor.writerow(['Nome do Aluno', 'Número do Aluno', 'Número da Máquina', 'Responsável', 'Data', 'Horário'])
            for aluno in reservas:
                escritor.writerow([aluno[0], aluno[1], aluno[2], responsavel, data, horario])


        time.sleep(1)    
        print("Salvando dados...", end='\r')
        time.sleep(1)
        print(" " *35, end='\r')


        print(f"\nOs dados foram salvos no arquivo: {nome_arquivo}")
        break


    else:
        time.sleep(0.5)
        print("\nVerificando...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print('\nSenha ou Login Inválidos!\n')
        tentativas -= 1


    if tentativas == 0:
        print('\nVocê tentou muitas vezes')
        break
