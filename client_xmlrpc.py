import xmlrpc.client
import socket

conexao = xmlrpc.client.ServerProxy("http://localhost:8000/")

valor_inicial = float(input("Digite o valor do investimento inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): "))
periodo_meses = int(input("Digite a quantidade de parcelas: "))

resposta = conexao.juros_compostos(valor_inicial, taxa_juros, periodo_meses)

print(f"Montante final: R$ {resposta['montante_final']}")
print(f"Total de juros: R$ {resposta['juros_totais']}")
print("\nEvolução dos juros acumulados:")
for mes, valor in resposta['historico_juros'].items():
    print(f"{mes}: R$ {valor}")

print(f"\nTempo de processamento no servidor: {resposta['duracao']} segundos")

ip_local = socket.gethostbyname(socket.gethostname())
print(f"IP do cliente: {ip_local}")
