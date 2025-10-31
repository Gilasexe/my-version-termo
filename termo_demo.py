# === Imports ===
import time
from palavras_termo import *
import sys
import os

# === Variaveis ===
palavra = "pilha" # aqui determinamos a palavra
a1, a2, a3, a4, a5 = palavra # aqui atribuimos cada variavel a uma letra

run = True # botei essa variavel apenas pra utilizar na tentativa
vzs_tentativa = 0 # coloquei essa variavel para contar quantas tentativas o usuario fez

# aviso de demo
print("ISTO É APENAS UMA DEMO, ESPERE ERROS.\n")
time.sleep(2)

# === Processamento e saida ===
while True:
    vzs_tentativa += 1
    primeira_letra = False
    segunda_letra = False
    terceira_letra = False
    quarta_letra = False
    quinta_letra = False
    while run:
        try:
            tentativa = str(input("\nDigite a sua tentativa: ").upper()) # aqui pegamos a tentativa do usuario e colocamos .lower() pra organizar
            if tentativa in dicionario_palavras: # checando se a palavra existe no dicionario
                b1, b2, b3, b4, b5 = tentativa.lower()
                break
            else:
                print("\nPalavra desconhecida, tente novamente")
                continue
        except ValueError: # caso o usuario digite mais de 5 letras ele retorna a informação de que é no maximo 5 letras, e deixa o usuario tentar denovo
            print("\nMáximo 5 letras.")
    # e daqui pra baixo temos as verificações, e o retorno das tais.
    if a1 == b1:
        print("\n🟢 A primeira letra esta correta.")
        primeira_letra = True
    else:
        if b1 in palavra:
            print("\n🟠 tem essa letra mas não ta no lugar certo.")
        else:
            print("\n❌ a primeira letra esta incorreta.")

    if a2 == b2:
        print("\n🟢 A segunda letra esta correta.")
        segunda_letra = True
    else:
        if b2 in palavra:
            print("\n🟠 tem essa letra mas não ta no lugar certo.")
        else:
            print("\n❌ a segunda letra esta incorreta.")

    if a3 == b3:
        print("\n🟢 A terceira letra esta correta.")
        terceira_letra = True
    else:
        if b3 in palavra:
            print("\n🟠 tem essa letra mas não ta no lugar certo.")
        else:
            print("\n❌ a terceira letra esta incorreta.")

    if a4 == b4:
        print("\n🟢 A quarta letra esta correta.")
        quarta_letra = True
    else:
        if b4 in palavra:
            print("\n🟠 tem essa letra mas não ta no lugar certo.")
        else:
            print("\n❌ a quarta letra esta incorreta.")

    if a5 == b5:
        print("\n🟢 A quinta letra esta correta.")
        quinta_letra = True
    else:
        if b5 in palavra:
            print("\n🟠 tem essa letra mas não ta no lugar certo.")
        else:
            print("\n❌ a quinta letra esta incorreta.")
    
    if primeira_letra and segunda_letra and terceira_letra and quarta_letra and quinta_letra: # aqui verificamos se todas as letras são verdadeiras
        print("\nParabéns você acertou a palavra!")
        time.sleep(1)
        break
    else:
        if vzs_tentativa > 4:
            print(f"\nVocê atingiu o numero maximo de tentativas, a palavra era {palavra}")
            break
        else:
            print("\nTry again bitch")