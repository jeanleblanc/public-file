#physique #synthèse 

# Programme (qualification) :

### FLUIDES, STATIQUE

~~Notion de pression~~. ~~Hydrostatique~~. ~~Poussée d’Archimède~~. ~~Loi de Boyle et Mariotte~~. Composition et décomposition de forces. Moment de force. Équilibre. Leviers et machines simples. Loi de Hooke (ressorts). Loi du frottement sec (F = k.N).

### DYNAMIQUE

Lois de Newton : principe d’inertie, loi fondamentale de la dynamique, principe des actions réciproques.

### TRAVAIL, ÉNERGIE, PUISSANCE

Travail et puissance d’une force. Énergie cinétique, potentielle de gravitation et potentielle élastique. Bilans d’énergie.

### OPTIQUE

Lois de la réflexion et de la réfraction, réflexion totale. Images formées par les miroirs plans et les lentilles. Lentilles (formules de conjugaison, grandissement).

### ÉLECTROCINÉTIQUE

~~Intensité de courant.~~ ~~Résistance.~~ ~~Énergie et puissance électrique.~~ ~~Circuits électriques.~~

### FORCES ET MOUVEMENTS

MRU, MRUV. Vitesse et accélération instantanées. Mouvement circulaire uniforme. Force centripète. Loi de la gravitation universelle. Lois de Kepler. Tir balistique.

### ÉLECTROSTATIQUE

Quantité d’électricité. Force et champ électriques, DDP électrique.

### ÉLECTROMAGNÉTISME

Sources de champ magnétique, force de Laplace et de Lorentz, flux magnétique, lois de Lenz et de Faraday et auto-induction. Transformateur électrique.

### OSCILLATIONS ET ONDES

Période, fréquence, oscillateur harmonique (pendule simple, ressort). Résonance. Ondes mécaniques. Vitesse de propagation, longueur d’onde, propriétés générales (Doppler, modes stationnaires, diffraction, interférences). Ondes électromagnétiques.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f3684df-730d-41ae-864a-e08c845396e2/Untitled.png)

# Analyse dimensionnelle et grandeurs du SIU
voir wikipedia

# Fluide et statique

**Un fluide** est une chose qui prend la forme de son contenant. (gaz et liquide)

Les liquides, contrairement aux gaz, sont **incompressible**, càd que le volume est constant.

**La densité** d’un corps $(d)$ rapport entre sa masse volumique et celle d’un corps de référence.

Pour les liquide et solide $\rho_{ref} = \rho_{eau} = 1000 (kg/m^3)$

La densité est sans dimension.

$d=\frac{\rho_{objet}}{\rho_{ref}}=\frac{\rho_{objet}}{\rho_{eau}}$

L’intérêt de connaître la densité d’un objet elle qu’elle représente le pourcentage de l’objet immerger. Par exemple si la densité d’un objet est de 0,6 alors 60% de l’objet sera immergé dans l’eau.

Si la densité est supérieur à 1 l’objet va alors coulé dans l’eau.

**Principe de pascal :** ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Si j’applique une pression à un fluide incompressible, cette pression est distribué équitablement dans tout le fluide. Donc la pression est la même en tout point du liquide à une hauteur donné.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Exemple
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d0add54-4266-460c-ae78-6158697b7257/Untitled.png)
    

## Notion de pression

Dans le cas d’une action mécanique, la pression est la force exercé par quantité de surface. Quand on applique une force sur un objet et que celui-ci l’applique lui même sur autre chose, la force appliqué sur l’objet sera alors répartis dans toute la surface de contacte entre les deux objets. Donc, au plus la surface est petite, au plus la force va être concentrée. On établis alors la loi suivante :

$$ P = \frac{F}{V} $$

Les unité sont donc $N.m^{-2} = kg \cdot m\cdot s^{-2} . m^{-2} = ML^{-1}T^{-2}$ aussi appelé Pascal (Pa).

Les fluides exercent une pression tout comme les solides. Un corp dans un liquide subit le pression du liquide au dessus de lui. Ainsi, plus un liquide est profond, plus la pression sera importante. Pour les gaz, cela se passe exactement de la même manière.

Donc si un objet tombe dans l’eau, la pression exercée sur lui est de : $P=\frac{F}{S}$ où F est le poids de la colonne d’eau au dessus de l’objet, elle est donc de $m_e g$ (me la masse de l’eau au dessus de l’objet). On peut exprimer Me en fonction de la masse volumique de l’eau et de volume : $m_e = \rho_e V_e$. On peut alors injecter dans la formule de base et simplifier avec V=S.h :

$P = \rho_ehg$

On remarque alors ici que la pression ne dépend plus de la surface mais plus que de la masse volumique de l’eau (ou de tout autre liquide) ainsi que de la profondeur de l’objet. On montre ici que la pression ne dépend nullement de l’objet.

$P = \rho hg$

Il est à noté que la pression ne s’applique pas qu’au dessus de l’objet.

La pression est une grandeur scalaire.

La pression absolue est la mesure de la pression par rapport au vide (on ajoute la pression atmosphérique). Elle ne peut pas être négative. Souvent inutile car pression atmosphérique quasiment la même partout sur terre.

$P_{absolue}=\rho hg + P_{atm}$ on utilise $\rho$ air seulement quand on veut calculer la pression à une altitude donnée.

$P_{atm} = 1,01 \times 10^5 Pa$ (au niveau de la mer)

La Pression relative est la pression absolue sans la pression atmosphérique.

