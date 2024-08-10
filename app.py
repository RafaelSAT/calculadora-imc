import PySimpleGUI as sg
import re

sg.theme('Reddit')
#sg.Push() serve para centralizar o elemento, para isto coloque em ambos os lados
layout = [
    [sg.Push(),sg.Text('Digite seu peso (em Kg)'),sg.Push()],    
    [sg.Push(),sg.Input(key='peso', size= 20),sg.Push()],
    [sg.Push(),sg.Text('Digite sua altura (em Cm)'),sg.Push()],
    [sg.Push(),sg.Input(key='altura', size= 20),sg.Push()],         
    [sg.Push(),sg.Button(button_text='Calcular IMC'),sg.Push()],    
    [sg.Push(),sg.Text(k='imc', visible=False),sg.Push()]
]

window = sg.Window('Cálculo IMC', layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event =='Calcular IMC':
        # Remove qualquer caractere diferente de um digito
        altura = re.sub('[^0-9]', '', values['altura'])
        peso = re.sub('[^0-9]', '', values['peso'])        
        if len(altura) > 2 and len(altura) < 4:

            if altura.isdigit() and peso.isdigit():
                #Coloca um '.' na string, para que o cálculo seja feito
                altura = altura[0] + '.' + altura[1] + altura[2]

                imc = float(peso) / (float(altura) * float(altura))

                if imc < 16:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Muito Abaixo do Peso')            
                    window['imc'].update(text_color = 'brown')
                    window['imc'].update(visible = True)
                elif imc >= 17 and imc <= 18.9:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Abaixo do Peso')            
                    window['imc'].update(text_color = 'brown')
                    window['imc'].update(visible = True)
                elif imc >= 19 and imc <= 24.9:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Peso Normal')            
                    window['imc'].update(text_color = 'green')
                    window['imc'].update(visible = True)
                elif imc >= 25 and imc <= 29.9:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Acima do Peso')            
                    window['imc'].update(text_color = 'green')
                    window['imc'].update(visible = True)
                elif imc >= 30 and imc <= 34.9:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Obesidade I')            
                    window['imc'].update(text_color = 'red')
                    window['imc'].update(visible = True)
                elif imc >= 35 and imc <= 39.9:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Obesidade II (Severa)')            
                    window['imc'].update(text_color = 'red')
                    window['imc'].update(visible = True)
                elif imc >= 40:
                    window['imc'].update(f'Seu IMC é: {imc:.1f} - Obesidade III (Mórbida)')            
                    window['imc'].update(text_color = 'black')
                    window['imc'].update(visible = True)

            else:
                window['imc'].update('Por favor digite apenas números')
                window['imc'].update(visible = True)
        else:
               window['imc'].update('Por favor digite a altura em CM')