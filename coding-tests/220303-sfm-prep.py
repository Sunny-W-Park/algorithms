#1

def main():
    x = input()

    enemy = 0
    warrior = 0

    for i in range(len(x)):
        if x[i] == '(':
            enemy += 1
        if x[i] == ')':
            warrior += 1

    if enemy == warrior:
        print('Yes')
    else:
        print('No')

if __name__=="__main__":
    main()

#2 SQL

#3 WEB
