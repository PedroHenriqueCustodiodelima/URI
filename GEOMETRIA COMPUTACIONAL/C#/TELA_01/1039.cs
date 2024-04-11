using System;
class Program
{
    static void Main()
    {
        while (true)
        {
            try
            {
                string[] input = Console.ReadLine().Split();
                int r1 = int.Parse(input[0]);
                int x1 = int.Parse(input[1]);
                int y1 = int.Parse(input[2]);
                int r2 = int.Parse(input[3]);
                int x2 = int.Parse(input[4]);
                int y2 = int.Parse(input[5]);

                double distancia = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));

                if (r1 >= distancia + r2)
                {
                    Console.WriteLine("RICO");
                }
                else
                {
                    Console.WriteLine("MORTO");
                }
            }
            catch (Exception)
            {
                break;
            }
        }
    }
}
