#include<bits/stdc++.h>
using namespace std;

int power(int base, int expo){
    if(expo<0){
        throw expo;
    }else if(expo==0){
        return 1;
    }else if(expo%2==0){
        return power(base*base, expo/2);
    }
    else{
        return base*power(base, expo-1);
    }
}

bool palindrome(string s){
    if(s.length()<2){
        return true;
    }else{
        char first = s[0];
        char last = s[s.length()-1];
        if(first==last){
            string rest = s.substr(1, s.length()-2);
            return palindrome(rest);
        }else{
            return false;
        }
    }
}

void printbinary(int n){
    if(n<2){
        cout<<n;
    }else{
        int lastdigit = n%2;
        int restofdigits = n/2;
        printbinary(restofdigits);
        printbinary(lastdigit);
    }
}

// void reverseLines(ifstream& input){
//     string line;
//     if(getline(input, line)){
//         reverseLines(input);
//         cout<<line<<endl;
//     }
//     else{

//     }
// }

int main(){
    cout<<power(3,2)<<endl;
    cout<<palindrome("raecar")<<endl;
    printbinary(11);
    return 0;
}