$P_{abs}=P_r+P_{atm}$

Les unités utilisé sont le Pascal (Pa), mais d’autres sont également utilisé :

Atmosphère (atm) = $1,01\times 10^5(Pa)$

Le bar = $10^5 (Pa)$

## La poussé d’Archimède

C’est quand on immerge un objet dans un liquide, cet objet émet une force ascendante dont l’amplitude est égale au poids du liquide déplacer.

-   ********************************Démonstration********************************
    
    On place dans un bassin d’eau un cube de dimension $d$. L’objet va alors subir une pression de chaque côté, la pression étant la même pour chaque point à une hauteur donné, les pression à droite et à gauche vont s’annuler. L’objet subit donc 2 forces, $F_2$ et $F_1$ étant respectivement la force au dessus et en dessous de l’objet.
    
    $F_2 = P_2 \times d^2$
    
    $F_1 = P_1 \times d^2$
    
    On peut dire que $P_1>P_2 \iff F_1>F_2$ car le point 1 étant plus bas que le point 2 la pression est donc plus grande.
    
    La force total qui s’applique sur le cube est donc
    
    $F_{tot} = F_1 -F_2$ (F2 négatif car opposé a F1)
    
    $= P_1\times d^2 - P_2\times d^2 \\ = (P_1-P_2)d^2\\ =(\rho (h+d)g - \rho hg)d^2$ car la distance 1 est juste la distance 2 plus une longueur du cube.
    
    $= (h+d-h)\rho g d^2$ Les $h$ s’annulent et les $d$ s’assemblent.
    
    $F_{tot}=d^3\rho g$
    
    $d^3$ (le volume) $\times$ $\rho$ (la masse volumique) = $m$ (la masse)
    
    $m\times g =$ le poids du liquide déplacé $= P_{archimède}$
    

$P_{A} = \rho g V_{fluide} (N)$

Si le poids d’un objet est supérieur à la poussé d’Archimède qu’il subit, cet objet va couler. Dans le cas contraire l’objet flotte.

Si la masse volumique d’un objet est plus grande que celle du fluide dans lequel il est immerger, cet objet coule.

-   Démonstration
    
    Le poids et la poussé d’Archimède sont opposé donc :
    
    $F_{tot} = P_{A} - P\\ =\rho_f V_f g -mg \\ =\rho_f V_f g - \rho_o V_o g \\ = Vg(\rho_f-\rho_o)$ car si l’objet est totalement imerger les volumes sont les mêmes.
    
    On peut clairement voir que si la masse volumique de l’objet est plus grande, la valeur de la parenthèse sera négative donc la force résultante sera orienté vers le bas.
    

Théorème d’Archimède : **Tout corps plongé dans un fluide subit une force verticale, dirigée vers le haut, et dont l'intensité est égale au poids du volume de fluide déplacé ; cette force est appelée poussée d'Archimède.**

$P_A = P_{fluide}$

Il est à noté que la poussé d’Archimède ne dépend pas de la profondeur.

## La loi de Boyle-Mariotte et thermodynamique

$PV =nRT$

Pression, volume, nombre de mole, constante des gaz parfaits, température.

Une des loi de la thermodynamique constituant la loi des gaz parfaits.

$P_1 \times V_1 = P_2 \times V_2$ (si la température est constante)

# Electrostatique

****Effet triboélectrique :**** phénomène électrostatique créé par la mise en contact de deux matériaux de nature différente. Il survient lorsqu'une partie des électrons de la surface de contact de l’un des deux matériaux est transféré à l’autre et que ce transfert subsiste lors de la séparation. L'effet triboélectrique peut être augmenté par un apport d'énergie mécanique en frottant les matériaux l'un contre l'autre (friction).

1 coulomb (C) = $|6,24 \times 10^{18}|$ fois la charge d’un proton ou électron ça correspond à la quantité de charge transportée en 1s par un courant de 1A. Et donc la charge d’un électron $(q_e)$ = $1,6 \times 10^{-19}(C)$ (l’inverse). aussi appeler charge élémentaire.

Charge nette : sommes des charges d’un objet. On la calcul par le nombre de proton et d’électron. Dans le cas d’un transfère de charge, seul les électrons se déplace. Un électron, ne pouvant pas se diviser en un plus petit élément, ne permet qu’une charge nette multiple entier de sa charge.

## La loi de Coulomb

$F_e = k \frac{|q_1\times q_2|}{d^2}$

Coulomb essaye de prévoir la force électrostatique (attractive ou répulsive) entre deux charge.

Rapport entre la valeur absolue du produit des charge et cette force diminue en fonction de la distance.

A noter qu’un parallélisme peut être fait avec la formule de la gravitation universelle de Newton $(F_g=G\frac{m_1\times m_2}{d^2})$. La constante de newton étant bien plus faible la force gravitationnelle sera plus faible que celle électrique.

Comme c’est une Force les unités sont des Newton.

La constante de Coulomb est de $9\times 10^9(N\cdot m^2\cdot C^{-2})$

******************************************Conservation de la charge :****************************************** dans une système isoler (aucune charge ne rentre ni sort), la sommes des charges est constante

$\Sigma_q =$ constante. Donc peut importe les réactions qui se font dans ce système, la charge ne changera pas. En outre, on ne peut ni crée, ni détruire une charge.

Par exemple un photon (charge nulle) peut se diviser en deux particule, une électron et un antiélectron/positrons (identique à un électron mais de charge opposé). Comme ils ont la même charge mais opposé, la sommes de leurs charge sera nulle.

