#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <chrono>

using namespace std;

class TreeNode{
public:
    int n;
    TreeNode* parent;
    vector<TreeNode*> nodes;

    TreeNode(TreeNode* parent, int n){
        this -> parent = parent;
        this -> n = n;
    }

    vector<TreeNode*> getNodes(){
        nodes.push_back(new TreeNode(this, n+3) );
        nodes.push_back(new TreeNode(this, n*2) );
        return nodes;
    }
};

void getPath(TreeNode* tNode, int n1){
    vector<int> order;
    TreeNode* node = tNode;
    while(node->n != n1){
        order.push_back(node->n);
        node = node->parent;
    }
    order.push_back(node->n);

    cout << order[order.size()-1];
    for (int i = order.size()-2; i >= 0; --i){
        cout << " -> " << order[i];
    }
    cout << endl;
}

void findPath(int n1, int n2){
    TreeNode* treeRoot = new TreeNode(nullptr, n1);
    queue<TreeNode*> q;
    q.push(treeRoot);

    while (!q.empty()){
        TreeNode* s = q.front();
        q.pop();
        if (s->n > n2+3)
            continue;
        if (s->n == n2){
            getPath(s, n1);
            break;
        }
        for (auto tNode: s->getNodes()){
            q.push(tNode);
        }
    }

}

int main()
{
    // +3 *2
    int n1, n2;
    cin >> n1 >> n2;

    auto time_start = std::chrono::steady_clock::now();
    findPath(n1, n2);

    auto finish = std::chrono::steady_clock::now();
    std::chrono::duration<double> diff = finish-time_start;
    std::cout<< diff.count() << std::endl;

    return 0;
}
