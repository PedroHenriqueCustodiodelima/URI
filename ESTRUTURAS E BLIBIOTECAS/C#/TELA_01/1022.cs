using System;
using System.Collections.Generic;

namespace TDA_Rational
{
    class Input
    {
        public class Rational
        {
            public int N;
            public int D;

            public Rational(int N_, int D_)
            {
                this.N = N_;
                this.D = D_;
            }
        }
        public class Equation
        {
            public Rational X;
            public Rational Y;
            public char op;

            public Equation(Rational X_, Rational Y_, char op_)
            {
                this.X = X_;
                this.Y = Y_;
                this.op = op_;
            }
        }

        public static Rational X, Y;
        public static List<Equation> input_ = new List<Equation>();
        public static int N;

        public static Equation Read_equation()
        {
            char[] space = { ' ' };
            string eq = Console.ReadLine();
            string[] variables = eq.Split(space);
            int N1, N2, D1, D2;
            char op;
            N1 = int.Parse(variables[0]);
            D1 = int.Parse(variables[2]);
            op = char.Parse(variables[3]);
            N2 = int.Parse(variables[4]);
            D2 = int.Parse(variables[6]);
            X = new Rational(N1, D1);
            Y = new Rational(N2, D2);
            Equation e = new Equation(X, Y, op);
            return e;
        }

        public static List<Equation> Read()
        {
            N = int.Parse(Console.ReadLine());
            for (int i = 0; i < N; i++)
            {
                input_.Add(Read_equation());
            }

            return input_;
        }

    }

    class Operations
    {
        public static int N, D, GDC;
        public static Input.Rational Resp;

        public static void Soma_(Input.Equation input_)
        {
            N = input_.X.N * input_.Y.D + input_.Y.N * input_.X.D;
        }

        public static void Sub_(Input.Equation input_)
        {
            N = input_.X.N * input_.Y.D - input_.Y.N * input_.X.D;
        }

        public static void Mult_(Input.Equation input_)
        {
            N = input_.X.N * input_.Y.N;
        }

        public static void Div_(Input.Equation input_)
        {
            N = input_.X.N * input_.Y.D;
        }

        public static void Find_GDC(int a, int b)
        {
            while (b > 0)
            {
                int rem = a % b;
                a = b;
                b = rem;
            }
            GDC = a;
        }

        public static int Simplify(Input.Rational rat)
        {
            if (Math.Abs(rat.N) > Math.Abs(rat.D))
            {
                Find_GDC(Math.Abs(rat.N), Math.Abs(rat.D));
            }
            else
            {
                Find_GDC(Math.Abs(rat.D), Math.Abs(rat.N));
            }

            return GDC;
        }

        public static Input.Rational Calculate(Input.Equation input_)
        {
            D = input_.X.D * input_.Y.D;
            if (input_.op == '+')
            {
                Soma_(input_);
            }
            else if (input_.op == '-')
            {
                Sub_(input_);
            }
            else if (input_.op == '*')
            {
                Mult_(input_);
            }
            else if (input_.op == '/')
            {
                Div_(input_);
                D = input_.Y.N * input_.X.D;
            }
            Resp = new Input.Rational(N, D);
            return Resp;
        }
    }

    class Output
    {
        public class Result
        {
            public Input.Rational Resp;
            public Input.Rational Simp_Resp;

            public Result(Input.Rational resp1, Input.Rational resp2)
            {
                this.Resp = resp1;
                this.Simp_Resp = resp2;
            }
        }

        public static List<Result> output_ = new List<Result>();
        public static Input.Rational rat1, rat2;

        public static void ExecuteOperations(List<Input.Equation> input_)
        {
            for (int i = 0; i < Input.N; i++)
            {
                rat1 = Operations.Calculate(input_[i]);
                int GDC = Operations.Simplify(rat1);
                rat2 = new Input.Rational(rat1.N / GDC, rat1.D / GDC);
                Result res = new Result(rat1, rat2);
                Console.WriteLine(res.Resp.N + "/" + res.Resp.D + " = " + res.Simp_Resp.N + "/" + res.Simp_Resp.D);
            }

        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Input.Equation> list_ = Input.Read();
            Output.ExecuteOperations(list_);
        }
    }
}