**Un matériau conducteur** : Les électrons peuvent se déplacer librement.

****Un matériau isolant :**** L’inverse, les électrons ne peuvent pas se déplacer.

**************************************Un condensateur :************************************** permet de stocker une charge. Sa capacité indique le nombre de charge qu’il peut stocker.

## Courant électrique

Le **courant électrique** est un déplacement de charges. Les déplacements de charges créent le courant électrique. On dit qu’il est continu quand le flux de charge est constant et dans la même direction.

Le sens du courant est représenté par une flèche qui correspond toujours au sens de circulation des charges positives.

Sa grandeur = **intensité**. Quantité de charge passant à travers une surface par unité de temps.

$I=\frac{dq}{dt}$ (d pour des valeurs infinitésimales) = ampère

**La tension électrique** est la variation de d’Energie potentielle électrique par unité de charge.

C’est assez difficile de se représenter ce qu’est la tension (analogie avec la gravité pour 1 charge seule)

$\Delta E_{pe}=qU \leftrightarrow U= \frac{\Delta E_{pe}}{q}$ (différence d’énergie potentielle électrique, charge, tension → $\neq$ ?) = volt

Cf. [](https://www.youtube.com/embed/kS25vitrZ6g?rel=0)[https://www.youtube.com/embed/kS25vitrZ6g?rel=0](https://www.youtube.com/embed/kS25vitrZ6g?rel=0) (Feynman sur l’électricité)

**La puissance électrique** est l’énergie électrique échangée par unité de temps. Sont unité est le joule par seconde ou Watt $(W) \rightarrow 1W = 1J/s$.

La puissance est donc $P=\frac{dE}{dt}$. Comme on sait que le courant est un flux de charges n par unité de temps et que la tension mesure l’énergie transférée par unité de charge on peut réécrire :

$P=\frac{dE}{dt} = \frac{dE}{dq}\cdot \frac{dq}{dt} = UI$

On peut réécrire selon la loi de Ohm $(U=RI)$ :

$P=RI^2 = \frac{U^2}{R}$

Courant alternatif ?

## Résistances et loi de Ohm

**Conducteur parfait** : matériaux dans lequel les charges peuvent bouger sans être ralentis.

**Résistance** : matériaux qui ralenti les charges. va permettre de réduire le flux d’un courant.

Résistance électrique : Mesure de la force avec laquelle s’oppose un objet au passage d’un courant électrique. Unité sont des Ohm $(\Omega \implies \frac{kg\cdot m^2}{s^3\cdot A^2})$ dépend du matériaux de la température (augmente car plus d’E cinétique.) de la longueur et de la surface de section.

Résistivité $(\rho)$ mesure delà force ave c laquelle un matériau donné s’oppose au passage d‘un courant électrique. $(\Omega \cdot m)$

Loi d’Ohm : $U=RI$. Ce qui nous donne une définition de la résistance : $R = \frac{U}{I}$. Il est à noté que pour des conditions et un matériaux donné la résistance est constante ; U et I sont dépanadant l’un de l’autre.

Si la résistance augmente, l’intensité diminue (tension constante).

Si la résistance augmente, la tension augmente (intensité constante).

**Circuit en série** : Les éléments sont mit les uns à la suite des autres sans embranchement. Le courant est le même partout (intensité constante), la différence de potentiel est répartie entre les résistances, la tension la plus élevée sera aux bornes de la résistance la plus grande.

$R_{tot} = R_{éq} = \displaystyle\sum_{i} R_i$

************************************Circuit en parallèle :************************************ Circuit où il y a des embranchement, le courant n’est pas le même partout, il est répartis entre les résistances, la différence de potentiel est la même aux bornes de chaque résistance. Le courant sera le plus élevé dans la résistance la plus fiable.

$R_{tot} = \displaystyle\sum_{i} \frac{1}{R_i}$

Une batterie transforme l’E chimique en électrique (parfaite = sans résistance).

Force électromotrice est la différence de potentielle produite par une source de tension. (V)

## Ampèremètre et Voltmètre

Ampèremètre permet de connaitre le courant qui traverse quelque chose, il faut alors qu’il soit branché en série et qu’il ait une résistance faible, car si la résistance était élevée on modifierai la quantité de courant et fausserai les donnée de l’ampèremètre. Si on le brancherai en parallèle, tout le courant préfèrerai passé dans l’ampèremètre (car résistance très faible), il va donc grillé.

Le Voltmètre car on cherche a mesuré la tension au borne d’un composant, càd de part et d’autre. Cherche la tension en un point n’a pas d’intérêt car elle est la $\neq$ de potentiel électrique en deux point. Comme il est branché en parallèle, il se doit d’avoir un très grande résistance car si non le courant passerais uniquement par le voltmètre,

## Lois de Kirchhoff

# Forces

## Réaction normale et force de contact

Une réaction normale c’est la force exercée par une surface sur un objet en contact avec elle, qui évite que l'objet passe au travers. C’est une force électromagnétique, résultante des répulsion qui s’exercent à l’échelle de chaque atome (les e- se repoussent). C’est une force de contact. Elle est perpendiculaire à la surface, a l’inverse d’une force de frottement qui elle sera parallèle à la surface.

La force de réaction est due à l’ampleur de la déformation de la surface ou du volume d’une surface. → vont chercher à revenir spontanément à leur forme naturelle.

On peut déterminer une réaction normale grâce à l’accélération selon la direction perpendiculaire à la surface. Donc, on utilise la 2ème loi de Newton que l’on peut exprimer en fonction de l’accélération $(a=\frac{\Sigma F}{m})$. Pour un objet simplement poser sur une surface horizontale, la norme de la réaction normale sera de $mg$.

## Force de frottement

**Statique** : La force qui empêche le glissement entre deux surface.

Il est de même intensité que la force de poussée, de même direction mais de sens opposé. On peut constater que la force de frottement statique maximal est plus grande la celle de frottement cinétique (il est plus difficile de commencer a pousser un objet que de perpétuer le mouvement)?

**Dynamique :** Si les deux surfaces glissent, on parle de frottement dynamique (ou cinétique). Cette force s’oppose au mvmt et freine.

$f_c =\mu_cR_N$ où $f_c$ la force de frottement, $\mu_c$ le coefficient de frottement cinétique qui est sans unité, et $R_N$ La réaction normale. On remarque en effet que celui-ci ne dépend pas de la surface car il est une force ponctuel, donc si l’on modifie la surface on diminue la force en chaque points et cela s’équilibre avec le frottement.

En statique :

$f_{s \space max} = \mu_sR_N$.

Il est à noter qu’il s’agit de la force maximal, ainsi si la force maximal est de 50 N et que l’on exerce une force de poussé de 40 N sur une machine à lavée la force de frottement sera de 40 N. Si l’on pousse avec une force strictement supérieur à 50N alors on ne parle plus de force de frottement statique mais cinétique.

**Un plan incliné** : surface oblique sur laquelle un objet peut descendre ou monter en glissant ou roulant ou tout simplement posé. C’est l’un des 10 type de machine simples.

On considère donc les donnés dans un autre plan telle que $a_{\perp}=\frac{\Sigma F_{\perp}}{m}$ et $a_{||}=\frac{\Sigma F_{||}}{m}$. On peut quasiment toujours supposé que $a_{\perp} = 0$. Les composante du poids peuvent être exprimer par rapport à l’axe : $P{\perp}=mg \sin\theta$ et $P|| =mg\cos\theta$

-   car
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/55bb9e23-d63a-4a0d-b837-7c0c6cc1fccf/Untitled.png)
    

