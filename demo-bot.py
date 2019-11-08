#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#
# THIS EXAMPLE HAS BEEN UPDATED TO WORK WITH THE BETA VERSION 12 OF PYTHON-TELEGRAM-BOT.
# If you're still using version 11.1.0, please see the examples at
# https://github.com/python-telegram-bot/python-telegram-bot/tree/v11.1.0/examples

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Hola bienvenido al bot de ayuda para el cáncer de mama, ¿cuál es tu duda? Elige uno de los siguientes comandos /concepto,/sintomas,/recomendaciones')


def concepto(update, context):
    update.message.reply_text("El cáncer de mama es una enfermedad en la cual las células de la mama se multiplican sin control. Existen distintos tipos de cáncer de mama. El tipo de cáncer de mama depende de qué células de la mama se vuelven cancerosas")
    update.message.reply_text("¿Quieres ver los tipos de cancer?")

   
def sintomas(update, context):
    update.message.reply_text("Los signos de advertencia del cáncer de mama pueden ser distintos en cada persona. Algunas personas no tienen ningún tipo de signos o síntomas.")
    update.message.reply_text("Algunas señales de advertencia del cáncer de mama son:")
    update.message.reply_text("1. Aumento del grosor o hinchazón de una parte de la mama")
    update.message.reply_text("2. Irritación o hundimientos en la piel de la mama")
    update.message.reply_text("3. Hundimiento del pezón o dolor epn esa zona")
    update.message.reply_text("4. Secreción del pezón, que no sea leche, incluso de sangre")
    update.message.reply_text("5. Dolor en cualquier parte de la mama")

def recomendaciones(update, context):
     update.message.reply_text("Para la lucha contra el cáncer de mama es recomendable la "+
     "prolongación de la lactancia materna más allá de los seis meses e incluso por encima del año,seguir una alimentación variada y equilibrada bajo el patrón de la dieta mediterránea"+
     "mantener un peso saludable, evitar el sobrepeso y la obesidad,prescindir del consumo de alcohol,evitar la terapia hormonal sustitutiva de la menopausia. ")


def tipos(update, context):
     
     if(update.message.text == "SI" or update.message.text =="si" or update.message.text =="Si"):
            update.message.reply_text("Los tipos más comunes de cáncer de mama son: Carcinoma ductal infiltrante y Carcinoma lobulillar infiltrante")
            update.message.reply_text("Elije un tipo /ductal ó /lobulillar")

def ductal(update, context):
    update.message.reply_text("Las células cancerosas se multiplican fuera de los conductos e invaden otras partes del tejido mamario. Estas células cancerosas invasoras también pueden diseminarse, o formar metástasis, en otras partes del cuerpo")

def lobulillar(update, context):
    update.message.reply_text("Las células cancerosas se diseminan de los lobulillos a los tejidos mamarios cercanos. Estas células cancerosas invasoras también pueden diseminarse a otras partes del cuerpo.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1055151698:AAGrlRXwnKp4Mwhg_sYxesrMigItwCKIp4A", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sintomas", sintomas))
    dp.add_handler(CommandHandler("recomendaciones", recomendaciones))
    dp.add_handler(CommandHandler("concepto", concepto))
    dp.add_handler(CommandHandler("ductal", ductal))
    dp.add_handler(CommandHandler("lobulillar", lobulillar))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, tipos))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()