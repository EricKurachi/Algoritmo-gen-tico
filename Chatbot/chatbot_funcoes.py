import wikiparser
import requests

def search_wikipedia(pesquisa):
    #url = 'https://pt.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Peixe&format=json'
    #resp = requests.get(url)
    #pesquisa = resp.json()
    #print(pesquisa)

    busca = wikiparser.getParagraph('https://en.wikipedia.org/wiki/{}'.format(pesquisa))
    resultado = busca.get('data')
    return resultado

def conversar():
    print ('Olá, vamos conversar!')
    fala = 'Primeira fala'

    while fala != 'Tchau':

        fala = input()
        if fala.find('oi') != -1 or fala.find('como vai você') != -1 or fala.find('olá') != -1 :
            print('Olá')
        else:
            print('Desculpe. Não sei como te responder')


