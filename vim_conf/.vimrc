set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)
" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set splitbelow
set splitright
"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"Enable folding
set foldmethod=indent
set foldlevel=99

"Enable folding with the spacebar
nnoremap <space> za
Plugin 'tmhedberg/SimpylFold'
let g:SimpylFold_docstring_preview=1

"proper PEP 8 indentation
au BufNewFile,BufRead *.py
			\ set tabstop=4 |
			\ set softtabstop=4 |
			\ set shiftwidth=4 |
			\ set textwidth=79 |
			\ set expandtab |
			\ set autoindent |
			\ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css
			\ set tabstop=2 |
			\ set softtabstop=2 |
			\ set shiftwidth=2

Plugin 'vim-scripts/indentpython.vim'

"Flagging Unnecessary Whitespace
highlight BadWhitespace ctermbg=red guibg=darkred
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"UTF-8 Support
set encoding=utf-8

"Auto-Complete
"Bundle 'Valloric/YouCompleteMe'
"let g:ycm_autoclose_preview_window_after_completion=1
"map <leader>q  :YcmCompleter GoToDefinitionElseDeclaration<CR>

"Syntax Checking/Highlighting
Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'
let python_highlight_all=1
syntax on

"Color Schemes
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
if has('gui_running')
	set background=dark
	colorscheme solarized
else
	colorscheme zenburn
endif
call togglebg#map("<F5>")

"File Browsing
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

"Super Searching
Plugin 'kien/ctrlp.vim'

"Line Numbering
"set nu

"Git Integration
Plugin 'tpope/vim-fugitive'

"Powerline
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

"System Clipboard
set clipboard=unnamed

"Pydiction
filetype plugin on
let g:pydiction_location = '/root/.vim/bundle/pydiction/complete-dict' 
let g:pydiction_menu_height = 3
