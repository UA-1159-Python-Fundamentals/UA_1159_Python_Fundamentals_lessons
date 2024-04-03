import telebot
from telebot import types
import main
import os
import datetime
import matplotlib.pyplot as plt

bot = telebot.TeleBot('7168473402:AAH6iDTw4HJVEzKVHdr_Vcrc-FXZEUXGKdA')

expense_categories = main.expense_categories

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """ 
    Using this bot you can track your everyday expenses
    """)

# Menu: If you want add new functionality start from adding button here
def generate_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_add_expense = types.KeyboardButton('Add expense')
    button_summary = types.KeyboardButton('Summary')
    button_add_category = types.KeyboardButton('Add category')
    button_clear_data = types.KeyboardButton('Clear Data')
    button_send_file = types.KeyboardButton('Send file')
    button_photo_summary = types.KeyboardButton('Photo Summary')
    markup.add(button_add_expense, button_summary, button_add_category, button_clear_data, button_send_file, button_photo_summary)
    bot.send_message(chat_id, "Menu:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    generate_menu(message.chat.id)

# 1) Adding expense start from here
@bot.message_handler(func=lambda message: message.text == 'Add expense')
def add_expense_name(message):
    msg = bot.send_message(message.chat.id, "Enter expense name:")
    bot.register_next_step_handler(msg, process_name_step)

def generate_category_message(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = [types.KeyboardButton(category) for category in expense_categories]
    markup.add(*buttons)
    bot.send_message(chat_id, "Choose expense category:", reply_markup=markup)

# 2) Second step of adding expense. Adding name of expense.
def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    generate_category_message(chat_id)
    bot.register_next_step_handler(message, process_category_step, name)

# 3) Third step of adding expense. Adding category of expense.
def process_category_step(message, name):
    chat_id = message.chat.id
    category = message.text
    date = datetime.date.today()
    msg = bot.send_message(chat_id, "Enter expense amount:")
    bot.register_next_step_handler(msg, process_amount_step, name, category, date)

# 4) Fourth step of adding expense. Adding $amount$ and save to file like row. 
def process_amount_step(message, name, category, date):
    chat_id = message.chat.id
    amount = message.text

    if not amount.replace('.', '', 1).isdigit():
        bot.send_message(chat_id, "Please enter a valid number.")
        msg = bot.send_message(chat_id, "Enter expense amount again:")
        bot.register_next_step_handler(msg, process_amount_step, name, category, date)
        return

    try:
        amount = float(amount)
    except ValueError:
        bot.send_message(chat_id, "Please enter a valid number.")
        msg = bot.send_message(chat_id, "Enter expense amount again:")
        bot.register_next_step_handler(msg, process_amount_step, name, category, date)
        return

    markup = types.ReplyKeyboardRemove()
    bot.send_message(chat_id, f"Expense added successfully!\nName: {name}\nCategory: {category}\nAmount: {amount}\nDate: {date}", reply_markup=markup)
    
    main.save_user_expense(main.Expense(name=name, category=category, amount=float(amount), date=date), "expenses.csv")
    generate_menu(chat_id)

# Functional of button Add Category.
@bot.message_handler(func=lambda message: message.text == 'Add category')
def add_category(message):
    msg = bot.send_message(message.chat.id, "Enter the name of the new category:")
    bot.register_next_step_handler(msg, process_new_category)

# Append existing list of categories.
def process_new_category(message):
    new_category = message.text
    expense_categories.append(new_category)
    bot.send_message(message.chat.id, f"Category '{new_category}' added successfully!")
    generate_menu(message.chat.id)

# Functional of button Summary.
@bot.message_handler(func=lambda message: message.text == 'Summary')
def get_summary(message):
    if not os.path.exists("expenses.csv"):
        bot.send_message(message.chat.id, "Your file with expenses is empty")
        return

    expenses = main.read_expenses("expenses.csv")

    total_expenses = 0
    summary = ""
    for category in expense_categories:
        total_amount = main.get_total_amount_for_category(category, "expenses.csv")
        total_expenses += total_amount
        summary += f"{category}: {total_amount}\n"

    dates = [expense.date for expense in expenses]
    min_date = min(dates)
    max_date = max(dates)

    summary += f"\nTotal expenses: {total_expenses}\n"
    summary += f"{min_date} - {max_date}"

    bot.send_message(message.chat.id, summary)

# Functional of button Clear Data.
@bot.message_handler(func=lambda message: message.text == 'Clear Data')
def clear_data(message):
    main.clear_expense_data("expenses.csv")
    bot.send_message(message.chat.id, "Data cleared successfully!")

# Functional of button Send file.
@bot.message_handler(func=lambda message: message.text == 'Send file')
def send_file(message):
    if os.path.exists("expenses.csv"):
        bot.send_document(message.chat.id, open("expenses.csv", "rb"))
    else:
        bot.send_message(message.chat.id, "Your file don't exist.")

# Functional of button Photo Summary.
@bot.message_handler(func=lambda message: message.text == 'Photo Summary')
def get_photo_summary(message):
    if not os.path.exists("expenses.csv"):
        bot.send_message(message.chat.id, "Your file with expenses is empty, please add some expenses")
        return

    # Побудова графіку
    plt.figure(figsize=(6, 4))
    plt.bar(expense_categories, [main.get_total_amount_for_category(category, "expenses.csv") for category in expense_categories], color='forestgreen')
    plt.xlabel('Categories')
    plt.ylabel('$')
    plt.title('Expenses by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Збереження графіку як файл зображення
    graph_filename = "expenses_graph.png"
    plt.savefig(graph_filename)

    # Надіслати графік як фото
    bot.send_photo(message.chat.id, open(graph_filename, 'rb'))

    # Видалення файлу зображення після надсилання
    os.remove(graph_filename)

bot.polling(non_stop=True)
