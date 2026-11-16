nome = ["Notebook Pro", "Mouse Gamer", "Cadeira Ergonômica", "Monitor 27 pol",
"Teclado Mecânico", "Headset USB", "Webcam Full HD", "Mesa em L",
"SSD 1TB", "Caixa de Som", "Mousepad XXL", "Suporte Monitor"]

categorias = ["Computadores", "Periféricos", "Móveis", "Computadores",
"Periféricos", "Áudio e Vídeo", "Áudio e Vídeo", "Móveis",
"Computadores", "Áudio e Vídeo", "Periféricos", "Móveis"]

faturados = [7200.0, 450.0, 1890.0, 2300.0, 620.0, 380.0,
540.0, 1450.0, 690.0, 760.0, 120.0, 310.0]

custos = [5900.0, 280.0, 2050.0, 1750.0, 410.0, 395.0,
360.0, 980.0, 720.0, 470.0, 45.0, 330.0]
campos = ['produto', 'categoria', 'faturamento', 'custo']

vendas = [
    dict(zip(campos, linha))
    for linha in zip(nome, categorias, faturados, custos, strict=True)
]

lucrativos = [venda for venda in vendas if venda["faturamento"]> venda["custo"]]
segmentos = {venda["categoria"] for venda in vendas}
por_segmento = {
    segmento: sum(venda["faturamento"] for venda in vendas if venda["categoria"] == segmento)
    for segmento in sorted(segmentos)
}

lideres = {
    segmento:
    max(
        (venda for venda in vendas if venda["categoria"] == segmento),
        key=lambda venda: venda["faturamento"]
    )["produto"]
    for segmento in sorted(segmentos)
}

faturamento_total = sum(faturados)

ticket = faturamento_total/len(vendas)

custo_total = sum(custos)

lucro = faturamento_total - custo_total

margem = lucro / faturamento_total * 100

vendas_ordenadas = sorted(vendas, key=lambda venda: venda['faturamento'] - venda['custo'], reverse=True)

top_3 = vendas_ordenadas[:3]

for venda in top_3:
    lucro_produto = venda["faturamento"] - venda["custo"]
    print(f"Produto: {venda['produto']} |  Lucro: R${lucro_produto:.2f}")

print('='*40)
print("PIPELINE ANALÍTICO DE VENDAS")
print('='*40)

print("1.INDICADORES GERAIS")
print(f"{'Quantidade de vendas':<25} > {len(vendas)}")
print(f"{'Vendas lucrativas':<25} > {len(lucrativos)}")
print(f"{'Faturamento total':<25} > R$ {faturamento_total:.2f}")
print(f"{'Ticket médio':<25} > R$ {ticket:.2f}")
print(f"{'Custo total':<25} > R$ {custo_total:.2f}")
print(f"{'Lucro':<25} > R$ {lucro:.2f}")
print(f"{'Margem líquida':<25} > {margem:.2f}%")

print('='*40)

print('='*40)
print("     FATURAMENTO POR CATEGORIA")
print('='*40)

for categoria, faturamento in por_segmento.items():
    print(f"{categoria:<25} > R${faturamento:.2f}")
print('='*40)

print('='*40)
print("     PRODUTO LÍDER POR CATEGORIA")
print('='*40)

for categoria, produto in lideres.items():
    print(f"{categoria:<25} > {produto}")

print('='*40)

print('='*40)
print("     TOP 3 PRODUTOS MAIS LUCRATIVOS")
print('='*40)

for venda in top_3:
    lucro_produto = venda['faturamento'] - venda['custo']
    print(f"{venda['produto']:<25} > R$ {lucro_produto:.2f}")

print("=" * 40)







