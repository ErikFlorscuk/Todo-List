import PySimpleGUI as sg

# Criando o Layout
def janela_ini():

    sg.theme('Dark')

    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('ToDo List',layout=layout,finalize=True)

# Criar a janela
janela = janela_ini()

# criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = janela_ini()

