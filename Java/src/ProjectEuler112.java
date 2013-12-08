public class ProjectEuler112 {
	
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();

		double proportion = 0;
		int i = 1;
		int myCount = 0;
		while (proportion != 0.99) {
			if (isBouncy(i) == 1) {
				myCount++;
			}
			proportion = (double)(myCount) / (double)(i);
			i++;
		}
		System.out.println(i - 1);
		System.out.println(proportion);

		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println(totalTime);
	}
	
	public static int isBouncy (int n) {
		//System.out.println("param is " + n);
		int[] nVal = int2Arr(n);
		//	If the number only has one or two digits then it cannot be bouncy.
		if (nVal.length < 3) {
			return 0;
		}
		//	Use int and floor to store the highest and lowest digit of our numbers thus far.
		//	If the next digit is between the ceil and floor values then we have a bouncy number.
		//	If next digit is higher of lower than ceil or floor respextively, then we reset 
		//	ceil and floor to be the new higher or lower value resp.
		int floor;
		int ceil;
		if (nVal[0] < nVal[1]) {
			floor = nVal[0];
			ceil = nVal[1];
			for(int i = 2; i < nVal.length; i++) {
				if (nVal[i] < ceil) {
					return 1;
				}
				else {
					ceil = nVal[i];
				}
			}
		}
		else if (nVal[1] < nVal[0]) {
			floor = nVal[1];
			ceil = nVal[0];
			for(int i = 2; i < nVal.length; i++) {
				if (nVal[i] > floor) {
					return 1;
				}
				else {
					floor = nVal[i];
				}
			}
		}
		//	If the first two digits are the same, remove the first digit 
		//	from the number and compute again.
		else if (nVal[0] == nVal[1]) {
			int exp = nVal.length - 1;
			int newNum = (int)(n - (nVal[0] * Math.pow(10, exp)));
			return isBouncy(newNum);
		}
		return 0;
	}
	
	
	/* 
	 * Contains errors, so is not to be used, kept for sake of records.
	 */
	public static int isBouncy_old (int n) {
		int[] nVal = int2Arr(n);
		if (nVal.length < 3) {
			return 0;
		}
		for (int i = 0; i < nVal.length - 2; i++) {
			int inner = nVal[i];
			for(int j = i+1; j < nVal.length - 1; j++) {
				int mid = nVal[j];
				int outer = nVal[j+1];
				//System.out.println("mid is" + mid);
				//System.out.println("outer is " + outer);
				if ((inner < mid && outer < mid) || (inner > mid && outer > mid)) {
					return 1;
				}
			}
		}
		return 0;
	}

	public static int[] int2Arr (int n) {
		String temp = Integer.toString(n);
		int[] newGuess = new int[temp.length()];
		for (int i = 0; i < temp.length(); i++) {
		    newGuess[i] = temp.charAt(i) - '0';
		}
		return newGuess;
	}
}


