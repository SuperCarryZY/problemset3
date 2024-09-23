# CMPS 6610 Problem Set 03
## Answers

**Name:**_________Yan Zhu________________


Place all written answers from `problemset-03.md` here for easier grading.




- **1b.**

Work:

the algorithm will iterate through all  n  elements in the list. For each element, the update function is called, which performs a constant-time comparison (x == key). Therefore, the total work is proportional to  O(n) .

Span:

 Since iterate processes each element in a strictly sequential manner, the span is also proportional to  O(n)。



- **1d.**

Work: O(n)
Span: O(log n)
In this case, the reduce function recursively divides the list into smaller sublists and combines the results.
The reduce function divides the list in half at each step, and the depth of recursion is  O(log n) ,


- **1e.**

Work:  O(n) 
Span:  O(log_{3/2} n) 

Each recursive step still processes the entire list of size n, so the total work remains proportional to  O(n)  across all levels of recursion.
Thus, the work is still  O(n) .
At each level, the larger part (two-thirds) of the list is processed. Thus span:O(log_{3/2} n) 


- **3b.**
Work:
Each recursive call processes one element of the list, and then recursively processes the remaining  n - 1  elements.
Thus, the recurrence for work can be written as:
W(n) = W(n-1) + O(1)
W(n) = O(n)

Span:
Each recursive call processes one element, and then the recursion continues with the remaining  n - 1  elements. The recurrence for span can be written as:
S(n) = S(n-1) + O(1)
S(n) = O(n)




- **3d.**

Work:  O(n) 
Span:  O(\log n) 

The map operation applies paren_map to each element in parallel, resulting in  O(n)  work and  O(1)  span. The scan phase, using contraction, also takes  O(n)  work and  O(\log n)  span due to halving the problem size at each step. The reduce phase, which computes the minimum over the prefix sums, performs  O(n)  work and has a span of  O(\log n) . Thus, the total work for the solution is  O(n) , while the span remains  O(\log n) .



- **3f.**

Work:  O(n) 
Span:  O(\log n) 

Each recursive step splits the input list into two halves, and the recursive calls are processed in parallel. The merging step, where the results from the left and right halves are combined, takes constant time  O(1) . Thus, the work recurrence is  W(n) = 2W(n/2) + O(1) , which solves to  O(n) , meaning the total work is linear in the size of the input list.

For the span, since the recursive calls are executed in parallel, the depth of the recursion (the longest dependency chain) dictates the span. The span recurrence is  S(n) = S(n/2) + O(1) , which solves to  O(\log n) , meaning the span grows logarithmically with the size of the input.


- **4a.**

Suppose there are 6 students, named A, B, C, D, E, and F, where:
A, B, and C are white hats.
D, E, and F are black hats.

The following pairwise inquiries are conducted:

	A and B mutually confirm that the other is a white hat because they are both white hats, so their answers are consistent.
	D and E mutually confirm that the other is a white hat, but in reality, they are both black hats, so they are lying.
	C and F might have conflicting answers: C, being a white hat, will say that F is a black hat, while F, being a black hat, might say that C is a black hat, or vice versa.

After this round of inquiries, we get the following two groups:

	Group 1: A and B, who mutually confirm that the other is a white hat.
	Group 2: D and E, who mutually confirm that the other is a white hat.

At this point, both groups are mutually confirming that the other is a white hat, but since the black hats can lie and conspire, we cannot be sure which group consists of the white hats and which consists of the black hats. Based on the results of the pairwise inquiries, we can only divide the students into two groups, but we cannot further distinguish between the black hats and the white hats within each group.

This example illustrates well why the number of white hats must be strictly greater than n/2 in order to distinguish between black hats and white hats.

In this example, the black hats (D, E, and F) are able to mutually confirm that the others are white hats, and their answers are consistent, making it impossible to differentiate them from the white hats through pairwise inquiries alone. This is because the black hats have enough numbers to conspire and deceive you. When the number of black hats equals the number of white hats (as in this example, where there are 3 black hats and 3 white hats), the black hats can mutually confirm each other and fully mimic the behavior of white hats. As a result, you don’t have enough information to distinguish between the black hats and the white hats because the answers from both groups of students are consistent.


- **4b.**

After each round of interviews, we can analyze the conflicting pairs and eliminate the students involved. In each round of interviews, if there are multiple conflicting pairs, we can eliminate at least two students (i.e., the students in each conflicting pair). Therefore, each round of interviews can reduce the problem size by a constant fraction (i.e., eliminate a portion of n). Even if some pairs do not have conflicts, after n/2 interviews, the size of the problem will still be reduced.



- **4c.**

Although the problem size is reduced in each round of pairwise interviews, the number of interviews conducted per round gradually decreases.

In the first round, there are  n/2  pairs of students, so  n/2  interviews are conducted.
In the second round, after eliminating some students, there are  n/2  students left, so  n/4  interviews are conducted.
In the third round, after further eliminating students,  n/4  students remain, so  n/8  interviews are conducted.

Thus, the total number of interviews across all rounds is:

\[
n/2 + n/4 + n/8 + n/16 + \dots
\]

Each round’s number of interviews is halved compared to the previous round. Although the number of interviews decreases each round, the sum of the interviews across all rounds does not exceed  n .

In the end, the total number of interviews is approximately  n , so the overall time complexity is  O(n) .


