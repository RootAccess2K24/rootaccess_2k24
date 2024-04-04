#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/types.h>

#define COLOR_RED   "\033[1;31m"
#define COLOR_WHITE   "\033[1;37m"

int rand_num(){
	time_t t1;
	srand ( (unsigned) time (&t1));
	return t1%100;
}
void flagp(){
	char flag[64];
	FILE *file = fopen("flag.txt","r");
	if(file==NULL){
		printf("flag not found!\n");
		exit(0);
	} 
	fgets(flag,sizeof(flag),file);
	printf("%s",flag);
}

int game(){
	printf("\nGuess my number between 0-99: ");
	char usinp[400];
	scanf("%s",&usinp);
	int val = rand_num();
	char snum[100];
	sprintf(snum,"%d",val);
	if(strstr(usinp,snum)){
		printf("My number %s\n",snum);
		printf("Kudos!");
		return 1;
	} else{
		printf("My number %s\n",snum);
		printf("Not even close!");
		return 0;
	}
}

int main(){
	printf(COLOR_RED"\n.'''''..    ......     ......   .........        "COLOR_WHITE"   ..        ......    .....  .''''''.  .......   ......      \n ");
	printf(COLOR_RED"dOOOOKWO  ;OO0O0XNl .xOOOOOXN; 'OOOXNXX0;          "COLOR_WHITE":NX;     cdO0O0O; .lk0OOOx' cOOOOOOc .kKOOOOd..dX0OOOO;      \n");
    printf(COLOR_RED"....cx0k. cO   ..dX.,Wk   .'kO     lK'            "COLOR_WHITE"'KddXo   .kl'.     ;O;.       ....... ,Xdl:..   O0o:...       \n");
    printf(COLOR_RED".XXOOKMX'  xx  '00XW,:Wd  :00XK.   .OWl           "COLOR_WHITE";XX'.dWc  'NKo.     cNk'      cWXOOOOx. oOOOOOo. ;kOOOOO;      \n");
    printf(COLOR_RED".Xc  lXk.  xx   ..ON':Xl   .,K0    .dN;           "COLOR_WHITE"kMNO;.dk. .O0.      ,X:       cKk.....      lkXl     'x0O      \n");
    printf(COLOR_RED".O,   ,Od  'kxdddxOc .lkxdddkO;    .:O'          "COLOR_WHITE":kc... .k:  ;0kdddd,  lkddddd. .lO0OOOx..dxxkK0o. :xxxOKO'      \n");
    int count = 0;
    for(int i=0;i<5;i++){
    	count = count + game();
    }
    if(count == 5){
    	flagp();
    }
}
