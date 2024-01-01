using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            string[] input = Console.ReadLine().Split();
            string n = input[0];
            string d = input[1];

            if (n == "0" && d == "0")
            {
                break;
            }

            int[,] l = new int[int.Parse(d), int.Parse(n)];
            string s = "no";
            int[] jantar = new int[int.Parse(n)];

            for (int i = 0; i < int.Parse(d); i++)
            {
                input = Console.ReadLine().Split();
                for (int j = 0; j < int.Parse(n); j++)
                {
                    l[i, j] = int.Parse(input[j]);
                    if (l[i, j] == 1)
                    {
                        jantar[j]++;
                    }
                }
            }

            if (Array.IndexOf(jantar, int.Parse(d)) >= 0)
            {
                s = "yes";
            }

            Console.WriteLine(s);
        }
    }
}
