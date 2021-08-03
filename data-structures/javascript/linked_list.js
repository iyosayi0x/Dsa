class Node {
  constructor(head = null, next = null) {
    this.head = head;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  /* addding to add_to_begining */
  add_to_begining(new_item) {
    let node = new Node(new_item, this.head);
    this.head = node;
  }
  /* adding to end */
  add_to_end(new_item) {
    if (this.head === null) {
      this.add_to_begining(new_item);
      return;
    }
    let itr = this.head;
    while (itr) {
      if (itr.next === null) {
        itr.next = new Node(new_item, null);
        break;
      }
      itr = itr.next;
    }
  }

  /* inserting at */
  insert_at(index, new_item) {
    if (index-1 > this.length()-1 || index < 0) {
      throw new Error("Invalid index");
    }
    if (index === 0) {
      this.add_to_begining(new_item);
      return;
    }
    let itr = this.head;
    let count = 0;
    while (itr) {
      if (count+1 == index) {
        itr.next = new Node(new_item, itr.next);
        break;
      }
      count++;
      itr = itr.next;
    }
  }

  /* replace at */
  delete_at(index) {
    if (index-1 > this.length()-1 || index < 0) {
      throw new Error("Invalid index");
    }
    if (index === 0) {
      this.head = this.head.next;
      return;
    }
    let itr = this.head;
    let count = 0;
    while (itr) {
      if (count+1 == index) {
        itr.next = itr.next.next;
        break;
      }
      count++;
      itr = itr.next;
    }
  }

  /* checking if empty */
  isEmpty() {
    return this.head? false: true;
  }
  length() {
    if (this.head === null) {
      return 0;
    }
    let itr = this.head;
    let count = 0;
    while (itr) {
      count++;
      itr = itr.next;
    }
    return count;
  }

  /* insering many values */
  insert_values(item_list) {
    this.head = null;
    item_list.forEach(item => this.add_to_end(item));
  }
  /* printing node */
  print_list() {
    let itr = this.head;
    let listr = "";
    while (itr) {
      listr += ` ${itr.head} --> `;
      itr = itr.next;
    }
    console.log(listr);
  }

}

const li = new LinkedList();

li.add_to_end(10);
li.add_to_end(20);
li.add_to_begining(30);
li.add_to_end(130);
li.print_list();
li.insert_at(4, "name");
li.print_list();
li.delete_at(2);
li.print_list();
li.insert_values(["2", "4", 6 , 10 , 20]);
li.print_list();
li.delete_at(3);
li.print_list();
console.log(li.length());