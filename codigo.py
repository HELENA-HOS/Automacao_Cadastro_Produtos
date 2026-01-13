
# Passo a passo do programa

import pyautogui
import time

pyautogui.PAUSE = 1

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "helena_oliveirasilva@yahoo.com"
senha = "123456"

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer pausa maior para o site carregar
time.sleep(3)


# Passo 2: Fazer login
pyautogui.click(x=680, y=395)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")


# Passo 3: Abrir base de dados (importar arquivo)
import pandas as pd
base_dir = __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0]
csv_path = base_dir + '\\produtos.csv'
tabela = pd.read_csv(csv_path)


# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=622, y=286) # clica no campo código
    # codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") # passa para o proximo campo
    
    # marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") # passa para o proximo campo
    
    # tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") # passa para o proximo campo
    
    # categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab") # passa para o proximo campo
    
    # preco
    preco = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab") # passa para o proximo campo
    
    # custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") # passa para o proximo campo
    
    # obs
    obs = str(tabela.loc[linha,"obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") # passa para o botao ENVIAR

    pyautogui.press("enter") # salva o produto

    pyautogui.scroll(5000) # rola a tela para o início

# Passo 5: Repetir passo 4 até finalizar lista de produtos