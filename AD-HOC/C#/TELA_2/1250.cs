using System;

class Program
{
    static void Main()
    {
        int n, x, i, j, cont;
        char c;

        n = int.Parse(Console.ReadLine());

        for (i = 0; i < n; i++)
        {
            x = int.Parse(Console.ReadLine());
            cont = 0;
            int[] tiro = new int[x];
            char[] pulo = new char[x + 1];

            string input = Console.ReadLine();
            for (j = 0; j < x; j++)
            {
                tiro[j] = int.Parse(input.Split(' ')[j]);
            }

            pulo = Console.ReadLine().ToCharArray();

            for (j = 0; j < x; j++)
            {
                if (pulo[j] == 'S')
                {
                    if (tiro[j] < 3)
                        cont++;
                }
                else
                {
                    if (tiro[j] > 2)
                        cont++;
                }
            }
            
            Console.WriteLine(cont);
        }
    }
}
