# Links consultados:
#  https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
#  https://www.psycopg.org/docs/
#  https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
#  https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge
#  https://holypython.com/gui-with-python-checkboxes-and-radio-buttons-pysimplegui-part-ii/
#  


import PySimpleGUI as sg
import psycopg2

def limpar():
    window['-NOME-'].update('')
    window['-EMAIL-'].update('')
    window['-CPF-'].update('')
    window['-GENERO-F-'].update(True)
    #window['-ESTADO-SP-'].update(True)
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

        '''if lista[indice][5]: window['-ESTADO-SP-'].update(True)
        elif lista[indice][5]: window['-ESTADO-RO-'].update(True)
        elif lista[indice][5]: window['-ESTADO-AC-'].update(True)
        elif lista[indice][5]: window['-ESTADO-TO-'].update(True)
        elif lista[indice][5]: window['-ESTADO-MA-'].update(True)
        elif lista[indice][5]: window['-ESTADO-CE-'].update(True)
        elif lista[indice][5]: window['-ESTADO-SE-'].update(True)
        elif lista[indice][5]: window['-ESTADO-MG-'].update(True)
        elif lista[indice][5]: window['-ESTADO-ES-'].update(True)
        elif lista[indice][5]: window['-ESTADO-SC-'].update(True)
        elif lista[indice][5]: window['-ESTADO-MS-'].update(True)
        elif lista[indice][5]: window['-ESTADO-MT-'].update(True)
        elif lista[indice][5]: window['-ESTADO-GO-'].update(True)
        else: lista[indice][5]: window['-ESTADO-DF-'].update(True)'''

        window['-LOGRADOURO-'].update( lista[indice][5] )
        window['-CEL-'].update( lista[indice][6] )


def todos():
    global indice
    global lista
    resposta = []
    with con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM ALUNO;")
            resposta = cursor.fetchall()
    lista.clear()
    listaString = ''
    for i in range(len(resposta)):
        lista.append( list(resposta[i]) )
        lista[i][4] = True if lista[i][4] == 'M' else False
        listaString += str(i+1) +') ' + resposta[i][1] + '\n'
    sg.popup('Resultado:\n\n' + listaString)
    # sg.popup('Quantidade de registros: ' + str(len(resposta)))
    indice = 0
    atualiza()

# Inicialização BD

con = psycopg2.connect(host="localhost", database="gemini", user="postgres", password="1234")

with con:
    with con.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS ALUNO (
	                        IDALUNO SERIAL PRIMARY KEY NOT NULL,
	                        NOME VARCHAR(70) NOT NULL,
	                        EMAIL VARCHAR(40) NOT NULL,
	                        CPF VARCHAR(15) UNIQUE,
                          GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M', 'F')),
                          LOGRADOURO VARCHAR(70) NOT NULL,
                          CELULAR VARCHAR(11) NOT NULL
                );""")

lista=[]
indice = 0

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
    ]
]

window = sg.Window("Sistema de genrenciamento PILOT SCHOOL", layout, use_default_focus=False)

# ENQUANTO VERDADE RODAR SEMPRE
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "-LIMPAR-":
        limpar()
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

window.close()

# Fazer as mudanças para a base persistente
con.commit()

# Fechar a comunicação com o servidor
cursor.close()
con.close()