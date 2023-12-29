using System;

class Program
{
    static void Main()
    {
        int n, i, j, num, kg;
        float preco, total;
        string frutas;

        if (int.TryParse(Console.ReadLine(), out n))
        {
            total = 0.0f;
            kg = 0;

            for (i = 0; i < n; i++)
            {
                num = 0;

                if (float.TryParse(Console.ReadLine(), out preco))
                {
                    total += preco;
                }

                frutas = Console.ReadLine();

                for (j = 0; j < frutas.Length; j++)
                {
                    if (frutas[j] == ' ')
                    {
                        num++;
                    }
                }

                kg += num + 1;

                Console.WriteLine("day {0}: {1} kg", i + 1, num + 1);
            }

            Console.WriteLine("{0:F2} kg by day", (float)kg / n);
            Console.WriteLine("R$ {0:F2} by day", total / n);
        }
    }
}
