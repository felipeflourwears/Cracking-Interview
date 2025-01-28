import { deleteDuplicate, invertirCadena, sumArray } from '../utils';

function App() {
 
  invertirCadena("Hello world")
  console.log("SUM FROM APP: ", sumArray([1, 2, 3, 4, 5]))
  console.log("Delete Duplicated: ", deleteDuplicate([1, 2, 2, 3, 4, 4]))
  return (
    <>
      <h1 className="text-3xl font-bold underline">
       Hello World
      </h1>
    </>
  )
}

export default App
