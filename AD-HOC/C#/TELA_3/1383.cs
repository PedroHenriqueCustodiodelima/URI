using System;

class Program
{
    static string IsSudoku(int[,] matriz)
    {
        for (int i = 0; i < 9; i++)
        {
            int[] testador = new int[10];
            for (int j = 0; j < 9; j++)
            {
                if (testador[matriz[i, j]] != 0)
                {
                    return "NAO";
                }
                else
                {
                    testador[matriz[i, j]] = 1;
                }
            }
        }

        for (int i = 0; i < 9; i++)
        {
            int[] testador = new int[10];
            for (int j = 0; j < 9; j++)
            {
                if (testador[matriz[j, i]] != 0)
                {
                    return "NAO";
                }
                else
                {
                    testador[matriz[j, i]] = 1;
                }
            }
        }

        for (int i = 2; i < 9; i += 3)
        {
            int[] testador = new int[10];
            for (int j = i - 2; j <= i; j++)
            {
                for (int k = i - 2; k <= i; k++)
                {
                    if (testador[matriz[j, k]] != 0)
                    {
                        return "NAO";
                    }
                    else
                    {
                        testador[matriz[j, k]] = 1;
                    }
                }
            }
        }

        return "SIM";
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        for (int h = 1; h <= n; h++)
        {
            int teste = 0;
            int[,] matriz = new int[9, 9];

            for (int i = 0; i < 9; i++)
            {
                string[] input = Console.ReadLine().Split();
                for (int j = 0; j < 9; j++)
                {
                    matriz[i, j] = int.Parse(input[j]);
                }
            }

            string saida = IsSudoku(matriz);

            Console.WriteLine($"Instancia {h}");
            Console.WriteLine(saida);
            Console.WriteLine();
        }
    }
}
