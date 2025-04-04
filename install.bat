@echo off
echo Installation du lecteur video au demarrage...

:: Créer un raccourci dans le dossier de démarrage
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\VideoPlayer.lnk'); $Shortcut.TargetPath = '%~dp0video_player.exe'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.Save()"

echo Installation terminee!
pause 