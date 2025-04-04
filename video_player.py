import pygame
import sys
import os
import datetime
import glob

def get_current_week():
    # Obtenir la date actuelle
    today = datetime.datetime.now()
    # Calculer le numéro de la semaine
    week_number = today.isocalendar()[1]
    return week_number

def find_video_file():
    # Chemin du dossier contenant les vidéos
    video_dir = "C:/Videos_Diapo"  # À modifier selon votre emplacement
    current_week = get_current_week()
    
    # Chercher le fichier correspondant à la semaine actuelle
    video_pattern = f"Diapo_accueille_S{current_week}.mp4"
    video_path = os.path.join(video_dir, video_pattern)
    
    # Vérifier si le fichier existe
    if os.path.exists(video_path):
        return video_path
    
    # Si le fichier n'existe pas, chercher le fichier de la semaine précédente
    previous_week = current_week - 1
    if previous_week < 1:
        previous_week = 52  # Retour à la dernière semaine de l'année précédente
    
    video_pattern = f"Diapo_accueille_S{previous_week}.mp4"
    video_path = os.path.join(video_dir, video_pattern)
    
    if os.path.exists(video_path):
        return video_path
    
    return None

def main():
    # Initialisation de pygame
    pygame.init()
    
    # Obtenir les dimensions de l'écran
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    
    # Créer une fenêtre en plein écran
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Lecteur Vidéo")
    
    # Trouver le fichier vidéo approprié
    video_path = find_video_file()
    
    if video_path is None:
        print("Erreur: Aucun fichier vidéo trouvé pour la semaine actuelle ou précédente!")
        pygame.quit()
        sys.exit()
    
    # Initialiser le lecteur vidéo
    pygame.mixer.init()
    pygame.mixer.music.load(video_path)
    
    # Lire la vidéo en boucle
    pygame.mixer.music.play(-1)  # -1 pour la lecture en boucle
    
    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Échap pour quitter
                    running = False
        
        # Mettre à jour l'affichage
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 