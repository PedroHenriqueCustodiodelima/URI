using System;

class Program
{
    static void Main()
    {
        int px1, py1, px2, py2;
        int resultado = 2;
        int x, y;

        while (true)
        {
            string[] input = Console.ReadLine().Split();
            px1 = int.Parse(input[0]);
            py1 = int.Parse(input[1]);
            px2 = int.Parse(input[2]);
            py2 = int.Parse(input[3]);

            if (px1 == 0 && py1 == 0 && px2 == 0 && py2 == 0)
            {
                break;
            }

            x = Math.Abs(px1 - px2);
            y = Math.Abs(py1 - py2);

            if (px1 == px2 && py1 == py2)
            {
                resultado = 0;
                Console.WriteLine(resultado);
            }
            else if (px1 == px2 && py1 != py2)
            {
                resultado = 1;
                Console.WriteLine(resultado);
            }
            else if (px1 != px2 && py1 == py2)
            {
                resultado = 1;
                Console.WriteLine(resultado);
            }
            else if (x == y)
            {
                resultado = 1;
                Console.WriteLine(resultado);
            }
            else
            {
                resultado = 2;
                Console.WriteLine(resultado);
            }
        }
    }
}