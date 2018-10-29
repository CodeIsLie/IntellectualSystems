#include <iostream>
#include <ctime>
#include <map>
#include "Node.h"
#include "Search_algs.h"
#include "Heuristics.h"

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


int main() {
    int prev_time = (double)clock() / CLOCKS_PER_SEC * 1e3;

    srand(time(0));
    // vector<size_t> startGrid = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0};
    //vector<size_t> startGrid = {15, 1, 2, 12, 8, 5, 6, 11, 4, 9, 10, 7,3, 14, 13, 0};

    vector<size_t> startGrid = {1, 4, 3, 2, 5, 6, 12, 8, 9, 10, 11, 7, 13, 14, 15, 0};
    map<int, int> times;
    map<int, int> times_cnts;
//    Node* idanswer = IDAStar(new Node(startGrid), Manhetten);
//    showPath(idanswer);
//    idanswer = IDAStar(new Node(startGrid), Conflicts);
//    showPath(idanswer);

    for (int cnt_steps = 70; cnt_steps < 300; cnt_steps+=10)
        for (int i = 0; i < 1; ++i) {
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