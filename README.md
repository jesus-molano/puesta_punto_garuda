# Puesta a punto de Garuda
## Install Drivers
Mirror List: /etc/pacman.d/chaotic-mirrorlist
```
sudo pacman -Sy
```
## Enable firewall it with the following command:
```
sudo ufw enable
sudo ufw status verbose
```
## Enable TRIM for SSD
```
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
```
sudo pacman -S steam
sudo pacman -S gnome-keyring
yay -S ttf-cascadia-code
yay -S nodejs npm
yay -S visual-studio-code-bin
yay -S google-chrome
yay -S runjs
yay -S youtube-music
yay -S figma-linux
yay -S stacer
```
## Delete neofetch line en fish
```
code .config/fish/config.fish
```
## Habilitar Khronkite config(Instalar antes)
```
mkdir -p ~/.local/share/kservices5/
ln -s ~/.local/share/kwin/scripts/krohnkite/metadata.desktop
~/.local/share/kservices5/krohnkite.desktop
```
## Borrar Guest User
```
sudo pacman -R systemd-guest-user
```
## Config alacritty cambiar fuente, colores y opacidad
```
code .config/alacritty/alacritty.yml
```
```
font: Cascadia Code PL
window:
opacity:0.6
```
**One Dark Pro**
```
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

# Fixing Errors
Graphics Error: Alt+Shift+F12
