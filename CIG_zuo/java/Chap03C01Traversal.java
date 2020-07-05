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

        sol.preOrderRecur(n1);
        sol.inOrderRecur(n1);
        sol.postOrderRecur(n1);

    }

    public void postOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        preOrderRecur(head.left);
        preOrderRecur(head.right);
        System.out.println( head.value+  " ");
    }

    public void inOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        preOrderRecur(head.left);
        System.out.println( head.value+  " ");
        preOrderRecur(head.right);
    }

    public void preOrderRecur(Node head) {
        if (head == null) {
            return ;
        }
        System.out.println( head.value+  " ");
        preOrderRecur(head.left);
        preOrderRecur(head.right);
    }
}
