[[toc]]

# chap03
## chap3-5 Arrow function
它使用由等号和大于号字符组成的箭头=>代替function关键字
it uses an arrow made up of an equal sign and a greater-than character

these two definitions of sqare do the same thing:
```javascript
const square1 = (x) => {return x * x;};
const square2 = x => x * x;

```

## chap3-8 closure
能够引用封闭作用域中的局部绑定的特定实例的功能被称为闭包closure
the feature - being able to reference a specific instance of a local binding in an enclosing scope - is called closure.

```javascript
function multiplier(factor){
    return number => number * factor;
}
let twice = multiplier(2);
console.log(twice(5))
```
thinking about programs like this takes some practice. A good mental model is to think of function values as containing both the code in their body and the environment in which they are created. When called , the function body sees the environment in which it was created, not the environment in which it is called.
一个好的思路模型是将函数值视为同时包含其函数体内的代码和创建它们的环境。

## chap4-5 对象
创建对象的一种方法是使用大括号作为表达式。
one way to create an object is by using braces as an expression.
这意味总大括号在JavaScript中有两种含义。在语句开头，它们用来开始一个语句块。在任何其它位置，他们描述一个对象。

## chap4-7
相关性度量的是对统计变量之间的依赖性。统计变量与编程变量不完全相同。在统计学中，你通常有一组测量值，每个测量值都会测量每个变量。变量之间的相关性通常表示为-1到1之间的值。零相关意味着变量不相关。1表示完全相关，-1也意味着变量是完全相关的，但他们是对立的。
Correlation is a measure of dependence between statistical variables. A statistical variable is not quite the same as a programming variable. In statistics you typically have a set of measurements, and each variable is measured for every measurement. Correlation between variables is usually expressed as a value that ranges from -1 to 1. Zero correlation means the variables are not related. A correlation of one indicates that the two are perfectly related—if you know one, you also know the other. Negative one also means that the variables are perfectly related but that they are opposites—when one is true, the other is false

计算两个布尔变量之间的相关性度量，我们可以使用phi系数。 phi coefficient 