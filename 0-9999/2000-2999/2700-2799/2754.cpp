#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main(){
    string a;
    float score; 
    cin >> a;
    
    if(a=="A+")
        score= 4.3; 
    else if(a=="A0")
        score= 4.0; 
    else if(a=="A-")
        score= 3.7; 
    else if(a=="B+")
        score= 3.3; 
    else if(a=="B0")
        score= 3.0; 
    else if(a=="B-")
        score= 2.7; 
    else if(a=="C+")
        score= 2.3; 
    else if(a=="C0")
        score= 2.0; 
    else if(a=="C-")
        score= 1.7; 
    else if(a=="D+")
        score= 1.3; 
    else if(a=="D0")
        score= 1.0; 
    else if(a=="D-")
        score= 0.7; 
    else if(a=="F")
        score= 0.0; 
    
    printf("%.1f",score);
    
}