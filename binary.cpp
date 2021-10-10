#include<iostream>
using namespace std;

int search(int *arr, int length, int target)
{
    int start = 0;
    int end = length-1;
    int mid = 0;

    while (start <= end){
        mid = (start+end) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            start = mid+1;
        else 
            end = mid-1;
        
    }
    return -1;
}

int recursive_search(int *arr, int start, int end, int target)
{
    int mid = (start+end) / 2;
    if (start > end)
        return -1;

    if (arr[mid] == target)
        return mid;
    else if (arr[mid] < target)
        return recursive_search(arr, mid+1, end, target);
    else  
        return recursive_search(arr, start, mid-1, target);
    
    
}
int main(int argc, const char * argv[])
{
    int arr[10] = {1,2,3,5,7,11,14,19,25,30};
    int num;
    int result;

    cout << "찾고자 하는 수를 입력하세요." << endl;

    cin >> num;

    int arr_size = sizeof(arr) / sizeof(*arr);
    result = search(arr,arr_size, num);
    if (result == -1)
        cout << "값이 존재하지 않습니다." << endl;
    else
        cout << "index:" << result << "에 있습니다." << endl;
    
    result = recursive_search(arr,0,arr_size-1, num);
    if (result == -1)
        cout << "값이 존재하지 않습니다." << endl;
    else
        cout << "index:" << result << "에 있습니다." << endl;

    return 0;
}