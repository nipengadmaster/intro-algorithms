#include <stdio.h>
#include <stdlib.h>

#define MAX 0x7fffffff

int a[100010];
long long count;


void merge(int p, int q, int r)
{
     int n1, n2, *left, *right, i, j, k;
     n1 = q - p + 1;
     n2 = r - q;
     left = (int *)malloc((n1+1)*sizeof(int));
     right = (int *)malloc((n2+1)*sizeof(int));
     for(i=0; i<n1; i++)
          left[i] = a[p+i];
     for(i=0; i<n2; i++)
          right[i] = a[q+i+1];
     left[n1] = MAX;
     right[n2] = MAX;
     for(i=0, j=0,k=p; k<=r; k++)
          if(left[i]<=right[j])
          {
               a[k] = left[i];
               i ++;
          }
          else
          {
               count = count + q + 1 + j - k;
               a[k] = right[j];
               j ++;
          }
     free(left);
     free(right);

}
