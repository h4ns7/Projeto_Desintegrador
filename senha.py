#  Material consultado:
#  https://www.blog.pythonlibrary.org/2021/01/20/pysimplegui-working-with-multiple-windows/

import PySimpleGUI as sg

def make_win1():
    layout = [  [sg.Text('usuário:', size=(8, 1)), sg.InputText(key='-USER-', size=(15, 1))],
                [sg.Text('senha:', size=(8, 1)), sg.InputText('', size=(15, 1), key='-PASSWORD-', password_char='*')],
                [sg.Button('Entrar', size=(10, 1), key='-ENTRAR-')]   ]
    return sg.Window('Autenticação', layout, location=(200, 150), finalize=True)
def make_win2():
    layout = [[sg.Text('Produto:', size=(8, 1)), sg.InputText(key='-PRODUTO-', size=(15, 1))],
              [sg.Text('Quantidade:', size=(8, 1)), sg.InputText(key='-QUANTIDADE-', size=(15, 1))],
              [sg.Text('Valor:', size=(8, 1)), sg.InputText(key='-VALOR-', size=(15, 1))],
              [sg.Button('Armazenar', size=(10, 1), key='-ARMAZENAR-')]   ]
    return sg.Window('Cadastrinho...', layout, finalize=True, location=(100, 100))
window1, window2 = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    elif event == '-ENTRAR-' and not window2:
        if values['-USER-'] == 'admin' and  values['-PASSWORD-'] == 'admin':
            window2 = make_win2()
            window1.close()
        else:
            window['-USER-'].update( '' )
            window['-PASSWORD-'].update( '' )
            sg.popup('Usuário/Senha incorretas', location=(100, 100))
    elif event == '-ARMAZENAR-':
        sg.popup('Vou armazenar no SGBD....', location=(100, 100))
        window['-PRODUTO-'].update( '' )
        window['-QUANTIDADE-'].update( '' )
        window['-VALOR-'].update( '' )