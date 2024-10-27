import HeaderListas from "../../components/headerListas/HeaderListas"
import SectionListas from "../../components/sectionListas/SectionListas"
const lista = [
    {
        id: 1,
        nome: "Caixa cento",
        quantidade: 1,
        valor: 5.60
    },
    {
        id: 2,
        nome: "forminhas de brigadeiro",
        quantidade: 1,
        valor: 3.50
    }
]


function ListaEmbalagens() {
  return (
    <main className={``}>
        <HeaderListas 
            titulo={"Embalagens"}
            totalLista={30}
        />
        <SectionListas 
            lista={lista}
        />
    </main>
  )
}

export default ListaEmbalagens
