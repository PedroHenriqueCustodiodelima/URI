using System;

class Program
{
    static void Main()
    {
        int N = 1;

        while (N != 0)
        {
            N = int.Parse(Console.ReadLine());

            if (N != 0)
            {
                int s1 = 0;
                int s2 = 0;

                for (int i = 0; i < N; i++)
                {
                    string[] input = Console.ReadLine().Split();
                    int A = int.Parse(input[0]);
                    int B = int.Parse(input[1]);

                    if (A > B)
                    {
                        s1++;
                    }
                    else if (A < B)
                    {
                        s2++;
                    }
                }

                Console.WriteLine(s1 + " " + s2);
            }
        }
    }
}
