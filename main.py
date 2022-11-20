from tkinter import *
from tkinter import ttk


janela = Tk()

def atualiza():
    import requests

    dados_api = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?lat=-23.5506507&lon=-46.6333824&appid=suaidentificacao')
    temperaturas = dados_api.json()['main']
    return temperaturas

sensacao = round(atualiza()['feels_like'] -273.15)
minima = round(atualiza()['temp_min'] - 273.15)
maxima = round(atualiza()['temp_max'] - 273.15)
atual = round(atualiza()['temp'] - 273.15)
print(atual)

frm = ttk.Frame(janela, padding=20)
frm.grid()
ttk.Label(frm, text="Temperatura atual: ", padding=5).grid(column=0, row=0)
ttk.Label(frm, text=f"{atual}°C").grid(column=1, row=0)
ttk.Label(frm, text="Temperatura minima: ", padding=5).grid(column=0, row=1)
ttk.Label(frm, text=f"{minima}°C").grid(column=1, row=1)
ttk.Label(frm, text="Temperatura maxima: ", padding=5).grid(column=0, row=2)
ttk.Label(frm, text=f"{maxima}°C").grid(column=1, row=2)
ttk.Button(frm, text='Atualizar', command=atualiza()).grid(column=1, row=3)




if __name__ == '__main__':
    janela.mainloop()
