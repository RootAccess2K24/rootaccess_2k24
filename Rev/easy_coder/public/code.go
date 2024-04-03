package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func myfunc1(num int) string {
	var init string
	for num > 0 {
		var i int = num % 2
		val := strconv.Itoa(i)
		init += val
		num = num / 2
	}
	var aur_bhai_kaisa_laga string
	for _, char := range init {
		aur_bhai_kaisa_laga = string(char) + aur_bhai_kaisa_laga
	}
	var l int = len(aur_bhai_kaisa_laga)
	var y int = 8 - l
	if y != 0 {
		for y > 0 {
			aur_bhai_kaisa_laga = string("0") + aur_bhai_kaisa_laga
			y--
		}
	}
	return aur_bhai_kaisa_laga
}
func myfunc2(num int) string {
	var init string
	for num > 0 {
		var i int = num % 2
		val := strconv.Itoa(i)
		init += val
		num = num / 2
	}
	var aur_bhai_kaisa_laga string
	for _, char := range init {
		aur_bhai_kaisa_laga = string(char) + aur_bhai_kaisa_laga
	}
	var l int = len(aur_bhai_kaisa_laga)
	var y int = 6 - l
	if y != 0 {
		for y > 0 {
			aur_bhai_kaisa_laga = string("0") + aur_bhai_kaisa_laga
			y--
		}
	}
	return aur_bhai_kaisa_laga
}
func myfunc3(char rune) int {
	var val int = int(char)
	return val
}
func myfunc4(str string) []string {
	var x int = len(str) % 6
	for x > 0 {
		str += string("0")
		x--
	}
	var chunk = []string{}
	for i := 0; i < len(str)-6; i = i + 6 {
		chunk = append(chunk, str[i:i+6])
	}
	return chunk
}
func myfunc5(myfunc4 []string) []int64 {
	var x = []int64{}
	for _, i := range myfunc4 {
		var y int64
		y, _ = strconv.ParseInt(i, 2, 8)
		x = append(x, y)
	}
	return x
}
func func12(myfunc4 []int64) string {
	var arr string = "abcdefghijklmnopqrstuvwxyz+/ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
	var ans string
	for _, i := range myfunc4 {
		ans += string(arr[i])
	}
	return ans
}
func myfunc6(str string) []string {
	var x int = len(str) % 8
	for x > 0 {
		str += string("0")
		x--
	}
	var chunk = []string{}
	for i := 0; i < len(str)-8; i = i + 8 {
		chunk = append(chunk, str[i:i+8])
	}
	return chunk
}
func funC7(enc string) []int {
	var arr string = "abcdefghijklmnopqrstuvwxyz+/ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
	index := []int{}
	for _, char := range enc {
		for i := range arr {
			if rune(arr[i]) == char {
				index = append(index, i)
			}
		}
	}
	return index
}
func funcy(enc []int64) string {
	var str string
	for _, char := range enc {
		str += string(char)
	}
	return str
}
func main() {
	fmt.Printf("Bol bhai tereko kya chahiye :")
	reader := bufio.NewReader(os.Stdin)
	inp, _ := reader.ReadString('\n')
	var str string
	for _, i := range inp {
		str += myfunc1(myfunc3(i))
	}
	var c []string = myfunc4(str)
	var x []int64 = myfunc5(c)
	enc := func12(x)
	fmt.Println("Yeh le tera maal bro : ", enc)
}