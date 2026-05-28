# -*- coding: utf-8 -*-
# ==============================================================================
# FIAP - Data Science: Artificial Intelligence, Analytics, Cloud & Data Platforms
# Disciplina: Data Driven Application & Data Science
# Avaliação: 2026 1ª Global Solutions
# ==============================================================================
# INTEGRANTES:
# 1. [Nome do Aluno 1] - RM: [XXXXX] (Representante)
# 2. [Nome do Aluno 2] - RM: [XXXXX]
# 3. [Nome do Aluno 3] - RM: [XXXXX]
# ==============================================================================

# ------------------------------------------------------------------------------
# CORES ANSI
# Códigos especiais que o terminal interpreta como cores.
# Cada código muda a cor do texto que vem depois dele.
# RESET garante que a cor volte ao normal após cada uso.
# ------------------------------------------------------------------------------
RESET   = "\033[0m"
BOLD    = "\033[1m"
VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
CIANO   = "\033[96m"
AZUL    = "\033[94m"
MAGENTA = "\033[95m"
BRANCO  = "\033[97m"

# ------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES DE EXIBIÇÃO
# Funções são blocos de código reutilizáveis. Aqui usamos para padronizar
# a aparência das linhas divisórias e cabeçalhos ao longo do programa.
# ------------------------------------------------------------------------------

def linha(cor=CIANO, char="═", tamanho=58):
    """Imprime uma linha decorativa com a cor e o caractere escolhidos."""
    print(f"{cor}{char * tamanho}{RESET}")

def cabecalho(texto, cor=AZUL):
    """Imprime um bloco de cabeçalho com linha acima e abaixo."""
    linha(cor)
    print(f"{BOLD}{cor}  {texto}{RESET}")
    linha(cor)

def secao(texto, cor=CIANO):
    """Imprime um título de seção com linha simples."""
    print(f"\n{BOLD}{cor}  ▸ {texto}{RESET}")
    linha(cor, "─", 58)

def item(rotulo, valor, cor_rotulo=BRANCO, cor_valor=AMARELO):
    """Imprime uma linha no formato  Rótulo: Valor  com cores separadas."""
    print(f"  {cor_rotulo}{rotulo}:{RESET} {cor_valor}{valor}{RESET}")

# ------------------------------------------------------------------------------
# INICIALIZAÇÃO DAS LISTAS DE ARMAZENAMENTO
# Cada lista guarda um tipo de informação para todos os eventos.
# A posição 0 de cada lista pertence ao Evento 1, a posição 1 ao Evento 2, etc.
# Isso garante que os dados de um mesmo evento fiquem "alinhados" entre as listas.
# ------------------------------------------------------------------------------
tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []

# Exibe o cabeçalho principal do sistema
print()
cabecalho("  SISTEMA DE MONITORAMENTO ESPACIAL AMBIENTAL", AZUL)
print(f"  {CIANO}Satélite: FIAP-ENV-01  |  Cobertura: Brasil{RESET}")
linha(AZUL, "═")
print()

# ==============================================================================
# 1. ENTRADA DE DADOS
# ==============================================================================

# Pede a quantidade de eventos. O loop 'while True' repete a pergunta
# enquanto o valor digitado for inválido (texto ou número <= 0).
while True:
    try:
        qtd_eventos = int(input(f"{BOLD}{VERDE}  Insira a quantidade de eventos a registrar: {RESET}"))
        if qtd_eventos > 0:
            break
        print(f"  {VERMELHO}✗ A quantidade deve ser maior que zero.{RESET}")
    except ValueError:
        print(f"  {VERMELHO}✗ Digite um número inteiro válido.{RESET}")

