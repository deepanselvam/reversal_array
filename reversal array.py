class Solution:
    @staticmethod
    def Reverse_the_array(arr):
        i,j = 0,len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

if __name__ == '_main_':
    array=list(map(int,input().split()))
    ob=Solution()
    ob.Reverse_the_array(arr)
    print(*arr)
