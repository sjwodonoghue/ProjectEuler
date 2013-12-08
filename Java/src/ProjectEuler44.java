
import java.lang.Math.*;

public class ProjectEuler44 {

	public static void main(String[] args) {
		int i = 1;
		int proceed = 1;
		int ans = 0;
		while (proceed == 1) {
			int p = getPentNum(i); 
			for (int j = 1; j < i; j++) {
				int ptmp = getPentNum(j);
				int sum = p + ptmp;
				int diff = p - ptmp;
				if ((isPentNum(sum) == 1) && (isPentNum(diff) == 1)){
					System.out.println(Math.abs(diff));
					int D = Math.abs(diff);
					if (D < ans) {
						ans = D;
					}
					else if (((double)(D) / ans) > Math.pow(10, 6)) {
						proceed = 0;
					}
				}
			}
			i++;
		}
		
	}
	
	public static int getPentNum(int n){
		return (n * (3*n -1)) / 2;
	}
	
	public static int isInt(double x)	{
		double x_floor = Math.floor(x);
		if (x_floor == x) 
			{	return 1;	}
		else
			{	return 0;	}
	}

	public static int isPentNum (int x) {
		double n = (Math.sqrt((24 * x) + 1) + 1) / 6;
		if (isInt(n) == 1) {
			return 1;
		}
		else {
			return 0;
		}	
	}
	
}
