1, =, i, 0
2, =, a, arr_init, 20
3, =, tt2, 1
4, array_access, tt3, a, tt2
5, =, tt3, 3
6, array_asgn, a, tt2, tt3
7, <, tt4, i, 4
8, conditional_goto, ==, 1, tt4, l3
9, goto, l1
10, label, l3
11, =, tt5, i
12, *, tt6, tt5, 1
13, array_access, tt7, a, tt6
14, +, tt7, 1, tt7
15, array_asgn, a, tt6, tt7
16, label, l1
17, >, tt8, i, 1
18, conditionaltgoto, ==, 1, tt8, l8
19, =, tt12, i
20, *, tt13, tt12, 1
21, array_access, tt14, a, tt13
22, =, tt14, 1
23, array_asgn, a, tt13, tt14
24, goto, l9
25, label, l8
26, =, tt9, i
27, *, tt10, tt9, 1
28, array_access, tt11, a, tt10
29, -, tt11, 1, tt11
30, array_asgn, a, tt10, tt11
31, label, l9
32, =, tt15, 2
33, *, tt16, tt15, 1
34, array_access, tt17, a, tt16
35, print, tt17
36, exit