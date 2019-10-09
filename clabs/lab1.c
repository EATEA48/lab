#include <stdio.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
float a,x,g,f,y;
printf("Vvedite x: ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
g=4*(-4*a*a+a*x+5*x*x)/(-20*a*a+28*a*x+3*x*x);
printf("g=%f\n\n", g);

printf("Vvedite x ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
f=atan(24*a*a-25*a*x+6*x*x);
printf("f=%f\n\n", f);

printf("Vvedite x ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
y=log(2*a*a-7*a*x+6*x*x+1);
printf("y=%f\n\n", y);
}
