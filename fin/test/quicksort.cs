class quickSort
    {
        // int len = 5;
        int[] array = new int[5];

        
        void sort(int left, int right)
        {
            int pivot, leftend, rightend; 
            leftend = left;
            rightend = right;
            pivot = array[left];
 
            while (left < right)
            {
                while ((array[right] >= pivot) && (left < right))
                {
                    right--;
                }
 
                if (left > right || left < right)
                {
                    array[left] = array[right];
                    left++;
                }
 
                while ((array[left] <= pivot) && (left < right))
                {
                    left++;
                }
 
                if (left > right || left < right)
                {
                    array[right] = array[left];
                    right--;
                }
            }
 
            array[left] = pivot;
            pivot = left;
            left = leftend;
            right = rightend;
 
            if (left < pivot)
            {
                sort(left, pivot - 1);
            }
 
            if (right > pivot)
            {
                sort(pivot + 1, right);
            }
        return;
        }
        void QuickSort(int len)
        {
            sort(0, len - 1);
            return;
        }
        void Main()
        {
            array[0]=1;
            array[1]=10;
            array[2]=4;
            array[3]=8;
            array[4]=-98;          
            int t=0;
            int len =5;
            QuickSort(len);
            while(t<5){
                print(array[t]);
                t++;
            }
 
        }
    }