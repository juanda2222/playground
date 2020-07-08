package main

import (
	"bytes"
	"fmt"
	"strings"
)

const (
	CONST_1 = 3               // The winning score in a game of Pig
	CONST_2 = "constant_word" // The number of games per series to simulate
)

func main() {

	fmt.Printf("hello, world\n")
	var s = "Japan"
	x := true // implicit declaration

	//---------------------
	// conditional staments
	//---------------------
	if !x {
		fmt.Println("true", s)
	} else {

		fmt.Println("true", s)
		sum := 0
		for i := 1; i <= 20; i++ {
			sum += i
		}
		fmt.Printf("Sum =  %d\n", sum)

		//while equivalent:
		for false {
		}
	}

	//------------------
	// string processing
	//------------------
	// Creating and initializing slice of string
	myslice := []string{"Welcome", "To",
		"GeeksforGeeks", "Portal"}

	// Concatenating the elements
	// present in the slice
	// Using join() function
	result := strings.Join(myslice, "-")
	fmt.Println("Joined strings: ", result)

	//-----------------
	// bytes processing
	//-----------------
	var my_buffer bytes.Buffer

	for i := 0; i < 10; i++ {
		my_buffer.WriteString("b")
	}

	fmt.Println(my_buffer.String())

	//-------
	// arrays
	//-------
	var vec [CONST_1]int
	vec = [...]int{12, 22, 52}

	// for {key}, {value} := range {list}
	for key, value := range vec {
		fmt.Println("My value", value, " is in key: ", key)
	}

	//----------
	// functions
	//----------
	fmt.Println("Function return value: ", dumb_function("foo_word"))
}

//-----------
// functions
//-----------
func dumb_function(word string) int {
	fmt.Println("Input function word: ", word)
	return 10
}
