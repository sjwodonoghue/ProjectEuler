/*

Solution algorithm to Project Euler problem 39. http://projecteuler.net/problem=39.

*/

import java.lang.Math.*;
import java.util.*;

public class ProjectEuler39 {

	public static void main(String[] args) {
		
		List<Integer> pvals = new ArrayList<Integer>();
		//	Check each possible unique pair of integers that cannot sum to more than 1000 and get hypoteneuse.
		//	If hypoteneuse is an integer, and perimeter is below 1000, add perimeter to list.
		for (int i = 1; i < 500; i++) {
			for (int j = i; j < 500; j++) {
				double hypoteneuse = getHypoteneuse(i,j);
				if ((isInt(hypoteneuse) == 1) && (i + j + hypoteneuse <= 1000)) {
					pvals.add(i + j + (int)(hypoteneuse));
				}
			}
		}
		//	Sort the list (This is crucial!).
		Collections.sort(pvals);
		//	This array holds the current most found perimeter and the number of times it occurs will be 
		//	replaced with new values if we find a more common perimeter.
		int[] pair = {pvals.get(0), 1};
		int psize = pvals.size();
		//	This is temporary version of pair array. 
		int[] tmp_pair = {pvals.get(0), 1};
		for (int i = 1; i < psize; i++) {
			int myVal = pvals.get(i);
			if (myVal == tmp_pair[0]) {
				tmp_pair[1]++; 		//Count is increased for this value
				if(tmp_pair[1] > pair[1]) {
					pair[0] = tmp_pair[0];
					pair[1] = tmp_pair[1];
				}
			}
			else {
				tmp_pair[0] = myVal;
				tmp_pair[1] = 1;
			}
		}
		System.out.println(Arrays.toString(pair));

	}
	
	public static double getHypoteneuse(int x, int y) {
		return  Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
	}
	
	public static int isInt(double x)	{
		double x_floor = Math.floor(x);
		if (x_floor == x) 
			{	return 1;	}
		else
			{	return 0;	}
	}
	
	
}
