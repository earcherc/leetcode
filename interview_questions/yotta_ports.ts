// const someAsyncFunc = () => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(100)
//         }, 5000)
//     })
// }

// const handler = async () => {
//     const result = await someAsyncFunc()
//     console.log(result)
// }

// handler()

// function operation(a: number, b: number, func: (x: number, y: number ) => number) {
//     return func(a, b)
// }

// function addMultiply(a: number, b: number, factor: number) {
//     return (a + b) * factor
// }

// const result = operation(2,3, (x, y) => addMultiply(x,y,2))
// console.log(result)

const func = (a: string, b?: string): void => {
    console.log(a && b ? `${a}` + ', ' + `${b}` : a ? `${a}` : b ? `${b}` : 'No Input')
}

func('hello', 'world')
