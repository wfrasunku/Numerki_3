import functions
import functionSolving

def main():
    functions_list = functions_menu()
    newton_cotes = functionSolving.newton_cotes_limes(functions_list, 0.01)
    for nodes in range(2, 6):
        gauss_chebyshev = functionSolving.gauss_chebyshev(functions_list, nodes)
        print("Dla", nodes, "węzłów, wartość Gaussa-Czybyszewa wynosi:", gauss_chebyshev)
    print("Wartość Newtona-Cotesa wynosi:", newton_cotes)



def functions_menu():
    functions_list: list = []
    functions_amount = 0
    while True:
        try:
            print(' 0) zakończ listę\n', '1) wielomian\n', '2) sinus\n', '3) cosinus\n', '4) tangens\n',
                  '5) cotanges\n', '6) moduł\n', '7) pieriwastek')
            functions_amount += 1
            equation = int(input(f'Dodaj równanie nr {functions_amount}: '))
            if 0 <= equation <= 7:
                match equation:
                    case 0:
                        if functions_amount > 1:
                            break
                        print('Najpierw musisz dodać funkcje! \n')
                        functions_amount -= 1
                    case 1:
                        while True:
                            factors_list: list = []
                            try:
                                i = int(input('\nPodaj najwyższą potęgę wielomianu: '))
                                for i in range(i + 1, 0, -1):
                                    x = float(input(f'Wartość x^{i - 1}: '))
                                    factors_list.append(x)
                                equation = functions.Polynomial(factors_list)
                                functions_list.append(equation)
                                break
                            except ValueError:
                                print('Niepoprawna wartość!')
                    case 2:
                        equation = functions.Sinus()
                        functions_list.append(equation)
                    case 3:
                        equation = functions.Cosinus()
                        functions_list.append(equation)
                    case 4:
                        equation = functions.Tangens()
                        functions_list.append(equation)
                    case 5:
                        equation = functions.Cotangens()
                        functions_list.append(equation)
                    case 6:
                        equation = functions.Abs()
                        functions_list.append(equation)
                    case 7:
                        equation = functions.Root()
                        functions_list.append(equation)
            else:
                print('Niepoprawna wartość!\n')
                functions_amount -= 1
        except ValueError:
            print('Niepoprawna wartość!\n')
            functions_amount -= 1

    return functions_list


if __name__ == '__main__':
    main()
