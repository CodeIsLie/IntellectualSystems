#include <iostream>
#include <vector>
#include <functional>
#include <queue>
#include <unordered_set>
#include <ctime>
#include <random>

using namespace std;

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

void showGrid(Node* node){
    vector<size_t >& grid = node->grid;
    for (int i = 0; i < grid.size(); ++i){
        if (i%4 == 0)
            cout << endl;
        cout << grid[i] << ' ';
    }
    cout << endl;
}

void showPath(Node* node){
    int steps = 0;
    while (node != nullptr){
        //showGrid(node);
        node = node -> parent;
        steps++;
    }
    cout << endl << "count steps is " << steps;
}

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

int Manhetten(Node* node){
    vector<size_t>& grid = node->grid;
    int sum = 0;
    for (int i = 0; i < 16; ++i){
        if (grid[i] == 0)
            continue;
        size_t currentI = (15 + grid[i]) % 16;
        int dx = abs((i % 4) - int(currentI % 4));
        int dy = abs(i/4 - int(currentI/4));
        sum += dx + dy;
    }
    return sum;
}

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

Node* randomState(Node* startState, int steps){
    Node* node = startState;
    while (steps--){
        auto moves = node->getMoves();
        node = moves[rand() % moves.size()];
    }
    return node;
}

int main() {
    srand(time(0));
    vector<size_t> startGrid = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0};
    //vector<size_t> startGrid = {15, 1, 2, 12, 8, 5, 6, 11, 4, 9, 10, 7,3, 14, 13, 0};
    for (int i = 0; i < 30; ++i) {
        Node *start = new Node(startGrid);
        start = randomState(start, 70);
        start->parent = nullptr;

        Node *answer = AStar(start, Manhetten);
        showPath(answer);
    }
    return 0;
}