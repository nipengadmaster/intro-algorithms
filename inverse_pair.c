#include<iostream>
#include<stdlib.h>
using namespace std;


void printArray(int arry[])
{
  int len = sizeof(arry) / sizeof(arry[0]);
  for(int i=0;i<len;i++)
  {
    cout<<arry[i]<<" ";
  }
  cout<<endl;

}

int MergeArray(int arry[],int start,int mid,int end,int temp[])//数组的归并操作
{

  //int leftLen=mid-start+1;//arry[start...mid]左半段长度
  //int rightLlen=end-mid;//arry[mid+1...end]右半段长度

  int i = mid;

  int j = end;

  int k = 0;
  //临时数组末尾坐标
  int count = 0;

  //设定两个指针ij分别指向两段有序数组的头元素，将小的那一个放入到临时数组中去。
  while(i>=start && j>mid)
  {

    if(arry[i]>arry[j])
    {

      temp[k++]=arry[i--];
      //从临时数组的最后一个位置开始排序
      count+=j-mid;
      //因为arry[mid+1...j...end]是有序的，如果arry[i]>arry[j]，那么也大于arry[j]之前的元素，从a[mid+1...j]一共有j-(mid+1)+1=j-mid

    }

    else
    {

      temp[k++]=arry[j--];

    }

  }

  //  cout<<"调用MergeArray时的count："<<count<<endl;

  while(i>=start)//表示前半段数组中还有元素未放入临时数组
  {

    temp[k++]=arry[i--];

  }


  while(j>mid)
  {

    temp[k++]=arry[j--];

  }


  //将临时数组中的元素写回到原数组当中去。
  for(i=0;i<k;i++)
    arry[end-i]=temp[i];


  printArray(arry);
  //输出进过一次归并以后的数组，用于理解整体过程
  return count;


}


int InversePairsCore(int arry[],int start,int end,int temp[])
{

  int inversions = 0;

  if(start<end)
  {

    int mid=(start+end)/2;

    inversions+=InversePairsCore(arry,start,mid,temp);
    //找左半段的逆序对数目
    inversions+=InversePairsCore(arry,mid+1,end,temp);
    //找右半段的逆序对数目
    inversions+=MergeArray(arry,start,mid,end,temp);
    //在找完左右半段逆序对以后两段数组有序，然后找两段之间的逆序对。最小的逆序段只有一个元素。
  }

  return inversions;

}



int InversePairs(int arry[],int len)
{

  int *temp=new int[len];

  int count=InversePairsCore(arry,0,len-1,temp);

  delete[] temp;

  return count;

}


int merge_inverse(int array[], int start, int mid, int end)
{
  int *L = new int[mid-start];
  int i,j;
  int p = 0;
  int q = 0;

  for(i=start;i<=mid;i++)
  {
    L[p++] = array[i];
  }
  int *R = new int[end-mid-1];
  for(i=mid+1;i<=end;i++)
  {
    R[q++] = array[i];
  }
  int k = 0;
  int res = 0;

  cout<<"L"<<endl;
  printArray(L);
  cout<<"R"<<endl;
  printArray(R);

  cout<<">>>>"<<start<<"--"<<end<<endl;
  cout<<"k: "<<k<<endl;
  i = 0;
  j = 0;
  k = start;

  while(k < end-start)
  {
    cout<<"lplp"<<endl;

    if(L[i] > R[j])
    {
      res += 1;
      j ++;
      array[k] = R[j];
      cout<<"逆序对: "<<L[i]<<" & "<<R[j]<<endl;

    }
    else
    {
      cout<<"lplp"<<endl;

      i ++;
      array[k] = L[j];
    }
    cout<<"lplp"<<endl;
    k += 1;

  }

  return res;
}



int inverse_pairs(int array[],int start,int end)
{
  cout<<"s: "<<start<<"  e: "<<end<<endl;
  printArray(array);

  if(start == end)
  {
    return 0;
  }
  int res = 0;
  int mid = (start + end) / 2;
  res += inverse_pairs(array, start, mid);
  res += inverse_pairs(array, mid+1, end);
  cout<<start<<"+"<<mid<<"+"<<end<<endl;
  res += merge_inverse(array, start, mid, end);
  return res;
}



int main()
{

  //int arry[]={7,5,6,4};
  int array[]=
    {
      2,7,5,1,3,8
    }
  ;

  int len = sizeof(array) / sizeof(array[0]);
  printArray(array);

  int res = inverse_pairs(array, 0, len-1);
  cout<<res<<endl;
  return 0;

}
