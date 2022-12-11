

import PySimpleGUI as sg
import psycopg2
from PySimpleGUI import *





# Telas
def make_win1():
    layout = [
        [Image(filename='Projeto_Desintegrador/logo.png')],
        [sg.Button('Cadastrar Aluno'),sg.Button('Cadastrar Instrutor'),sg.Button('Cadastrar Curso'),sg.Button('Sair')]]
    return sg.Window('Sistema de Cadastro Pilot School', layout, location=(800,600), finalize=True)

def make_win2():

    

    layout = [
        [Image(filename='Projeto_Desintegrador/aluno.png')],
    [
        sg.Text("Nome:", size=(5, 1)),
        sg.InputText(size=(30, 1), key="-NOME-", focus=True),
        sg.Text("E-mail:", size=(5, 1)),
        sg.InputText(size=(30, 1), key="-EMAIL-")
    ],

    [
        sg.Text("CPF:", size=(5, 1)),
        sg.InputText(size=(15, 1), key="-CPF-"),
        sg.Text("Gênero:", size=(8, 1)),
        sg.Radio('Masculino', 'GRUPO1', default=False, key="-GENERO-M-"),
        sg.Radio('Feminino', 'GRUPO1', default=True, key="-GENERO-F-")
    ],
    [
        sg.Text("Logradouro:", size=(10, 1)),
        sg.InputText(size=(40, 1), key="-LOGRADOURO-"),
        sg.Text("Celular:", size=(5, 1)),
        sg.InputText(size=(12, 1), key="-CEL-")
    ],

    [
        sg.Button('Cadastrar', size=(8, 1), key="-INSERIR_ALUNO-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR_ALUNO-"),
        sg.Button('Remover', size=(8, 1), key="-REMOVER_ALUNO-"),
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR_ALUNO-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS_ALUNO-"),
        sg.Button('Sair')
    ]       
              
              
  ]
    return sg.Window('Cadastro de alunos - Pilot School', layout, finalize=True, element_justification='c')
def make_win3():
    layout = [
        [Image(filename='Projeto_Desintegrador/instrutor.png')],

    [
        sg.Text("Nome:", size=(8, 1)),
        sg.InputText(size=(30, 1), key="-NOME-", focus=True),
        sg.Text("E-mail:", size=(8, 1)),
        sg.InputText(size=(30, 1), key="-EMAIL-")
    ],
    [
        sg.Text("CPF:", size=(8, 1)),
        sg.InputText(size=(15, 1), key="-CPF-"),
        sg.Text("Gênero:", size=(8, 1)),
        sg.Radio('Masculino', 'GRUPO1', default=False, key="-GENERO-M-"),
        sg.Radio('Feminino', 'GRUPO1', default=True, key="-GENERO-F-")
    ],
    [
        sg.Text("Logradouro:", size=(8, 1)),
        sg.InputText(size=(30, 1), key="-LOGRADOURO-"),
        sg.Text("Celular:", size=(8, 1)),
        sg.InputText(size=(12, 1), key="-CEL-"),
        sg.Text("Valor:", size=(8, 1)),
        sg.InputText(size=(8, 1), key="-VALOR-")
    ],
    [
        sg.Button('Cadastrar', size=(8, 1), key="-INSERIR_INSTRUTOR-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR_INSTRUTOR-"),
        sg.Button('Remover', size=(8, 1), key="-REMOVER_INSTRUTOR-"),
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR_INSTRUTOR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS_INSTRUTOR-"),
        sg.Button('Sair')
    ]]
    return sg.Window('Cadastro de Instrutores - Pilot School', layout, finalize=True,element_justification='c')

