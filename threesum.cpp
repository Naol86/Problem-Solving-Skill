#include <iostream>
#include <vector>
#include<set>

using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> ans;
        int i, j, k;
        for (i = 0; i < nums.size(); i++)
        {
            for (j = i + 1; j < nums.size(); j++)
            {
                for (k = j + 1; k < nums.size(); k++)
                {
                    if (nums[i] + nums[j] + nums[k] == 0){
                        set<int> temp={nums[i],nums[j],nums[k]};
                        if ( temp.size()==3)
                        {
                            vector<int> temp2(temp.begin(),temp.end());
                            ans.push_back(temp2);
                        }
                    }
                }
            }
        }
        return ans;
    }
};

int main()
{
    Solution ob;
    vector<int> temp = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> ans;
    ans = ob.threeSum(temp);
    for (auto &str : ans)
    {
        cout << str << ' ';
    }
}