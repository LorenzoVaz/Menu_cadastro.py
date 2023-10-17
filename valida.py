import defs

def Nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome valido.')
                break
        else:
            return nome.strip(' ')
                     
def Senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Error! Entrada vazia.')
            continue
        return senha.strip(' ')

def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Error! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido! Deve conter "@" e ".com"')
        
def Data():
    while True:  
        data = input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print('Error! Entrada inválida.')
            continue        
        temp = ''.join(data.split('/'))      # retorna uma string de valores sem '/'
        if not temp.isnumeric():             # analisa se essa string tem caracteres
            print('Insira uma data válida')
            continue
        # data.count('/') retorna o numero de '/' na data
        if data.count('/') == 2 and data != '//':   # Checa se data tem duas '/' e não é apenas //
            dia, mes, ano = data.split('/')  # cada valor divido é jogado nas variaveis em sequencia
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
                return data.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaaa')   
                            
def Login():
    while True:
        login = input('Login: ')
        if login == '':
            print('Error! Entrada vazia.')
            continue
        return login.strip(' ')
        
def tele():
    while True:
        tele = input('Telefone (Apenas Números): ')
        if tele == '':
            print('Error! Entrada vazia.')
            continue
        elif not tele.isnumeric():
            print('Insira apenas números.')
            continue   
        else:
            if 9 <= len(tele) <= 11:
                return tele
            else:
                print('O número deve ter entre 9 - 11 caracteres.')

def ender(): 
    while True:
        print('=== < ''\033[1;32m''Seu Endereço Completo!''\033[0;0m'' > ===')
        dados = {
            'Rua': input('Rua: '),
            'Numero': input('Numero: '),
            'Complemento': input('Complemento: '),
            'Bairro': input('Bairro: '),
            'CEP': input('CEP: '),
            'Cidade': input('Cidade: '),
            'Referencia': input('Referencia: '),
        }   

        return dados
    