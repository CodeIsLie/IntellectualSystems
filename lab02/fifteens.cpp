#include <iostream>
#include <functional>
#include <queue>
#include <unordered_set>
#include <ctime>
#include <map>
#include "Node.h"

#define TIME

using namespace std;

void showGrid(Node* node){
    vector<size_t >& grid = node->grid;
    for (int i = 0; i < grid.size(); ++i){
        if (i%4 == 0)
            cout << endl;
        cout << grid[i] << ' ';
    }
    cout << endl;
}

int showPath(Node* node){
    int steps = 0;
    while (node != nullptr){
        //showGrid(node);
        node = node -> parent;
        steps++;
    }
    //cout << endl << "count steps is " << steps;
    return steps;
}

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

int Conflicts(Node* node){
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

    for (int y=0; y < 4; ++y){
        for (int x=0; x < 4; ++x){
            for (int x1 = x+1; x1<4; ++x1){
                if (grid[y*4 + x] && grid[y*4 + x1])
                    if ((grid[y*4 + x]-1) / 4 == y && (grid[y*4 + x1]-1) / 4 == y && grid[y*4 + x] > grid[y*4 + x1]){
                        sum += 2;
                    }
            }
            for (int y1 = y+1; y1<4; ++y1){
                if (grid[y*4 + x] && grid[y1*4 + x])
                    if ((grid[y*4 + x]-1) % 4 == x && (grid[y1*4 + x]-1) % 4 == x && grid[y*4 + x] > grid[y1*4 + x]){
                        sum += 2;
                    }
            }
        }
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


int main() {
    int prev_time = (double)clock() / CLOCKS_PER_SEC * 1e3;

    srand(time(0));
    // 143256C89AB7DEF0
    // vector<size_t> startGrid = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0};
    //vector<size_t> startGrid = {15, 1, 2, 12, 8, 5, 6, 11, 4, 9, 10, 7,3, 14, 13, 0};

    vector<size_t> testGrid = {1, 4, 3, 2, 5, 6, 12, 8, 9, 10, 11, 7, 13, 14, 15, 0};
    cout << Conflicts(new Node(testGrid)) << endl;

    vector<size_t> startGrid = {1, 4, 3, 2, 5, 6, 12, 8, 9, 10, 11, 7, 13, 14, 15, 0};
    map<int, int> times;
    map<int, int> times_cnts;
//    Node* idanswer = IDAStar(new Node(startGrid), Manhetten);
//    showPath(idanswer);
//    idanswer = IDAStar(new Node(startGrid), Conflicts);
//    showPath(idanswer);

    for (int cnt_steps = 10; cnt_steps < 200; cnt_steps+=10)
        for (int i = 0; i < 10; ++i) {
            Node *start = new Node(startGrid);
            start = randomState(start, cnt_steps);
            start->parent = nullptr;
            Node *answer = AStar(start, Conflicts);
            int steps = showPath(answer);

    #ifdef TIME
            cout << "\n=========== ";
            int time = ((double)clock() / CLOCKS_PER_SEC * 1e3) - prev_time;
            times[steps] += time;
            times_cnts[steps] ++;
            cout << time;
            prev_time = ((double)clock() / CLOCKS_PER_SEC * 1e3);
    #endif

    //        Node* idanswer = IDAStar(start, Conflicts); //IDAStar(start, Manhetten);
    //        showPath(idanswer);
    //#ifdef TIME
    //        cout << "\n=========== ";
    //        cout<< ((double)clock() / CLOCKS_PER_SEC * 1e3) - prev_time;
    //        prev_time = ((double)clock() / CLOCKS_PER_SEC * 1e3);
    //        cout << endl;
    //#endif
        }

    for (auto vals: times){
        printf("steps = %d AVG time = %d\n", vals.first, vals.second/times_cnts[vals.first]);
    }
    return 0;
}