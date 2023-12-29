using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        while (true)
        {
            try
            {
                List<int> ladoDireito = new List<int>();
                List<int> ladoEsquerdo = new List<int>();
                int par = 0;

                int n = int.Parse(Console.ReadLine());

                for (int i = 0; i < n; i++)
                {
                    string[] input = Console.ReadLine().Split();
                    int tamBota = int.Parse(input[0]);
                    char lado = input[1][0];

                    if (lado == 'D')
                    {
                        ladoDireito.Add(tamBota);
                    }
                    if (lado == 'E')
                    {
                        ladoEsquerdo.Add(tamBota);
                    }
                }

                foreach (int j in ladoDireito)
                {
                    if (ladoEsquerdo.Contains(j))
                    {
                        par++;
                        ladoEsquerdo.Remove(j);
                    }
                }

                Console.WriteLine(par);
            }
            catch (Exception)
            {
                break;
            }
        }
    }
}
