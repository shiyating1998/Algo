# Bucket sort
# map each number in the array into a bucket
# sort the numbers in the bucket using any sorting algorithm 
# join the results of each bucket 

from quicksort import quickSort

def bucketSort(arr, bucketSize):
    minVal = min(arr)
    maxVal = max(arr)

    numOfBuckets = (maxVal - minVal) // bucketSize + 1 
   
    buckets = [[] for _ in range(numOfBuckets)]    

    # map val into individual buckets
    for val in arr:
        index = (val - minVal) // bucketSize
        buckets[index].append(val)

    # sort them using quicksort
    for bucket in buckets:
        quickSort(bucket,0,len(bucket)-1)

    print("buckets:",buckets)
    # flatten the buckets    
    arr = [item for bucket in buckets for item in bucket]
    return arr

if __name__ == "__main__":
    array = [4,12,9,2,20,8,6,10]   
    #bucketSort(array,5)
    print(bucketSort(array,10))





# Java implementation 

# public class BucketSort implements IArraySort {

#     private static final InsertSort insertSort = new InsertSort();

#     @Override
#     public int[] sort(int[] sourceArray) throws Exception {
#         // 对 arr 进行拷贝，不改变参数内容
#         int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);

#         return bucketSort(arr, 5);
#     }

#     private int[] bucketSort(int[] arr, int bucketSize) throws Exception {
#         if (arr.length == 0) {
#             return arr;
#         }

#         int minValue = arr[0];
#         int maxValue = arr[0];
#         for (int value : arr) {
#             if (value < minValue) {
#                 minValue = value;
#             } else if (value > maxValue) {
#                 maxValue = value;
#             }
#         }

#         int bucketCount = (int) Math.floor((maxValue - minValue) / bucketSize) + 1;
#         int[][] buckets = new int[bucketCount][0];

#         // 利用映射函数将数据分配到各个桶中
#         for (int i = 0; i < arr.length; i++) {
#             int index = (int) Math.floor((arr[i] - minValue) / bucketSize);
#             buckets[index] = arrAppend(buckets[index], arr[i]);
#         }

#         int arrIndex = 0;
#         for (int[] bucket : buckets) {
#             if (bucket.length <= 0) {
#                 continue;
#             }
#             // 对每个桶进行排序，这里使用了插入排序
#             bucket = insertSort.sort(bucket);
#             for (int value : bucket) {
#                 arr[arrIndex++] = value;
#             }
#         }

#         return arr;
#     }

#     /**
#      * 自动扩容，并保存数据
#      *
#      * @param arr
#      * @param value
#      */
#     private int[] arrAppend(int[] arr, int value) {
#         arr = Arrays.copyOf(arr, arr.length + 1);
#         arr[arr.length - 1] = value;
#         return arr;
#     }

# }