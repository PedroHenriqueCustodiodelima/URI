using System;

class Program
{
    static void Main()
    {
        for (int j = 0; j < 100; j++)
        {
            int n = int.Parse(Console.ReadLine());

            if (n == 0)
            {
                break;
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    string[] input = Console.ReadLine().Split();
                    int a = int.Parse(input[0]);
                    int b = int.Parse(input[1]);
                    int c = int.Parse(input[2]);
                    int d = int.Parse(input[3]);
                    int e = int.Parse(input[4]);

                    if (a <= 127 && b > 127 && c > 127 && d > 127 && e > 127)
                    {
                        Console.WriteLine("A");
                    }
                    else if (a > 127 && b <= 127 && c > 127 && d > 127 && e > 127)
                    {
                        Console.WriteLine("B");
                    }
                    else if (a > 127 && b > 127 && c <= 127 && d > 127 && e > 127)
                    {
                        Console.WriteLine("C");
                    }
                    else if (a > 127 && b > 127 && c > 127 && d <= 127 && e > 127)
                    {
                        Console.WriteLine("D");
                    }
                    else if (a > 127 && b > 127 && c > 127 && d > 127 && e <= 127)
                    {
                        Console.WriteLine("E");
                    }
                    else
                    {
                        Console.WriteLine("*");
                    }
                }
            }
        }
    }
}
