class Stack{
  constructor(){
    this.stack = [];
  }
  add(new_item){
    this.stack = [new_item , ...this.stack];
  }
  pop(){
    this.stack = this.stack.slice(1,);
  }
  print_stack(){
    console.log(this.stack);
  }
  isEmpty(){
   return this.stack.length ===0 ? true : false ;
    
  }
}

const stack = new Stack();
stack.add("name");
stack.add(2);
stack.add(4);
stack.print_stack();
stack.pop();
stack.print_stack();
stack.pop();
stack.print_stack();
console.log(stack.isEmpty());
