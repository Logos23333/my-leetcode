import java.util.*;

public class leetcode {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        System.out.println(map.toString());
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement) };
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    public static void main(String[] args){
        int[] nums={1,2,3,2,3,3};
        int target =6;
        
        int[] result=twoSum(nums, target);
        for(int i=0;i<result.length;i++){
            System.out.println(result[i]);
        }
        
    }
}