En statique : $R_N = mg\cos\theta$ où thêta est l’angle entre l’axe horizontal et l’axe perpendiculaire a la surface.

## Couple et équilibre

Couple ($\tau)$ est une mesure de la capacité d’une force à provoquer la rotation d’un objet autour d’un axe. ($ML^2T^{-2}$ mais pas des joules). Le couple résultant est la somme des couples appliqués à un système. Lorsque le couple résultant appliqué à un système est nul il y a un équilibre de rotation.

Un bras de levier est un segment qui lie l’axe de rotation à la ligne d’action de la force. (m)

Le pivot ou axe de rotation ou encore point de fixation est le point autour duquel un objet tourne.

$\tau = rF\sin\theta = F_\perp r$ . Couple positif = sens trigonométrique.

-   car
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/839d2824-cb5f-4bac-b752-f89e1518dbcc/Untitled.png)
    

## Moments

Presque la même chose qu’un couple, on le calcule de la même manière. La distance entre l’axe de rotation et la force s’appelle bras de levier. En statique, la somme des moment dans un sens égal la somme des moment dans l’autre sens.

La différence avec un couple, c’est qu’un moment est une grandeur physique tandis qu’un couple est la résultante d’une distribution de forces dont la somme vectorielle est nulle.

## Effet de levier.

L'effet de levier est un concept de physique qui décrit la capacité d'une force appliquée à un bras de levier à faire tourner un objet autour d'un axe de rotation. Le bras de levier est la distance entre l'axe de rotation et le point où la force est appliquée. Plus le bras de levier est long, plus la force appliquée aura d'effet de levier.

Le rapport entre les distance du point de pivots sera le nombre de fois la force nécessaire pour faire bouger l’autre côté.

Donc $F_2.d_2 = F_1.d_1$

## Poulie et cale

$W_e=W_s$ donc

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e43fc3a-e477-44e5-b6bb-3bf3eae80451/Untitled.png)

On peut établir la même chose pour l’énergie potentiel.

$E_p =mgh=F_e.d$, on voit que si on augmente la distance la force diminue, donc sur un plan incliné la force est plus faible.

## Force de tension

C’est une force exercé par un fil (câble corde ou chaine) sur un autre objet. C’est une force de traction, on ne peut pas exercé une poussé avec une corde.

**Calculer une force** : Faire bilan des forces exercées sur l’objet, Exprimer la deuxième loi de Newton $(a=\frac{\Sigma F}{m})$ selon l’axe de la direction de la force voulue, isoler cette force.

# Travail et Energie

****************************L’Energie**************************** est la capacité d’une système à produire un travail. Le travail est un mouvement d’Energie. S’exprime en joule = 1 Newton pour déplacer un objet de 1m.

Kilocalorie = Quantité d’énergie nécessaire pour élever 1kg d’eau de 1°C.

1kilocalorie = 4184 J.

On peut donc écrire, pour un objet de masse $m$ est déplacé d’une distance $d$ sur une surface horizontale sous l’action d’une force parallèle à cette surface : $W = m\times a\times d = F\times \Delta x$. Si la force est parallèle. Si non $W=F\Delta x \cos\theta$.

Si l’on veut soulever un objet alors : $W=mgh$

