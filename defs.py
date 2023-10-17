import valida
import datetime
import os
from time import sleep

def limpaTerminal():              
    return os.system('cls' if os.name == 'nt' else 'clear')
    
def criaBarra():                  # Criar barras para estilo
    return print('-' * 32)
    
data = datetime.datetime.now()    # Atualização data diária para def relatorio()
dia = data.day
mes = data.month
ano = data.year

def menu():
    print('======= <<< ''\033[1;96m''SalesForce''\033[0;0m'' >>> =======')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente       |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Cliente        |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Mostrar Clientes        |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatório         |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                    |')
    print('--------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('--------------------------------')
    return x


'''def de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins'''
def cadastro():
    limpaTerminal()
    print('==== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > =====')
    nome  = valida.Nome()    # Retorna o nome validado
    login = valida.Login()   # Retorna o login validado
    
    # --> Conferir se já existe o login cadastrado
    lerlogins = open('logins.txt', 'r')
    for linha in lerlogins.readlines():    # Ler linhas do arquivo logins.txt
        
        valores = linha.split('-')
        #--> Cria lista com valores da linha 
        # Nome: Vitor -Login: vitim --> ['Nome: Vitor','Login: vitim'...]
        
        if login == valores[1].split(':')[1].strip():  
        # Confere se login cadastrado é igual login da linha
        
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Login já existente!''\033[0;0m')    
            criaBarra()
            return                         # return para parar a funçao e não cadastrar
    lerlogins.close()
    
    senha = valida.Senha()   # Retorna a senha validada
    email = valida.Email()   # Retorna o email validado
    data  = valida.Data()    # Retorna a data validada
    tele  = valida.tele()    # Retorna o telefone validado
    ender = valida.ender()   # Retorna o endereco validado em um discinario 
    
    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Cliente Cadastrado com sucesso!''\033[0;0m')
    criaBarra()
            
    # --> Adiciona dados no banco de dados login.txt
    logins = open("logins.txt", 'a')
    logins.write(f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Data de Nascimento: {data} -Numero de celular: {tele} -Endereco:{ender} \n')
    logins.close()
    return 

'''Logar um usuário e printar seus dados cadastrados'''
def mostraDados():
    
    limpaTerminal() 
    print('==== << ''\033[1;33m''Dados do Cliente''\033[0;0m'' >> ====')
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0;0m')
    criaBarra()
    
    userlogin = input('Login: ')       
    usersenha = input('Senha: ')      
            
    valida = False                     # Variavel de validação do login
    logins = open('logins.txt', 'r')   
    for linha in logins.readlines():   # Percorre cada linha do logins.txt
        valores = linha.split('-')
        if userlogin == valores[1].split(':')[1].strip() and usersenha in valores[2].split(':')[1].strip():
            
            # Checa se login e senha são iguais no Logim e Senha da linha
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Cliente Logado! Dados do usuário: ''\033[0;0m')
            criaBarra()                
            
            for percorre in range(len(valores)):  
            #for no range do tamanho da lista criada
                
                if valores[percorre].split(':')[0] == 'Endereco': 
                # ['Nome: Vitor','Login: vitim',...,'Endereco: {}']
                # [['Nome','Vitor'],['Login', 'vitim'],...,['Endereco', '{}']]
                    
                    dictEndereco = eval(valores[percorre].split('Endereco:')[1])
                    # ['Nome: Vitor -Login: vitim ...','{}']
                    
                    for chave in dictEndereco:
                        print(f'{chave}: {dictEndereco[chave]}')
                        sleep(0.2)
                
                else:
                    print(valores[percorre])
                    sleep(0.2)
            
            criaBarra()
            valida = True    # valida o login e break
            logins.close()
            break
    
    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha inválidos''\033[0;0m')  #Não achou login and senha
        criaBarra()


'''def para exibir todos os clientes ja cadastrados'''        
def clientesCadastrados():
    limpaTerminal()
    print('===== Clientes Cadastrados =====')
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():    
        # Ler cada linhas
        l = linha.split('-')            
        # Divide no '-' e forma uma lista com os valores divididos
        print('\033[1;92m'f'{l[0]} | {l[1]}''\033[0;0m') 
        # printa primeiros indices --> Nome: nome | Login: login
    criaBarra()
    return 


'''def para criar relatorio conforme exemplo pedido'''
def relatorio():
    
    countClient = 0    # variavel para contar o numero de clientes
    nomess = []        # lista para armazenar nomes dos clientes
    
    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')              
        nomess.append(l[0])      # Adiciona o primeiro valor (no caso 'Nome: nome') na lista          
        countClient += 1         # conta um cliente
     
    limpaTerminal()                      
    arquivo = open("dados.txt", "w+")             # "w+" para criar o relatorio 
    arquivo.write('Relatorio de Clientes \n')
    arquivo.write('\n')
    arquivo.write(f'A loja SalesForce possui {countClient} cliente(s) \n')
    
    for i in range(len(nomess)):                # for range para percorrer os idices da lista nomess
        arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))    # printa cada indice da lista 
    arquivo.write(f'Russas, {dia}/{mes}/{ano}.')  # data atualizada para o relatorio gerado
    criaBarra()
    print('\033[1;32m'"Relatorio gerado em 'dados.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return 