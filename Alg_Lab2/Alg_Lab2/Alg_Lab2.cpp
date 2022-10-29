#include <iostream>

int board[8][8];
int count = 0;

int iterations = 0;

void PrintBoard()
{
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            std::cout << ((board[i][j]) ? "# " : ". ");
        }
        std::cout<<'\n';
    }
}

bool CheckBoard(int a, int b)
{
    for (int i = 0; i < a; i++)
    {
        if (board[i][b])
        {
            return false;
        }
    }
    for (int i = 1; i <= a && b - i >= 0; i++)
    {
        if (board[a - i][b - i])
        {
            return false;
        }
    }
    for (int i = 1; i <= a && b + i < 8; i++)
    {
        if (board[a - i][b + i])
        {
            return false;
        }
    }
    return true;
}

void SetQueen(int row)
{
    if (row == 8)
    {
        PrintBoard();
        std::cout << "Result №" << count++ << "\n\n";
    }
    for (int i = 0; i < 8; i++)
    {
        if (CheckBoard(row, i))
        {
            board[row][i] = 1;
            SetQueen(row + 1);
            board[row][i] = 0;
            iterations++;
        }
    }
}

int main()
{
    setlocale(LC_ALL, "Russian");
    SetQueen(0);
    std::cout << iterations;
}
