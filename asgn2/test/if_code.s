1, fn_call_1, Main
2, fn_def, Main, 0
3, =, i, 0
4, =, _t1, 1
5, *, _t2, _t1, 1
6, array_access, _t3, a, _t2
7, =, _t3, 3
8, array_asgn, a, _t2, _t3
9, <, _t4, i, 4
10, conditional_goto, ==, 1, _t4, l3
11, goto, l1
12, label, l3
13, =, _t5, i
14, *, _t6, _t5, 1
15, array_access, _t7, a, _t6
16, +, _t7, 1, _t7
17, array_asgn, a, _t6, _t7
18, label, l1
19, >, _t8, i, 1
20, conditional_goto, ==, 1, _t8, l8
21, =, _t12, i
22, *, _t13, _t12, 1
23, array_access, _t14, a, _t13
24, =, _t14, 1
25, array_asgn, a, _t13, _t14
26, goto, l9
27, label, l8
28, =, _t9, i
29, *, _t10, _t9, 1
30, array_access, _t11, a, _t10
31, -, _t11, 1, _t11
32, array_asgn, a, _t10, _t11
33, label, l9
34, =, _t15, 2
35, *, _t16, _t15, 1
36, array_access, _t17, a, _t16
37, print, _t17
38, exit
