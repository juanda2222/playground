function seAbre(horarios, minimo){
    let aTiempo = 0;
    for(let i =0 ;i< horarios.length;i++){
        if(horarios[i]<=0){
            aTiempo ++;
            console.log("cero o negativos")
        }
        if(aTiempo >= minimo){
              return true;
        } else{
            return false;
        }

    }
}

let horarios_vec = [ -1, -4, 3, 6, 0]
let minimo = 2

console.log("Se abre? ", seAbre(horarios_vec, minimo))