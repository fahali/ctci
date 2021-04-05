# 1.7 Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

## Approach

The first thing to note is that our image is square, because the matrix uses the same `N` value for width and height. It really helps to draw out test cases to see what is happening with a rotated array. See my examples below:

```
A, B
C, D
```

becomes

```
C, A,
D, B
```

Here is the transformation:

```
0, 0 => 0, 1
0, 1 => 1, 1
1, 0 => 0, 0
1, 1 => 1, 0
```

```
A, B, C
D, E, F
G, H, I
```

becomes

```
G, D, A
H, E, B
I, F, C
```

Here is the transformation:

```
0, 0 => 0, 2
0, 1 => 1, 2
0, 2 => 2, 2
1, 0 => 0, 1
1, 1 => 1, 1
1, 2 => 2, 1
2, 0 => 0, 0
2, 1 => 1, 0
2, 2 => 2, 0
```

I was seeing a pattern but needed more examples to form the idea. Even though the image is square, I tried a 4 x 3 matrix to see if my assumptions hold true:

```
A, B, C, D
E, F, G, H
I, J, K, L
```

becomes

```
I, E, A
J, F, B
K, G, C
L, H, D
```

Here is the transformation:

```
0, 0 => 0, 2
0, 1 => 1, 2
0, 2 => 2, 2
0, 3 => 3, 2
1, 0 => 0, 1
1, 1 => 1, 1
1, 2 => 2, 1
1, 3 => 3, 1
2, 0 => 0, 0
2, 1 => 1, 0
2, 2 => 2, 0
2, 3 => 3, 0
```

Here is what I came up with:

-   the new row index is the same as the old column index
-   the new column index is determined by MAX_ROWS minus the original row index

A naive approach would be to make an empty NxN matrix, and copy over each element from the old matrix to the new one using the rules outlined above. However, this solution requires `O(n)` extra space since we are creating a copy of the original matrix. There is a better solution where we copy over each item index by index, that is `O(1)` extra space, but I have not grokked it fully so I won't show it here (for now). Both solutions require `O(n^2)` time because we have to touch each item in the NxN matrix.
