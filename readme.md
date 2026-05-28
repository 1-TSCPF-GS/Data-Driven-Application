# 🛰️ Sistema de Monitoramento Espacial Ambiental

> Ferramenta de linha de comando para registro, análise e relatório de eventos ambientais detectados via satélite — desenvolvida como parte da **Global Solution 2026** da FIAP.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Como Usar](#como-usar)
- [Estrutura do Código](#estrutura-do-código)
- [Exemplo de Uso](#exemplo-de-uso)
- [Integrantes](#integrantes)

---

## Sobre o Projeto

O **Sistema de Monitoramento Espacial Ambiental** simula o processamento de dados coletados pelo satélite fictício **FIAP-ENV-01**, com cobertura sobre o território brasileiro.

O sistema permite registrar múltiplos eventos ambientais — como desmatamento, queimadas e variações climáticas — validar as informações inseridas, e gerar automaticamente um relatório analítico com os principais indicadores.

---

## Funcionalidades

- ✅ Registro de múltiplos eventos ambientais com validação completa de entrada
- ✅ Seleção guiada por menus numerados (tipo de evento, região)
- ✅ Possibilidade de encerrar o registro antes do limite informado
- ✅ Cálculo automático de métricas:
  - Área total afetada
  - Média de intensidade
  - Região com maior número de ocorrências
  - Densidade média de ocorrências por km²
  - Evento mais crítico (por intensidade e área)
- ✅ Relatório final colorido e formatado no terminal

---

## Pré-requisitos

- **Python 3.8** ou superior
- Terminal com suporte a **cores ANSI** (padrão no Linux, macOS e Windows Terminal)

Verifique sua versão do Python:

```bash
python --version
```

Nenhuma biblioteca externa é necessária. O projeto usa apenas recursos nativos do Python.

---

## Como Executar

**1. Clone ou baixe o repositório:**

```bash
git clone https://github.com/1-TSCPF-GS/Data-Driven-Application.git
cd Data-Driven-Application

```

**2. Execute o arquivo principal:**

```bash
python 26.1.GS.monitoramento.py
```

> 💡 Em alguns sistemas, pode ser necessário usar `python3` no lugar de `python`.

---

## Como Usar

Ao iniciar o programa, siga as instruções exibidas no terminal:

### Passo 1 — Quantidade de eventos

Informe quantos eventos deseja registrar. O valor deve ser um número inteiro maior que zero.

```
  Insira a quantidade de eventos a registrar: 3
```

### Passo 2 — Registro de cada evento

Para cada evento, o sistema solicitará:

| Campo | Tipo | Restrições |
|---|---|---|
| Tipo de evento | Menu (1 a 4) | Desmatamento, Queimadas, Variação Climática, Uso do Solo |
| País | Texto livre | — |
| Região | Menu (1 a 9) | Norte, Nordeste, Leste, Sudeste, Sul, Sudoeste, Oeste, Noroeste, Centro |
| Cidade | Texto livre | — |
| Área afetada | Número decimal | Deve ser maior que zero (ex: `150.5`) |
| Intensidade | Número inteiro | Entre 1 e 10 |
| Ocorrências | Número inteiro | Deve ser maior que zero |

### Passo 3 — Continuar ou encerrar

Após cada evento registrado, o sistema pergunta se deseja continuar ou gerar o relatório antecipadamente:

```
  1 - Sim, continuar
  2 - Não, encerrar registro e gerar relatório
```

### Passo 4 — Relatório

Ao final, o sistema exibe automaticamente o **Relatório de Análise Ambiental** com todas as métricas calculadas.

---

## Estrutura do Código

```
26.1.GS.monitoramento.py
│
├── Configuração de cores ANSI
├── Funções auxiliares de exibição
│   ├── linha()       → linha decorativa
│   ├── cabecalho()   → bloco de título
│   ├── secao()       → título de seção
│   └── item()        → linha rotulo: valor
│
├── Inicialização das listas de armazenamento
│
├── [1] Entrada de Dados
│   ├── Validação da quantidade de eventos
│   └── Loop de registro por evento
│       ├── Tipo, País, Região, Cidade
│       ├── Área afetada, Intensidade, Ocorrências
│       └── Opção de encerramento antecipado
│
├── [3] Análise de Dados
│   ├── Totais e médias
│   ├── Agrupamento por região
│   ├── Densidade de ocorrências
│   └── Identificação do evento mais crítico
│
└── [4] Relatório de Resultados
    ├── Resumo Geral
    ├── Análises
    └── Evento Mais Crítico
```

---

## Exemplo de Uso

```
══════════════════════════════════════════════════════════
    SISTEMA DE MONITORAMENTO ESPACIAL AMBIENTAL
  Satélite: FIAP-ENV-01  |  Cobertura: Brasil
══════════════════════════════════════════════════════════

  Insira a quantidade de eventos a registrar: 2

────────────────────────────────────────────────────────
    EVENTO 1 DE 2
────────────────────────────────────────────────────────

  Selecione o tipo de evento:
  1 - Desmatamento
  ...

══════════════════════════════════════════════════════════
    RELATÓRIO DE ANÁLISE AMBIENTAL
══════════════════════════════════════════════════════════

  ▸ Resumo Geral
  ──────────────────────────────────────────────────────
  Total de eventos registrados: 2
  Área total afetada: 430 km²
  Média de intensidade: 7.5 / 10
```

---

## Integrantes

Projeto desenvolvido para a **1ª Global Solution 2026** — FIAP  
Disciplina: *Data Driven Application & Data Science*

| Nome | RM |
|---|---|
| Gabrielle Trindade Ferreira  | 569092 |
| Halen Zhang | 569733 |
| João Marcos Borba Rodrigues Gonçalves | 571021 |

---

<p align="center">
  Desenvolvido com 🛰️ por DataSquad · FIAP 2026
</p>