Si la force n’est pas constante, on peut alors tracer un graphique de la force en fonction de la distance, le travail sera alors l’air sous ce graphique.

-   Visualisation
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a485e40a-1f5e-446f-a8ae-ed632f04d6cc/Untitled.png)
    

Si un travail fourni à un systè-me est positif (moteur), le système reçoit de l’énergie provenant de son environnement. Si un travail fourni à un système est négatif (résistant), le système donne de l’énergie à son environnement. Il est négatif quand le déplacement et la composante parallèle au déplacement de la force sont de sens opposé.

Une force concervatrice est une force dont le travail dépend uniquement des positions initiaale et finale. Le travail net est nul lorsque les positions de départ et de fin sont les mêmes.

Une force non concervatrice est une force dont le travail dépend du chemin suivit (force de forttement).

**************L’E cinétique ($E_c$)** est l’E que possède un corps du fait de son mouvement par rapport à un référentiel donné. Elle dépend de la masse et de la vitesse.

$E_c = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 = \frac{1}{2}mv^2$

Pour un objet ponctuel de masse m, parcourant un chemin reliant deux points, la variation d’Ec est $\Delta E_c = W_{tot}$

**L’E potentielle de pesanteur** est le travail qu’un objet peut fournir du fait de sa position dans un champ de pesanteur.

A l’echelle planétaire, le champ gravitationnelle n’est pas uniforme.

On peut dire $E_p (d) = -\frac{Gm_1m_2}{d}$.

Quand on est infiniment loins l’Energie potentielle gravitationnelle est nulle.

Cela permet de déterminer l’énergie nécessaire pour se déplacer d’un corps à l’autre dans le syst-me solaire.

Un puit gravitationnel est l’altitude qu’il faut “franchir” pour pouvoir passer d’une corps planétaire à un autre.

**le principe de conservation de l’énergie** dit que dans un système fermé, la somme des énergies est constante. On écrit alors pour un système :

$E_{ci} + E_{pi} +E_{pei} = E_{cf}+E_{pf}+E_{pef}+Q_f$ Ou alors sous la forme complète :

$\frac{1}{2}mv^2_i + mgh_i + \frac{1}{2} kx^2_i = \frac{1}{2}mv^2_f + mgh_f + \frac{1}{2} kx^2_f + Q_f$

******L’Energie mécanique****** est la somme de l’énergie potentielle et de l’énergie cinétique d’un système :

$E_m = E_p + E_c$

********L’Energie thermique******** est la quantité d’E contenue dans un système en fonction de sa température. Elle se transfère sous forme de chaleur.

La variation d’E thermique totale lors d’un frottement entre deux objet peut être exprimer selon une vitesse constante. $\Delta E_t = \mu_c F_N d$

La force de trainée exercée sur un objet en mouvement dans un fluide, c’est quand on déplace un objet dans un fluide, on le met en mouvement, ainsi le mouvement macroscopique du fluide est redistribué en une multitude de mouvement microscopiques. Ces mouvement sont causent d’une augmentation de l’énergie thermique du système.

La puissance est une mesure de la vitesse à laquelle un travail est fourni. En d’autre termes, c’est une Energie par unité de temps. Son unité est le watt $(W)$, $1W = 1J/s$ donc $P = \frac{\Delta E}{\Delta t}$.

Il existe trois manières d’exprimer la puissance :

La puissance instantanée $(P_i)$, la puissance mesurée à un instant donné. ($\Delta t \rightarrow0)$

La puissance moyenne $P_{moy}$, est la puissance mesurée sur une longue periode. $(\Delta t>)$. On peut la calculer en déterminant l’air sous la courbe $P(t)$ et de diviser cette valeur par la durée.

La puissance maximal $P_{max}$ est la valeur maximale que peut prendre la puissance instantanée dans un système particulier sur une longue période.

Pour relié la puissance et le mouvement on peut remplacer le travail par son expression

$P = \frac{F \Delta x cos \theta}{\Delta t}$ et donc si la trajectoire est parrallèle ç la fore $P=Fv$

On peut également ecrire $P_i = m.a.v$ il est à noté qu’il s’agit bien d’une puissance instantanée ici car on a à la fois l’accélération et la vitesse, comme la vitesse change au fil du temps, cette expression n’a de sens que si on prend la vitesse à un moment donné. Si non on peut utiliser la vitesse moyenne : $P_{moy} = m. a.\frac{1}{2}(v_f - v_i)$

Les chevaux vapeur métrique désigne la puissance nécessaire pour soulever une masse de 75kg sur une distance de 1m en 1s. $1ch = 735,5W$

## Chaleur et Energie thermique

$\Delta Q = mc\Delta T$. la quantité d’énergie c’est la masse fois la capacité thermique massique fois la différence de température.

$c_{eau}= 4186 J/kg.K$

dans un système isoler, la somme des transfère de chaleur est nulle. $Q_1+Q_2+Q_3 = 0$

L’Enthalpie de changement d’état c’est la variation d’entalpie qui accompagne un certain changement d’état. $\Delta H_{1\rightarrow2}$. L’Energie nécessaire à un changement d’état est $Q = m\Delta H_{1\rightarrow2}$.

$\Delta H_{l\rightarrow v} = 2,3 \cdot10^6 J/kg$

Il existe 3 mode de transfère thermique :

Conduction thermique. Il va y avoir une réaction atomique exothermique. échange d’E au seins d’un même système sans déplacement de matière (dans un même corps ou entre deux corps)

