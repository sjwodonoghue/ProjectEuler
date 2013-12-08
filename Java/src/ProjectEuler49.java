
public class ProjectEuler49 {

	public static void main(String[] args){
		
		for (int i = 1001; i < 10000; i+= 2) {
			if (isPrime(i)) {
				
			}
		}
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

}
