import PySimpleGUI as sg

def make_win1():
    layout = [[sg.Text('Bem vindo ao sistema Pilot School'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Button('Cadastrar aluno'),
              sg.Button('Cadastrar instrutor'),
              sg.Button('Cadastrar curso'),
              sg.Button('Sair')]]
    return sg.Window('Window Title', layout, location=(800,600), finalize=True)



def make_win2():
    layout = [

    [
        sg.Text("Nome:", size=(8, 1)),
        sg.InputText(size=(70, 1), key="-NOME-", focus=True)
    ],
    [
        sg.Text("E-mail:", size=(8, 1)),
        sg.InputText(size=(40, 1), key="-EMAIL-")
    ],
    [
        sg.Text("CPF:", size=(8, 1)),
        sg.InputText(size=(40, 1), key="-CPF-")
    ],
    [
        sg.Text("Gênero:", size=(8, 1)),
        sg.Radio('Masculino', 'GRUPO1', default=False, key="-GENERO-M-"),
        sg.Radio('Feminino', 'GRUPO1', default=True, key="-GENERO-F-")
    ],
    [
        sg.Text("Logradouro:", size=(8, 1)),
        sg.InputText(size=(70, 1), key="-LOGRADOURO-")
    ],
    [
        sg.Text("Celular:", size=(8, 1)),
        sg.InputText(size=(70, 1), key="-CEL-")
    ],
    [
        sg.Button('Limpar', size=(8, 1), key="-LIMPAR-"),
        sg.Button('Inserir', size=(8, 1), key="-INSERIR-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR-"),
        sg.Button('Remover', size=(8, 1), key="-REMOVER-")
    ],
    [
        sg.Button('<<', size=(8, 1), key="-<<-"),
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS-"),
        sg.Button('>>', size=(8, 1), key="->>-")
    ],
    [
      sg.Button('Sair')
    ]
              
              
              
  ]
    return sg.Window('Cadastro de alunos - Pilot School', layout, finalize=True)
window1, window2 = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Cadastrar aluno' and not window2:
        window2 = make_win2()
window.close()