import HeaderListas from "../../components/headerListas/HeaderListas"
import SectionListas from "../../components/sectionListas/SectionListas"
const lista = [
    {
        id: 1,
        nome: "Papel Film",
        quantidade: 1,
        valor: 5.60
    },
    {
        id: 2,
        nome: "Papel Manteiga",
        quantidade: 1,
        valor: 3.50
    }
]


function ListaInsumos() {
  return (
    <main className={``}>
        <HeaderListas 
            titulo={"Insumos"}
            totalLista={30}
        />
        <SectionListas 
            lista={lista}
        />
    </main>
  )
}

export default ListaInsumos
