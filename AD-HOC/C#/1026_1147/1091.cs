using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            int K = int.Parse(Console.ReadLine());
            if (K == 0)
                break;

            string[] input = Console.ReadLine().Split();
            int N = int.Parse(input[0]);
            int M = int.Parse(input[1]);

            for (int i = 0; i < K; ++i)
            {
                input = Console.ReadLine().Split();
                int X = int.Parse(input[0]);
                int Y = int.Parse(input[1]);
                int dX = X - N;
                int dY = Y - M;

                if (dX == 0 || dY == 0)
                    Console.WriteLine("divisa");
                else if (dX < 0 && dY > 0)
                    Console.WriteLine("NO");
                else if (dX > 0 && dY > 0)
                    Console.WriteLine("NE");
                else if (dX < 0 && dY < 0)
                    Console.WriteLine("SO");
                else if (dX > 0 && dY < 0)
                    Console.WriteLine("SE");
            }
        }
    }
}
