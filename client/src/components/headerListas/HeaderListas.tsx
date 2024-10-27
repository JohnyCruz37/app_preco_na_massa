import style from "./HeaderListas.module.css"
import React from "react";

import { MdArrowBack, MdPlaylistAdd } from 'react-icons/md';

interface HeaderListaProps {
    titulo: string;
    totalLista: number;
}

const HeaderListas: React.FC<HeaderListaProps> = ({titulo, totalLista = 0}) => {
  return (
    <header className={`bloco-sombra ${style.headerLista}`}>
        <div className="areaBtnVoltar">
            <MdArrowBack size={45} className={`icone`}/>
        </div>
        <div className={`${style.areaTitulo}`}>
            <h2>{`${titulo}`}</h2>
            <span>{`Número de itens: ${totalLista}`}</span>
        </div>
        <div className="areaBtnAdd">
            <MdPlaylistAdd size={45} className={`icone`}/>
        </div>
    </header>
  )
}

export default HeaderListas
