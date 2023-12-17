using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            string[] input = Console.ReadLine().Split();
            string b = input[0];
            string n = input[1];

            if (b == "0" && n == "0")
            {
                break;
            }

            int[] r = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            for (int i = 0; i < int.Parse(n); i++)
            {
                string[] transaction = Console.ReadLine().Split();
                int d = int.Parse(transaction[0]);
                int c = int.Parse(transaction[1]);
                int v = int.Parse(transaction[2]);

                r[d - 1] -= v;
                r[c - 1] += v;
            }

            char saida = 'S';

            foreach (int i in r)
            {
                if (i < 0)
                {
                    saida = 'N';
                    break;
                }
            }

            Console.WriteLine(saida);
        }
    }
}