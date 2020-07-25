import java.util.Stack;

/**
 * Created by AZ 2020-07-05
 */

public class Chap03C01Traversal {


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
        sol.postOrderRecur(n1);
        sol.preOrderUnRecur(n1);

    }

    public void postOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        preOrderRecur(head.left);
        preOrderRecur(head.right);
        System.out.print( head.value+  " ");
    }

    public void inOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        preOrderRecur(head.left);
        System.out.print( head.value+  " ");
        preOrderRecur(head.right);
    }

    public void preOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        System.out.print( head.value+  " ");
        preOrderRecur(head.left);
        preOrderRecur(head.right);
    }
    public void preOrderUnRecur(Node head) {
        System.out.print("pre-order: ");
        if(head !=null){
            Stack<Node> stack = new Stack<Node>();
            stack.add(head);
            while (!stack.isEmpty()) {
                head = stack.pop();
                System.out.print(head.value + " ");
                if (head.right != null) {
                    stack.push(head.right);
                }
                if (head.left != null) {
                    stack.push(head.left);
                }
            }
        }
        System.out.println();
    }

}
