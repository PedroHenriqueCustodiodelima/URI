using System;

class Program
{
    static void Merge(int[] array, int start, int middle, int end)
    {
        int[] tempArray = new int[end - start + 1];
        int p1 = start, p2 = middle + 1;
        int index = 0;

        while (p1 <= middle && p2 <= end)
        {
            if (array[p1] < array[p2])
                tempArray[index++] = array[p1++];
            else
                tempArray[index++] = array[p2++];
        }

        while (p1 <= middle)
            tempArray[index++] = array[p1++];

        while (p2 <= end)
            tempArray[index++] = array[p2++];

        for (int i = 0, k = start; i < tempArray.Length; i++, k++)
            array[k] = tempArray[i];
    }

    static void MergeSort(int[] array, int start, int end)
    {
        if (start < end)
        {
            int middle = (start + end) / 2;
            MergeSort(array, start, middle);
            MergeSort(array, middle + 1, end);
            Merge(array, start, middle, end);
        }
    }

    static void Main()
    {
        int casos, numero, tamanhoPares = 0, tamanhoImpares = 0;
        int i = 0, j = 0;

        casos = int.Parse(Console.ReadLine());
        int[] impares = new int[casos];
        int[] pares = new int[casos];

        while (casos-- > 0)
        {
            numero = int.Parse(Console.ReadLine());

            if (numero % 2 == 0)
            {
                tamanhoPares++;
                pares[i++] = numero;
            }
            else
            {
                tamanhoImpares++;
                impares[j++] = numero;
            }
        }

        MergeSort(pares, 0, tamanhoPares - 1);
        MergeSort(impares, 0, tamanhoImpares - 1);

        for (i = 0; i < tamanhoPares; i++)
            Console.WriteLine(pares[i]);

        for (i = tamanhoImpares - 1; i >= 0; i--)
            Console.WriteLine(impares[i]);
    }
}