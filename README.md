# 🍷 WineProton Manager  

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Herramienta GUI para gestionar entornos Wine/Proton e instalar componentes**  

🔧 **Características principales**:  
- Gestión de múltiples prefixes (Wine y Proton)  
- Instalación automatizada de componentes via Winetricks  
- Soporte para programas personalizados (.exe/.msi)  
- Interfaz intuitiva con temas claro/oscuro  
- Plataforma (Linux)  

🖼️ **Captura**:  
![Screenshot](docs/screenshot.png)

---

## 🚀 Instalación  
```bash
# Requisitos previos
sudo apt install wine winetricks konsole  # Para Linux

# Clonar repositorio
git clone https://github.com/EstebanKZL/WineProton-Manager.git
cd WineProton-Manager

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python3 WineProton-Manager.py
