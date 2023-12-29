using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        double ans = 0;
        double t = 0;

        while (true)
        {
            string line = Console.ReadLine();
            if (line == null)
                break;

            if (double.TryParse(Console.ReadLine(), NumberStyles.Any, CultureInfo.InvariantCulture, out double m))
            {
                ans += m;
                t += 1;
            }
        }

        if (t > 0)
        {
            Console.WriteLine($"{(ans / t):F1}");
        }
    }
}
