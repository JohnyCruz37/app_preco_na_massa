import style from "./ItemListas.module.css"

import { FaChevronRight } from 'react-icons/fa';

interface ItemListaProps {
    nome: string;
    quantidade: number;
    valor: number;
}

function ItemListas({nome, quantidade, valor}: ItemListaProps) {
  return (
    <tr className={`${style.itemLista} bloco-sem-contorno`}>
        <td>
            <span> Nome </span>
            <p> {nome} </p>
        </td>
        <td className={`${style.quantidade}`}>
            <span> Quantidade </span>
            <p> {quantidade} </p>
        </td>
        <td>
            <span> Valor </span>
            <p> {valor} </p>
        </td>
        <td>
            <FaChevronRight size={35} className="icone" />
        </td>
    </tr>
  )
}

export default ItemListas