def make_win4():
    layout = [
    [Image(filename='Projeto_Desintegrador/curso.png')],
    [sg.Text("Nome Curso: ", size=(10, 1)),sg.InputText(size=(30, 1), key="-NOMECURSO-", focus=True)],
    [sg.Text("Carga Horaria: ", size=(10, 1)),sg.InputText(size=(10, 1), key="-CARGA_CURSO-")],
    [sg.Text("Valor R$: ", size=(10, 1)),sg.InputText(size=(8, 1), key="-VALOR_CURSO-")],
    [sg.Button('Cadastrar', size=(8, 1), key="-INSERIR_CURSO-"),sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR_CURSO-"),sg.Button('Remover', size=(8, 1), key="-REMOVER_CURSO-"),sg.Button('Procurar', size=(8, 1), key="-PROCURAR_CURSO-"),sg.Button('Todos', size=(8, 1), key="-TODOS_CURSO-"),sg.Button('Sair')]]
    return sg.Window('Cadastro de Cursos - Pilot School', layout, finalize=True,element_justification='c')


def limparaluno():
    window['-NOME-'].update('')
    window['-EMAIL-'].update('')
    window['-CPF-'].update('')
    window['-GENERO-F-'].update(True)
    window['-LOGRADOURO-'].update('')
    window['-CEL-'].update('')



def limparinstrutor():
    window['-NOME-'].update('')
    window['-EMAIL-'].update('')
    window['-CPF-'].update('')
    window['-GENERO-F-'].update(True)
    window['-LOGRADOURO-'].update('')
    window['-CEL-'].update('')
    window['-VALOR-'].update('')



def limparcurso():
    window['-NOMECURSO-'].update('')
    window['-CARGA_CURSO-'].update('')
    window['-VALOR_CURSO-'].update('')



def atualizaaluno():
    if len(lista) == 0:
        limparaluno()
    else:
        window['-NOME-'].update( lista[indice][1] )
        window['-EMAIL-'].update( lista[indice][2] )
        window['-CPF-'].update( lista[indice][3] )
        if lista[indice][4]: window['-GENERO-M-'].update(True)
        else: window['-GENERO-F-'].update(True)
        window['-LOGRADOURO-'].update( lista[indice][5] )
        window['-CEL-'].update( lista[indice][6] )


def atualizainstrutor():
    if len(lista) == 0:
        limparinstrutor()
    else:
        window['-NOME-'].update( lista[indice][1] )
        window['-EMAIL-'].update( lista[indice][2] )
        window['-CPF-'].update( lista[indice][3] )
        if lista[indice][4]: window['-GENERO-M-'].update(True)
        else: window['-GENERO-F-'].update(True)
        window['-LOGRADOURO-'].update( lista[indice][5] )
        window['-CEL-'].update( lista[indice][6])
        window['-VALOR-'].update( lista[indice][7])



def atualizacurso():
    if len(lista) == 0:
        limparcurso()
    else:
        window['-NOMECURSO-'].update( lista[indice][1] )
        window['-CARGA_CURSO-'].update( lista[indice][2] )
        window['-VALOR_CURSO-'].update( lista[indice][3] )



def todosalunos():

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
    atualizaaluno()






def todosinstrutor():

    global indice
    global lista
    resposta = []
    with con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM INSTRUTOR;")
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
    atualizainstrutor()


def todoscurso():

    global indice
    global lista
    resposta = []
    with con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM CURSO;")
            resposta = cursor.fetchall()
    lista.clear()
    listaString = ''
    for i in range(len(resposta)):
        lista.append( list(resposta[i]) )
        listaString += str(i+1) +') ' + resposta[i][1] + '\n'
    sg.popup('Resultado:\n\n' + listaString)
    # sg.popup('Quantidade de registros: ' + str(len(resposta)))
    indice = 0
    atualizacurso()




# Inicialização BD

con = psycopg2.connect(host="localhost", database="gemini", user="postgres", password="1234")

with con:
    with con.cursor() as cursor:
        cursor.execute("""
        
        
        CREATE TABLE IF NOT EXISTS ALUNO (
	        IDALUNO SERIAL PRIMARY KEY NOT NULL,
	        NOME VARCHAR(70) NOT NULL,
	        EMAIL VARCHAR(40) NOT NULL,
	        CPF VARCHAR(15) UNIQUE,
            GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M', 'F')),
            LOGRADOURO VARCHAR(70) NOT NULL,
            CELULAR VARCHAR(11) NOT NULL
        );





        CREATE TABLE IF NOT EXISTS INSTRUTOR (
	        IDINSTRUTOR SERIAL PRIMARY KEY NOT NULL,
	        NOME VARCHAR(70) NOT NULL,
	        EMAIL VARCHAR(40) NOT NULL,
	        CPF VARCHAR(15) UNIQUE NOT NULL,
            GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M' ,'F')),
            LOGRADOURO VARCHAR(70) NOT NULL,
            CELULAR VARCHAR(15) NOT NULL,
	        VALORHORA NUMERIC (6,2) NOT NULL
        );
                
                
        CREATE TABLE IF NOT EXISTS CURSO(
	        IDCURSO SERIAL PRIMARY KEY NOT NULL,
	        NOME_CURSO VARCHAR(40) NOT NULL,
	        CARGA_HORARIA VARCHAR (10) NOT NULL,
	        VALOR NUMERIC(6,2) NOT NULL
        );
        

        CREATE TABLE  IF NOT EXISTS TURMA( 
	        IDTURMA SERIAL PRIMARY KEY NOT NULL,
	        ID_CURSO INTEGER NOT NULL,
	        ID_INSTRUTOR INTEGER NOT NULL,
	        PERIODO CHAR(10) NOT NULL CHECK( PERIODO IN ('MATUTINO','VESPERTINO','NOTURNO')),
	        SALA_TURMA CHAR(1) NOT NULL CHECK ( SALA_TURMA IN ('1','2','3') ),
	        FOREIGN KEY(ID_CURSO) REFERENCES CURSO(IDCURSO) ON DELETE CASCADE ON UPDATE CASCADE,
	        FOREIGN KEY(ID_INSTRUTOR) REFERENCES INSTRUTOR(IDINSTRUTOR) ON DELETE CASCADE ON UPDATE CASCADE 
        );



        CREATE TABLE IF NOT EXISTS CURSO_TURMA (
	        IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	        IDTURMA INTEGER REFERENCES TURMA(IDTURMA),
	        PRIMARY KEY (IDCURSO, IDTURMA)
        );

        

        CREATE TABLE IF NOT EXISTS HISTORICO(
	        IDHISTORICO SERIAL PRIMARY KEY NOT NULL,
	        ID_ALUNO INTEGER NOT NULL,
	        NUMERO_DE_VOLTAS SMALLINT NOT NULL,
	        VELOCIDADE VARCHAR(10) NOT NULL,
	        TEMPO VARCHAR(10) NOT NULL,
	        VOLTA_MAIS_RAPIDA SMALLINT NOT NULL,
	        NOTA NUMERIC (4,2) NOT NULL,
	        RESULTADO CHAR(10) NOT NULL CHECK( RESULTADO IN ('APROVADO','REPROVADO')),
	        FOREIGN KEY(ID_ALUNO) REFERENCES ALUNO (IDALUNO) ON DELETE CASCADE ON UPDATE CASCADE 
        );


        CREATE TABLE IF NOT EXISTS PROVA(
	        IDPROVA SERIAL PRIMARY KEY NOT NULL,
	        ID_ALUNO INTEGER NOT NULL,
	        NOME_PROVA VARCHAR (80) NOT NULL,
	        TIPO_PROVA CHAR(7)  NOT NULL CHECK ( TIPO_PROVA IN ('PRÁTICA','TEÓRICA') ),
	        NOTA NUMERIC(4,2) NOT NULL,
	        DATA_PROVA DATE NOT NULL,
	        VALOR NUMERIC(6,2) NOT NULL,
	        SALA CHAR(1) NOT NULL CHECK ( SALA IN ('0', '1','2','3') ),
	        FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO)  
        );

        CREATE TABLE IF NOT EXISTS CURSO_PROVA (
	        IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	        IDPROVA INTEGER REFERENCES PROVA(IDPROVA),
	        PRIMARY KEY(IDCURSO, IDPROVA)	
        );

        CREATE TABLE IF NOT EXISTS MATRICULA(
	        IDMATRICULA INTEGER PRIMARY KEY,
	        DATA_MATRICULA DATE NOT NULL,
	        ID_ALUNO INTEGER NOT NULL,
	        ID_CURSO INTEGER NOT NULL, 
	        ID_TURMA INTEGER NOT NULL,
	        ID_HISTORICO INTEGER,
	        FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO (IDALUNO) ,
	        FOREIGN KEY (ID_CURSO) REFERENCES CURSO (IDCURSO),
	        FOREIGN KEY (ID_TURMA) REFERENCES TURMA (IDTURMA) ,
	        FOREIGN KEY (ID_HISTORICO) REFERENCES HISTORICO (IDHISTORICO) 
            );

        """)

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
        
        sg.Button('Inserir', size=(8, 1), key="-INSERIR-"),
        sg.Button('Atualizar', size=(8, 1), key="-ATUALIZAR-")
    ],
    [
        
        sg.Button('Procurar', size=(8, 1), key="-PROCURAR-"),
        sg.Button('Todos', size=(8, 1), key="-TODOS-"),
        sg.Button('Aluno'),
        sg.Button('Exit')
    ]
]

