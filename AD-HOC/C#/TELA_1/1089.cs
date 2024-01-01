using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            int n = int.Parse(Console.ReadLine());
            if (n == 0)
                break;

            int[] h = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            Array.Resize(ref h, n + 2);
            h[n] = h[0];
            h[n + 1] = h[1];

            int picos = 0;
            for (int i = 1; i <= n; i++)
            {
                if (h[i] < h[i - 1] && h[i] < h[i + 1])
                {
                    picos++;
                }
                else if (h[i] > h[i - 1] && h[i] > h[i + 1])
                {
                    picos++;
                }
            }

            Console.WriteLine(picos);
        }
    }
}
