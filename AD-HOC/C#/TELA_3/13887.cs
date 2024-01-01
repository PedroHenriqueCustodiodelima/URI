using System;

class Program
{
    static void Main()
    {
        int L = 1;
        int R = 1;

        while (L != 0 && R != 0)
        {
            int sl = 0;
            int sr = 0;

            string[] input = Console.ReadLine().Split();
            L = int.Parse(input[0]);
            R = int.Parse(input[1]);

            if (L != 0 && R != 0)
            {
                sl += L;
                sr += R;
                Console.WriteLine(sl + sr);
            }
        }
    }
}
