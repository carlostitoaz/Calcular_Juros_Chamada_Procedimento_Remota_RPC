from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import time

class ManipuladorRequisicao(SimpleXMLRPCRequestHandler):
    def log_request(self, code='-', size='-'):
        ip_cliente = self.client_address[0]
        print(f"Nova conexão com o cliente de IP: {ip_cliente}")

def juros_compostos(valor, taxa_percentual, quantidade_meses):
    inicio_proc = time.time()
    taxa_decimal = taxa_percentual / 100
    saldo = valor
    historico_juros = {}

    for mes in range(1, quantidade_meses + 1):
        saldo *= (1 + taxa_decimal)
        juros_mes = saldo - valor
        historico_juros[f"Mês {mes}"] = round(juros_mes, 2)

    juros_totais = round(saldo - valor, 2)
    montante_final = round(saldo, 2)
    fim_proc = time.time()
    duracao = round(fim_proc - inicio_proc, 6)

    return {
        "montante_final": montante_final,
        "juros_totais": juros_totais,
        "historico_juros": historico_juros,
        "duracao": duracao
    }

servidor_rpc = SimpleXMLRPCServer(("localhost", 8000), requestHandler=ManipuladorRequisicao, allow_none=True)
print("Servidor ativo e aguardando conexões na porta 8000...")
servidor_rpc.register_function(juros_compostos, "juros_compostos")
servidor_rpc.serve_forever()
