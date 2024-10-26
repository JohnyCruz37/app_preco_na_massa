import style from "./NavBar.module.css"
import { useState } from "react";
import OffCanvasMenu from "../offcanvasMenu/OffCanvasMenu";

import { FaBookOpen, FaUserCircle, FaThList } from 'react-icons/fa';
import { FiMenu } from 'react-icons/fi';

function NavBar() {
    const [isMenuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => setMenuOpen(!isMenuOpen);


  return (
    <nav className={`navbar fixed-bottom ${style.NavBar}`}>
        <FaBookOpen size={40}  className={`${style.icone}`}/>

        <FiMenu size={40}  className={`${style.icone}`} onClick={toggleMenu}/> 
        <OffCanvasMenu
            isOpen = {isMenuOpen}
            onclose={toggleMenu}>
                <ul className={`${style.listaItensMenu}`}>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <FaThList size={35} />
                        <h6>Lista Fichas Técnicas</h6>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <FaThList size={35} />
                        <h6>Lista Ingredientes</h6>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <FaThList size={35} />
                        <h6>Lista Insumos</h6>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <FaThList size={35} />
                        <h6>Lista Embalagens</h6>
                    </li>
                </ul>
        </OffCanvasMenu>

        <FaUserCircle size={40}  className={`${style.icone}`}/> 
    </nav>
  )
}

export default NavBar