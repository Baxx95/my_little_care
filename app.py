import streamlit as st
import pandas as pd
from PIL import Image

#-------------------------------------------------------
tab_prod = pd.read_csv("df2_v3.csv")
df_data = pd.read_csv('donnes_labaled_type_produit.csv')
descriptif=[['gra','adouciss','nourr','apai','brill','protect','fondant','onctueux','vitamin','forte porosité','ondulé'],
             ['brill','calmer','liss','stimul','fortifi','assouplir','apai','pouss','irrit','nourr','vitamin','huileux','pouss','faible porosité'],
             ['nourr','revitali','boucl','apai','couleur','surgraiss','assoupliss','brill','frisotti','prote','puissant','calmer','sec',
              'cuir','stimul','hydrat','gainant','antioxyd','sensibl','fortifi','liss','vitamin','fri','assainiss','pouss','cass',
              'alourdir','soyeux','fin','faible porosité','cheuveux epai','epai','cheveux moyennement epai'],
             ['nourr','hydrat','pellicul','menthol','renforc','sec','brill','humect','cassant','impuret','naturel','lavag','karit','chute','gra','irrit'],
             ['vitamin','traitement','profond','boost','traumat','soupless','sec','liss','reconstructeur','color'],
             ['spray','fortifi','glisser','boucl','nutrit','sec','irr','cheveux naturel','boucl','ondulé'],
             ['nourr', 'brill', 'boucl', 'hydrat', 'ricin', 'fri', 'cheveux naturel'],
             ['renforc','soin','cass','protein','puissanc','sec','cass','ondulé','boucl','cheveux epai','irrit','cheveux naturel'],
             ['activatr','hydrat','boucl','douceur','ondulé','boucl','fri','cheveux naturel'],
             ['antipelliculair','boucl','cass','irrit','doux','nourr','routin','apai','traitement','shampo','pellicul','sec','soin','soulag','naturel']]

#-------------------------------------------------------
def mots(descriptif):
    """
    retourne la liste de tous les mots de descriptif, de manière unique, dans une seule liste
    """
    liste_de_mots = []
    for desc in descriptif:
        for i in desc : 
            if not(i in liste_de_mots):
                liste_de_mots.append(i)
    return liste_de_mots

#-------------------------------------------------------
def cosij(ui,uj):
    """
    retourne le resultat du calcul de s_ij pour 2 valeurs ui(i) et uj(j)
    paramètres :
    les vecteurs ui et uj de modules mod(ui) et mod(uj)
    """
    s=0
    for i in range(len(ui)):
        if mod(ui) != 0 and mod(uj) != 0 :
            s += ui[i]*uj[i]/(mod(ui)*mod(uj))
        elif mod(ui) != 0 and mod(uj) == 0 :
            s += ui[i]*uj[i]/mod(ui)
        elif mod(ui) == 0 and mod(uj) != 0:
            s += ui[i]*uj[i]/mod(uj)
        else:
            s += 0
    return s

#-------------------------------------------------------
def mod(u):
    """
    calcule le module du vecteur mis en paramètre
    """
    s=0
    for i in range(len(u)):
        s += u[i]*u[i]
    s = s**0.5
    return s

#-------------------------------------------------------
def tab_input_v2(desc):
    mots_elements = mots(descriptif)
    nombre_de_mots = len(desc)
    return [desc.count(mot)/nombre_de_mots if nombre_de_mots != 0 else 0 for mot in mots_elements]
#-------------------------------------------------------
img = Image.open("new_logo.png") 
st.image(img, width=300)

#-------------------------------------------------------
st.subheader("Informations personnelles :")
age = st.selectbox(
        'Quel âge avez-vous ?',
         list(range(17,105)))

genre = st.radio(
        'Quel est votre sexe ? ',
        ("Femme", "Homme", "Non Binaire"))

Nom=st.text_input('Nom : ')

Prenom=st.text_input('Prénom : ')

Email=st.text_input('Email : ')

#-------------------------------------------------------
st.subheader("État actuel de la chevelure :")
rep1 = st.selectbox(
        'Comment sont vos cheveux naturellement ?',
         ['Caucasiens', 'Métissés','Crépus'])

rep2 = st.selectbox(
        'Vos cheveux sont actuellement :',
         ['Lissés', 'Colorés','Permanentés', 'Naturels', 'Méchés'])

rep3 = st.selectbox(
        "Quelle est l’épaisseur de vos cheveux ?",
         ['Fins','Cheveux moyennement épais','Cheuveux épais'])
 
rep4 = st.selectbox(
        "Quelle est la longueur de vos cheveux ?",
         ['Longs','Courts','Aux épaules'])

rep5 = st.multiselect(
    "Comment est votre cuir chevelu ? \nSélectionnez jusqu’à 2 :",
         ['Sec', 'Gras','Pelliculaire', 'Irrité', 'Sain'])
   
rep6 = st.selectbox(
        'Quelle est la porosité de vos cheveux ?',
         ['Faible porosité','Porosité normale','Forte porosité'])
   
rep7 = st.radio(
        'Vous a-t-on diagnostiqué une maladie du cuir chevelu ?',
        ("Oui", "Non"))
if rep7 == "Oui":
    rep8 = st.selectbox(
        'De quelle maladie s’agit-il ?',
         ['Pelade','Alopécie','Kyste'])

image_cheveux = st.file_uploader("Envoyez - nous une photo de vos cheveux pour un diagnostic plus précis (Optionnel)")
if image_cheveux is not None:
    # To read file as bytes:
    bytes_data = image_cheveux.getvalue()
    #st.write(bytes_data)  

