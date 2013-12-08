
public class ProjectEuler34 {

	
	public static void main(String[] args) {

		int mySum = 0;
		for (int i = 3; i < 10000000; i++) {
			if (sumFactDigs(i) == i) {
				mySum += i;
			}
		}
		
		System.out.println(mySum);
	}
	
	public static int factorial(int n) {
		int ans = 1;
		for (int i = 1; i <=n; i++) {
			ans *= i;
		}
		return ans;
	}
	
	public static int[] int2Arr (int n) {
		String temp = Integer.toString(n);
		int[] newGuess = new int[temp.length()];
		for (int i = 0; i < temp.length(); i++) {
		    newGuess[i] = temp.charAt(i) - '0';
		}
		return newGuess;
	}
	
	public static int sumFactDigs(int n) {
		int[] temp = int2Arr(n);
		int mySum = 0;
		for (int i = 0; i < temp.length; i++) {
			mySum += factorial(temp[i]);
		}
		return mySum;
	}

}