# O loop 'while' substitui o 'for' aqui para permitir parada antecipada.
# A variável 'i' controla o número do evento atual, começando em 0.
# O loop para quando 'i' chega ao limite OU quando o usuário decide encerrar.
i = 0
while i < qtd_eventos:
    print()
    linha(MAGENTA, "─")
    print(f"  {BOLD}{MAGENTA}  EVENTO {i + 1} DE {qtd_eventos}{RESET}")  # i ainda não foi incrementado aqui
    linha(MAGENTA, "─")

    # --- TIPO DE EVENTO ---
    # Exibe um menu numerado e só aceita as opções de 1 a 4.
    while True:
        print(f"\n  {CIANO}Selecione o tipo de evento:{RESET}")
        print(f"  {AMARELO}1{RESET} - Desmatamento")
        print(f"  {AMARELO}2{RESET} - Queimadas")
        print(f"  {AMARELO}3{RESET} - Variação Climática")
        print(f"  {AMARELO}4{RESET} - Uso do Solo")
        opcao_tipo = input(f"  {BOLD}Opção (1 a 4): {RESET}").strip()

        if opcao_tipo == '1':
            tipo = "Desmatamento"
            break
        elif opcao_tipo == '2':
            tipo = "Queimadas"
            break
        elif opcao_tipo == '3':
            tipo = "Variação Climática"
            break
        elif opcao_tipo == '4':
            tipo = "Uso do Solo"
            break
        else:
            print(f"  {VERMELHO}✗ Opção inválida. Digite um número de 1 a 4.{RESET}")

    # --- PAÍS ---
    # Recebe o nome do país como texto livre.
    pais = input(f"  {BOLD}País: {RESET}").strip()

    # --- REGIÃO ---
    # Exibe um menu com as 9 regiões disponíveis.
    # A lógica é a mesma do tipo: só aceita opções válidas.
    while True:
        print(f"\n  {CIANO}Selecione a região:{RESET}")
        print(f"  {AMARELO}1{RESET} - NORTE      {AMARELO}2{RESET} - NORDESTE   {AMARELO}3{RESET} - LESTE")
        print(f"  {AMARELO}4{RESET} - SUDESTE    {AMARELO}5{RESET} - SUL        {AMARELO}6{RESET} - SUDOESTE")
        print(f"  {AMARELO}7{RESET} - OESTE      {AMARELO}8{RESET} - NOROESTE   {AMARELO}9{RESET} - CENTRO")
        opcao_regiao = input(f"  {BOLD}Opção (1 a 9): {RESET}").strip()

        regioes_map = {
            '1': "NORTE",    '2': "NORDESTE", '3': "LESTE",
            '4': "SUDESTE",  '5': "SUL",      '6': "SUDOESTE",
            '7': "OESTE",    '8': "NOROESTE", '9': "CENTRO"
        }

        # Dicionários funcionam como uma tabela de consulta:
        # se a opção digitada existir no dicionário, pega o valor correspondente.
        if opcao_regiao in regioes_map:
            regiao = regioes_map[opcao_regiao]
            break
        else:
            print(f"  {VERMELHO}✗ Opção inválida. Digite um número de 1 a 9.{RESET}")

    # --- CIDADE ---
    cidade = input(f"  {BOLD}Cidade: {RESET}").strip()

    # --- ÁREA AFETADA ---
    # Usa 'float' para aceitar números decimais (ex: 123.5 km²).
    # O loop garante que a área seja sempre um número positivo.
    while True:
        try:
            area = float(input(f"  {BOLD}Área afetada (km²): {RESET}"))
            if area > 0:
                break
            print(f"  {VERMELHO}✗ A área deve ser maior que zero.{RESET}")
        except ValueError:
            print(f"  {VERMELHO}✗ Digite um número válido (ex: 150.5).{RESET}")

    # --- INTENSIDADE ---
    # Usa 'int' porque a escala é de números inteiros de 1 a 10.
    while True:
        try:
            intensidade = int(input(f"  {BOLD}Intensidade do impacto (1 a 10): {RESET}"))
            if 1 <= intensidade <= 10:
                break
            print(f"  {VERMELHO}✗ A intensidade deve estar entre 1 e 10.{RESET}")
        except ValueError:
            print(f"  {VERMELHO}✗ Digite um número inteiro válido.{RESET}")

    # --- NÚMERO DE OCORRÊNCIAS ---
    while True:
        try:
            ocorr = int(input(f"  {BOLD}Número de ocorrências detectadas: {RESET}"))
            if ocorr > 0:
                break
            print(f"  {VERMELHO}✗ O número de ocorrências deve ser maior que zero.{RESET}")
        except ValueError:
            print(f"  {VERMELHO}✗ Digite um número inteiro válido.{RESET}")

    # Adiciona (append) os dados validados ao final de cada lista.
    # A ordem de inserção é sempre a mesma, garantindo que o índice i
    # corresponda ao mesmo evento em todas as listas.
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(ocorr)

    # Avança o contador para o próximo evento.
    i += 1

    print(f"\n  {VERDE}✔ Evento {i} registrado com sucesso!{RESET}")

    # --- PERGUNTA DE CONTINUAÇÃO ---
    # Só aparece se ainda houver eventos restantes a registrar.
    # Isso evita a pergunta desnecessária após o último evento.
    eventos_restantes = qtd_eventos - i
    if eventos_restantes > 0:
        print(f"\n  {CIANO}Eventos registrados: {AMARELO}{i}{CIANO} | Restantes: {AMARELO}{eventos_restantes}{RESET}")
        while True:
            print(f"  {CIANO}Deseja registrar o próximo evento?{RESET}")
            print(f"  {AMARELO}1{RESET} - Sim, continuar")
            print(f"  {AMARELO}2{RESET} - Não, encerrar registro e gerar relatório")
            opcao_continuar = input(f"  {BOLD}Opção (1 ou 2): {RESET}").strip()

            if opcao_continuar == '1':
                # Usuário quer continuar: sai do while interno e volta ao loop principal.
                break
            elif opcao_continuar == '2':
                # Usuário quer parar: força o fim do loop principal
                # atribuindo a 'i' o valor limite, o que encerra o while externo.
                print(f"\n  {AMARELO}⚠ Registro encerrado pelo usuário com {i} evento(s).{RESET}")
                i = qtd_eventos
                break
            else:
                print(f"  {VERMELHO}✗ Opção inválida. Digite 1 para continuar ou 2 para encerrar.{RESET}")

