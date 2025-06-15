package main

import (
	"fmt"
	"strconv"
	"strings"
)

func memory_out() {
	var N int
	fmt.Scanln(&N)

	s := ""
	for i := 1; i <= N; i++ {
		s += strconv.Itoa(i)
	}

	idx := strings.Index(s, strconv.Itoa(N))
	fmt.Println(idx + 1)

}

func main() {
	var N int
	fmt.Scanln(&N)

	Nstr := strconv.Itoa(N)
	Nlen := len(Nstr)

	// ASCII 문자만 다루므로 byte로 처리
	window := make([]byte, 0, Nlen)
	pos := 1

	for i := 1; ; i++ {
		s := strconv.Itoa(i)
		for j := 0; j < len(s); j++ {
			window = append(window, s[j])

			// 윈도우가 Nlen보다 작으면 맨 앞에 삭제
			if len(window) > Nlen {
				window = window[1:]
				pos++
			}

			if len(window) == Nlen && string(window) == Nstr {
				fmt.Println(pos)
				return
			}
		}
	}
}
