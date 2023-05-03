class MyQueue {
public:
    stack <int> s1;
    stack <int> s2;
    MyQueue() {
        
    }
    
    void push(int x) {
        if(s2.empty()) s1.push(x);
        else{
            while(!s2.empty()){
                s1.push(s2.top());
                s2.pop();
            }
            s1.push(x);
        }
    }
    
    int pop() {
        int top;
        if(s1.empty() && s2.empty()){
            return {};
        }if(s1.empty() && !s2.empty()){
            top =s2.top();
            s2.pop(); 
        }if(!s1.empty() && s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
            top = s2.top();
            s2.pop();
        }
        return top;
    }
    
    int peek() {
        int top;
        if(s1.empty() && s2.empty()){
            return {};
        }if(s1.empty() && !s2.empty()){
            top = s2.top();
        }if(!s1.empty() && s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
            top = s2.top();
        }
        return top;
    }
    
    bool empty() {
         if(s1.empty() && s2.empty()) return true;
         else return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */