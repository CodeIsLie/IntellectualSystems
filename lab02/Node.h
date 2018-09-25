//
// Created by Ilya on 25.09.2018.
//
#ifndef LAB02_NODE_H
#define LAB02_NODE_H

#include <vector>
#include <random>

using std::vector;

class Node{
public:
    Node* parent;
    vector<size_t> grid;
    int x;
    int y;
    Node(vector<size_t> grid, int x=-1, int y=-1, Node* parent= nullptr){
        this -> grid = move(grid);
        if (x==-1 && y==-1){
            for (int i = 0; i < this->grid.size(); ++i){
                if (this->grid[i] == 0){
                    x = i % 4;
                    y = i / 4;
                }
            }
        }
        this -> x = x;
        this -> y = y;
        this->parent = parent;
    }

    Node* getNode(int newX, int newY){
        vector<size_t> newGrid = grid;
        newGrid[x+ y*4] = newGrid[newX + newY*4];
        newGrid[newX + newY*4] = 0;
        return new Node(newGrid, newX, newY, this);
    }

    vector<Node*> getMoves(){
        vector<Node*> moves;
        if (x > 0){
            moves.push_back(getNode(x-1, y));
        }
        if (x < 3){
            moves.push_back(getNode(x+1, y));
        }
        if (y > 0){
            moves.push_back(getNode(x, y-1));
        }
        if (y < 3){
            moves.push_back(getNode(x, y+1));
        }

        return move(moves);
    }
};

struct GridEquals{
public:
    bool operator()(const Node* node1, const Node* node2) const{
        return node1->grid == node2->grid;
    }
};

struct GridHash{
public:
    size_t operator()(const Node* node) const{
        size_t hash1 = 0;
        size_t hash2 = 0;
        const vector<size_t>& grid = node->grid;
        int i;
        for (i = 0; i < 8; ++i){
            hash1 <<= 2;
            hash1 += grid[i];
        }
        for (; i< 16; ++i){
            hash2 <<= 2;
            hash2 += grid[i];
        }
        return hash1 ^ hash2;
    }
};

Node* randomState(Node* startState, int steps);




#endif //LAB02_NODE_H