window = sg.Window("Sistema de genrenciamento PILOT SCHOOL", layout, use_default_focus=False)

# ENQUANTO VERDADE RODAR SEMPRE

window1, window2 = make_win1(), None  
while True:      
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        if window == window2:       
            window2 = None
        elif window == window1:    
            break    
    elif event == 'Cadastrar Aluno' and not window2:
        window2 = make_win2()
    elif event == 'Cadastrar Instrutor' and not window2:
        window2 = make_win3()
    elif event == 'Cadastrar Curso' and not window2:
        window2 = make_win4()
    elif event == "-INSERIR_ALUNO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO ALUNO (NOME, EMAIL, CPF, GENERO, LOGRADOURO, CELULAR) VALUES (%s, %s, %s, %s, %s, %s);",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), values['-LOGRADOURO-'], values['-CEL-'] ))
        limparaluno()
    elif event == "-ATUALIZAR_ALUNO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("UPDATE aluno SET NOME = %s, EMAIL = %s, CPF = %s, GENERO = %s, LOGRADOURO = %s, CELULAR = %s WHERE id = %s",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), lista[indice][0]),values['-LOGRADOURO-'], values['-CEL-'] )
        lista[indice] = [lista[indice][0], values['-NOME-'], values['-EMAIL-'], values['-CPF-'], values['-GENERO-F-'], values['-LOGRADOURO-'], values['-CEL']]        
    elif event == "-REMOVER_ALUNO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM ALUNO WHERE IDALUNO = %s", (lista[indice][0],))
        lista.pop(indice)
        indice -= 1
        atualizaaluno()
    elif event == "-PROCURAR_ALUNO-":
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

                sg.Table(values=resposta,headings=['COD','Valor','Dt Pago','Dt Vence','Status','COD Aluno','COD Matricula'], max_col_width=35,
                           auto_size_columns=True,
                           justification='center',
                           num_rows=22,
                           enable_events=True,
                           key='PROCURAR_ALUNO',
                           row_height=19,
                           tooltip=''),sg.Push(),
                sg.Push(),sg.Text('Menu Mensalidade', font=("Comic Sans", 14)),sg.Push()
                sg.popup('Resultado:\n\n' + listaString)
                indice = 0
                atualizaaluno()
    elif event == "-TODOS_ALUNO-":
        todosalunos()
    elif event == "->>-":
        indice += 1
        if indice >= len(lista): indice = len(lista)-1
        atualizaaluno()
    elif event == "-<<-":
        indice -= 1
        if indice <= 0: indice = 0
        atualizaaluno()




