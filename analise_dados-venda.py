# Carregar Dados: A aplicação deve ser capaz de carregar dados de vendas de arquivos .csv. Os dados podem incluir informações como ID do produto, nome do produto, quantidade vendida, preço do produto, data da venda, etc.

# Limpeza de Dados: A aplicação deve ser capaz de limpar os dados, lidando com valores ausentes, removendo duplicatas, etc.

# Análise de Dados: A aplicação deve ser capaz de realizar várias análises nos dados, como vendas totais, vendas por produto, vendas por mês, etc. Deve ser capaz de gerar insights úteis a partir dos dados.

# Visualização de Dados: A aplicação deve ser capaz de visualizar os resultados da análise de dados usando gráficos e tabelas. Isso pode incluir gráficos de barras, gráficos de linhas, histogramas, etc.

# Exportar Resultados: Por fim, a aplicação deve ser capaz de exportar os resultados da análise de dados para um formato facilmente legível, como um novo arquivo .csv ou um relatório em PDF.

import pandas as pd
import matplotlib.pyplot as plt
import colorama

colorama.init()

while True:
  try:
    tabela = pd.read_csv(caminho_arquivo)
    break
  except:
    caminho_arquivo = input("Caminho do Arquivo: ")

vendas = tabela["Quantidade Vendida"]
relatorio = pd.DataFrame({"Vendas Totais": [vendas.sum()], "Vendas Médias": [vendas.mean()], "Venda Máxima": [vendas.max()] ,"Venda Mínima": [vendas.min()]})
tabela.plot(x="Data da Venda", y="Quantidade Vendida")

tabela_resposta = str()
graficos_resposta = str()
exportar_resposta = str()

def solicitar_acao(mensagem : str, acao):
  resposta = str()
  while resposta not in ["S", "N"]:
    resposta = input(colorama.Style.RESET_ALL + mensagem).upper()
    if resposta == "S":
      acao()

solicitar_acao("Deseja visualizar a tabela? (S/N) ", lambda: (print(colorama.Fore.BLUE + tabela.to_string()),print(colorama.Fore.BLUE + relatorio.to_string())))
solicitar_acao("Deseja visualizar o gráfico? (S/N) ", lambda: plt.show())
solicitar_acao("Deseja exportar o relatório? (S/N) ", lambda: (relatorio.to_csv("relatorio.csv", index=False),print(colorama.Fore.GREEN + "Relatório exportado com sucesso")))