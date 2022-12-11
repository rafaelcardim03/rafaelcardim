import telebot
import pandas as pd
from datetime import date

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)
data_em_texto = data_atual.strftime('%d/%m/%Y')
#print(data_em_texto)





#estrutura para leitura das planilhas
programacao = pd.read_excel("dhl.xlsx", sheet_name="BASE",usecols=[8])
soma_programacao = int(programacao.sum())
#print(soma_programacao)

separacao = pd.read_excel("separacao.xlsx", sheet_name="Planilha1", usecols=[1])
total_separado = int(separacao.sum())

percentual = int(total_separado / soma_programacao * 100)
#print(total_separado)
#print(percentual)

 #= ('Olá, a programação é de', soma_programacao, 'no momento temos um total de', total_separado, '-' , percentual, '%')

#================================= // #######################################################################################

#estrutura do bot
CHAVE_API = 


bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["programacaodhl"])
def programacaodhl(mensagem):
    bot.send_message(mensagem.chat.id, f"Olá, o total da programação é de {soma_programacao} volumes.")

@bot.message_handler(commands=["status"])
def status(mensagem):
    bot.send_message(mensagem.chat.id, f"Olá, no momento temos um total de {total_separado} volumes separados, que representa {percentual}% da programação.")

@bot.message_handler(commands=["DHL"])
def DHL(mensagem):
    texto = f"""
    O que você quer? (Clique em uma opção)
    /programacaodhl Programação DHL (atualizada {data_em_texto})
    /status Status da Operação
    """
    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /DHL"""
    bot.reply_to(mensagem, texto)

bot.polling()
