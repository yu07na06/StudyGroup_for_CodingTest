#include <iostream>
#include <cmath>
using namespace std;
int n, t[100002];
int main() {
    // 알칼리는 음수, 산성은 양수
    cin>>n; for(int i=0;i<n;++i) cin>>t[i];
    
    int s=0, e=n-1, as=0, ae=n-1, min_sum = 1e11;
    while(s<e) {
        int combined = t[s]+t[e];
        //cout << s << ", " << e << " :: " << combined << '\n';
        
        if(min_sum > abs(combined)) {
            min_sum = abs(combined);
            as=s, ae=e;
        }
        
        if(combined == 0) {
            as=s, ae=e;
            break;
        } else if(combined > 0) {
            e--;
        } else if(combined < 0) {
            s++;
        }
    }
    cout<<t[as]<<' '<<t[ae];
    return 0;
}
