#include <iostream>
using namespace std;

int gcd(int x, int y) {
    while (y != 0) {
        int r = x%y;
        x = y;
        y = r;
    }
    return x;
}

int lcm(int x, int y) {
    return (x*y)/gcd(x,y);
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << gcd(a,b) << '\n';
    cout << lcm(a,b) << '\n';
    return 0;
}


