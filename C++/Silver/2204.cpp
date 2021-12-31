#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

bool checkCaptial(string a, string b) {
	for (int i = 0; i < a.size(); i++) {
		if (a[i] >= 'a' && a[i] <= 'z') {
			a[i] -= 32;
		}
	}

	for (int i = 0; i < b.size(); i++) {
		if (b[i] >= 'a' && b[i] <= 'z') {
			b[i] -= 32;
		}
	}

	if (a.compare(b) > 0) {
		return false;
	}
	return true;
}

int main(){
    while(true){
        int a;
        cin >> a;
        if(a==0) break;

        string *strArr = new string[a];

        for(int i = 0 ; i < a ;i++){
            cin >> strArr[i];
        }
        sort(strArr,strArr+a,checkCaptial);
        cout << strArr[0]<<endl;
        delete[] strArr;    

    }
}