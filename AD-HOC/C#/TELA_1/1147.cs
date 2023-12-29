using System;

class Program
{
    static int[] dr = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dc = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int[] dr2 = {1, 1};
    static int[] dc2 = {-1, 1};

    static bool Val(int i, int j)
    {
        return i >= 0 && i < 8 && j >= 0 && j < 8;
    }

    static int GetX(string input)
    {
        return input[0] - '1';
    }

    static int GetY(string input)
    {
        return input[1] - 'a';
    }

    static void Main()
    {
        int[,] tab = new int[8, 8];
        int c = 1;

        while (true)
        {
            string input = Console.ReadLine();
            if (input == "0")
                return;

            int x = GetX(input);
            int y = GetY(input);
            Array.Clear(tab, 0, tab.Length);

            for (int i = 0; i < 8; ++i)
            {
                input = Console.ReadLine();
                tab[GetX(input), GetY(input)] = 1;
            }

            int ans = 0;
            for (int i = 0; i < 8; ++i)
            {
                if (Val(x + dr[i], y + dc[i]))
                {
                    int flag = 0;
                    for (int j = 0; j < 2; ++j)
                    {
                        if (Val(x + dr[i] + dr2[j], y + dc[i] + dc2[j]))
                        {
                            if (tab[x + dr[i] + dr2[j], y + dc[i] + dc2[j]] != 0)
                            {
                                flag = 1;
                                break;
                            }
                        }
                    }
                    if (flag == 0)
                        ++ans;
                }
            }

            Console.WriteLine($"Caso de Teste #{c++}: {ans} movimento(s).");
        }
    }
}