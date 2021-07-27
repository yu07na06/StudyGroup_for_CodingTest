/*
-> 노가다로 구현하려 함
-> 투 포인터 개념 몰랐음
*/

#include <stdio.h>

#define maxArray 10000

int main()
{
    int N, M, idx;
    int low = 0, high = 0, cnt = 0, sum = 0;
    int arrN[maxArray];

    scanf("%d %d", &N, &M);

    for (idx = 0; idx < N; idx++){
        scanf(" %d", &arrN[idx]);
    }
/*
    printf("N=%d, M=%d\n", N, M);
    for (idx = 0; idx < N; idx++){
        printf("%d ", arrN[idx]);
    }
    printf("\n");
*/
    while(1)
    {
        if (sum >= M) 
            sum -= arrN[low++];
        else if (high == N)
            break;
        else
            sum += arrN[high++];
        
        if (sum == M)
            cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}
