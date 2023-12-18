class Rational:
    def __init__(self, N_, D_):
        self.N = N_
        self.D = D_


class Equation:
    def __init__(self, X_, Y_, op_):
        self.X = X_
        self.Y = Y_
        self.op = op_


class Input:
    X = Rational(0, 0)
    Y = Rational(0, 0)
    input_ = []
    N = 0

    @staticmethod
    def read_equation():
        eq = input().split()
        N1, N2, D1, D2 = int(eq[0]), int(eq[4]), int(eq[2]), int(eq[6])
        op = eq[3]
        Input.X = Rational(N1, D1)
        Input.Y = Rational(N2, D2)
        e = Equation(Input.X, Input.Y, op)
        return e

    @staticmethod
    def read():
        Input.N = int(input())
        for _ in range(Input.N):
            Input.input_.append(Input.read_equation())
        return Input.input_


class Operations:
    N, D, GDC = 0, 0, 0
    Resp = Rational(0, 0)

    @staticmethod
    def soma(input_):
        Operations.N = input_.X.N * input_.Y.D + input_.Y.N * input_.X.D

    @staticmethod
    def sub(input_):
        Operations.N = input_.X.N * input_.Y.D - input_.Y.N * input_.X.D

    @staticmethod
    def mult(input_):
        Operations.N = input_.X.N * input_.Y.N

    @staticmethod
    def div_(input_):
        Operations.N = input_.X.N * input_.Y.D
        Operations.D = input_.Y.N * input_.X.D

    @staticmethod
    def find_GDC(a, b):
        while b > 0:
            rem = a % b
            a = b
            b = rem
        Operations.GDC = a

    @staticmethod
    def simplify(rat):
        if abs(rat.N) > abs(rat.D):
            Operations.find_GDC(abs(rat.N), abs(rat.D))
        else:
            Operations.find_GDC(abs(rat.D), abs(rat.N))
        return Operations.GDC

    @staticmethod
    def calculate(input_):
        Operations.D = input_.X.D * input_.Y.D
        if input_.op == '+':
            Operations.soma(input_)
        elif input_.op == '-':
            Operations.sub(input_)
        elif input_.op == '*':
            Operations.mult(input_)
        elif input_.op == '/':
            Operations.div_(input_)
        Resp = Rational(Operations.N, Operations.D)
        return Resp


class Output:
    class Result:
        def __init__(self, resp1, resp2):
            self.Resp = resp1
            self.Simp_Resp = resp2

    output_ = []
    rat1 = Rational(0, 0)
    rat2 = Rational(0, 0)

    @staticmethod
    def execute_operations(input_):
        for i in range(Input.N):
            Output.rat1 = Operations.calculate(input_[i])
            GDC = Operations.simplify(Output.rat1)
            Output.rat2 = Rational(Output.rat1.N // GDC, Output.rat1.D // GDC)
            res = Output.Result(Output.rat1, Output.rat2)
            print(f"{res.Resp.N}/{res.Resp.D} = {res.Simp_Resp.N}/{res.Simp_Resp.D}")


def main():
    list_ = Input.read()
    Output.execute_operations(list_)


if __name__ == "__main__":
    main()
