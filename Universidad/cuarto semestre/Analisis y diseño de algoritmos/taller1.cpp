#include <iostream>
using namespace std;

int merge(int arr[], int temp[], int left, int mid, int right) {
    int inversions = 0;
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            inversions += (mid - i + 1); // Contar inversiones
        }
    }

    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    while (j <= right) {
        temp[k++] = arr[j++];
    }

    for (int p = left; p <= right; p++) {
        arr[p] = temp[p];
    }

    return inversions;
}

int mergeSort(int arr[], int temp[], int left, int right) {
    int inversions = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        inversions += mergeSort(arr, temp, left, mid);
        inversions += mergeSort(arr, temp, mid + 1, right);
        inversions += merge(arr, temp, left, mid, right);
    }
    return inversions;
}

int main() {
    int arr[] = {48, 45, 14, 71, 11, 77, 44, 65, 47, 78};
    int n = sizeof(arr) / sizeof(arr[0]);
    int temp[n];
    int inversions = mergeSort(arr, temp, 0, n - 1);

    cout << "Arreglo ordenado: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    cout << "Inversiones realizadas: " << inversions << endl;

    return 0;
}
