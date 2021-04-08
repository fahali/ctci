# 1.8 Zero Matrix

Write an algorithm such that if an element in an **MxN** matrix is `0`, its entire row and column are set to `0`.

## Approach

We need to iterate over the matrix first and find out which rows and columns need to be zeroed out. We can store the row and column information in two arrays, then iterate over each array to zero out the matrix. This requires `O(N^2)` time complexity (we need to touch every element in the initial check) and `O(N)` space complexity (we require two separate 1 dimensional arrays). There is a better solution that uses `O(1)` extra space which I will put up later.
