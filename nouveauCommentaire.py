import requests

data = {
  "body": "blamabllzlzlzlz",
  "rating": 5,
  "author": "Ivana",
  "publicationDate": "2020-01-09T13:30:25.756Z",
  "book": "books/1b08c9ab-6254-4015-ad14-bac3e5c008df"
}
r_post_commmentaire = requests.post("https://demo.api-platform.com/reviews", json = data)

dico_post_commmentaire = r_post_commmentaire.json()

print(("le nouveau commentaire a ete ajoute: "))
print(dico_post_commmentaire)

post_id = dico_post_commmentaire.get('@id')

print("Id du nouveau commentaire est: ",post_id)
