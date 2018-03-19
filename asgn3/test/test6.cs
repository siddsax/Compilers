using System;
// using System.Collections.Generic;
// using System.Text;
// namespace prog
    class Program
    {
        public void mergemethod(int [] numbers, int left, int mid, int right)
        {
            int [] temp = new int[25];
            int i, left_end, num_elements, tmp_pos;
            left_end = (mid - 1);
            tmp_pos = left;
            num_elements = (right - left + 1);
            while ((left <= left_end) && (mid <= right))
            {
                if (numbers[left] <= numbers[mid])
                    temp[tmp_pos++] = numbers[left++];
                else
                    temp[tmp_pos++] = numbers[mid++];
            }
            while (left <= left_end)
                temp[tmp_pos++] = numbers[left++];
            while (mid <= right)
                temp[tmp_pos++] = numbers[mid++];
            i = 0;
            while (i < num_elements ){
                numbers[right] = temp[right];
                right--;
                i++;
            }
        }
         public void sortmethod(int [] numbers, int left, int right)
        {
          int mid;
          if (right > left)
          {
            mid = (right + left) / 2;
            sortmethod(numbers, left, mid);
            sortmethod(numbers, (mid + 1), right);
            mergemethod(numbers, left, (mid+1), right);

          }
        }

        void Main(string[] args)
        {

            int[] numbers = new int[10];
            int len = 9;
            Console.WriteLine("MergeSort :");
            sortmethod(numbers, 0, len - 1);
            int i = 0;
            while(i<9)
            {
                Console.WriteLine(numbers[i]);                
            }
            
            Console.Read();
         }
   }
