
import java.lang.Math.*;
import java.util.ArrayList;
import java.util.List;

public class ProjectEuler47 {

	public static void main(String[] args) {
				
		int proceed = 1;
		int i = 647;
		while (proceed == 1) {
			System.out.println(i);
			if (getNumPrimeDivs2(i) == 4) {
				if ((getNumPrimeDivs2(i+1) == 4) && (getNumPrimeDivs2(i+2) == 4) && (getNumPrimeDivs2(i+3) == 4)) {
					System.out.println(i);
					System.out.println(i+1);
					System.out.println(i+2);
					proceed = 0;
				}
				i++;
			}
			else {
				i++;
			}
		}
	}
	

	public static int getNumDivs (int n) {
		double lim = (n / 2) + 1;
		int numDivs = 0;
		for (int i = 2; i <= lim; i++) {
			if ((n % i) == 0) {
				numDivs++;
			}
		}
		return numDivs;
	}
	
	public static List<Integer> getDivs (int n) {
		double lim = (n / 2) + 1;
		List<Integer> divisors = new ArrayList<Integer>();
		for (int i = 2; i <= lim + 1; i++) {
			if ((n % i) == 0) {
				divisors.add(i);
			}
		}
		return divisors;
	}
	
	public static int isPrime (int n){
		if (getNumDivs(n) == 0) {
			return 1;
		}
		else {
			return 0;
		}
	}
	
	public static int getNumPrimeDivs(int n) {
		List<Integer> divisors = getDivs(n);
		int size = divisors.size();
		int count = 0;
		for (int i = 0; i < size; i++) {
			if (isPrime(divisors.get(i)) == 1 ) {
				count ++;
			}
		}
		return count;
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

	public static int getNumPrimeDivs2(int n) {
		List<Integer> divisors = getPrimeDivs(n);
		return divisors.size();
	}

	
	
}

