// 1: This ought to be a RESTful call
// 2: No JSX - Just vanilla javascript 

const complex = `digraph {
    size="20"
    rankdir = LR
    graph [splines = true]
    node[color="black", shape="rectangle", overlap=false]
    {rank=same; r r2;}
    {rank=same; m1 c1;}
    
    r[label = "BlueFishBrownDirt"]
    r2[label="DinoFoot"]
  
    u [label="SquareCircle"]
  
    u->r [label="added"]
    u->r2 [label="added"]
  
    r->melk [label="?"]
    r->ei [label="LinearBox"]
    r->MNO [label="2 SkyShoe"]
    r->DEF [label="100 g"]
    r->ABC [label="Aoi"]
    r->OPQ [label="Brown Purple"]
    r->RST [label="PinkOrange"]
  
    co1 [label="Chicken Teeth"]
  
    r->co1 [label="course"]
    r2->co1 [label="course"]
  
    c1 [label="Silver"]
    c2 [label = "Bright Black"]
    m1 [label="Matte Water"]
  
    u->c1 [label="Low alpha red"]
    u->c2[label = "watermelor mars"]
    c1->r [label="to"]
    c2->r [label="to"]
  
    c1->m1 [label="media"]
  
  
    r2->DEF [label="Cat noise"]
  
    r2->Shirts [label="Whale hat"]
    r->Pants [label="Whale hat"]
  }`

const simple = `graph {
    grandparent -- "parent A";
    child;
    "parent B" -- child;
    grandparent --  "parent B";
  }`

const boxey = `
digraph D {

    subgraph cluster_p {
      label = "Parent";
  
      subgraph cluster_c1 {
        label = "Child one";
        a;
  
        subgraph cluster_gc_1 {
          label = "Grand-Child one";
           b;
        }
        subgraph cluster_gc_2 {
          label = "Grand-Child two";
            c;
            d;
        }
  
      }
  
      subgraph cluster_c2 {
        label = "Child two";
        e;
      }
    }
  }
`
let thing = `digraph D {

    node [shape=plaintext fontname="Sans serif" fontsize="8"];
  
    task_menu [ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 1</b></td></tr>
       <tr><td align="left">Choose Menu</td></tr>
       <tr><td align="left"><font color="darkgreen">done</font></td></tr>
     </table>>];
  
    task_ingredients [ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 2</b></td></tr>
       <tr><td align="left">Buy ingredients</td></tr>
       <tr><td align="left"><font color="darkgreen">done</font></td></tr>
     </table>>];
  
    task_invitation [ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 4</b></td></tr>
       <tr><td align="left">Send invitation</td></tr>
       <tr><td align="left"><font color="darkgreen">done</font></td></tr>
     </table>>];
  
    task_cook [ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 5</b></td></tr>
       <tr><td align="left">Cook</td></tr>
       <tr><td align="left"><font color="red">todo</font></td></tr>
     </table>>];
  
    task_table[ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 3</b></td></tr>
       <tr><td align="left">Lay table</td></tr>
       <tr><td align="left"><font color="red">todo</font></td></tr>
     </table>>];
  
    task_eat[ label=<
     <table border="1" cellborder="0" cellspacing="1">
       <tr><td align="left"><b>Task 6</b></td></tr>
       <tr><td align="left">Eat</td></tr>
       <tr><td align="left"><font color="red">todo</font></td></tr>
     </table>>];
  
  
    task_menu        -> task_ingredients;
    task_ingredients -> task_cook;
    task_invitation  -> task_cook;
    task_table       -> task_eat;
    task_cook        -> task_eat;
  
  }`

const working1 = `digraph {
    }`

const working2 = `digraph {
    }`

class Memory {

  constructor() {
    this.ary = []

    this.ary.push(simple)
    this.ary.push(complex)
    this.ary.push(boxey)
    this.ary.push(thing)
    this.ary.push(working1) // working 
    this.ary.push(working2) // working 

  }
  getDrawing(id) {
    const x = this.ary[id];
    return x
  }
  setDrawing(id, details) {
    this.ary[id] = details;
    //    console.log(id + "\n" + details + "\nand \n" + this.ary[id])
  }
}

export {
  Memory
}
