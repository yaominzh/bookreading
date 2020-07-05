[[toc]]

# 1.1 自定义函数的引入
## e1.1 给出平面上两个点的坐标，求两点之间的曼哈顿距离。
```cpp
#include<iostream>
using namespace std;
int main(){
    double x1, y1, x2, y2;
    double dx, dy;
    cin >> x1>> y1>>x2>>y2;
    if(x1>x2)
        dx=x1-x2;
    else
        dx = x2-x1;
    if(y1>y2)
        dy=y1-y2;
    else
        dy=y2-y1;
    cout<<dx+dy<<endl;
    return 0;
}
```

test | test2 | test3
--- | --- | ---
aa<br/>aa | bb |aa