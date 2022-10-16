

def main():
    for i in range(10000):
        file = 'file'+str(i)+'.txt'
        f = open(file, 'x')
        f.write("This is file " + str(i+1))
        f.close()


if __name__ == '__main__':
    exit(main())
