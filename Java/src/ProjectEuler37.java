
import java.util.Arrays;

public class ProjectEuler37 {

	public static void main(String[] args) {
		//int n = 12345;
		//System.out.println(rmLeft(n));
		//System.out.println(rmRight(n));
		
		int n = 11;
		int mySum = 0;
		int myCount = 0;
		while (myCount < 11) {
			if (isPrime(n)) {
				if (isTrunLeft(n) & isTrunRight(n)) {
					System.out.println("value of n is " + n);
					myCount++;
					mySum += n;
				}
			}
			n += 2;
		}

		System.out.println(mySum);
	}
	
	public static boolean isPrime(int n){
		n = Math.abs(n);
		if (n == 1) {
			return false;
		}
		if (n % 2 == 0) {
			return false;
		}
		else {
			for (int i = 3; i <= Math.sqrt(n); i = i+2) {
				if (n % i == 0) {
					return false;
				}
			}
		}
		return true;
	}


	public static int[] int2Arr (int n) {
		String temp = Integer.toString(n);
		int[] newGuess = new int[temp.length()];
		for (int i = 0; i < temp.length(); i++) {
		    newGuess[i] = temp.charAt(i) - '0';
		}
		return newGuess;
	}
	
	public static int rmLeft(int n) {
		int[] temp =  Arrays.copyOfRange(int2Arr(n), 1, int2Arr(n).length);	
		return arr2Int(temp);	
	}

	public static int rmRight(int n) {
		int[] temp =  Arrays.copyOfRange(int2Arr(n), 0, int2Arr(n).length - 1);	
		return arr2Int(temp);	
	}

	public static int arr2Int(int[] n) {
		String temp = "";
		for(int i = 0; i < n.length; i++) {
			temp += String.valueOf(n[i]);
		}
		if (temp.length() != 0) {
			return Integer.parseInt(temp);
		}
		else {
			return 0;
		}
	}
	
	public static boolean isTrunLeft(int n) {
		int nLen = int2Arr(n).length;
		for (int i = 1; i < nLen; i++) {
			n = rmLeft(n);
			//System.out.println(n);
			if(!isPrime(n)) {
				return false;
			}
		}
		return true;

	}
	
	public static boolean isTrunRight(int n) {
		int nLen = int2Arr(n).length;
		//System.out.println(nLen);
		for (int i = 1; i < nLen; i++) {
			n = rmRight(n);
			//System.out.println(n);
			if(!isPrime(n)) {
				return false;
			}
		}
		return true;
	}
		

}
