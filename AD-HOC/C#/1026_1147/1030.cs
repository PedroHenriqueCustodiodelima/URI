using System;

class Program
{
    static ushort Recorrencia(ushort qtsSoldados, ushort qtsPulos)
    {
        ushort retorno = 0;

        for (ushort i = 2; i <= qtsSoldados; i++)
        {
            retorno = (ushort)((retorno + qtsPulos) % i);
        }

        return retorno;
    }

    static void Main()
    {
        ushort casos;
        ushort qtsInstancias;
        ushort qtsSoldados, qtsPulos;

        casos = ushort.Parse(Console.ReadLine());

        qtsInstancias = 0;
        while (casos-- > 0)
        {
            string[] inputs = Console.ReadLine().Split();
            qtsSoldados = ushort.Parse(inputs[0]);
            qtsPulos = ushort.Parse(inputs[1]);

            Console.WriteLine($"Case {++qtsInstancias}: {Recorrencia(qtsSoldados, qtsPulos) + 1}");
        }
    }
}