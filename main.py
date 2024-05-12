import menu
import functionSolving


def main():
    file_path = 'chebyshev.txt'
    functions_list = menu.functions_menu()
    precision = menu.precision_menu()
    newton_cotes = functionSolving.newton_cotes_limes(functions_list, precision)
    for nodes in range(2, 6):
        data = menu.read_data(file_path, nodes)
        gauss_chebyshev = functionSolving.gauss_chebyshev(functions_list, nodes, data)
        print("Dla", nodes, "węzłów, wartość Gaussa-Czybyszewa wynosi:", gauss_chebyshev)
    print("Wartość Newtona-Cotesa wynosi:", newton_cotes)


if __name__ == '__main__':
    main()
