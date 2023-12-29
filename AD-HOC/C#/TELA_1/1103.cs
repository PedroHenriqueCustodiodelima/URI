using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            string[] input = Console.ReadLine().Split();
            int H1 = int.Parse(input[0]);
            int M1 = int.Parse(input[1]);
            int H2 = int.Parse(input[2]);
            int M2 = int.Parse(input[3]);

            if (H1 == M1 && H1 == H2 && H2 == M2 && H2 == 0)
            {
                break;
            }
            else
            {
                int x = H1 * 60 + M1;
                int y = H2 * 60 + M2;

                if (y <= x)
                {
                    y += 24 * 60;
                }

                Console.WriteLine(Math.Abs(y - x));
            }
        }
    }
}
