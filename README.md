# DiapoAC - Lecteur Vidéo Automatique par Semaine

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

DiapoAC est une application Windows qui permet de lire automatiquement des vidéos en plein écran au démarrage du système, en sélectionnant intelligemment la vidéo correspondant à la semaine en cours.

## 🚀 Fonctionnalités

- 📅 Détection automatique de la semaine en cours
- 🎥 Lecture de la vidéo correspondant à la semaine actuelle
- 🔄 Lecture de la vidéo de la semaine précédente si celle de la semaine actuelle n'existe pas
- 🖥️ Mode plein écran
- 🔁 Lecture en boucle
- ⌨️ Appuyez sur Échap pour quitter

## 📋 Prérequis

- Python 3.x
- Windows 10 ou supérieur
- Les dépendances listées dans `requirements.txt`

## 🔧 Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-username/DiapoAC.git
   cd DiapoAC
   ```

2. Créez un dossier `C:/Videos_Diapo` (ou modifiez le chemin dans le code)

3. Placez vos fichiers vidéos dans ce dossier avec le format suivant :
   - `Diapo_accueille_S14.mp4` pour la semaine 14
   - `Diapo_accueille_S15.mp4` pour la semaine 15
   - etc.

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

5. Compilez l'application en exécutable :
   ```bash
   pyinstaller --onefile --windowed video_player.py
   ```

6. Exécutez `install.bat` pour configurer le démarrage automatique

## 🗑️ Désinstallation

Pour désinstaller, supprimez simplement le raccourci dans le dossier de démarrage de Windows.

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub. 