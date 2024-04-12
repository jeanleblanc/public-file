# Vim cheat sheet of the week  



  
Can be Devided into 3 part   
- vim motion : edit et navigate code
- vim editeur : load files and edit  
- vim plugins : extend fonctionnality  
  
## Vim motions  
  
3 modes :  
- normal  
- insert  
- normal  
  
Plusieur clavier l'un au dessus de l'autre  
  
normal : deplacement  
insert : ecrire  
visul : select and minupulate text   
 VIsual  :   
 - normal visual :  pareil que la souris  
 - block visual : select txt as a block  
  
provide leader key, more layer of short cut   
  
COmmand mode : donner des commande à l'éditeur de txt  
  
**w** is for save  
  
Navigate en normal mode :   
up down left right : kjhl resp. peuvent être combiné avec un nombre : 5j = 5x down  
  
**Horizontal motion**  
w = en avant mot par mot  
b = inverse  
end of the word : e en avant   
$ fin de la ligne   
0 debut de la ligne   
^ premier non empty caractere  
f+charactères va au prohcain charactère de la ligne   
F+char = va au dernier charactere de la ligne  
  
**Vertical motion**  
() = une ligne en haut en bas resp  
{} = un paragraphe  
ctrl d et ctrl u = up and down half a page  
ctrl f et ctrl b = full page  
gg = debut   
G = fin  
  
**Insert**  
i = insert avant char  
a = insert après char  
I = debut de la ligne  
A = fin de la ligne  
o = insert à la ligne suivant   
O = insert à la ligne d'avant.  
c = change a word  
s = replace + insert  
  
y = yanks  
p = paste  
yy = copy la ligne  
yi+( ou { ou [= copie entre parenthese ou brace exclude (  
ya + = copie include (  
  
u = undo de last change  
ctrl r = redo  
  
d = delete  
d + w = delete word  
d + s = delete sentence  
d + p = delete paragraph  
d + d = line  
d + t + char = delete to char  
  
. = repeat key,   
  
/ + terme = va rechercher le termes a partir du curseur  
navigate over thoses termes = n en avant N en arrière  
* = recherche le mot courant après  
\#  = recherche en arrière  
  
book mark  
m + char = marque la position sous le char  
altgr7 + char = retourne à la marque  
Predifine book mark  
altgr7 altgr7  = last two position   
altgr7 . = last editing position  
        