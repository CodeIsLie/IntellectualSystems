//
// Created by Ilya on 25.09.2018.
//

#include "Search_algs.h"

using namespace std;

bool isGoal(vector<size_t> grid){
    for (int i = 0; i < grid.size()-1; ++i){
        if (i+1 != grid[i])
            return false;
    }
    return grid[grid.size()-1] == 0;
}

bool solvable(Node* node){
    vector<size_t > grid = node->grid;
    int cntInversions = 0;
    for (int i = 0; i < grid.size(); ++i){
        for (int j = i+1; j < grid.size(); ++j){
            if (grid[i] && grid[j] && grid[i] > grid[j])
                cntInversions++;
        }
    }

    int y = node->y;
    return (cntInversions%2 == 0 && y%2==1) || (cntInversions%2 == 1 && y%2==0);
}

Node* AStar(Node* node, function<int(Node*)> h){
    if (!solvable(node)){
        cout << "Unsolvable" << endl;
        return node;
    }

    unordered_set<Node*, GridHash, GridEquals> used;
    priority_queue<pair<int, Node*>> qq;
    qq.emplace(-h(node), node);

    while (!qq.empty()){
        auto node = qq.top();
        used.insert(node.second);
        qq.pop();

        if (isGoal(node.second->grid)){
            return node.second;
        }

        int pathLength = -node.first - h(node.second);
        for (Node* to: node.second->getMoves()){
            //showGrid(to);
            if (used.find(to) == used.end()) {
                size_t heur = h(to) + pathLength + 1;
                qq.emplace(-heur, to);
            }
        }
    }
}

Node* IDAStar(Node* node, function<int(Node*)> h, int deep){
    unordered_set<Node*, GridHash, GridEquals> used;

    priority_queue<pair<int, Node*>> qq;
    qq.emplace(-h(node), node);

    while (!qq.empty()){
        auto node = qq.top();
        used.insert(node.second);
        qq.pop();

        if (isGoal(node.second->grid)){
            return node.second;
        }

        int pathLength = -node.first - h(node.second);
        if (pathLength + 1 >= deep)
            return nullptr;
        for (Node* to: node.second->getMoves()){
            if (used.find(to) == used.end()) {
                size_t heur = h(to) + pathLength + 1;
                qq.emplace(-heur, to);
            }
        }
    }
    return nullptr;
}

Node* IDAStar(Node* node, function<int(Node*)> h){
    if (!solvable(node)){
        cout << "Unsolvable" << endl;
        return node;
    }

    for (int i = 0; i < 90; ++i){
        Node* answer = IDAStar(node, h, i);
        if (answer != nullptr && isGoal(answer->grid)){
            return answer;
        }
    }
}