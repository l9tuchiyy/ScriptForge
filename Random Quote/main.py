import requests
import json

class Quote:
    def __init__(self, id, quote, author):
        self.id = id
        self.quote = quote
        self.author = author

quotes = []
dumping = {}

headers = {
    "User-Agent": "ScriptForge/1.0"
}

num = 0

def show_quote():
    response = requests.get(
        "https://dummyjson.com/quotes/random",
        headers=headers)
    now_quote = response.json()
    print(f'Цитата N{now_quote["id"]}\n'
          f'{now_quote["quote"]}\n'
          f'\t\t\t{now_quote["author"]}')
    yes_no = input('Сохранить цитату? [нет/да]').lower()
    if yes_no == 'да':
        quote = Quote(now_quote["id"], now_quote["quote"], now_quote["author"])
        quotes.append(quote)
        save_quotes()
    return

def save_quotes():
        data = []

        try:
            with open("quotes.json", "r", encoding="UTF-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for quote in quotes:
            data.append({
                "id": quote.id,
                "quote": quote.quote,
                "author": quote.author
            })

        with open("quotes.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        quotes.clear()

def show_quotes():
    with open('quotes.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
        if not data:
            print('Вы не сохранили ни одной цитаты!')
        else:
            for el, quote in enumerate(data, start=1):
                print(f'{el}) {quote["quote"]}\n'
                    f'\t\t\t{quote["author"]}')

while True:
    print(f'Выбирите действие:\n'
          f'1. Показать цитату\n'
          f'2. Показать сохраненные цитаты\n'
          f'3. Выйти')
    try:
        num = int(input(''))
    except ValueError:
        print('Введите число!')
        continue
    if num == 1:
        show_quote()
    elif num == 2:
        show_quotes()
    elif num == 3:
        print('Спасибо за работу! До свидания!')
        break
    else:
        print('Введите число от 1 до 3!')