# Instrutor 


    elif event == "-INSERIR_INSTRUTOR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO INSTRUTOR (NOME, EMAIL, CPF, GENERO, LOGRADOURO, CELULAR, VALORHORA) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), values['-LOGRADOURO-'], values['-CEL-'],values['-VALOR-'] ))
        limparinstrutor()
    elif event == "-ATUALIZAR_INSTRUTOR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("UPDATE INSTRUTOR SET NOME = %s, EMAIL = %s, CPF = %s, GENERO = %s, LOGRADOURO = %s, CELULAR = %s, VALORHORA = %s WHERE id = %s",
                    (values['-NOME-'], values['-EMAIL-'], values['-CPF-'], ('M' if values['-GENERO-M-'] else 'F'), lista[indice][0]),values['-LOGRADOURO-'], values['-CEL-'], values['-VALOR-'])
        lista[indice] = [lista[indice][0], values['-NOME-'], values['-EMAIL-'], values['-CPF-'], values['-GENERO-M-'], values['-LOGRADOURO-'], values['-CEL'],values['-VALOR-']]        
    elif event == "-REMOVER_INSTRUTOR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM INSTRUTOR WHERE IDINSTRUTOR = %s", (lista[indice][0],))
        lista.pop(indice)
        indice -= 1
        atualizainstrutor()
    elif event == "-PROCURAR_INSTRUTOR-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("SELECT * FROM INSTRUTOR WHERE nome LIKE %s;",
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
                atualizainstrutor()
    elif event == "-TODOS_INSTRUTOR-":
        todosinstrutor()
    elif event == "->>-":
        indice += 1
        if indice >= len(lista): indice = len(lista)-1
        atualizainstrutor()
    elif event == "-<<-":
        indice -= 1
        if indice <= 0: indice = 0
        atualizainstrutor()




