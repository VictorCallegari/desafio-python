investimentos = [
    {"Opção": 1, "Descrição": "Ampliação da capacidade do armazém ZDP em 5%", "Custo": 470000, "Retorno": 410000, "Risco": "Baixo"},
    {"Opção": 2, "Descrição": "Ampliação da capacidade do armazém MGL em 7%", "Custo": 400000, "Retorno": 330000, "Risco": "Baixo"},
    {"Opção": 3, "Descrição": "Compra de empilhadeira", "Custo": 170000, "Retorno": 140000, "Risco": "Médio"},
    {"Opção": 4, "Descrição": "Projeto de P&D I", "Custo": 270000, "Retorno": 250000, "Risco": "Médio"},
    {"Opção": 5, "Descrição": "Projeto de P&D II", "Custo": 340000, "Retorno": 320000, "Risco": "Médio"},
    {"Opção": 6, "Descrição": "Aquisição de novos equipamentos", "Custo": 230000, "Retorno": 320000, "Risco": "Médio"},
    {"Opção": 7, "Descrição": "Capacitação de funcionários", "Custo": 50000, "Retorno": 90000, "Risco": "Médio"},
    {"Opção": 8, "Descrição": "Ampliação da estrutura de carga rodoviária", "Custo": 440000, "Retorno": 190000, "Risco": "Alto"},
    {"Opção": 9, "Descrição": "Construção de datacenter", "Custo": 320000, "Retorno": 120000, "Risco": "Alto"},
    {"Opção": 10, "Descrição": "Aquisição de empresa concorrente", "Custo": 800000, "Retorno": 450000, "Risco": "Alto"},
    {"Opção": 11, "Descrição": "Compra de serviços em nuvem", "Custo": 120000, "Retorno": 80000, "Risco": "Baixo"},
    {"Opção": 12, "Descrição": "Criação de aplicativo mobile e desktop", "Custo": 150000, "Retorno": 120000, "Risco": "Baixo"},
    {"Opção": 13, "Descrição": "Terceirizar serviço de otimização da logística", "Custo": 300000, "Retorno": 380000, "Risco": "Médio"}
]

teto_custo = {
    "Baixo": 1200000,
    "Médio": 1500000,
    "Alto": 900000
}

teto_minimo = {
    "Baixo": 2,
    "Médio": 2,
    "Alto": 1
}

capital_disponivel = 2400000

# Função para calcular o retorno total de uma solução
def calcular_retorno_total(sol):
    retorno_total = 0
    for i in range(len(investimentos)):
        if sol[i] == 1:
            retorno_total += investimentos[i]["Retorno"]
    return retorno_total

# Função para verificar se uma solução atende às restrições
def verificar_restricoes(sol):
    categorias = {"Baixo": 0, "Médio": 0, "Alto": 0}
    total_selecionado = 0
    for i in range(len(investimentos)):
        if sol[i] == 1:
            categorias[investimentos[i]["Risco"]] += 1
            total_selecionado += 1
    for risco in categorias:
        if categorias[risco] < teto_minimo[risco]:
            return False
        custo_total = sum(investimentos[i]["Custo"] for i in range(len(investimentos)) if sol[i] == 1 and investimentos[i]["Risco"] == risco)
        if custo_total > teto_custo[risco]:
            return False
    custo_total = sum(investimentos[i]["Custo"] for i in range(len(investimentos)) if sol[i] == 1)
    if custo_total > capital_disponivel:
        return False
    return total_selecionado == 5

# Função para gerar todas as combinações de soluções possíveis
def gerar_solucoes():
    solucoes = []
    for i in range(2**len(investimentos)):
        sol = [int(x) for x in bin(i)[2:].zfill(len(investimentos))]
        if verificar_restricoes(sol):
            solucoes.append(sol)
    return solucoes

# Encontrar a solução ótima
solucoes_possiveis = gerar_solucoes()
melhor_solucao = max(solucoes_possiveis, key=calcular_retorno_total)

# Imprimir a solução ótima
print("Retorno total esperado: R$", calcular_retorno_total(melhor_solucao))
print("Projetos selecionados:")
for i in range(len(investimentos)):
    if melhor_solucao[i] == 1:
        print(f"Opção {investimentos[i]['Opção']}: {investimentos[i]['Descrição']}")

