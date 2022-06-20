#include<stdio.h>

int max(int a, int b)
{
    return a >b ? a : b;
}
int main(){
    int N;
    int maxPrice = 0;
    scanf("%d",&N);

    for(int i = 0 ;i<N;i++)
    {
        int dice1, dice2, dice3;
        int maxValue = 0;
        int price = 0;
        scanf("%d %d %d",&dice1, &dice2,&dice3);

        if(dice1 == dice2 && dice2 == dice3)
            price+=(10000 + 1000*dice1);
        else if(dice1 == dice2 || dice1 == dice3)
            price +=(1000+dice1*100);
        else if(dice2 == dice3)
            price +=(1000+dice2*100);
        else
        {
            maxValue = max(dice1,dice2);
            maxValue = max(maxValue,dice3);
            price += (maxValue*100);
        }
        maxPrice = max(maxPrice, price);
    }

    printf("%d",maxPrice);
    return 0;
}