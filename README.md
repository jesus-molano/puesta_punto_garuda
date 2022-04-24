# Puesta a punto de Garuda
## Install Drivers
Mirror List: /etc/pacman.d/chaotic-mirrorlist
```fish
sudo pacman -Sy
```
## Enable firewall it with the following command:
```fish
sudo ufw enable
sudo ufw status verbose
```
## Enable TRIM for SSD
```fish
sudo systemctl enable fstrim.timer
```
## Fuentes Microsoft
Software Manager → Search for ttf-ms-fonts → Install
## Grub Rápido
Garuda Welcome → Garuda Boot Options → Set menu timeout to 1s
## Borrar paquetes huérfanos
Garuda Welcome → Garuda Assistant → Remove orphans
## Limpiar Cache de paquetes
Garuda Welcome → Garuda Assistant → Clean package cache
## Instalaciones
```fish
sudo pacman -S steam
sudo pacman -S heroic-games-launcher-bin
sudo pacman -S gnome-keyring
yay -S ttf-cascadia-code
yay -S nodejs npm
yay -S visual-studio-code-bin
yay -S google-chrome
yay -S runjs
yay -S spotify
yay -S figma-linux
yay -S stacer
yay -s github-cli
```
## Delete neofetch line en fish
```fish
code .config/fish/config.fish
```
## Habilitar Khronkite config(Instalar antes)
```fish
mkdir -p ~/.local/share/kservices5/
ln -s ~/.local/share/kwin/scripts/krohnkite/metadata.desktop
~/.local/share/kservices5/krohnkite.desktop
```
## Borrar Guest User
```fish
sudo pacman -R systemd-guest-user
```
## Config alacritty cambiar fuente, colores y opacidad
```fish
code .config/alacritty/alacritty.yml
```
```yml
font: Cascadia Code PL
window:
opacity:0.6
```
**One Dark Pro**
```yml
colors:
# Default colors
primary:
background: '0x1e2127'
foreground: '0xabb2bf'
# Normal colors
normal:
black: '0x1e2127'
red: '0xe06c75'
green: '0x98c379'
yellow: '0xd19a66'
blue: '0x61afef'
magenta: '0xc678dd'
cyan: '0x56b6c2'
white: '0xabb2bf'
# Bright colors
bright:
black: '0x5c6370'
red: '0xe06c75'
green: '0x98c379'
yellow: '0xd19a66'
blue: '0x61afef'
magenta: '0xc678dd'
cyan: '0x56b6c2'
white: '0xffffff'
```

## FontForge Python
alias ttfcompress =  ‘/usr/local/bin/ttfcompress.py’

/usr/local/bin/ttfcompress.py
```python
#!/usr/bin/env python
from sys import argv;
import fontforge;
font = fontforge.open(argv[1]);
font.generate(argv[1][0:-3] + "woff");
font.generate(argv[1][0:-3] + "woff2");
font.close();
```



# Fixing Errors
Graphics Error: Alt+Shift+F12
