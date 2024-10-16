# r - Leitura
# w - Escrita e substitui o conteudo existente
# x - Escrita em arquivos novos
# a - Escrita inserindo novos dados sem alterar ou excluir os existentes

def arquivo_escrita():
    empregados_file = open('empregados.txt', 'a')
    linhas = list()
    linhas.append('Teste linha 1\n')
    linhas.append('Teste linha 2\n')
    empregados_file.writelines(linhas)
    empregados_file.close()

def leitura_arquivo():
    empregados_file = open('empregados.txt', 'r')
    print(empregados_file.readable())
    print(empregados_file.read())
    empregados_file.close()

leitura_arquivo()