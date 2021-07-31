# dotfiles
![Qtile](/.screenshots/qtile.png)

***Language***
- English
- [Spanish](https://github.com/franfermar/dotfiles/blob/master/README.es.md)

# Introduction
This guide has been written for personal use. That is why if you come looking to document yourself, the only thing you are going to find are reminders. If you want to find good documentation, take a look at the dotfiles of [@antoniosarosi](https://github.com/antoniosarosi/).

# System configuration
For the login screen I try [lightdm](https://wiki.archlinux.org/title/LightDM_(Espa%C3%B1ol)). I have specifically used this [tema](https://aur.archlinux.org/packages/lightdm-slick-greeter/). If you want to configure graphically check  [lightdm-settings](https://aur.archlinux.org/packages/lightdm-settings/).

Also, I have modify grub theme. You can check it [grub](https://github.com/stuarthayhurst/argon-grub-theme).

## Windows

| Key                     | Action                           |
| ----------------------- | -------------------------------- |
| **mod + j**             | next window (down)               |
| **mod + k**             | next window (up)                 |
| **mod + shift + h**     | decrease master                  |
| **mod + shift + l**     | increase master                  |
| **mod + shift + j**     | move window down                 |
| **mod + shift + k**     | move window up                   |
| **mod + shift + f**     | toggle floating                  |
| **mod + tab**           | change layout                    |
| **mod + [1-9]**         | Switch to workspace N (1-9)      |
| **mod + shift + [1-9]** | Send Window to workspace N (1-9) |
| **mod + period**        | Focus next monitor               |
| **mod + comma**         | Focus previous monitor           |
| **mod + w**             | kill window                      |
| **mod + ctrl + r**      | restart wm                       |
| **mod + ctrl + q**      | quit                             |

The following keybindings will only work if you install all programs needed:

```bash
sudo pacman -S rofi thunar firefox alacritty redshift scrot
```

To set up *rofi*,
[check this README](https://github.com/antoniosarosi/dotfiles/tree/master/.config/rofi),
and for *alacritty*, [this one](https://github.com/antoniosarosi/dotfiles/tree/master/.config/alacritty).


## Apps

| Key                 | Action                        |
| ------------------- | ----------------------------- |
| **mod + m**         | launch rofi                   |
| **mod + shift + m** | window nav (rofi)             |
| **mod + b**         | launch browser (firefox)      |
| **mod + e**         | launch file explorer (thunar) |
| **mod + return**    | launch terminal (alacritty)   |
| **mod + r**         | redshift                      |
| **mod + shift + r** | stop redshift                 |
| **mod + s**         | screenshot (scrot)            |

# Software

## Basic utilities

| Software                                                                                            | Utility                          |
| --------------------------------------------------------------------------------------------------- | -------------------------------- |
| **[networkmanager](https://wiki.archlinux.org/index.php/NetworkManager)**                           | Self explanatory                 |
| **[network-manager-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**         | *NetworkManager* systray         |
| **[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**                                   | Self explanatory                 |
| **[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**                     | *pulseaudio* GUI                 |
| **[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**             | Laptop screen brightness         |
| **[xinit](https://wiki.archlinux.org/index.php/Xinit)**                                             | Launch programs before wm starts |
| **[libnotify](https://wiki.archlinux.org/index.php/Desktop_notifications)**                         | Desktop notifications            |
| **[notification-daemon](https://www.archlinux.org/packages/community/x86_64/notification-daemon/)** | Self explanatory                 |
| **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**                            | Automounter                      |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**                   | Volume systray                   |

## Fonts, theming and GTK

| Software                                                                               | Utility                    |
| -------------------------------------------------------------------------------------- | -------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Compositor for Xorg        |
| **[UbuntuMono Nerd Font](https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono/)** | Nerd Font for icons        |
| **[Material Black](https://www.gnome-look.org/p/1316887/)**                            | GTK theme and icons        |
| **[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**  | GUI for changing themes    |
| **[feh](https://wiki.archlinux.org/index.php/Feh)**                                    | CLI for setting wallpapers |

## Apps

| Software                                                              | Utility                  |
| --------------------------------------------------------------------- | ------------------------ |
| **[alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Terminal emulator        |
| **[thunar](https://wiki.archlinux.org/index.php/Thunar)**             | Graphical file explorer  |
| **[ranger](https://wiki.archlinux.org/index.php/Ranger)**             | Terminal based explorer  |
| **[neovim](https://wiki.archlinux.org/index.php/Neovim)**             | Terminal based editor    |
| **[rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menu and window switcher |
| **[scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Screenshot               |
| **[redshift](https://wiki.archlinux.org/index.php/Redshift)**         | Take care of your eyes   |
| **[geeqie]((https://archlinux.org/packages/extra/x86_64/geeqie/))**         | Image viewer                     |
