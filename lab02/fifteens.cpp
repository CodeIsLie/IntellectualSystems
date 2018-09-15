#include <iostream>
#include <vector>

using namespace std;

class Node{
    vector<vector<int>> grid;
    int x;
    int y;
    Node(vector<vector<int>>& grid, int x, int y){
        this -> grid = move(grid);
        this -> x = x;
        this -> y = y;
//        for (int i = 0; i < 4; ++i){
//            for (int j = 0; j < 4; ++j){
//                if (grid[i][j] == 0) {
//                    x = j;
//                    y = i;
//                }
//
//            }
//        }
    }

    Node* getNode(int newX, int newY){
        vector<vector<int>> newGrid = grid;
        newGrid[x][y] = newGrid[newX][newY];
        newGrid[newX][newY] = 0;
        return new Node(newGrid, newX, newY);
    }

    vector<Node*> getMoves(){
        vector<Node*> moves;
        if (x > 0){
            int newX = x-1;
            int newY = y;
            moves.push_back(getNode(newX, newY));
        }

        if (x < 3){
            int newX = x+1;
            int newY = y;
            moves.push_back(getNode(newX, newY));
        }

        return moves;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}