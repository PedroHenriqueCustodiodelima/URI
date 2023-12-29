using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {
            string entrada = Console.ReadLine();

            char letra = entrada[1];
            int primeiro = int.Parse(entrada[0].ToString());
            int segundo = int.Parse(entrada[2].ToString());

            if (primeiro == segundo)
            {
                int produto = primeiro * segundo;
                Console.WriteLine(produto);
            }
            else if (char.IsUpper(letra))
            {
                int subtracao = segundo - primeiro;
                Console.WriteLine(subtracao);
            }
            else if (char.IsLower(letra))
            {
                int soma = primeiro + segundo;
                Console.WriteLine(soma);
            }
        }
    }
}