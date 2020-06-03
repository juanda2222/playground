const faa = () => {
    if (!this.bar){
        this.bar = "bar"; 
    }
    this.bar += "bar"; 
    console.log(this.bar)
}
function foo(){
    if (!this.bar){
        this.bar = "bar"; 
    }
    this.bar += "bar"; 
   console.log(this.bar)
}

faa()
foo()