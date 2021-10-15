# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from expression import Expression


def get_user_values(var_list):
    var_values = []
    for v in var_list:
        val = float(input(f"Input the value for the variable {v}:"))
        unc = float(input("\b +/- "))
        var_values.append((v, val, unc))
    return var_values


def get_user_expr():
    return input("Please input the mathematical expression you would like to propogate using pythonic math\n\n\t\t:")


if __name__ == '__main__':
    expr_str = get_user_expr()
    expr = Expression(expr_str)

    if expr.is_safe_to_exec():
        variables = expr.get_variables()
        values = get_user_values(variables)
        print(expr.propagate_uncertainty(values))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
