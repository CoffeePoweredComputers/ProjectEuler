#include <stdio.h>

int main(){
	int smallest_num = 1;
	while(1){
		int found = 1;
		for(int i = 1; i < 21; i++){
			if(smallest_num % i != 0){
				found = 0;
				smallest_num++;
				continue;
			}
		}
		if(found){
			break;
		}
	}
	printf("%d\n",smallest_num);
	return 0;
}
