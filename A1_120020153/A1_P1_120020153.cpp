#include <iostream>
using namespace std;

long mergeSortAndCount(long arr[], int left, int right);
long merge(long arr[], int left, int mid, int right);

int main() {
    int N;
    cin >> N; // Number of people in the queue
    long heights[N];

    for (int i = 0; i < N; i++) {
        cin >> heights[i]; // Heights of people in the queue
    }

    long disorderPairs = mergeSortAndCount(heights, 0, N - 1);
    cout << disorderPairs << endl;

    return 0;
}

long mergeSortAndCount(long arr[], int left, int right) {
    long count = 0;
    if (left < right) {
        int mid = (left + right) / 2;
        count += mergeSortAndCount(arr, left, mid);
        count += mergeSortAndCount(arr, mid + 1, right);
        count += merge(arr, left, mid, right);
    }
    return count;
}

long merge(long arr[], int left, int mid, int right) {
    long temp[right - left + 1];
    long count = 0;

    int i = left;
    int j = mid + 1;
    int k = 0;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            count += (mid - i + 1); // Count inversions during merge
        }
    }

    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    while (j <= right) {
        temp[k++] = arr[j++];
    }

    for (int l = 0; l < k; l++, right--) {
        arr[right] = temp[right - left];
    }
    return count;
}
