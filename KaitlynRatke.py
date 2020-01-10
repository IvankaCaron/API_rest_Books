import requests

url = 'https://demo.api-platform.com/books?order[author]=desc&author=Dr.%20Kaitlyn%20Ratke'
r_author = requests.get(url)

dico_author = r_author.json()

liste_author = dico_author['hydra:member']

for i in range(len(liste_author)):
    for k, v in liste_author[i].items():
        if k == 'title':
            title = v
            #print(title)
        if k == 'author':
            author = v
            #print(author)
            print('Le livre écrit par ', author, ' : ', title)