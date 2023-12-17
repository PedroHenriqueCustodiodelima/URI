using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        while (true)
        {
            string[] input = Console.ReadLine().Split();
            string a = input[0];
            string b = input[1];

            if (a == b && a == "0")
            {
                break;
            }

            List<int> fa = Console.ReadLine().Split().Select(int.Parse).ToList();
            List<int> fb = Console.ReadLine().Split().Select(int.Parse).ToList();

            HashSet<int> setA = new HashSet<int>(fa);
            HashSet<int> setB = new HashSet<int>(fb);

            HashSet<int> c = setB;
            int f = 0;

            if (setA.Count < setB.Count)
            {
                c = setA;
                setA = setB;
            }

            c.RemoveWhere(x => setA.Contains(x));

            Console.WriteLine(c.Count);
        }
    }
}