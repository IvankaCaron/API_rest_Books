import requests
url = 'https://demo.api-platform.com/books?order[publicationDate]=desc&page=1'
r_books = requests.get(url)
dico_books = r_books.json()

liste_books = dico_books.get("hydra:member")
liste_10_books = liste_books[0:10]


for i in range(len(liste_10_books)):
    for k, v in liste_10_books[i].items():
        if k == 'title':
            titre = v
            #print(titre)
        if k == 'publicationDate':
            publicationDate = v
            publicationDate = publicationDate[0:10]
            #print(publicationDate)
            print('Title : ', titre, ' , Publié :', publicationDate)

        