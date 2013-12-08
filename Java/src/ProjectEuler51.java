import java.util.ArrayList;
import java.util.List;



public class ProjectEuler51 {

	public static void main(String[] args) {
		
		int i = 10872364;
		String eye = Integer.toString(i);
		String c = eye.substring(2,6);
		System.out.println(eye.length());
		
		System.out.println("Value is " + replaceDigit(198798, 3, 5));
		
		if (0.99 == 0.9900000) {
			System.out.println("They the same");
		}
	}
	
	public static List<Integer> getPrimeDivs (int n) {
		double lim = (n / 2) + 1;
		List<Integer> divisors = new ArrayList<Integer>();
		if ((n % 2) == 0) {
			divisors.add(2);
		}
		for (int i = 3; i <= lim + 1; i+=2) {
			if (((n % i) == 0) && (isPrime(i) == 1)) {
				divisors.add(i);
			}
		}
		return divisors;
	}

	public static int getNumPrimeDivs(int n) {
		List<Integer> divisors = getPrimeDivs(n);
		return divisors.size();
	}

	public static int isPrime (int n){
		if (getNumPrimeDivs(n) == 0) {
			return 1;
		}
		else {
			return 0;
		}
	}
	
	public static int replaceDigit(int num, int digit, int rVal) {
		int numLen = Integer.toString(num).length();
		int exp = numLen - digit + 1;
		int curDigit = getNthDigit(num, exp);
		num = (int)(num - (curDigit * Math.pow(10, exp - 1)));
		num = (int)(num + (rVal * Math.pow(10, exp - 1)));
		return num;
	}
	
	public static int getNthDigit(int number, int n) {    
		  return (int) ((number / Math.pow(10, n - 1)) % 10);
	}

	
	
}
