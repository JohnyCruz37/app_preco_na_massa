import style from "./NavBar.module.css"
import { Link } from "react-router-dom";
import { useState } from "react";
import OffCanvasMenu from "../offcanvasMenu/OffCanvasMenu";

import { FaBookOpen, FaUserCircle, FaThList } from 'react-icons/fa';
import { FiMenu } from 'react-icons/fi';

function NavBar() {
    const [isMenuOpen, setMenuOpen] = useState(false);
    const toggleMenu = () => setMenuOpen(!isMenuOpen);

  return (
    <nav className={`navbar fixed-bottom ${style.NavBar}`}>
        <FaBookOpen size={40}  className={`icone`}/>

        <FiMenu size={40}  className={`icone`} onClick={toggleMenu}/> 
        <OffCanvasMenu
            isOpen = {isMenuOpen}
            onclose={toggleMenu}>
                <ul className={`${style.listaItensMenu}`}>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <Link to={"/"}>
                            <FaThList size={35} />
                            <h6>Lista Fichas Técnicas</h6>
                        </Link>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <Link to={"/lista-ingredientes"}>
                            <FaThList size={35} />
                            <h6>Lista Ingredientes</h6>
                        </Link>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <Link to={"/lista-insumos"}>
                            <FaThList size={35} />
                            <h6>Lista Insumos</h6>
                        </Link>
                    </li>
                    <li onClick={()=> setMenuOpen(false)} className={`${style.itemMenu}`}>
                        <Link to={"/lista-embalagens"}>
                            <FaThList size={35} />
                            <h6>Lista Embalagens</h6>
                        </Link>
                    </li>
                </ul>
        </OffCanvasMenu>

        <FaUserCircle size={40}  className={`icone`}/> 
    </nav>
  )
}

export default NavBar