# ==============================================================================
# 3. ANÁLISE DE DADOS
# ==============================================================================

# len() retorna o tamanho da lista, ou seja, o total de eventos registrados.
total_eventos = len(tipos_eventos)

# Percorre todas as posições das listas para acumular a soma das áreas
# e das intensidades em variáveis separadas.
soma_areas        = 0.0
soma_intensidades = 0.0
for i in range(total_eventos):
    soma_areas        += areas_afetadas[i]
    soma_intensidades += intensidades[i]

# Divide a soma pelo total para obter a média aritmética simples.
media_intensidade = soma_intensidades / total_eventos

# max() encontra o maior valor da lista.
# index() retorna a posição (índice) desse valor, para sabermos de qual evento se trata.
maior_area      = max(areas_afetadas)
idx_maior_area  = areas_afetadas.index(maior_area)

# Para descobrir a região com mais ocorrências, precisamos agrupar.
# regioes_unicas guarda cada região apenas uma vez (sem repetição).
# soma_ocorr_regiao guarda, na mesma posição, o total de ocorrências daquela região.
# Exemplo: se regioes_unicas[2] = "NORTE", então soma_ocorr_regiao[2] = total do NORTE.
regioes_unicas    = []
soma_ocorr_regiao = []

for i in range(total_eventos):
    regiao_atual = regioes[i]

    if regiao_atual not in regioes_unicas:
        # Região nova: adiciona à lista e registra as ocorrências pela primeira vez.
        regioes_unicas.append(regiao_atual)
        soma_ocorr_regiao.append(ocorrencias[i])
    else:
        # Região já existente: encontra onde ela está e soma as novas ocorrências.
        idx_reg = regioes_unicas.index(regiao_atual)
        soma_ocorr_regiao[idx_reg] += ocorrencias[i]

# Identifica a região com o maior total acumulado de ocorrências.
max_ocorr_regiao        = max(soma_ocorr_regiao)
idx_regiao_mais_afetada = soma_ocorr_regiao.index(max_ocorr_regiao)
regiao_campea           = regioes_unicas[idx_regiao_mais_afetada]

# Soma todas as ocorrências de todos os eventos para calcular a densidade.
soma_total_ocorrencias = 0
for ocorr in ocorrencias:
    soma_total_ocorrencias += ocorr

# Densidade = total de ocorrências ÷ área total.
# O 'if ... else 0' evita divisão por zero caso a soma das áreas seja 0.
densidade_media = soma_total_ocorrencias / soma_areas if soma_areas > 0 else 0

# Conta quantos eventos individuais têm intensidade acima da média calculada.
eventos_acima_da_media = 0
for i in range(total_eventos):
    if intensidades[i] > media_intensidade:
        eventos_acima_da_media += 1

# Identifica o evento mais crítico:
# - Prioridade 1: maior intensidade.
# - Prioridade 2 (desempate): maior área afetada.
# Começa assumindo que o primeiro evento (índice 0) é o mais crítico,
# depois compara com todos os outros.
idx_critico = 0
for i in range(1, total_eventos):
    if intensidades[i] > intensidades[idx_critico]:
        idx_critico = i
    elif intensidades[i] == intensidades[idx_critico]:
        if areas_afetadas[i] > areas_afetadas[idx_critico]:
            idx_critico = i

# ==============================================================================
# 4. RELATÓRIO DE RESULTADOS
# ==============================================================================

print()
print()
cabecalho("  RELATÓRIO DE ANÁLISE AMBIENTAL", VERDE)

secao("Resumo Geral", VERDE)
item("Total de eventos registrados", total_eventos)
item("Área total afetada",           f"{soma_areas:.0f} km²")
item("Média de intensidade",         f"{media_intensidade:.1f} / 10")

secao("Análises", CIANO)
item("Região com maior nº de ocorrências",     regiao_campea)
item("Eventos acima da média de intensidade",  eventos_acima_da_media)
item("Densidade média de ocorrências",         f"{densidade_media:.2f} ocorrências/km²")
item("Evento com maior área afetada",
     f"{tipos_eventos[idx_maior_area]} em {cidades[idx_maior_area]} ({maior_area:.0f} km²)")

secao("Evento Mais Crítico", VERMELHO)
item("Tipo",          tipos_eventos[idx_critico],  cor_valor=VERMELHO)
item("Local",         f"{cidades[idx_critico]}, {regioes[idx_critico]}, {paises[idx_critico]}", cor_valor=VERMELHO)
item("Intensidade",   f"{intensidades[idx_critico]} / 10",   cor_valor=VERMELHO)
item("Área afetada",  f"{areas_afetadas[idx_critico]:.0f} km²", cor_valor=VERMELHO)

print()
linha(VERDE)
print(f"  {BOLD}{VERDE}Total de desastres registrados: {total_eventos}{RESET}")
linha(VERDE)
print()
 