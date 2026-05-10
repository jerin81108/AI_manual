#include <stdio.h>
#define P 5
#define R 3

int main() {
    int alloc[P][R] = {{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}};
    int max[P][R]   = {{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}};
    int avail[R]    = {3,3,2};
    int need[P][R], work[R], finish[P], seq[P];
    int i, j, count=0, found;

    for(i=0;i<P;i++) for(j=0;j<R;j++) need[i][j]=max[i][j]-alloc[i][j];
    for(j=0;j<R;j++) work[j]=avail[j];
    for(i=0;i<P;i++) finish[i]=0;

    while(count<P) {
        found=0;
        for(i=0;i<P;i++) {
            if(!finish[i]) {
                int ok=1;
                for(j=0;j<R;j++) if(need[i][j]>work[j]){ok=0;break;}
                if(ok) {
                    for(j=0;j<R;j++) work[j]+=alloc[i][j];
                    seq[count++]=i; finish[i]=1; found=1;
                }
            }
        }
        if(!found) break;
    }

    if(count==P) {
        printf("No Deadlock. Safe Sequence: ");
        for(i=0;i<P;i++) printf("P%d%s",seq[i],i<P-1?" -> ":"\n");
    } else {
        printf("DEADLOCK DETECTED!\n");
    }
    return 0;
}
