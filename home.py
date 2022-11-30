import PySimpleGUI as sg
import psycopg2

def make_win1():
    layout = [[sg.Text('Bem vindo ao sistema Pilot School'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Button('Cadastrar Aluno'),
              sg.Button('Cadastrar Instrutor'),
              sg.Button('Cadastrar Curso'),
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
       
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS-")
        
    ],
    [
      sg.Button('Sair')
    ]]
    return sg.Window('Cadastro de alunos - Pilot School', layout, finalize=True)

def make_win3():
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
        sg.Text("Valor:", size=(8, 1)),
        sg.InputText(size=(70, 1), key="-VAL-")
    ],
    [
        sg.Button('Limpar', size=(8, 1), key="-LIMPAR-"),
        sg.Button('Inserir', size=(8, 1), key="-INSERIR-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR-"),
        sg.Button('Remover', size=(8, 1), key="-REMOVER-")
    ],
    [
        
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS-")
        
    ],
    [
      sg.Button('Sair')
    ]]
    return sg.Window('Cadastro de Instrutores - Pilot School', layout, finalize=True)

def make_win4():
    layout = [

    [sg.Text("Nome Curso: ", size=(10, 1)),sg.InputText(size=(40, 1), key="-NOME-", focus=True)],
    [sg.Text("Carga Horaria: ", size=(10, 1)),sg.InputText(size=(40, 1), key="-CARGA-")],
    [sg.Text("Preço: ", size=(10, 1)),sg.InputText(size=(40, 1), key="-VALOR-")],
    [sg.Button('Limpar', size=(8, 1), key="-LIMPAR-"),sg.Button('Inserir', size=(8, 1), key="-INSERIR-"),
    sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR-"),sg.Button('Remover', size=(8, 1), key="-REMOVER-")],
    [sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),sg.Button('Todos', size=(8, 1), key="-TODOS-")],
    [sg.Button('Sair')]]
    return sg.Window('Cadastro de Cursos - Pilot School', layout, finalize=True)

def limpar():
    window['-NOME-'].update('')
    window['-EMAIL-'].update('')
    window['-CPF-'].update('')
    window['-GENERO-F-'].update(True)
    window['-LOGRADOURO-'].update('')
    window['-CEL-'].update('')

def atualiza():
    if len(lista) == 0:
        limpar()
    else:
        window['-NOME-'].update( lista[indice][1] )
        window['-EMAIL-'].update( lista[indice][2] )
        window['-CPF-'].update( lista[indice][3] )
        if lista[indice][4]: window['-GENERO-M-'].update(True)
        else: window['-GENERO-F-'].update(True)
        window['-LOGRADOURO-'].update( lista[indice][5] )
        window['-CEL-'].update( lista[indice][6] )


con = psycopg2.connect(host="localhost", database="gemini", user="postgres", password="1234")
with con:
    with con.cursor() as cursor:
        cursor.execute(""" 
        
        
        
        """)

lista=[]
indice = 0


window1, window2 = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break

    elif event == "-INSERIR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO ALUNO (NOME, EMAIL, CPF, GENERO, LOGRADOURO, CELULAR) VALUES (%s, %s, %s, %s, %s, %s);",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), values['-LOGRADOURO-'], values['-CEL-'] ))
        limpar()
    elif event == "-ATUALIZAR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("UPDATE ALUNO SET NOME = %s, EMAIL = %s, CPF = %s, GENERO = %s, LOGRADOURO = %s, CELULAR = %s WHERE id = %s",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), lista[indice][0]),values['-LOGRADOURO-'], values['-CEL-'] )
        lista[indice] = [lista[indice][0], values['-NOME-'], values['-EMAIL-'], values['-CPF-'], values['-GENERO-M-'], values['-LOGRADOURO-'], values['-CEL']]        
    elif event == "-REMOVER-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM ALUNO WHERE IDALUNO = %s", (lista[indice][0],))
        lista.pop(indice)
        indice -= 1
        atualiza()
    elif event == "-PROCURAR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("SELECT * FROM ALUNO WHERE nome LIKE %s;",
                    ('%'+values['-NOME-']+'%',))
                resposta = cursor.fetchall()
                lista.clear()
                listaString = ''
                for i in range(len(resposta)):
                    lista.append( list(resposta[i]) )
                    lista[i][4] = True if lista[i][4] == 'M' else False
                    listaString += str(i+1) +') ' + resposta[i][1] + '\n'
                sg.popup('Resultado:\n\n' + listaString)
                indice = 0
                atualiza()
    elif event == "-TODOS-":
        todos()
    elif event == "->>-":
        indice += 1
        if indice >= len(lista): indice = len(lista)-1
        atualiza()
    elif event == "-<<-":
        indice -= 1
        if indice <= 0: indice = 0
        atualiza()
    elif event == 'Cadastrar Aluno' and not window2:
        window2 = make_win2()
    elif event == 'Cadastrar Instrutor' and not window2:
        window2 = make_win3()
    elif event == 'Cadastrar Curso' and not window2:
        window2 = make_win4()


window.close()

con.commit()
cursor.close()
con.close()