import click
import requests
from bs4 import BeautifulSoup
from modules.Word.managers.DictionaryManager import DictionaryManager
import re


@click.command()
@click.option('--url', help='URL to fetch from')
@click.pass_context
def search(ctx, url):
    dictionary_manager: DictionaryManager = ctx.obj[DictionaryManager]
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    words_list = re.sub(' +', ' ', soup.text).split()
    words_found = {}
    print("Starting...")
    i = 1
    percentage = 5
    percentage_increments = 5
    for word in words_list:
        if (i / len(words_list) * 100) > percentage:
            print(f'{percentage}% read')
            percentage += percentage_increments
        i += 1
        if word in words_found:
            words_found[word] += 1
            continue
        dictionary_manager.is_word(word)
        words_found[word] = 1
    print("Complete...")
