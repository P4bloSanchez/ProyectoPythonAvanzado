from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler, MessageHandler,filters,ContextTypes
import TokenBererniz

TOKEN : Final = TokenBererniz.token
BOT_USERNAME: Final = '@Bererniz_bot'

async def start_command(update, context):
	await update.message.reply_text('Hola, como estas? Espero que bien' +
            '\nPara sumar: /sumar\nPara restar: /restar' +
            '\nPara multiplicar: /multi\nPara dividir: /dividir' +
            'Si necesita ayuda: /help')

async def sumar(update, context):
    try:
        nums = [float(num) for num in context.args]
        resultado = sum(nums)
        await update.message.reply_text(f'La suma es: {resultado}')
    except ValueError:
        update.message.reply_text('Ingrese otros numeros por favor.')

async def restar(update, context):
    try:
        nums = [float(num) for num in context.args]
        resultado = nums[0] - sum(nums[1:])
        await update.message.reply_text(f'La resta es: {resultado}')
    except ValueError:
        await update.message.reply_text('Ingrese otros numeros por favor.')

async def multiplicar(update, context):
    try:
        nums = [float(num) for num in context.args]
        resultado = 1
        for num in nums:
            resultado *= num
        await update.message.reply_text(f'La multiplicación es: {resultado}')
    except ValueError:
        await update.message.reply_text('Ingrese otros numeros por favor.')

async def dividir(update, context):
    try:
        nums = [float(num) for num in context.args]
        resultado = nums[0]
        for num in nums[1:]:
            resultado /= num
        await update.message.reply_text(f'La división es: {resultado}')
    except (ValueError, ZeroDivisionError):
        await update.message.reply_text('Ingrese otros numeros o evite ingresar 0 como divisor, por favor.')

async def ayuda(update,context):
	await update.message.reply_text('Para que realize una operación ingrese su comando de esta manera: "/operación" num1 num2')

if __name__ == '__main__':
	app = Application.builder().token(TOKEN).build()

	#Comandos
	app.add_handler(CommandHandler('start', start_command))
	app.add_handler(CommandHandler('sumar', sumar))
	app.add_handler(CommandHandler('restar', restar))
	app.add_handler(CommandHandler('multi', multiplicar))
	app.add_handler(CommandHandler('dividir',dividir))
	app.add_handler(CommandHandler('help',ayuda))

	app.run_polling(poll_interval=3)
