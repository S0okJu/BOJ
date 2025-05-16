#include<iostream>
#include<string>
using namespace std;

int main()
{
    string patient, doctor;
    string ans="go";
    cin >> patient;
    cin >> doctor;

    if(patient.length() < doctor.length())
    {
        ans = "no";
    }
    else{
        ans="go";
    }
    cout << ans;
    return 0;
}