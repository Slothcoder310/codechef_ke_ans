<h2><a href="https://www.codechef.com/START238D/problems/CRNET">Cricket Nets

Chef is practicing in a cricket nets session.

The session has two phases:

In the first phase, Chef scores 
1
1 run per ball, and each ball costs 
10
10 rupees.
This phase lasts for the first 
20
20 balls.
In the second phase, which starts after 
20
20 balls, Chef scores 
2
2 runs per ball, and each ball costs 
5
5 rupees.

Given that Chef scored a total of 
𝑋
X runs, determine the total amount he paid in rupees.
It is guaranteed that 
𝑋
X is even.

Input Format
The first line of input will contain a single integer 
𝑇
T, denoting the number of test cases.
Each test case consists of a single line containing one integer 
𝑋
X.
Output Format

For each test case, output on a new line the total amount paid by Chef.

Constraints
1
≤
𝑇
≤
100
1≤T≤100
2
≤
𝑋
≤
200
2≤X≤200
𝑋
X is even.
Sample 1:
Input
Output
5
2
20
40
42
100

20
200
250
255
400

Explanation:

Test case 
1
1: For 
𝑋
=
2
X=2, Chef scores all runs in the first phase.
He plays 
2
2 balls, each costing 
10
10 rupees.
Total cost 
=
2
×
10
=
20
=2×10=20 rupees.

Test case 
2
2: For 
𝑋
=
20
X=20, Chef scores all 
20
20 runs in the first phase.
Total cost 
=
20
×
10
=
200
=20×10=200 rupees.

Test case 
3
3: For 
𝑋
=
40
X=40, Chef first scores 
20
20 runs in the first phase for 
200
200 rupees.
The remaining 
20
20 runs are scored in the second phase, requiring 
10
10 balls.
Cost of second phase 
=
10
×
5
=
50
=10×5=50 rupees.
Total cost 
=
200
+
50
=
250
=200+50=250 rupees.

Test case 
4
4: For 
𝑋
=
42
X=42, Chef first scores 
20
20 runs in the first phase for 
200
200 rupees.
The remaining 
22
22 runs are scored in the second phase, requiring 
11
11 balls.
Cost of second phase 
=
11
×
5
=
55
=11×5=55 rupees.
Total cost 
=
200
+
55
=
255
=200+55=255 rupees.

Test case 
5
5: For 
𝑋
=
100
X=100, Chef first scores 
20
20 runs in the first phase for 
200
200 rupees.
The remaining 
80
80 runs are scored in the second phase, requiring 
40
40 balls.
Cost of second phase 
=
40
×
5
=
200
=40×5=200 rupees.
Total cost 
=
200
+
200
=
400
=200+200=400 rupees.</a></h2><h4>Difficulty: </h4>