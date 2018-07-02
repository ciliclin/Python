#!/bin/bash

WORK_PATH=`dirname $(readlink -f "$0")`

install_youcomleteme() {
	echo "<<install_youcomleteme>>"
	apt-get install build-essential cmake python-dev python3-dev -y
	cd ~/.vim/bundle/YouCompleteMe
	./install.py --clang-completer
	echo
}

copy_vim_dir() {
	#cd ~/.vim/bundle
	#git clone https://github.com/rkulla/pydiction.git
	echo "<<Copy vim dir>>"
	cd $WORK_PATH
	if [ -d /root/.vim ]; then
		mv /root/.vim /root/.vim.bak
	fi
	cat vim.bz2.parta* > vim.bz2
	#Single file limitation under 100MB for Github
	cd ~
	tar jxvf $WORK_PATH/vim.bz2
	echo
}

echo "==Initialize env setting=="
echo "Refer to https://realpython.com/vim-and-python-a-match-made-in-heaven/"
echo "Refer to https://blog.csdn.net/jeff_liu_sky_/article/details/53955888"

cp $WORK_PATH/.vimrc ~/

copy_vim_dir
#install_youcomleteme

echo
echo "Please run \"PluginInstall\" in vim"
echo "Installation is done"
