include <stdio.h>

#include <stdlib.h>

#include <math.h>
 


static long code[256]; /* Массив частот символов */

long sum=0;

float entr=0, prob, log2;

FILE *sfile;

int i, ch;



/**************/

void main(int argc, char *argv[])

 {

 if( argc < 2 )

   { printf("\n\nSyntax: ENTR SrcFile"); exit(1); }

 if( (sfile=fopen(argv[1],"rb")) == NULL )

   { printf("\n\nUnable to Open SrcFile"); exit(2); }

 /* Подсчитываем частоты символов */

 while( (ch=fgetc(sfile)) != EOF )

   { code[ch]++; sum++; }

 log2=log(2);

 /* Рассчет энтропии */

 for( i=0; i < 256; i++ )

   {

   if( code[i] == 0 ) continue;

   prob=code[i]/(float)sum; entr-=(prob*log(prob)/log2);

   }

 printf("\n Bytes: %8ld, Entropy= %6.3f, \

         Relative Entropy= %6.1f\%", sum,entr,entr/8*100);

 }
