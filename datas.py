from datetime import date, time, datetime, timedelta
'''
trabalhando o uso de data e hora atuais, interessante para uso com logs
'''
def exemplos_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))#Y maiusculo para ano compelto ex:2022


def exemplos_time():
    horario=  time(hour= 15, minute= 18, second=30)
    print(horario.strftime('%H:%M:%S'))

def exemplos_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.day)
    print(data_atual.strftime('%m/%y'))
    print(data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2010, 5, 5,)
    print(data_criada)
    nova_data = data_criada - timedelta(days=365, hours=2)
    print(nova_data)

if __name__ == '__main__':
    exemplos_date()
    exemplos_time()
    exemplos_datetime()

