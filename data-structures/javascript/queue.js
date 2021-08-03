class Queue {
  constructor() {
    this.queue = [];
  }
  enqueue(new_item) {
    this.queue = [new_item,
      ...this.queue];
  }
  dequeue() {
    this.queue.pop();
  }
  print_queue() {
    console.log(this.queue);
  }
  isEmpty() {
    return this.queue.length ===0 ? true : false ;
  }
}
const queue = new Queue();
queue.enqueue("Hello world");
queue.enqueue("Whats up");
queue.enqueue(1);
queue.print_queue();
queue.dequeue();
queue.print_queue();