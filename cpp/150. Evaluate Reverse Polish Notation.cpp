#include <iostream>
#include <stack>
#include <vector>
#include <math.h>

using namespace std;

class Solution {
public:
	int convert(string str){
		if(str.length() == 1 && !(int(str[0]) > 47 && int(str[0]) < 58)){
			return 300;
		}
		else
		{
			int i = 0;
			bool sign = false;
			if (str[0] == '-'){
				i = 1;
				sign = true;
			}
			int count = 0;
			int len = str.length();
			for(i;i<len;i++){
				count += (int(str[i]) - int('0')) * pow(10,len-i-1);
			}
			if (sign){
				return -1 * count;
			}
			return count;
		}
	}
    int evalRPN(vector<string>& tokens) {
		stack<int> temp;
		for(int i = 0; i < tokens.size(); i++){
			int op = convert(tokens[i]);
			if (op != 300)
				temp.push(op);
			else{
				int a,b,op;
				a = temp.top(); temp.pop();
				b = temp.top(); temp.pop();
				string h = tokens[i];
				op = int(h[0]);
				switch (op)
				{
				case 43:
					temp.push(a + b);
					break;
				case 42:
					temp.push(a * b);
					break;
				case 45:
					temp.push(a - b);
					break;
				case 47:
					temp.push(a / b);
					break;				
				default:
					break;
				}
			}
		}
        return temp.top();
    }
};
