/*  
    QUESTION FROM LEETCODE
    
    Given int array, return true if can reach last index
    Ex. nums = [2,3,1,1,4] -> true, index 0 to 1 to last

    Greedy: At each point, determine furthest reachable index

    Time: O(n)
    Space: O(1)
    
    ---
    
    Track the furthest reachable position and stop as soon as we know
    we can reach the end.
    
    Time: O(n) - Best case can be much faster with early termination
    Space: O(1)
    
    Key optimization: Stop immediately when we know we can reach the end.
*/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxReach = 0;  // Furthest index we can reach
        
        for (int i = 0; i <= maxReach && i < n; i++) {
            // If we've already reached or passed the last index, we're done
            if (maxReach >= n - 1) {
                return true;
            }
            
            // Update the furthest reachable position
            maxReach = max(maxReach, i + nums[i]);
        }
        
        // Check if we reached or passed the last index
        return maxReach >= n - 1;
    }
};
