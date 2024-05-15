import pyautogui as pag
import pandas as pd
import time

pag.PAUSE = 0.5

pag.press("win")
pag.write("chrome")
pag.press("enter")
pag.click(x=310, y=58)
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")

time.sleep(2)

pag.press("tab")
pag.write("leonardodeodonio@gmail.com")
pag.press("tab")
pag.write("123456")
pag.press("tab")
pag.press("enter")

time.sleep(2)

table = pd.read_csv("produtos.csv")

for linha in table.index:
    pag.click(x=654, y=343)
    pag.write(str(table.loc[linha,"codigo"]))
    pag.press("tab")

    pag.write(str(table.loc[linha,"marca"]))
    pag.press("tab")

    pag.write(str(table.loc[linha,"tipo"]))
    pag.press("tab")

    pag.write(str(table.loc[linha,"categoria"]))
    pag.press("tab")

    pag.write(str(table.loc[linha,"preco_unitario"]))
    pag.press("tab")

    pag.write(str(table.loc[linha,"custo"]))
    pag.press("tab")

    obs =str(table.loc[linha,"obs"])
    if obs != "nan":
        pag.write(obs)

    pag.press("tab")

    pag.press("enter")
    pag.scroll(5000)