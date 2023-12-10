using System;

class Program
{
    static int Josephus(int n, int k)
    {
        int retorno = 0;

        for (int i = 1; i < n; ++i)
            retorno = (retorno + k) % i;

        return retorno;
    }

    static void Main()
    {
        const int trueValue = 1;
        const int falseValue = 0;

        int qtsRegioes, pulo;

        while (trueValue == 1)
        {
            qtsRegioes = int.Parse(Console.ReadLine());

            if (qtsRegioes == 0)
                break;

            pulo = 1;
            while (trueValue == 1)
            {
                if (Josephus(qtsRegioes, pulo) != 11)
                    pulo++;
                else
                    break;
            }

            Console.WriteLine(pulo);
        }
    }
}
