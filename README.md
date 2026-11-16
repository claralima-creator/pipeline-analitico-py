#  Pipeline Analítico de Vendas e BI

Projeto desenvolvido em Python com o objetivo de praticar a organização, transformação e análise de dados de vendas, simulando um pequeno pipeline analítico de Business Intelligence (BI).

##  Objetivo

Transformar dados de vendas em informações úteis para análise de desempenho, identificando produtos lucrativos, categorias, indicadores financeiros e os produtos com maior lucro.

##  Tecnologias e conceitos utilizados

- **Python 3**
- `zip()` e `dict()` para estruturar os dados
- List Comprehension para filtrar vendas lucrativas
- Set Comprehension para identificar categorias únicas
- Dict Comprehension para agrupar faturamento por categoria
- Generator Expression para otimizar a busca dos produtos líderes
- `lambda` e `max()` para identificar produtos com maior faturamento
- `sum()` para calcular indicadores financeiros
- `sorted()` para classificar os produtos por lucro
- F-Strings para formatar o relatório final

## ⚙️ Funcionalidades

O pipeline realiza:

1. Organização de 12 registros de vendas em uma lista de dicionários.
2. Identificação das vendas lucrativas.
3. Identificação das categorias existentes.
4. Cálculo do faturamento por categoria.
5. Identificação do produto líder de cada categoria.
6. Cálculo dos indicadores gerais.
7. Classificação dos três produtos com maior lucro.
8. Geração de um relatório analítico no terminal.

##  Resultados da análise

| Indicador | Resultado |
|---|---:|
| Quantidade de vendas | 12 |
| Vendas lucrativas | 8 |
| Faturamento total | R$ 16.710,00 |
| Custo total | R$ 13.690,00 |
| Lucro total | R$ 3.020,00 |
| Ticket médio | R$ 1.392,50 |
| Margem líquida | 18,07% |

###  Top 3 produtos por lucro

| Produto | Lucro |
|---|---:|
| Notebook Pro | R$ 1.300,00 |
| Monitor 27 pol | R$ 550,00 |
| Mesa em L | R$ 470,00 |

##  Como executar

1. Tenha o Python instalado.
2. Clone este repositório ou baixe os arquivos.
3. Abra a pasta do projeto no VS Code.
4. Execute o arquivo Python:

```bash
python projeto.py
```

## Aprendizados

Este projeto foi uma oportunidade de consolidar conceitos fundamentais de Python e compreender como diferentes estruturas da linguagem podem trabalhar juntas para transformar dados em informações relevantes.

Também foi possível praticar raciocínio lógico, manipulação de listas e dicionários, expressões geradoras e cálculos aplicados a um cenário de negócios.

## Próximos passos

- Criar análises considerando apenas vendas lucrativas.
- Explorar novas métricas de desempenho.
- Evoluir o projeto com visualizações de dados.

---

**Projeto desenvolvido como parte dos meus estudos em Python e análise de dados.**
