import java.util.*;
import java.util.function.Function;
import javafx.util.Pair;

public class SimpleHashTable {
	private NodeList[] hashTable; 
	private double f;
    private int size;

    private class Node {
    	private int key;
    	private Object val;
    	private Node next;
    	
    	private Node(int k, Object o) {
    		this.key = k;
    		this.val = o;
    		this.next = null;
    	}

    	private Node next() {
    		return this.next;
    	}
    }

    private class NodeList {
    	private Node head;
    	private Node tail;

    	private NodeList() {
    		Node dummy = new Node(-1, null);
    		this.head = dummy;
    		this.tail = this.head;
    	}

    	private void add(Node n) {
    		this.tail.next = n;
    		this.tail = n;
    	}

    	private Object get(int k) {
    		Node curr = this.head.next;
    		while (curr != null) {
    			if (curr.key == k) {
    				return curr.val;
    			}
    			curr = curr.next;
    		}
    		return null;
    	}

    	private Object remove(int k) {
    		Node curr = this.head;
    		while (curr.next != null) {
    			if (curr.next.key == k) {
    				Object ans = curr.next.val;
    				if (curr.next == this.tail) {
    					this.tail = curr;
    				}
    				curr.next = curr.next.next;
    				return ans;
    			}
    			curr = curr.next;
    		}
    		return null;
    	}

    	private String myString() {
    		String ans = "";
    		Node curr = this.head.next;
    		while (curr != null) {
    			if (curr.val == null) {
    				ans += curr.key + ": null, ";
    			} else {
    				ans += curr.key + ": " + curr.val.toString() + ", ";
    			}
    			curr = curr.next;
    		}
    		if (ans.length() > 2) {
    			ans = ans.substring(0, ans.length()-2);
    		}
    		return ans;
    	}
    }

	public SimpleHashTable(int size, double fillFactor) {
		// Make resizing function later
		if (fillFactor > 1) {
			throw new IllegalArgumentException("Fill factor must be less than 1.");
		} else {
			this.f = fillFactor;
		}
      	this.size = size;
		this.hashTable = new NodeList[size];
	}

	public void add(int key, Object value) {
      	int bucket = key % this.size;
      	if (this.hashTable[bucket] == null) {
      		this.hashTable[bucket] = new NodeList();
      	} 
        this.hashTable[bucket].add(new Node(key, value));
	}

	public Object get(int key) {
		int bucket = key % this.size;
		if (this.hashTable[bucket] == null) {
			return null;
		} else {
			return this.hashTable[bucket].get(key);
		}
	}

	public Object remove(int key) {
		int bucket = key % this.size;
		if (this.hashTable[bucket] == null) {
			return null;
		} else {
			return this.hashTable[bucket].remove(key);
		}
	}

	public void print() {
		System.out.println("Buckets");
		for (int i=0; i<hashTable.length; i++) {
			if (hashTable[i] == null) {
				System.out.println(i + ":\t");
			} else {
				System.out.println(i + ":\t" + hashTable[i].myString());
			}
		}
	}
  
  	public static void main(String[] args) {
		SimpleHashTable h = new SimpleHashTable(10, 0.5);
      	for (int i=0; i<10; i++) {
      		h.add(i*i, new Integer(i));
      	}
      	h.print();

      	System.out.println();
      	System.out.println(h.get(16));
      	System.out.println(h.remove(16));
      	System.out.println(h.get(16));
      	System.out.println(h.remove(16));
      	System.out.println(h.remove(36));
      	System.out.println();

      	h.add(36, new Integer(36));
      	h.add(28, new Integer(28));

      	h.print();
	}
}
