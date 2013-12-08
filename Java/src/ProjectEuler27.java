

public class ProjectEuler27 {

	
	public static void main(String[] args) {
		int myCount = 0;
		int maxA = 0;
		int maxB = 0;
		
		for (int a = 999; a > -1000; a--) {
			for (int b = -999; b < 1000; b++) {
				if(isPrime(b)) {
					int n = 0;
					boolean proceed = true;
					while(proceed) {
						int tempVal = (int)(Math.pow(n, 2)) + (a * n) + b;
						if(isPrime(tempVal)) {
							n++;
						}
						else {
							proceed = false;
						}
					}
					if(n > myCount) {
						myCount = n;
						maxA = a;
						maxB = b;
						//System.out.println("----------------------------");
						//System.out.println(myCount);
					}
				}
			}
		}
		System.out.println(maxA);
		System.out.println(maxB);
		System.out.println(myCount);
		System.out.println(maxA * maxB);
	}
	
	
	
	public static boolean isPrime(int n){
		n = Math.abs(n);
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
}
