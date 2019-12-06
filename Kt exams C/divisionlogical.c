#include<stdio.h>
main()
{

int m1, m2, m3, m4, m5, per;

printf ("Enter marks in five subjects");
scanf ("%d %d %d %d %d", &m1, &m2, &m3, &m4, &m5);


per = (m1+m2+m3+m4+m5)/ 5 ;

if (per>=60)
printf ("First Division");

if ((per>=50) && (per<60))

printf ("Second Division");

if ((per>=40) && (per<50))

printf ("Third Division");

if (per<40)

printf ("Fail");

}
