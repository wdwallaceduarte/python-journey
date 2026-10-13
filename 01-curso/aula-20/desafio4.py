# Triagem de Prontuários em Hospital): Desenvolva um script para a recepção de um pronto-socorro que armazene os nomes dos pacientes na fila de espera como chaves e o nível de prioridade do atendimento (ex: "Verde", "Amarelo", "Vermelho") como valores em um dicionário. O programa deve permitir que o enfermeiro digite o nome de um paciente para verificar a gravidade do caso. Se o paciente for localizado, o sistema deve exibir a cor de sua pulseira de triagem; se o nome não for encontrado, o programa deve informar que a ficha médica ainda não foi aberta e que o paciente precisa passar pela triagem inicial.

nivel_prioridade = {
    'wallace': 'verde', 
    'duarte': 'amarelo', 
    'paula': 'verde',
    'ana': 'vermelho' 
}
while True:
    nome_paciente = input('\nNome do paciente: ').lower()

    if nome_paciente in nivel_prioridade:
        prioridade = nivel_prioridade[nome_paciente]
        print(f'\nPaciente: {nome_paciente}')
        # print(f'Cor da pulseira: {prioridade}')
        if prioridade == 'verde':
            print(f'Cor da pulseira: \33[32m{prioridade}\33[0m')
        elif prioridade == 'amarelo':
            print(f'Cor da pulseira: \33[33m{prioridade}\33[0m')
        elif prioridade == 'vermelho':
            print(f'Cor da pulseira: \33[31m{prioridade}\33[0m')

    else:
        print('Paciente não encontrado.')
        print('Paciente precisa passar pela triagem.\n')
