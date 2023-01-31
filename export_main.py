

def CreateTable(data,dataName,dataNumber):
    with open('Table.csv', 'a') as file:
        file.write('{};{};{}\n'
                    .format(data,dataName,dataNumber))

