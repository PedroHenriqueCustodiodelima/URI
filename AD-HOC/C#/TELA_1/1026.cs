using System;

class Program
{
    static void Main(string[] args)
    {
        string line;

        while ((line = Console.ReadLine()) != null)
        {
            string[] values = line.Split();

            uint a = uint.Parse(values[0]);
            uint b = uint.Parse(values[1]);

            uint c = a ^ b;

            Console.WriteLine(c);
        }
    }
}