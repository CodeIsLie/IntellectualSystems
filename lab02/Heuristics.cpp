//
// Created by Ilya on 25.09.2018.
//

#include "Heuristics.h"

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
