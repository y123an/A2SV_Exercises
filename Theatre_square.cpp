#include <iostream>
using namespace std;
#include <math.h>

int main()
{
    long double n, m, a;

    cin >> n >> m >> a;

    long long w = ceil(n / a);
    long long h = ceil(m / a);

    long long ans = w*h;

    cout << ans<<endl;
}