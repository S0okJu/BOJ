#include <stdio.h>

int ang(int n)
{
    if (n == 1)
        return 1;
    else if (n == 2)
        return 2;
    else if (n == 3)
        return 4;
    else
        return ang(n - 1) + ang(n - 2) + ang(n - 3);
}

int main()
{
    int t, n;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d", &n);
        printf("%d\n", ang(n));
    }
}