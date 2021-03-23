// 1: This ought to be a RESTful call
// 2: No JSX - Just vanilla javascript 

const complex = `digraph {
    size="6"
    rankdir = LR
    graph [splines = true]
    node[color="black", shape="rectangle", overlap=false]
    {rank=same; r r2;}
    {rank=same; m1 c1;}
    
    r[label = "Macaronischotel"]
    r2[label="Burrito's"]
  
    u [label="John"]
  
    u->r [label="added"]
    u->r2 [label="added"]
  
    r->melk [label="1 L"]
    r->ei [label="2 stuks"]
    r->macaroni [label="2 kopjes"]
    r->oudekaas [label="100 g"]
    r->kipbouillon [label="1 blokje"]
    r->ham [label="200 g"]
    r->peper [label="snufje"]
  
    co1 [label="Hoofdgerecht"]
  
    r->co1 [label="course"]
    r2->co1 [label="course"]
  
    c1 [label="20 dec 2017\n18:00"]
    c2 [label = "30 jan 2018\n17:00"]
    m1 [label="Nom nom.jpg"]
  
    u->c1 [label="checked in"]
    u->c2[label = "checked in"]
    c1->r [label="to"]
    c2->r [label="to"]
  
    c1->m1 [label="media"]
  
  
    r2->oudekaas [label="100 g"]
  
    r2->mexicaans [label="keuken"]
    r->hollands [label="keuken"]
  }`

const simple = `graph {
    grandparent -- "parent A";
    child;
    "parent B" -- child;
    grandparent --  "parent B";
  }`





class Memory {

    constructor() {
        this.ary = []
        this.index = 0

        this.ary.push(simple)
        this.ary.push(complex)
    }

    getNext() {
        const x = this.ary[this.index];
        this.index++
        if (this.index >= (this.ary.length)) {
            this.index = 0;
        }
        return x
    }
}

export {
    Memory
}