#Cadastro curso



    elif event == "-INSERIR_CURSO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("INSERT INTO CURSO (NOME_CURSO, CARGA_HORARIA, VALOR) VALUES (%s, %s, %s);",
                    (values['-NOMECURSO-'], values['-CARGA_CURSO-'], values['-VALOR_CURSO-']))
            limparcurso()
    elif event == "-ATUALIZAR_CURSO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("UPDATE CURSO SET NOME_CURSO = %s, CARGA_HORARIA = %s, VALOR = %s WHERE id = %s",
                    (values['-NOMECURSO-'], values['-CARGA_CURSO-'], values['-VALOR_CURSO-'] ))
        lista[indice] = [lista[indice][0], values['-NOMECURSO-'], values['-CARGA_CURSO-'], values['-VALOR_CURSO-']]        
    elif event == "-REMOVER_CURSO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("DELETE FROM CURSO WHERE IDCURSO = %s", (lista[indice][0],))
        lista.pop(indice)
        indice -= 1
        atualizacurso()
    elif event == "-PROCURAR_CURSO-":
        with con:
            with con.cursor() as cursor:
                cursor.execute("SELECT * FROM CURSO WHERE NOME_CURSO LIKE %s;",
                    ('%'+values['-NOMECURSO-']+'%',))
                resposta = cursor.fetchall()
                lista.clear()
                listaString = ''
                for i in range(len(resposta)):
                    lista.append( list(resposta[i]) )
                    listaString += str(i+1) +') ' + resposta[i][1] + '\n'
                sg.popup('Resultado:\n\n' + listaString)
                indice = 0
                atualizacurso()
    elif event == "-TODOS_CURSO-":
        todoscurso()
    elif event == "->>-":
        indice += 1
        if indice >= len(lista): indice = len(lista)-1
        atualizacurso()
    elif event == "-<<-":
        indice -= 1
        if indice <= 0: indice = 0
        atualizacurso()



# Fazer as mudanças para a base persistente
con.commit()

# Fechar a comunicação com o servidor
cursor.close()
con.close()