#include <stdio.h>
/*
 general purpose devlopper sur linux
 Nomé un "system programming language" car utile pour coder des compileurs
 et des OS.
 contrairement à B et BCPL C possedes differents data type (string, integer...)
 C est un language asser low, àcd qu'il deals avec le même genre d'objet
 que les ordinateur(characters, num, adresses.)
 Ne propose pas d'oberateur pour directement interagir avec les composite objects
 C ne propose pas dde input/ouput facilities. Si  on veut avoir acces a des mécanisme
 de plus haut niveau il faut le faire explicitement, en appellant une fonction.
 C ne fonctionne que de manière direct, pas d'operation multiple ou simultanée.
 Garder le language le plus simple présente des avantages ; rapide a apprendre
 petit esapce.
 C match les capacité des differents ordinateur mais le codde ne change pas en
 fonction de la machine.
*/

// TUTORIAL INTRODUCTION

/*
#include <stdio.h> // Dit au compileur d'inclure la librerie standart input/output.

main() // defini une fonction "main" sans argument (parentheses)
{// contenu de la fonction.
    printf("hello, world\c salut"); // main appel la fonction printf
    // \n = new line.
}

*/

// Un prgramme en C, peut importe sa taille consiste en fonction et variables.
// Une fonction contien des statements qui specifie l'operation à exécuter.
// Les variables stocks des valeur qui vont etre utiliser durant ces opérations.

// on peut appeler no fonction comme on veut mais "main" est la ou le programme commence.
// Ca implique que tout les program doivent en contenir au moins h

// \n est un caractère invisible. Ainsi que \t (tab) et autre (voir 2.3)

// exercices : tester des bugs, + \c

// 1.2 variables and arithmetic expressions

/*
#include <stdio.h>

main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0; //set up initial value to function
    upper = 300;
    step = 20;

    fahr = lower;
    printf("Heading\n");
    while (fahr <= upper) // Create a loop
    {
        celsius = 5 * (fahr - 32) / 9;
        printf("%3.0f\t%6.0f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
*/

// Comments : line (//), paragraph (/**/)
// Variable doivent être declaré avant d'être utilisées. (en general au debut de la fonction)
// Declaration : anonce les propriétés des variables. Un type + list de variables.
// Int = integer (>< float => fractional part)
// Range depend de la machine (16, 32, 64-bit)
// DATA TYPE : char (characters), short (short integer), long (long integer), double (double precision floating point)

// Loop opearate as follow : check the condition in (), if true, the body is executed, and then the condition is retested...
//When it's false , the loop stop and continue to the statement right after it.
// Si body = one statement braces are unnecessary
// Dans C les fraction sont tronqué sur 0.

// Printf is an output formatting function. (cf chap 7)
// Comment avec "" qui indique ce qui va être imprimer
// % indique les endroit où les arguments seront substitué.
// %d précise un argument int.


// Qq problème avec ce première programme, pas joli car pas correctement justifié

// On peut changer %d avec un width %3d et %6d
// Si on veut plus précis on peut changer int to float => %3.0f
// Le 3.0 le zero indique le nombre de caractère après le decimal points.

// Maintenant on peut ecrire des fraction (3.0/9.0)

// %6.4f imprime un floating point, d'au moins 6 caractères de long et avec 4 chiffres après le point décimal.&
// %o = octal, %x = hexadécimal, %c = character, %s = character string, %% pour %


// The for statement : 

/*
#include <stdio.h>

main()
{
    int fahr;

    for (fahr = 300; fahr >= 0; fahr = fahr - 20)
        printf("%3d %6.1f\n", fahr,  (5.0/9.0)*(fahr-32));
}
*/


// Même output, mais de manière différentes
// CHangement principale : plus de variables
// Les variables sont devenues des cst et celsius est devenu un argument de print.

