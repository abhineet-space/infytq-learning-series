#include<bits/stdc++.h>
using namespace std;
int printNum(int n){
    if(n==1){
        cout<<1<<endl;
        //return 1;
    }
    printNum(n-1);
    cout<<n<<endl;
    //return 99;

}
int main(){
    printNum(7);
    return 0;
}