Convection, Déplacement de matière l’air chaud s’élève (car plus dense) et l’air froid va en bas.

Rayonnement, accéleration des particules chargées → rayonnement électromagnétique, on en voit une partie.

$\phi = \frac{Q}{t} = \lambda S \frac{\Delta T}{e}$ où la fraction est le flux thermique ou la quantité d’érgie thermique qui traverse la surface par unité de temps. $S$ l’air de la membranne, $\Delta T$ la différence de température entre les deux matériaux, $e$ l’épaisseur de la membrane, et $\lambda$ la constante de conductivité thermique du matériaux. Les unités sont des joules par seconde ou plutot des Watt.

# Propagation de la lumière

**La réflexion**

Spéculaire, un rayon rentre sur un miroir avec un certain angle incident et en ressort avec le même angle par rapport à la normale. Il est dit spéculaire car unique. La surface dioptrique est la surface sur laquelle le rayon va se réfléchir. Le diporte est surface dioptrique + milieu 1 + milieu 2

$\theta_i = \theta_r$

**La diffusion** elle se produit quand la surface n’est pas complement plane ou qu’il y a des interaction spécifique entre l’onde et la matière. Les rayon son réfléchis dans toutes les directions.

**La réfraction**, il se produit lorsque la lumière rentre dans un corps, la rayon lumineux est dévié, plus proche de la normale.

L’indice de réfraction $(n)$ d’un milieu exprime sa capacité à lralentire la lumière $(n=\frac{c}{v})$.

$\frac{\sin\theta_i}{\sin\theta_r} = \frac{n_2}{n_1}$ $n_1\cdot\sin\theta_i = n_2\cdot\sin\theta_r$. Au plus le milieu dans lequelle la lumière rentre est lentk au plus celle-ci va se raprocher de la normale.

Ces equation indique que pour une différence d’indice de milieu donnée, il y a un angle d’incidence maximum, au delà duquel les rayons ne savent plus passer du miliu lent à rapide (TOUJOURS).

$\theta_{lim} = \arcsin \frac{n_2}{n_1}$. Si $\theta_i > \theta_{lim}{}$ alors reflexion.

**Dispersion** : Un rayon de lumière blanche (composé de toute les longueurs d’onde du spectre du visible) sera décomposé au contacte de l’eau. Car l’indice de réfraction est différent pour chaque couleur du spectre, donc toutes les lumières se séparent.

## Optique géométrique

Une lentille est un objet fait d’un matériel transparent pouvant faire converger ou diverger la lumière. Une lentille convergente peut être représentée comme l’addition de deux cercles, alors qu’une divergente correspond à l’espace entre deux cercles.

-   voir
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec32e5d0-85c7-4477-8200-ebe27611e0f0/Untitled.png)
    

Elle est décrite par la position des centres des cercles qui la composent. On les appelle centre de courbures $(R_1, \space R_2)$. L’axe optique est une droite qui passe par les deux centres de courbure.

Les lentilles construise des images, réel (convergente) ou virtuelle (divergentes).

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d6687580-c6af-480c-bf0a-8123b8488453/Untitled.png)

La distance focale $(f)$ est la distance qui sépare les centre de la lentille de l’image formée par des rayons parallèle à l’axe. Positif pour les convergente et négatives pour les divergentes,.