//For statement is a loop, a generalization of the while.
// Dans les parenthèses, 3 parts separates by ; :
// 1 fahr = 0 initialization, fait avant que la loope soit entrer.
// 2 fahr <= 300 test, condition à tester, si vrai body exécuter.
// fahr = fahr + 20 increment, executer avant que la condition soit re evaluer.

//While or for ? le plus clair, for pour loops avec init et incre sont des phrases simple et logiquement relate


// 1.4 symbolic constants
// peut être compliquer de changer 300 et 20 systematiquement.
// manière est de leurs donné des noms avec un sens. create a symbolic name/constant

/*
#define NAME repalcement-text //(conventionnellement en majuscule)
*/



//1.5 Character Input and Output

// modèle supporter par la librérie standard : Text input/output deal as a streams of characters.
// text stream = une sequences de characters divisé en lignes (0+ charac + \n)
// Plusieurs fonction qui permete de lire/ecrire des charactères (get/putchar simplest)
// getchar() : lit le next input character from a text stream et le return as its value.
// putchar() : print a caracter quand elle est appelé.

// Copier l'input to l'output one character at a time :

/*
#include <stdio.h>

main()
{
    int c;

    c = getchar();
    while (c != EOF) // EFO = end of file 
    {
        putchar(c);
        c = getchar();
    }
}
*/
// Getchar jusqu'a ce qu'il y ait un type de charactères qui ne peut pas se confondre avec un caractères reel (càd EOF)

// les assignement (tq c = getchar()) sont des expression et leur valeur, 
// on peut re ecrire : 
/*

#include <stdio.h>

main()
{
    int c;

    while ((c=getchar()) != EOF) // EFO = end of file 
    {
        putchar(c);
    }
}
*/


// parethèse necessaire pour la priorité d'ordre

//1.5.2 character couting

/*
#include <stdio.h>

int main()
{
    long nc;

    nc =0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);

    return 0;
}
*/

/*
#include <stdio.h>

int main()
{
    double nc;
    
    for(nc=0; getchar() != EOF; ++nc)
        ; // null statement
    printf("%.0f\n", nc);
}
*/

// Si il n'y a pas de for or while, test fails, produit 0 ce qui est correct. si y'a rien a faire, rien n'est fait.


//1.5.3 line counting


/*
#include <stdio.h>

main() 
{
    int c, nl;

    nl = 0;
    while((c=getchar()) != EOF)
        if (c=='\n')
            ++nl;
    printf("%d\n", nl);
}
*/

// Compte le nombre de "nouvelle ligne"

// implemente un if qui test la condition entre parenthèse :

// == càd "is equal to" pour differenciier test d'égalité de l'assignement.

// '' represente integer value egal à une valeur numerique : EX : 'A' = 65

// exercices : 
/*
#include <stdio.h>
#include <time.h>
int main()
{
    int bl, tab, nl;
    bl = 0;
    nl =0;
    tab = 0;

    int a;

    while ((a=getchar()) != EOF)
    {
        if (a==' ')
            ++bl;
        else if (a=='\n')
            ++nl;
        else if (a=='\t')
            ++tab;
    }

      printf("\nBlanks : %d\tTab : %d     \tNew lines : %d\n", bl, tab, nl); 

return 0;
}
*/

/*
int main()
{
    int c, wasBlank = 0; // Initialisez wasBlank à 0
    while ((c=getchar()) != EOF)
    {
        if (c == ' ')
        {
            if (!wasBlank) 
            {
                putchar(' ');
                wasBlank = 1;
            }
        }
        else 
        {
            putchar(c);
            wasBlank = 0;
        }
    } 

    return 0;
}

*/

// 1.5.4 word couting
#define IN 1
#define OUT 0

main()
{
    int c, nl, nw, nc, state;

    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF)
        ++nc;
        if (c=='\n')
            ++nl;
        if (c == ' '|| c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT)
        {
            state = IN;
            ++ nw;
        }
    
    printf("%d %d %d\n", nl, nw, nc);
}
