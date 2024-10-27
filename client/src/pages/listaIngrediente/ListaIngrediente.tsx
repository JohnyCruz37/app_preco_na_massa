
import HeaderListas from "../../components/headerListas/HeaderListas"
import SectionListas from "../../components/sectionListas/SectionListas"
const lista = [
    {
        id: 1,
        nome: "leite",
        quantidade: 1,
        valor: 5.60
    },
    {
        id: 2,
        nome: "farinha de trigo",
        quantidade: 1,
        valor: 3.50
    }
]


function ListaIngrediente() {
  return (
    <main className={``}>
        <HeaderListas 
            titulo={"Ingredientes"}
            totalLista={30}
        />
        <SectionListas 
            lista={lista}
        />
    </main>
  )
}

export default ListaIngrediente
