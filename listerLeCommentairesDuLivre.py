import requests

url = ('https://demo.api-platform.com/books/1d52ba85-97c8-4cc3-b81a-40582f3aff64/reviews')

r_livre = requests.get(url)

dico_livre = r_livre.json()
liste_livre = dico_livre['hydra:member']


print("tous les commentaires du livre dont l’id est « 1d52ba85-97c8-4cc3-b81a- 40582f3aff64 :")
for i in range(len(liste_livre)):
    for k, v in liste_livre[i].items():
        if k == 'body':
            text = v
            print( text)