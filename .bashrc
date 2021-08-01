#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\] '

alias config='/usr/bin/git --git-dir=/home/franc/dotfiles/ --work-tree=/home/franc'
alias grub-update='grub-mkconfig -o /boot/grub/grub.cfg'
alias bat='cat /sys/class/power_supply/BAT0/capacity'
alias ls='exa --icons --group-directories-first'
alias la='exa --icons --A --group-directories-first'
alias tree='exa --tree --icons'
alias ..='cd ..'