#-----------------------------------------------------------
st.subheader("Routine capillaire ")
rep9 = st.selectbox(
        'Combien de fois lavez-vous vos cheveux ?',
         ['Tous les jours','Tous les 2-3 jours', '1 fois par semaine'])

rep10 = st.selectbox(
        'Qu’est ce que vous utilisez généralement pour coiffer vos cheveux ?',
         ['Gel', 'Fer à lisser', 'Mousse', 'Fer à boucler', 'Laque', 'Spray'])

rep11 = st.selectbox(
        'Sélectionnez l’un des traitements que vous avez actuellement ou que vous prévoyez d’avoir dans les prochaines semaines',
         ['Lait', 'Masque', 'Huiles', 'Soins sans rinçage', 'Shampooing sec', 'Après shampooing'])

rep12 = st.selectbox(
        'Colorez vous ou décolorez-vous vos cheveux ?',
         ['Parfois','Souvent','Non'])

#-----------------------------------------------------------
st.subheader("Objectifs")
rep13 = st.multiselect(
    'Sélectionnez jusqu’à 3 objectifs:',
    ['Réparation','Hydratation','Protection de la couleur','Boucles rebondies',
    'Soin du cuir chevelu','Lissage','Volume'])

#-----------------------------------------------------------
st.subheader("Futurs soins")
rep14 = st.selectbox(
        'Quels produits aimeriez-vous ajouter à votre routine ?',
         ["Soin de nuit","Shampoing sec","Sérum cuir chevelu","Huile pour cheveux","Lait"])

rep15 = st.selectbox(
        'Quel budget avez-vous par mois ?',
         ["10 €", "Entre 10 € - 30 €" ,"Entre 30 € - 50 €","+50 €"])

#-----------------------------------------------------------
st.subheader("Lifestyle")
rep16 = st.selectbox(
        'Où vivez-vous ?',
         ["Campagne","Urbain","Péri-urbain"])

rep17 = st.selectbox(
        'Quel est le temps moyen dans votre région ?',
         ["Ensoleillé","Neigeux","Pluvieux","Nuageux"])

rep18 = st.selectbox(
        'Comment définiriez-vous votre alimentation ?',
         ["Saine","Junkfood","Flexitarien","Végétarien","Végétalien"])

rep19 = st.selectbox(
        'Vous évoluez dans un environnement :',
         ["Stressant", "Calme" ,"Fatiguant"])

rep20 = st.radio(
        'Êtes-vous enceinte ou allaitante ?',
        ("Oui", "Non"))

#     option = 'liss' if option=='Lisses' else 'ondulé' if option=='Ondulés' else 'boucl' if option=='bouclés' else 'fri'
#     option1 = 'sec' if option1=='Sec' else 'gra' if option1=='Gras' else 'pellicul' if option1=='Pelliculaire' else 'irrit' if option1=='irrité' else option1
inputs = [rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep9,rep10,rep11,rep12,rep13,rep14,rep15,rep16,rep17,rep18,rep19,rep20]

def diagnostic(rep1,rep5,rep6):
    if rep1 == 'Crépus' and 'Sec' in rep5 and rep6 == 'faible porosité':
        rep = "Vous semblez avoir un problème d'hydratation et de production ou de rétention de sébum.\n"
    elif rep1 == 'Crépus' and 'Gras' in rep5 and rep6 == 'faible porosité':
        rep = "Vous semblez avoir un problème d'absortion et de rétention de corps gras externe à la surface de votre fibre capillaire.\n"
    elif rep1 == 'Crépus' and ('Sec' in rep5 and 'Pelliculaire' in rep5) and rep6 == 'faible porosité':
        rep = "Vous semblez avoir un problème de production de sébum et d'absortion de corps gras externe et d'eau à la surface de votre fibre capillaire.\n"
    elif rep1 == 'Crépus' and ('Gras' in rep5 and 'Pelliculaire' in rep5) and rep6 == 'faible porosité':
        rep = "Vous semblez avoir un problème de production de sébum et d'absortion de corps gras externe et d'eau à la surface de votre fibre capillaire.\n"
    else:
        rep = "Vous semblez ne pas avoir un problème particulier, mais un objectif à atteindre.\n"
    
    return rep

if st.button('Validez'):
        d={}
        for i in tab_prod.index:
            d[tab_prod["Unnamed: 0"].loc[i]] = cosij(tab_prod.loc[i].values[1:],tab_input_v2(inputs))
        
        d_sorted = sorted(d.items(), key=lambda t: t[1], reverse=True)
        ch=''
        i=0
        for typ in d_sorted:
            ch+=typ[0]+', '
            i+=1
            if i == 2:break
        
        prods = ch[:-2].split(',')
        prods = [typ.strip() for typ in prods]
        nb_prod = df_data[df_data.type_produit_traite == prods[0]].shape[0] + df_data[df_data.type_produit_traite == prods[1]].shape[0]

        st.write(diagnostic(rep1,rep5,rep6))
        st.write("Nous avons dans notre base d'articles", nb_prod, " produits de type ",prods[0]," et ", prods[1]," qui vous permettront d'atteindre vos objectifs.\nVeuillez prendre rendez-vous avec un de nos experts pour plus de détails sur les produts et leurs utilisations.")
        st.write("N'hésitez pas de consulter notre site [MyLittleCare](https://my-little-care.webflow.io/#Produit)")
