//
// Created by Ilya on 09.09.2018.
//
#include <queue>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;
class ForwardNode{
public:
    int n;
    ForwardNode* parent;

    ForwardNode(int n, ForwardNode* parent= nullptr){
        this -> parent = parent;
        this -> n = n;
    }

    vector<ForwardNode*> getNodes(){
        vector<ForwardNode*> nodes;
        nodes.push_back(new ForwardNode(n+3, this) );
        nodes.push_back(new ForwardNode(n*2, this) );
        return nodes;
    }
};

class BackNode{
public:
    int n;
    BackNode* parent;

    BackNode(int n, BackNode* parent= nullptr){
        this -> parent = parent;
        this -> n = n;
    }

    vector<BackNode*> getNodes(){
        vector<BackNode*> nodes;
        nodes.push_back(new BackNode(n-3, this) );
        if (n % 2 ==0)
            nodes.push_back(new BackNode(n/2, this) );
        return nodes;
    }
};

vector<int> getPath(ForwardNode* fNode, BackNode* bNode){
    vector<int> numbers(0);
    numbers.push_back(fNode->n);

    fNode = fNode ->parent;
    while (fNode!= nullptr){
        numbers.push_back(fNode -> n);
        fNode = fNode ->parent;
    }
    reverse(numbers.begin(), numbers.end());

    bNode = bNode ->parent;
    while (bNode != nullptr){
        numbers.push_back(bNode -> n);
        bNode = bNode ->parent;
    }
    return numbers;
}

void showPath(vector<int>& numbers){
    cout << numbers[0];
    for (int i = 1; i <numbers.size(); ++i){
        cout << " -> " << numbers[i];
    }
    cout << endl;
}

pair<ForwardNode*, BackNode*> bidirectional(int start, int end){
    // start 2 queues, one from start, second from end
    // create 2 sets, sets<TreeNode*>

    map<int, ForwardNode*> fSet;
    map<int, BackNode*> bSet;

    queue<pair<ForwardNode*, int>> fqueue;
    queue<pair<BackNode*, int>> bqueue;

    ForwardNode* fNode = new ForwardNode(start);
    fqueue.emplace(fNode, 0);
    fSet.emplace(start, fNode);

    BackNode* bNode = new BackNode(end);
    bqueue.emplace(bNode, 0);
    bSet.emplace(end, bNode);

    // while (True)
    // expand 1 layer from first queue, (delete old nodes), compare values with second set values (each with each)
    // vice versa , if find equals -> break, create path
    int i = 1;
    while (true){
        while (!fqueue.empty()){
            auto node = fqueue.front();
            if (node.second == i)
                break;
            fqueue.pop();

            auto it = bSet.find(node.first->n);
            if (it != bSet.end()){
                return make_pair(node.first, it->second);
            }
            for (auto fN: node.first->getNodes()){
                if (fN->n > end)
                    continue;
                if (fSet.find(fN -> n) == fSet.end()) {
                    fSet.emplace(fN->n, fN);
                    fqueue.emplace(fN, i);
                }
            }
        }

        while (!bqueue.empty()){
            auto node = bqueue.front();
            if (node.second == i)
                break;
            bqueue.pop();

            auto it = fSet.find(node.first->n);
            if (it != fSet.end()){
                return make_pair(it->second, node.first);
            }

            for (auto fN: node.first->getNodes()){
                if (bSet.find(fN -> n) == bSet.end()) {
                    bSet.emplace(fN->n, fN);
                    bqueue.emplace(fN, i);
                }
            }
        }

        i++;
    }
}

int main(int args, char* argv[]){
    int start;
    int end;
    std::string user_input(argv[1]);
    user_input += " ";
    user_input += argv[2];
    istringstream iss(user_input);
    iss >> start >> end;
    //cin >> start >> end;
    if (start > end){
        cout << "sorry, start number must be more than end number" << endl;
        return 0;
    }

    pair<ForwardNode*, BackNode*> nodes = bidirectional(start, end);
    vector<int> path = getPath(nodes.first, nodes.second);
    showPath(path);

    return 0;
}