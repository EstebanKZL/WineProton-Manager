# Instalación de WineProton Manager

## Dependencias

- Python 3.6 o superior
- PyQt5
- Wine o Proton instalado
- Konsole (para la salida de terminal)

## Instalación desde código fuente

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
   
2. Construye la AppImage:

   ```bash
   ./linuxdeploy-x86_64.AppImage --appdir AppDir -e src/WineProtonManagericon.py -i icons/WineProtonManagericon.png -d AppDir/WineProtonManager.desktop
