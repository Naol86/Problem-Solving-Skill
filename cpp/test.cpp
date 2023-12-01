#include <iostream>
#include <unordered_map>
#include <set>

using namespace std;


int main()
{
	unordered_map<string, int> lis;
	lis["one"] = 1;
	lis["two"] = 2;
	lis["three"] = 3;
	set<int> lis2 = {1,2,7,3,4,5,3,2};
	for(auto i : lis2){
		cout<<i<<endl;
	}
}
