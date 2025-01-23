# Application de QCM en Python

Une application console permettant de gérer des questionnaires à choix multiples (QCM) avec suivi des utilisateurs et de leurs scores.

## Démonstration vidéo
Vous pouvez visionner une démonstration de l'application en suivant ce lien : [https://youtu.be/S-5KlAUA7Qc](https://youtu.be/S-5KlAUA7Qc)

## Comment utiliser l'application
### Étape 1 : Lancer l'application
Ouvrez le fichier principal du projet. Vous avez le choix entre deux versions :

1. **Interface graphique** : Lancez l'application en exécutant `ui.py`.
2. **Application console** : Lancez l'application en exécutant `code.py`

### Étape 2 : Connexion utilisateur
Entrez un identifiant (nom ou ID).
Si l'identifiant existe déjà, vous aurez accès à votre historique.
Si l'identifiant est nouveau, un profil sera créé pour vous.

![Screenshot 2025-01-22 213419](https://github.com/user-attachments/assets/46ca7a0b-e86d-4903-ae96-48c0169d65a3)

### Étape 3 : Naviguer dans les options
Une fois connecté, vous aurez le choix entre :

- Commencer un nouveau quiz.
- Consulter votre historique.
- Exporter vos données.

![Screenshot 2025-01-22 213451](https://github.com/user-attachments/assets/1c385347-d5cd-437e-b07a-89db9e97eef7)

### Étape 4 : Commencer un quiz
Pour commencer un quiz, cliquez sur "Start Quiz" et choisissez une catégorie parmi celles disponibles.

### Étape 5 : Répondre aux questions
1. Répondez aux questions qui s'affichent en sélectionnant l'option souhaitée.
2. Après chaque question, un feedback immédiat sera donné :
   - Réponse correcte : Message de validation.
   - Réponse incorrecte : Affichage de la bonne réponse.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/7e657a2f-57a0-4845-a05f-ac8f66a0c35e" alt="Screenshot 2025-01-22 213720" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/71088d44-d5f7-4a27-adbc-0114e898e3af" alt="Screenshot 2025-01-22 213739" style="width: 48%;"/>
</div>

**Remarque** : Le chronomètre commence dès que vous démarrez le quiz. Si vous dépassez ce temps, le quiz s'arrête automatiquement et vous serez redirigé vers le résultat final.

### Étape 6 : Consulter le score et l'historique
1. Une fois le test terminé, votre score s'affichera.
2. Votre historique sera mis à jour avec la date et le score du test.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/d9eecd34-1e58-45c7-9d54-e867ed92ce1c" alt="Screenshot 2025-01-22 213517" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/1d693f75-ce76-4d6a-853f-6ec47680a947" alt="Screenshot 2025-01-22 213636" style="width: 48%;"/>
</div>

### Étape 7 : Exporter les résultats 
Vous pouvez exporter vos résultats au format CSV via une option dédiée.
Le fichier sera nommé automatiquement.

![Screenshot 2025-01-22 213650](https://github.com/user-attachments/assets/dec52b26-0b55-4132-9722-9fe88bd94efb)

## Prérequis Techniques

Pour exécuter cette application, vous devez avoir Python installé ainsi que la bibliothèque suivante :

### Bibliothèques nécessaires
- **Custom Tkinter** : pour l'interface graphique personnalisée.
  - Vous pouvez l'installer avec la commande suivante :

    ```bash
    pip install customtkinter
    ```
