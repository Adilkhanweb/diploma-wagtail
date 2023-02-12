export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w $\[\033[00m\] '
shopt -s histappend
readonly PROMPT_COMMAND="history -a"
readonly HISTFILE
readonly HISTFILESIZE 
readonly HISTSIZE 
readonly HISTCMD 
readonly HISTCONTROL 
readonly HISTIGNORE
[[ -f ~/.profile ]] && . ~/.profile
[[ -f ~/.bashrc ]] && . ~/.bashrc
export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w $\[\033[00m\] '
