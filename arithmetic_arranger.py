def arithmetic_arranger(list, bool):
    a = []
    b = []
    c = []
    l = []
    r = []
    run = True
    if len(list) >= 5:
        error1 = 'Error: Too many problems.'
        print(error1)
        run = False
        return error1
    else:
        for x in list:
            if "+" in x:
                x = x.split("+")
                x1 = x[0].strip()
                x2 = x[1].strip()
                if x1.isdigit() == True and x2.isdigit() == True:

                    if len(x1) <= 4 and len(x2) <= 4:
                        #print(f'{x1} and {x2}')

                        if len(x1) < len(x2):
                            l.append(len(x2))
                            a.append(x1)
                            b.append(x2)
                            c.append('+')
                            r.append(int(x1)+int(x2))
                        elif len(x1) == len(x2):
                            l.append(len(x2))
                            a.append(x1)
                            b.append(x2)
                            c.append('+')
                            r.append(int(x1) + int(x2))
                        else:
                            l.append(len(x1))
                            a.append(x1)
                            b.append(x2)
                            c.append('+')
                            r.append(int(x1) + int(x2))
                    else:
                        error6 = "Error: Numbers cannot be more than four digits."
                        print(error6)
                        run = False
                        return error6
                else:
                    error5 = "Error: Numbers must only contain digits."
                    print(error5)
                    run = False
                    return error5
            elif "-" in x:
                x = x.split("-")
                x1 = x[0].strip()
                x2 = x[1].strip()
                if x1.isdigit() == True and x2.isdigit() == True:
                    if len(x1) <= 4 and len(x2) <= 4:
                        #print(f'{x1} and {x2}')

                        if len(x1) < len(x2):
                            r.append(int(x1) + int(x2))
                            l.append(len(x2))
                            a.append(x1)
                            b.append(x2)
                            c.append('-')
                        elif len(x1) == len(x2):
                            r.append(int(x1) + int(x2))
                            l.append(len(x2))
                            a.append(x1)
                            b.append(x2)
                            c.append('-')
                        else:
                            r.append(int(x1) + int(x2))
                            l.append(len(x1))
                            a.append(x1)
                            b.append(x2)
                            c.append('-')

                    else:
                        error4 = "Error: Numbers cannot be more than four digits."
                        print(error4)
                        return error4
                else:
                    error3 = "Error: Numbers must only contain digits."
                    print(error3)
                    run = False
                    return error3

            else:
                error2 = "Error: Operator must be '+' or '-'."
                print(error2)
                run = False
                return error2
    if run == True:
        if bool == True:
            #First Line
            print(f'{a[0]:>{l[0] + 2}}{a[1]:>{l[1] + 6}}{a[2]:>{l[2] + 6}}{a[3]:>{l[3] + 6}}')
            #Second Line
            print(f'{c[0]:>0}{b[0]:>{l[0] + 1}}{c[1]:>5}{b[1]:>{l[1] + 1}}{c[2]:>5}{b[2]:>{l[2] + 1}}{c[3]:>5}{b[3]:>{l[3] + 1}}')
            #Dash Line
            print(f'{"_" * (l[0] + 2):>0}{"_" * (l[1] + 2):>{l[1] + 6}}{"_" * (l[2] + 2):>{l[2] + 6}}{"_" * (l[3] + 2):>{l[3] + 6}}')
            #Result Line
            print(f'{r[0]:>{l[0]+2}}{r[1]:>{l[1]+6}}{r[2]:>{l[2]+6}}{r[3]:>{l[3]+6}}')
        else:
            # First Line
            
            print(f'{a[0]:>{l[0] + 2}}{a[1]:>{l[1] + 6}}{a[2]:>{l[2] + 6}}{a[3]:>{l[3] + 6}}')
            # Second Line
            print(
                f'{c[0]:>0}{b[0]:>{l[0] + 1}}{c[1]:>5}{b[1]:>{l[1] + 1}}{c[2]:>5}{b[2]:>{l[2] + 1}}{c[3]:>5}{b[3]:>{l[3] + 1}}')
            # Dash Line
            print(
                f'{"_" * (l[0] + 2):>0}{"_" * (l[1] + 2):>{l[1] + 6}}{"_" * (l[2] + 2):>{l[2] + 6}}{"_" * (l[3] + 2):>{l[3] + 6}}')

    else:
        print("Some other error occurred.")


