import numpy as np
from bson import ObjectId
from flask import render_template, request, redirect, url_for
from app import app, mongo
from app.models import Produit, Commentaire
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# Charger l'architecture du modèle à partir du fichier JSON
with open("Model/model.json", "r") as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)

# Charger les poids du modèle
loaded_model.load_weights("Model/model.weights.h5")

# Initialiser le tokenizer
tokenizer = Tokenizer(num_words=100000, oov_token='<OOV>') 

# Charger max_sequence_length depuis le fichier
with open('Model/max_sequence_length.pkl', 'rb') as f:
    max_sequence_length = pickle.load(f)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/produits')
def liste_produits():
    produits = mongo.db.produits.find()
    return render_template('liste_produits.html', produits=produits)

@app.route('/produit/<produit_id>', methods=['GET', 'POST'])
def detail_produit(produit_id):
    produit = mongo.db.produits.find_one({'_id': ObjectId(produit_id)})
    commentaires = list(mongo.db.commentaires.find({ "produit_id": produit_id }))
    if request.method == 'POST':
        
        # Prétraitement du commentaire (vectorisation, tokenisation, rembourrage)
        commentaire_texte = request.form['commentaire']
        tokenizer.fit_on_texts(commentaire_texte)
        word_index = tokenizer.word_index
        commentaire_text = tokenizer.texts_to_sequences(commentaire_texte)
        commentaire_padded = pad_sequences(commentaire_text, maxlen=max_sequence_length)

        # Prédiction du sentiment du commentaire
        prediction = loaded_model.predict(commentaire_padded)
        confiance = prediction.max(axis=-1)[0]  

        # Évaluation de la prédiction
        if confiance >= 0.42: 
            Commentaire_Saved = "Le commentaire a ete sauvegarde dans la base de donnee selon le seuil qui est de 42, car j'ai constate que le commentaire positif est dans l'interval de 42-45 donc le niveau de confiance doit etre superieur ou egale au seuil"
            commentaire = {
                'produit_id': produit_id,
                'texte': commentaire_texte,
                'positif': True
            }
            mongo.db.commentaires.insert_one(commentaire)
            return render_template('detail_produit.html', produit=produit, commentaires=commentaires, confiance=confiance, Commentaire_Saved=Commentaire_Saved)
        else:
            Commentaire_Saved = "Le commentaire n'a pas ete sauvegarde dans la base de donnee selon le seuil qui est de 42, car j'ai constate que le commentaire negatif est dans l'interval de 0-41 donc le niveau de confiance doit etre superieur ou egale a au seuil"
            return render_template('detail_produit.html', produit=produit, confiance=confiance, Commentaire_Saved=Commentaire_Saved)
    else:
        commentaires = mongo.db.commentaires.find({'produit_id': produit_id})
        return render_template('detail_produit.html', produit=produit, commentaires=commentaires)