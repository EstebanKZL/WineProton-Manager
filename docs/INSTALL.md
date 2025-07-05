# Instalación de WineProton Manager

## Dependencias

- Python 3.6 o superior
- PyQt5
- Wine o Proton instalado
- Konsole (para la salida de terminal)

## Instalación desde código fuente

Ejecutar aplicación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/EstebanKZL/WineProtonManager.git
   cd WineProtonManager

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

3. Ejecuta la aplicación:

   ```bash
   python3 src/WineProtonManager.py


Creación de AppImage

1. Instala linuxdeployqt:

   ```bash
   wget https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
   chmod +x linuxdeploy-x86_64.AppImage
   wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
   chmod +x appimagetool-x86_64.AppImage
   
2. Copiar programa
   
   ```bash
   mkdir -p AppDir/usr/bin
   cp src/WineProtonManager.py AppDir/usr/bin/
   chmod +x AppDir/usr/bin/WineProtonManager.py
   
3. Crear AppDir/AppRun

   ```bash
   cat << 'EOF' > AppDir/AppRun
   #!/bin/bash
   HERE="$(dirname "$(readlink -f "$0")")"
   exec "$HERE/usr/bin/WineProtonManager.py" "$@"
   EOF
   chmod +x AppDir/AppRun
   
4. Construye la AppImage:

   ```bash
   pyinstaller --onefile src/WineProtonManager.py
   ./linuxdeploy-x86_64.AppImage --appdir AppDir -i icons/WineProtonManagericon.png -d AppDir/WineProtonManager.desktop
   ./appimagetool-x86_64.AppImage AppDir

5. Ejecutar programa
   
   ```bash
   ./WineProtonManager-v1.1.0-x86_64.AppImage
