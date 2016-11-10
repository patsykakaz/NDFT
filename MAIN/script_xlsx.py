from openpyxl import load_workbook
wb = load_workbook(filename='ndft.xlsx', read_only=True)
ws = wb['site internet - csv clean 0611 ']
x = []
for row in ws.rows:
    y = []
    for cell in row:
        y.append(cell.value)
    x.append(y)
x = x[1:]
from MAIN.models import *
for element in x:
    if element[0]:
        if element[12]:
            element[12] = element[12].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        if element[13]:
            element[13] = element[13].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        if element[14]:
            element[14] = element[14].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        if element[15]:
            element[15] = element[15].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        if element[16]:
            element[16] = element[16].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        if element[17]:
            element[17] = element[17].replace('é','e').replace('à','a').replace(' ', '_').replace('â','a').replace("’","_")
        k = Product(
                title_fr=element[0],
                title_en=element[0],
                town=element[1],
                productName_fr=element[2],
                productName_en=element[3],
                baseline_fr=element[4],
                baseline_en=element[5],
                presentation_product_fr=element[6],
                presentation_product_en=element[7],
                presentation_sup_fr=element[8],
                presentation_sup_en=element[9],
                price=element[10],
                discount=element[11],
                logo=element[12],
                illustration=element[13],
                illustration2=element[14],
                illustration3=element[15],
                illustration4=element[16],
                team_pic=element[17],
                mainLink=element[18],
                website=element[19],
                facebook=element[20],
                twitter=element[21],
                instagram=element[22],)
        k.save()
    else:
        print "an element has empty title" % element[0]

# 0 Quel est le nom de votre start-up ?
# 1 Quelle est la ville de votre start-up ?
# 2 Quel est le nom de votre produit ?
# 3 Quel est le nom de votre produit en anglais ?
# 4 Présentez votre produit en quelques mots.
# 5 Présentez votre produit en quelques mots en anglais.
# 6 Présentez votre produit de façon plus détaillée.
# 7 Présentez votre produit de façon plus détaillée en anglais.
# 8 Présentez votre start-up. 
# 9 Présentez votre start-up en anglais. 
# 10 Quel est le prix de votre produit ?
# 11 Si vous faites une réduction spécial Noël, précisez de combien et comment l\'obtenir.
# 12 Donnez-nous votre logo.
# 13 Donnez-nous la photo principale de votre produit.
# 14 Vous avez la possibilité de mettre une 2ème photo pour la page détaillée de votre cadeau.
# 15 Vous avez la possibilité de mettre une 3ème photo pour votre page détaillée.
# 16 Vous avez la possibilité de mettre une 4ème photo pour votre page détaillée.
# 17 Donnez-nous une photo de votre team.
# 18 Laissez-nous le lien de votre page produit.
# 19 Rappelez-nous également l adresse générale de votre site internet.
# 20 Quelle est votre page Facebook ?
# 21 Quelle est votre page Twitter ?
# 22 Quelle est votre page Instagram ?

# for k in kk : 
#     if k.logo != "":
#         split = k.logo.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.logo.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+split[-1]
#     if k.illustration != "":
#         split = k.illustration.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.illustration.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+split[-1]
#     if k.illustration2 != "":
#         split = k.illustration2.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.illustration2.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+split[-1]
#     if k.illustration3 != "":
#         split = k.illustration3.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.illustration3.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+split[-1]
#     if k.illustration4 != "":
#         split = k.illustration4.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.illustration4.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+ split[-1]
#     if k.team_pic != "":
#         split = k.team_pic.name.split('/static/media/')
#         try: 
#             split.remove('')
#         except: 
#             pass
#         k.team_pic.name = "/home/patsykakaz/NDFT/MAIN/static/media/uploads/illustration/"+ split[-1]
#     k.save()
