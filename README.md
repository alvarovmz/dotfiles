# alvarovmz's dotfiles

## Contents

* zsh
  * [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
* Vim
  * [python-mode](https://github.com/klen/python-mode)
  * [vim-surround](https://github.com/tpope/vim-surround)
  * Color scheme
* OSX
  * OS config
* Git
  * Config and aliases
* Python
  * Colors
  * History
  * Django project modules autoload
  * External Editor

## Install

- `git clone git://github.com/alvarovmz/dotfiles ~/.dotfiles`
- `cd ~/.dotfiles`
- `git submodule init`
- `git submodule update`
- `python bootstrap/bootstrap.py -i`

You must edit `gitconfig` file in order to set your personal commit data.

## Dependencies

* Vim: with ruby and python support (check your `vim --version`)
* jshint: npm install jshint

## Additional notes

Feel free to fork, send pull request, open issues...

## TODO

* Bootstrap
  * Uninstall
  * Backup current config
