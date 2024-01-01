using System;

class Program
{
    static void Main()
    {
        int cont = 1;
        while (true)
        {
            try
            {
                string n = Console.ReadLine();
                string[] calc = Console.ReadLine().Split();
                if (cont > 1)
                {
                    Console.WriteLine();
                }

                int f = 0, m = 0, pares = 0;
                for (int i = 0; i < calc.Length; i += 2)
                {
                    if (calc[i] == n)
                    {
                        pares++;
                        if (calc[i + 1] == "F")
                        {
                            f++;
                        }
                        else
                        {
                            m++;
                        }
                    }
                }

                Console.WriteLine($"Caso {cont}:");
                Console.WriteLine($"Pares Iguais: {pares}");
                Console.WriteLine($"F: {f}");
                Console.WriteLine($"M: {m}");
                cont++;
            }
            catch (Exception)
            {
                break;
            }
        }
    }
}
