#include<iostream>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        int temp = 1;
		while((x>>temp) <= x){
			temp++;
		}
		return --temp;
    }
};

int main()
{
	cout<<"sd";
}