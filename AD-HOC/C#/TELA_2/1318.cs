using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            try
            {
                string[] inputNM = Console.ReadLine().Trim().Split(' ');
                int N = int.Parse(inputNM[0]);
                int M = int.Parse(inputNM[1]);

                if (N == 0 && M == 0)
                {
                    break;
                }

                string[] inputTickets = Console.ReadLine().Trim().Split(' ');
                int[] bilhetes = new int[M];

                for (int i = 0; i < M; i++)
                {
                    bilhetes[i] = int.Parse(inputTickets[i]);
                }

                int resposta = 0;
                int[] contador = new int[N + 1];

                foreach (int bilhete in bilhetes)
                {
                    contador[bilhete] += 1;
                    if (contador[bilhete] == 2)
                    {
                        resposta += 1;
                    }
                }

                Console.WriteLine(resposta);
            }
            catch (Exception)
            {
                break;
            }
        }
    }
}