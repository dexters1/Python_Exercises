// generated using template: main.template
//---------------------------------------------------------------------------------

/*********************************************************************************
**
**  Module Name: main.c
**  Description:
**            Main file
** 
**  Author: Igor Ilic
**  Date:   03.08.2020 15:58:21
**********************************************************************************/

// generated using template: include.template
//---------------------------------------------------------------------------------

#include <math.h>
#include "block_functions.h"
#include "func.h"// generated using template: main_block.template
//---------------------------------------------------------------------------------


int main(int argc, char *argv[])
{

	/* Lokalne promenjljive */
	float blok1_var = 0.0f;
	float blok2_var = 0.0f;
	
	/* Pozivi funkcija */
	blok1_var = ulaz();
	blok2_var = sinus(blok1_var);
	izlaz(blok1_var);
	izlaz(blok2_var);
	
return 0;
}