# === Imports ===
import random
import time
from palavras_termo import dicionario_palavras # Importa a lista diretamente

# === Constantes do Jogo ===
TENTATIVAS_MAXIMAS = 6
TAMANHO_PALAVRA = 5

# === Preparação do Jogo ===
# Escolhe uma palavra aleatória da sua lista e a converte para maiúsculas
palavra_secreta = random.choice(dicionario_palavras).upper()
tentativas_restantes = TENTATIVAS_MAXIMAS
vitorioso = False

# === Mensagem de Boas-vindas ===
print("--- BEM-VINDO AO JOGO TERMO (DEMO) ---")
print(f"Adivinhe a palavra de {TAMANHO_PALAVRA} letras em {TENTATIVAS_MAXIMAS} tentativas.")
print("🟢 Letra certa no lugar certo.")
print("🟠 Letra certa no lugar errado.")
print("❌ Letra que não existe na palavra.")
print("-----------------------------------------")
time.sleep(1)

# === Loop Principal do Jogo ===
while tentativas_restantes > 0:
    print(f"\nVocê tem {tentativas_restantes} tentativa(s) restante(s).")
    
    # --- Validação da Entrada do Usuário ---
    try:
        tentativa = input("Digite sua tentativa: ").upper()

        # Validação 1: Tamanho da palavra
        if len(tentativa) != TAMANHO_PALAVRA:
            print(f"Erro: A palavra deve ter exatamente {TAMANHO_PALAVRA} letras. Tente novamente.")
            continue # Pula para o início do loop sem gastar uma tentativa

        # Validação 2: Palavra existe no dicionário
        if tentativa not in dicionario_palavras:
            print(f"'{tentativa}' não é uma palavra válida. Tente novamente.")
            continue # Pula para o início do loop sem gastar uma tentativa

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        continue
    
    # Se a entrada for válida, o jogo continua e uma tentativa é gasta
    tentativas_restantes -= 1

    # --- Lógica de Verificação das Letras (Alternativa Simples) ---
    feedback_final = ""

    for i in range(TAMANHO_PALAVRA):
        letra_da_tentativa = tentativa[i]
        
        # 1. É verde? (Posição e letra corretas)
        if letra_da_tentativa == palavra_secreta[i]:
            feedback_final += f"🟢 {letra_da_tentativa} "
        
        # 2. É amarela? (Letra existe, mas no lugar errado)
        elif letra_da_tentativa in palavra_secreta:
            # Condição para evitar repetição de amarelos
            total_na_secreta = palavra_secreta.count(letra_da_tentativa)
            ja_marcadas_verdes = 0
            ja_marcadas_amarelas = 0

            # Conta quantas vezes a letra já foi marcada como verde
            for j in range(TAMANHO_PALAVRA):
                if tentativa[j] == letra_da_tentativa and palavra_secreta[j] == letra_da_tentativa:
                    ja_marcadas_verdes += 1
            
            # Conta quantas vezes a letra já foi marcada como amarela (até a posição atual)
            for j in range(i):
                 if tentativa[j] == letra_da_tentativa and palavra_secreta[j] != letra_da_tentativa:
                     ja_marcadas_amarelas += 1
            
            if (ja_marcadas_verdes + ja_marcadas_amarelas) < total_na_secreta:
                feedback_final += f"🟠 {letra_da_tentativa} "
            else:
                feedback_final += f"❌ {letra_da_tentativa} " # Já usamos todas, então esta é cinza
        
        # 3. É cinza? (Letra não existe na palavra)
        else:
            feedback_final += f"❌ {letra_da_tentativa} "
            
    # Mostra o resultado da rodada para o usuário
    print(feedback_final)

    # --- Verificação de Vitória ---
    if tentativa == palavra_secreta:
        print("\n-----------------------------------------")
        print("🎉 PARABÉNS! VOCÊ ACERTOU A PALAVRA! 🎉")
        print("-----------------------------------------")
        vitorioso = True
        break # Encerra o loop do jogo

# === Fim de Jogo ===
if not vitorioso:
    print("\n-----------------------------------------")
    print("GAME OVER! Suas tentativas acabaram.")
    print(f"A palavra secreta era: {palavra_secreta}")
    print("-----------------------------------------")

# Pausa antes de fechar o programa
time.sleep(5)