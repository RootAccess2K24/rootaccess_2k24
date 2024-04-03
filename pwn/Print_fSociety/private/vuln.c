#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>

#define ANSI_COLOR_YELLOW     "\033[1;33m"
#define ANSI_COLOR_GREEN   "\033[1;32m"
#define ANSI_COLOR_RED   "\033[1;31m"
#define ANSI_COLOR_WHITE   "\033[1;37m"

int main(int argc, char **argv){
	setvbuf(stdout, NULL, _IONBF,0);

	char buf[64];
	char flag[64];
	char *flag_ptr = flag;

	gid_t gid = getegid();
	setresgid(gid,gid,gid);

	printf(ANSI_COLOR_GREEN"!!@#$%^&*()_+   @@@@@@@     @@@@@@@   @#$%^&*!@\n");
	printf(ANSI_COLOR_GREEN"!!        !!   @@$%#/$@@   @@$%#/$@@     $%    \n");
	printf(ANSI_COLOR_GREEN"!!        !!  @@       @@ @@       @@    #$    \n");
	printf(ANSI_COLOR_GREEN"!!@#$%^&*()_+ @@       @@ @@       @@    !@    \n");
	printf(ANSI_COLOR_GREEN"!!      !!     @@$%#/$@@   @@$%#/$@@     #$    \n");
	printf(ANSI_COLOR_GREEN"!!        !!    @@@@@@@     @@@@@@@      &*    \n");
	printf(ANSI_COLOR_YELLOW"Format might not be appropriate but go for it ~>\n");

	FILE *file = fopen("flag.txt","r");
	if(file==NULL){
		printf("flag not found!\n");
		exit(0);
	}
	fgets(flag,sizeof(flag),file);

	while(1){
		printf("# ");
		fgets(buf,sizeof(buf),stdin);
		printf(buf);
		printf("command not found\n");
	}
}