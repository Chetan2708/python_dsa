import java.util.ArrayList;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int lar=Integer.MIN_VALUE;
        ArrayList<Boolean> numbers = new ArrayList<>();
        for (int i = 0; i < candies.length ; i++){
            if (candies[i] > lar){
                lar = candies[i];
            }
        }
        for (int i = 0 ; i < candies.length ; i++){
            if (candies[i] +  extraCandies >= lar ){
                numbers.add(true);
            }
            else{
                numbers.add(false);
            }
        }
        return numbers;
    }
}