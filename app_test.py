import streamlit as st

#-------------------------------------------------------
#-------------------------------------------------------

st.subheader("Informations personnelles :")
age = st.selectbox(
        'Quel âge avez-vous ?',
         list(range(1,105)))
'vous avez choisi: ', age
genre = st.radio(
        'Quel est votre sexe ?',
        ("Femme", "Homme", "Non Binaire"))
Nom=st.text_input('Nom : ')
"Nom : ", Nom
Prenom=st.text_input('Prenom : ')
"Prenom : ", Prenom
num_tel=st.text_input('Numero de téléphone : ')
'Numero de téléphone : ', num_tel

#-------------------------------------------------------
st.subheader("État actuel de la chevelure :")
rep1 = st.selectbox(
        'Comment sont vos cheuveux naturellement ?',
         ['Lisses', 'Ondulés','bouclés', 'frisés'])
'vous avez choisi: ', rep1
rep2 = st.selectbox(
        'Vos cheuveux sont actuellement :',
         ['Lissés', 'colorés','permanentés', 'Naturels', 'Méchés'])
'vous avez choisi: ', rep2
rep3 = st.selectbox(
        "Quel est l'épaisseur de vos cheveux ?",
         ['cheveux pas epais','cheveux moyennement epai','cheuveux epai'])
'Vous avez choisi: ', rep3  
rep4 = st.selectbox(
        "Quelle est la longueur de vos cheveux ?",
         ['Long','Court','Au épaules'])
'Vous avez choisi: ', rep4
rep5 = st.selectbox(
        'Comment est votre cuir chevelu ?',
         ['Sec', 'Gras','Pelliculaire', 'irrité', 'Sain'])
'Vous avez choisi: ', rep5   
rep6 = st.selectbox(
        'Quelle est la porosité de vos cheveux ?',
         ['faible porosité','porosité normale','forte porosité'])
'Vous avez choisi: ', rep6   
rep7 = st.radio(
        'Vous a-t-on diagnostiqué une maladie du cuir chevelu ?',
        ("Oui", "Non"))
if rep7 == "Oui":
    rep8 = st.selectbox(
        'De quelle maladie s’agit-il ?',
         ['Pelade','Alopécie','Kyste'])
    'Vous avez choisi: ', rep8 

image_cheveux = st.file_uploader("Envoyez- nous une photo de vos cheveux pour un diagnostic plus précis (Optionnel)")
if image_cheveux is not None:
    # To read file as bytes:
    bytes_data = image_cheveux.getvalue()
    st.write(bytes_data)
    

#-----------------------------------------------------------
st.subheader("Routine capillaire ")
rep9 = st.selectbox(
        'A quelle fréquence vous lavez vous les cheveux ?',
         ['tous les jours','tous les 2-3 jours', '1 fois par semaine'])
'Vous avez choisi: ', rep9
rep10 = st.selectbox(
        'Qu’est ce que vous utilisez généralement pour coiffer vos cheveux ?',
         ['gel', 'fer à lisser', 'mousse', 'fer à boucler', 'laque', 'spray'])
'Vous avez choisi: ', rep10
rep11 = st.selectbox(
        'Sélectionnez l’un des traitements que vous avez actuellement ou que vous prévoyez d’avoir dans les prochaines semaines',
         ['lait', 'masque', 'huiles', 'soins sans rinçage', 'shampooing sec', 'après shampooing'])
'Vous avez choisi: ', rep11
rep12 = st.selectbox(
        'Colorez vous ou décolorez-vous vos cheveux ?',
         ['parfois','souvent','non'])
'Vous avez choisi: ', rep12
#-----------------------------------------------------------
st.subheader("Objectifs")
rep13 = st.multiselect(
    'Sélectionnez jusqu’à 3 objectifs:',
    ['Réparation','Hydratation','Protection de la couleur','Boucles rebondies',
    'Soin du cuir chevelu','Lissage','Volume'],)
'You selected:', rep13
#-----------------------------------------------------------
st.subheader("Futurs soins")
rep14 = st.selectbox(
        'Quels produits voudriez-vous inclure dans votre routine ?',
         ["Soin de nuit", "Shampoing sec" ,"Sérum cuir chevelu","Huile pour cheveux", "Lait"])
'Vous avez choisi: ', rep14
rep15 = st.selectbox(
        'Quel budget avez-vous par mois ?',
         ["10 €", "Entre 10 € - 30 €" ,"Entre 30 € - 50 €","+50 €"])
'Vous avez choisi: ', rep15
#-----------------------------------------------------------
st.subheader("Lifestyle")
rep16 = st.selectbox(
        'Où vivez-vous ?',
         ["Campagne", "Urbain" ,"Péri-urbain"])
'Vous avez choisi: ', rep16
rep17 = st.selectbox(
        'Quel est le temps moyen dans votre région ?',
         ["Ensoleillé", "Neigeux" ,"Pluvieux","Nuageux"])
'Vous avez choisi: ', rep17
rep18 = st.selectbox(
        'Comment définiriez-vous votre alimentation ?',
         ["Saine", "Junkfood" ,"Fléxitarien","Végétarien", "Végétalien"])
'Vous avez choisi: ', rep18
rep19 = st.selectbox(
        'Vous évoluez dans un environnement :',
         ["Stressant", "Calme" ,"Fatiguant"])
'Vous avez choisi: ', rep19
rep20 = st.radio(
        'Êtes-vous enceinte ou allaitante ?',
        ("Oui", "Non"))

inputs = [rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep8,rep9,rep10,rep11,rep12, rep13,rep14,rep15,rep16,rep17,rep18,rep19,rep20]
    
if st.button('Validez'):
        st.write("Nous avons dans notre base d'articles nb_prod produits de type __xxx__ , qui vous permettront d'atteindre vos objectifs.\nVeuillez prendre rendez-vous avec nos experts pour plus de détails sur les produts et leurs utilisations.")
        st.write(inputs)




