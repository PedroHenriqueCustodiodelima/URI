using System;

class Program
{
    const int MAXSIZE = 3502;
    const int MAXPRIME = 32650;
    static int[] primos = new int[MAXSIZE];

    static void Main()
    {
        PreenchePrimo();
        while (true)
        {
            int n = int.Parse(Console.ReadLine());
            if (n == 0)
                break;
            Console.WriteLine(Josephus(n));
        }
    }

    static int Josephus(int n)
    {
        int retorno = 0;
        for (int i = 1; i <= n; ++i)
            retorno = (retorno + primos[n - i]) % i;
        return retorno + 1;
    }

    static bool IsPrime(int x)
    {
        if (x == 2)
            return true;
        if (x % 2 == 0 || x < 2)
            return false;
        for (int i = 3; i * i <= x; i += 2)
            if (x % i == 0)
                return false;
        return true;
    }

    static void PreenchePrimo()
    {
        for (int i = 2, j = 0; j < MAXSIZE; ++i)
        {
            if (IsPrime(i))
                primos[j++] = i;
        }
    }
}
