# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from os import path
import subprocess 

mod = "mod4"
terminal = "alacritty"

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])

#############################
#           KEYS            #
#############################

keys = [

    # ------------ Windows Configs ------------

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

   # Grow and shrink windows
    Key([mod, "control"], "l", lazy.layout.grow()),
    Key([mod, "control"], "h", lazy.layout.shrink()),

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Prev layout"),

    # Kill window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # ------------ Apps Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Rofi app selector"),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="Rofi app using selector"),

    # Discord
    Key([mod], "d", lazy.spawn("discord"), desc="Opens discord"),

    # Browser
    Key([mod], "b", lazy.spawn("firefox"), desc="Opens firefox"),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot"), desc="All window screenshot"),

    # Screenshot select
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="Screenshot select"),

    # File Explorer
    Key([mod], "e", lazy.spawn("thunar"), desc="File explorer"),

    # Night screen
    Key([mod, "shift"], "r", lazy.spawn("redshift"), desc="Screen protection"),


    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Volume up"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Brightness down"),
]

###################################
#           WORKSPACES            #
###################################

groups = [Group(i) for i in [" ", " ", " ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

################################
#           LAYOUTS            #
################################

border_color="#4f76c7"
layout_conf = {
    'border_focus': border_color,
    'border_width': 3,
    'margin': 10
}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

################################
#           WIDGETS            #
################################

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def powerline(bg, fg):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )

colors = [["#282C34", "#282C34"], # Not using
          ["#ff9f1c", "#ff9f1c"], # Orange
          ["#ffffff", "ffffff"], # Font
          ["#7d2181", "#7d2181"], # Purple
          ["#f07178", "#f07178"], # Red salmon
          ["#4f76c7", "#4f76c7"], # Blue
          ["#9b9b9b", "#9b9b9b"], # Current screen
          ["#181818", "#181818"]] # Bar border

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=colors[2],
                    background=colors[7],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=15,
                    border_width=1,
                    active=colors[2],
                    inactive=colors[2],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=colors[6],
                    this_screen_border=["#ABB2BF", "#ABB2BF"],
                    other_current_screen_border=["#282C34", "#282C34"],
                    other_screen_border=["#282C34", "#282C34"]
                ),
                widget.WindowName(
                    foreground= colors[5],
                    background= colors[7],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=16,
                ),
                powerline(colors[7], colors[3]),
                widget.TextBox(
                    background = colors[3],
                    foreground = colors[2],
                    text=' '  # Icon: nf-fa-download
                ),
                widget.CheckUpdates(
                    no_update_string='0',
                    colour_no_updates=colors[2],
                    display_format='{updates}',
                    foreground = colors[2],
                    execute='alacritty',
                    background = colors[3],
                    update_interval=1800,
                    custom_command='checkupdates'
                ),
                powerline(colors[3], colors[4]),
                widget.TextBox(
                    text=' ',  # Icon: nf-fa-feed
                    background=colors[4],
                    foreground=colors[2]
                ),
                widget.Net(
                    backbround=["#8BCD50", "#8BCD50"],
                    interface='wlp2s0',
                    background=colors[4],
                    foreground=colors[2]
                ),
                powerline(colors[4], colors[1]),
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=colors[1]
                ),
                widget.CurrentLayout(
                    background=colors[1],
                    foreground=colors[2]
                ),
                powerline(colors[1], colors[5]),
                widget.TextBox(
                    text=' ',
                    foreground=colors[2],
                    background=colors[5],
                    fontsize=20,
                ),
                widget.Clock(
                    foreground=colors[2],
                    background=colors[5],
                    format='%d/%m/%Y',
                    padding=0,
                    
                ),
                widget.Sep(
                    padding=18,
                    foreground=colors[2],
                    background=colors[5],
                ),
                widget.Clock(
                    foreground=colors[2],
                    background=colors[5],
                    format='%H:%M %p',
                    padding=0,
                    fontsize=18,
                    
                ),
                powerline(colors[5], colors[7]),
                widget.Systray(
                    icon_size=23,
                    background=colors[7],
                ),
                widget.Battery(
                    colour_charge=colors[6],
                    charge_char=' ',
                    discharge_char='',
                    format='{char} {percent:2.0%}',
                    background=colors[7],
                ),
            ],
            25
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], 
border_focus=border_color
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
