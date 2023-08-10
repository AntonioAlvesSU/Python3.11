import pyautogui
import pandas as pd
import time

# importando a base de produtos
tabela = pd.read_csv("produtos.csv")
# print(tabela)

pyautogui.PAUSE = 3

# Aqui vamos abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar um tempinho para abrir o navegador no site
time.sleep(5)

# Agora vamos fazer o login
pyautogui.click(x=427, y=363)
pyautogui.write("bruno@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")    
pyautogui.click(x=672, y=524)

# Percorrendo linhas da tabela e cadastrando os produtos 
for linha in tabela.index:
    pyautogui.click(x=408, y=249)
    pyautogui.write(str(tabela.loc[linha, "codigo"])) 
    pyautogui.press("tab")
    #repetir para todos os campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.click(x=590, y=556) 
    pyautogui.scroll(5000)    
    
    