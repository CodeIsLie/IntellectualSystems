//
// Created by Ilya on 25.09.2018.
//
#include "Node.h"

Node* randomState(Node* startState, int steps){
    Node* node = startState;
    while (steps--){
        auto moves = node->getMoves();
        node = moves[rand() % moves.size()];
    }
    return node;
}