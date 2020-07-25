import java.util.Stack;

/**
 * Created by AZ 2020-07-05
 */

public class sanbox {
    public static void main(String[] args) {
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        n1.left = n2;
        n1.right= n3;
        System.out.println("test");
        Chap03C01Traversal sol = new Chap03C01Traversal();

//        sol.preOrderRecur(n1);
//        sol.inOrderRecur(n1);
        preOrder_iter(n1);
    }

    private static void preOrder_iter(Node head) {
        Node cur = head;
        if(cur!=null){
            Stack<Node> stack= new Stack<Node>();
            stack.push(cur);
            while(!stack.isEmpty()){
                cur=stack.pop();
                System.out.print(cur.value + " ");
                if (cur.right != null) {
                    stack.push(cur.right);
                }
                if (cur.left != null) {
                    stack.push(cur.left);
                }
            }

        }

    }

}
