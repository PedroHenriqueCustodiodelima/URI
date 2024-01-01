using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            int N = int.Parse(Console.ReadLine());

            if (N == 0)
                break;
            else
            {
                int ACUM = 0;

                for (int i = 1; i <= N; i++)
                {
                    string[] input = Console.ReadLine().Split();
                    int T = int.Parse(input[0]);
                    int Q = int.Parse(input[1]);

                    if (Q % 2 == 0)
                        ACUM += Q;
                    else
                        ACUM += Q - 1;
                }

                Console.WriteLine(ACUM / 4);
            }
        }
    }
}
