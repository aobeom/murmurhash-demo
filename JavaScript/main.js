var murmurHash3 = require("murmurhash3js");

// Return 32 bit unsigned int (2911983372)
const calc32 = (key) => {
    var h32 = murmurHash3.x86.hash32(key)
    return h32
}

// Return 128 bit hex (09c01ad2296d65bdb32ceb54cdb5b54a)
const calc128 = (key) => {
    var h128 = murmurHash3.x64.hash128(key)
    var new_h128 = ""
    for (let i = 0; i < 8; ++i) {
        new_h128 += h128.slice(14 - 2 * i, 16 - 2 * i);
    }

    for (let i = 0; i < 8; ++i) {
        new_h128 += h128.slice(30 - 2 * i, 32 - 2 * i);
    }
    return new_h128
}


const key = "Hello world"
var c32 = calc32(key)
console.log("Javascript 32 Bit: " + c32)

var c128 = calc128(key)
console.log("Javascript x64 128 Bit: " + c128)
