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



post_id = dico_post_commmentaire.get('@id')

print("Id du commentaire est: ",post_id)

#Changement de commentaire
#phrase initiale : blamabllzlzlzlz
#new : Dobry den
data_patch = {"body": "Dobry den"}
url2 = "https://demo.api-platform.com" + post_id
r_patch_commentaire = requests.patch(url2, json = data_patch, headers={'Content-Type': 'application/merge-patch+json'})

print("verification de changement (si 200 = OK) :",r_patch_commentaire)

dico_modification = r_patch_commentaire.json()

def content_commentaire(id):
    url = 'https://demo.api-platform.com' + id
    r_cmt_id = requests.get(url)
    dico_commid = r_cmt_id.json()
    for k, v in dico_commid.items():
        if k == 'body':
            return v

id = post_id

print("le commentaire ete change: ", content_commentaire(id))