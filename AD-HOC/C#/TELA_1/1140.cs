using System;
class Program
{
    static void Main()
    {
        while (true)
        {
            string t = Console.ReadLine().ToLower();
            if (t == "*")
                break;

            bool ok = true;
            string[] ps = t.Split(' ');
            char n = ps[0][0];

            foreach (string p in ps)
            {
                if (n != p[0])
                {
                    ok = false;
                    break;
                }
            }

            Console.WriteLine(ok ? "Y" : "N");
        }
    }
}
