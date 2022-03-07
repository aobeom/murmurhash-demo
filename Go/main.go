package main

import (
	"encoding/binary"
	"fmt"

	"github.com/spaolacci/murmur3"
)

// Return 32 bit unsigned int (2911983372)
func calc32(key string) uint32 {
	h32 := murmur3.Sum32([]byte(key))
	return h32
}

// Return 128 bit hex (09c01ad2296d65bdb32ceb54cdb5b54a)
func calc128(key string) string {
	h1, h2 := murmur3.Sum128([]byte(key))

	h1Byte := make([]byte, 8)
	h2Byte := make([]byte, 8)
	binary.LittleEndian.PutUint64(h1Byte, h1)
	binary.LittleEndian.PutUint64(h2Byte, h2)

	h128 := fmt.Sprintf("%x%x", h1Byte, h2Byte)
	return h128
}

func main() {
	key := "Hello world"

	c32 := calc32(key)
	fmt.Printf("Golang 32 Bit: %d\n", c32)

	c128 := calc128(key)
	fmt.Printf("Golang x64 128 Bit: %s\n", c128)
}
