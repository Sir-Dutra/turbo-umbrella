import requests
def retorno_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['bairro'])
    return dados_cep

if __name__ == '__main__':
    x = input("digite o cep:  ")
    retorno_cep(x)