Le foyer image $(F')$ et le foyer objet $(F)$ → $O \pm f$ resp.

On peut noter les formules : $\frac{1}{f} = (n-1)(\frac{1}{R_1}- \frac{1}{R_2})$ et

$\frac{1}{f} = \frac{1}{p'} -\frac{1}{p}$ pour les lentille convergente $\frac{1}{f'} = \frac{1}{p'} -\frac{1}{p}$ pour les divergente . Ici $n>1$. p et p’ sont les position de l’objet et de l’image, resp. par rapport au centre optique.

Ainsi $\frac{p}{p'}=\frac{AB}{A'B'}$ (AB la hauteur de l’objet).

Dans le cas d’une lentille convergente, $f>0$, $p' > 0$, $p<0$. Pour une lentille divergente $f'<0$, $p'<0$, $p< 0$. La lumière se déplacent de gauche à droite.

La vergence $C$ (ou puissance d’une lentille) est l’inverse de la distance focale : $C = \frac{1}{f}$. L’unité est en dioptrie ($D$ ou $\delta$).

**Propriété d’une lentille convergente :** un rayon parallèle à l’axe optique converge toujours dans la direction du foyer image et inversement. Un rayon passant par le centre optique n’a pas été dévié.

Grâce à ces propriétés, on peut construire une image, l’image d’un objet est l’endroit vers lequel tous les rayons qu’il émet convergent (après la lentille).

Le grandissement est donc le rapport entre la taille de l’image et l’objet $\gamma = \frac{A'B'}{AB}$

Dans le cas ou il y a plusieur lentille le grandissement totale est $\gamma_{tot} = \gamma_1 \cdot \gamma_2$

Ainsi, pour une lentille convergente,

Si l’objet est placé au delà de -2F, l’image est plus petite et renversée,

Si l’objet est placé à -2F, l’image est plus grande et renversée.

Si l’objet est pladcé entre -2F et -F, l’image est plus grande et renversée

si l’objet est placé” szur -F il n’y à pas d’image (elle se forme à l’infini).

Si l’objet est plac” avant -F, elle est virstuelle plus grande et droite.

************************Propriété d’une lentille divergente,************************ Un rayon parallèle à l’axe optique converge comme s’il semblait venir de F, un rayon qui se dirige vers F’ ressort parrallèlement. un rayon qui passe par le centre optique n’est pas dévié.

L’image construite sera toujours droite, plus petite et virtuelle. mais plus on est proche plus l’image est grande.

Si deux lentille sont très proche, on peut fusionner leurs convergence suivant $\frac{1}{f}=\frac{1}{f_1}+\frac{1}{f_2}$

Aberration chromatique et aberration spérique ?

## Miroirs

??

# Mouvements

**L’acceleration** Caractérise tout mouvement où il y a une variation du vecteur vitesse (vitesse + direction) donc changement de vitesse ou direction = accélération. Dans el cas du mouvement à une dimension, l’accel $a=\frac{\Delta v}{\Delta t}$ en $m/s^2$. Nombre de metre par seconde dont varie la vitesse algébrique chaque seconde.

Si l'accélération pointe dans le même sens que la vitesse algébrique, alors l'objet accélère. Si elle pointe dans le sens opposé, alors l'objet ralentit.

$v_ = v_0+a\Delta t \\ \Delta x = v_0\Delta t + \frac{1}{2}a\Delta t^2\\ v^2 = v_0^2 + 2a(\Delta x)\\ \Delta x = \frac{1}{2}(v_0 +v)\Delta t$

## MCU

L’acc centripète est l’accel qui provoque le mcu d’un objet. Toujours dirigé vers le centre du cercle. Elle ne fait que modifié la direction du vecteur vitesse, elle n’est pas cause d’un changement de vitesse. La force centripète disigne toutes forces causant le mcu d’un objet.

$\Theta$ = déplacement angulaire

$\omega$ = vitesse angulaire

L’Axe de rotation est l’axe autour duquel un objet peut tourner.

Accéleration angulaire ($\alpha)$ moyenne est la mesure du taux de variation de la vitesse angulaire par rapport au temps. (positive pour le sens trigonomètrique)

Accèleratin tangentielle $(a_t)$ est l’accélération linéaire d’un objet en rotatin perpendiculaire à l’accélération radiale.

$v=\omega r$, $\alpha = \frac{\Delta \omega}{\Delta t}$, $a_t = \alpha r$

$a_c = \frac{v^2}{R}$

# Lois de Newton

**Première loi de Newton : principe d'inertie** Un objet au repos reste au repos ou, s'il est en mouvement, conserve son vecteur vitesse constant, sauf s'il est soumis à une résultante des forces extérieures non nulle.

**************************************************Deuxième loi de Newton :**************************************************

$\Sigma F = ma$ ou encore $a = \frac{\Sigma F}{m}$

**Troisième loi de Newton : principe d'action - réaction** Si un objet A exerce une force sur un objet B, alors l'objet B exerce une force de même valeur et de sens opposé sur l'objet A.

## Lois universelle de la gravitation

La Force d’attractrion graavitationelle est la force d’attraction que deux corps de masse non nulle exercent entre eux

Le champ gravitationelle est un modèle qui permet d’expliquer la tendance d’un corp à exercer une force sur d’autre son intensité en un point donné s’exprime en $\frac{m}{s^2}$. l’intensité est noté $g_i$ et est par définition la force d'attraction gravitationnelle par unité de masse.

On note $m_i$ la masse inerte d’un corp. Si deux corps ont la meme masse inerte ils présentent la même accélération lorsqu’il sont soumis à la même force.

On note $m_p$ la masse pesante. C’est une propriété de la matière qui cause l’action d’un force sur un objet pacé dans un champ gravitationnel.

D’après les expériences $m_i = m_p$

La force d’attraction gravitationelle entre deux masse ponctuelles est proportionelle à leurs masse et inversement proportionelle à le carré de la distance qui les séparent.

$F_g = \frac{Gm_1m_2}{r^2}$

$g_i = \frac{F_g}{m_2} = \frac{Gm_1}{r^2}$ où $g_i$ est l’intensité du champ gravitationnel. donne pour résultat l’intensité du champ gravitationelle exercé par la masse $m_1$ sur tout coprs de masse $m_2$.

## Tir balistique

Un vecteur vitesse peut être décomposé en deux vecteurs, horizontal et vertical.

$||v_{ix}|| = \sin \theta \cdot||v_i||$ et $||v_{iy}|| = \cos \theta \cdot||v_i||$

Le temps passé en l’air d’un objet en négligeant le frottement de l’air. $t_a = \frac{v_i}{g} = \frac{||v_i||\sin\theta}{g}\cdot2$

Un objet va avencer horizontalement de manière constante.

La distance parcouru d’un objet va donc être de $d(\theta) = \frac{2\cdot||v_i||^2}{g}\cdot \cos\theta\sin\theta$

l’angle optimal, ou la distance va être la plus grande est $d'(\theta) = 0$. càd 45°.

Il est à noté que si un objet tombe d’une falèse avec une vitesse horizontale initiale, on considère généralement la vitesse verticale initiale comme nulle.

Si on est dans le cas d’un plan incliner il faut connaître les valeurs de chacunes des composantes et ensuite trouver l’hypoténuse.

# Mouvement ossillatoire

type de mouvement périodique

Ossillateur harmonique : 1/ Pos equ. stable. 2/ il ne doit pas y avoir de perte d’E. 3/ accéleration prop et de sens oposé à la pos.

$T$ la période en s

$f = \nu = \frac{1}{T}$ la fréquence en $s^{-1}$

equation de la position

$x (t) = A\sin(\omega t +\phi_o)$

équation de la vitesse

$v (t) = A\omega\sin(\omega t +\phi_o + \frac{\pi}{2})$

équation de l’accel.

$a (t) = -\omega^2 x(t)$

$F_r = -k\Delta x$ où $\Delta x$ est l’éllongation.

$F_{tot} = mg-kx$ à l’équilibre $=0$

$a = -\frac{k}{m}x \\ \omega = \sqrt{\frac{k}{m}} \\ T = 2\pi \sqrt{\frac{m}{k}} \iff \nu = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$. Il est donc à noté que la periode ne dépend pas de l’ossillation.

$E_{tot/mec}= E_c + E_{pe} = \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kA^2$

Dans un pendule simple

# Electro-magnétisme

************************************La regle de la main droite :************************************ Le champ magnétique entour le fil en cercles concentrique. Pouce dans la direction du courant nos doigts entoure le fil dans le sens des ligne du champ magnétique B.

## Le magnétisme

il y a deux pole, qui s’attire oposément.

Un aiment est un dipôle magnétique.

Les pôles sont dépandant l’un de l’autre. si on casse un aiment en deux on va tout de même retrouver le dipole.

1 Tesla (T) = 1 $\frac{Ns}{c.m}$ est l’amplitude du champ magnétique B. Il caractèrise l’amplitude de la force subie par une charge en mouvement dans le champ. le gauss : $1T = 10^4 G$

$\vec{F}= Q(\vec{v} \wedge \vec{B})$ avec Q la charge, v la vitesse et B la valeur du champ magnétique.

On peut ré-écrire $|F| = Q \times |\vec{v}| \times|\vec{B}| \times \sin\theta$

Une chaarge imobile ne ressent pas le champ magnétique.

**La regle de la main droite** : pouce premier vecteur, indexe deuxième vecteur majeur est la resultanted. Sauf que rentrant dans un champ magnétique, la vitesse d’une charge va changer à chaque instant. ce qui va donner un mcu avec comme force centripète la force résultante.

On peut calculer le rayon de la trajectoire d’une charge :

$R = \frac{m\cdot |\vec{v}|^2}{|\vec{F}|}$ (éximpré en m)

On peut re ecrire la formule selon $\vec{v} = \frac{\vec{l}}{t}$, $\vec{F} = I(\vec{l} \wedge\vec{B})$ où l est le vecteur déplacement. Il est à retenir que le resultat d’un produit vectoriel est toujours perpendiculaire aux deux autres vecteurs.

La force magnétique induit un courant → charge qui bouge.

Le travail de cette force $W = \vec{L} \cdot \vec{F}$ Donc $\frac{W}{Q} = \vec{L}(\vec{v}\wedge \vec{B})$. qui sont des joules par coulomb et donc des voltes. Donc une tension (ddp). Dans ce cas on dit Force electromotrice (FEM).

$FEM = |\vec{L}||\vec{v}||\vec{B}|$

Le flux magnétique est une quantité de champ magnétique qui passe à travers une surface donnée.

On peut noter $\Phi = BA\cos\theta$ où A est l’air traverrsée par un champ magnétique B et $\theta$ l’angle entre les vecteurs du champ magnétique et la surface. Unité Weber (Wb) sont des $T\times m^2$.

La densité de flux magnétique est $Wb/m^2$

La force magnétique est une composante de la force e-m. Du au mouvement de charge.

## Electromagnétisme

Une des 4 forces fondamentales

Un fil dans lequel passe un courant, il crée sont propre champ magnétique. en fait magnétisme et electrique sont la même chose mais de deux pdv différent.

$|\vec{B}| = \frac{\mu I}{2\pi R}$ où $\mu$ est une constante appelé perméabilité, elle est en $kg .m.A^{-2}.s^{-2}$. dans le vide $\mu_0 = 4\pi 10^{-7}$. R est la distance avec le fil electrique, ou le rayon du cercle que forme les vecteur composant.

L’induction electromagnétique est le processus par lequel un courant est induit (généréà par un champ magnétique variable.

La loi de faraday $\xi = \frac{d\Phi}{dt}$ où $\xi$ est la FEM et $\Phi$. L’amplitude de la FEM.

loi de Lenz renseingne sur le sens que va prendre le courant. $\xi = -\frac{d\Phi}{dt}$. Opposé au flux qui l’a induit.

On peut re écrire $\xi = -N\frac{d\Phi}{dt}$ où N corespont le nombre de bobines qui induit le champ magnétique.

## Champ électrique

## Champ magnétique

Notion qui décrit comment la force magnétique est distribuée dans l’espace autour et à l’intérieur d’un coprs magnétique. Rigoureusement parlant, un champ de vecteurs de force représente en chaque point l'amplitude et la direction que la force aurait sur une particule ponctuelle qui serait placée en ce point.

Il est décrit mathématiquement par un champ de vecteurs. On peut le voir comme un quadriage qui en chaque point comporte une “boussole” qui pointe dans la direction de la force et dont l’amplitude du vecteur vaut la force. On peut aussi représenter l’information contenue dans le champ de vecteurs en utilisant des lignes de champ ; ces lignes ne se croisent jamais, elle se concentrent naturellement dans les région de l’”espace où le champ magnétiqu est le plus intense, pas de début ni de fin, va de nord vers le sud.

C’est une grandeur vectorielle → direction et amplitude. Direction = bousole.

Il apparait dès lors qu’une charge est en mouvment.