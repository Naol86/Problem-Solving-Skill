#include <iostream>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

vector<int> solve(string s){
  long long int x;
  vector<int> ans;
  int temp = 1;
  for(int i = 1; i < s.length(); i ++){
    if (s[i] != s[i - 1]) {
      ans.push_back(temp);
      temp = 0;
    }
    temp += 1;
  }
  ans.push_back(temp);
  return ans;
}


vector<unsigned> facto() {
  vector<unsigned int> ans;
  unsigned int mod = 998244353;
  ans.push_back(1);
  for(int i = 1; i < (10^5) + 1; i++){
    int left;
    unsigned int back = ans.back();
    if (back){
      ans.push_back((back * i) % mod);
    }
    else {
      ans.push_back(i);
    }
  }
  return ans;
}




int main() {
  unsigned int x, mod = 998244353;
  vector<unsigned int> ans;
  ans = facto();
  string s;
  cin >> x;
  for(int i = 0; i < x; i ++){
    cin >> s;
    unsigned int anss = 1;
    vector<int> temp = solve(s);
    int leng = 0;
    for(int i : temp){
      if (i > 1){
        leng += (i - 1);
      }
      anss *= ans.at(i);
      anss %= mod;
    }
    cout << leng <<" "<< anss << endl;
  }
}