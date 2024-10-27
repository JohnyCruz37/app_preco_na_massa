import style from "./SectionListas.module.css"
import ItemListas from "../../components/itemListas/ItemListas"
interface ListaItem{
    id: number;
    nome: string;
    quantidade: number;
    valor: number;
}

interface SectionListasProps {
    lista: ListaItem[];
}

function SectionListas({lista}:SectionListasProps) {
  return (
    <section className={`${style.sectionLista} bloco-sec`}>
        <table className={`${style.tabela}`}>
            <tbody>
                {
                    lista.map((item) => (
                        <ItemListas
                            key={item.id}
                            nome={item.nome}
                            quantidade={item.quantidade}
                            valor={item.valor}
                        />
                    ))
                }
            </tbody>
        </table>
    </section>
  )
}

export default SectionListas
