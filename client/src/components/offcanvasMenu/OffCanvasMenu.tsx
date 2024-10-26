import style from "./offCanvasMenu.module.css"
import React, { useEffect, useRef } from "react";

interface OffcanvasMenuProps {
    isOpen: boolean;
    onclose: () => void;
    children: React.ReactNode
}


const OffCanvasMenu: React.FC<OffcanvasMenuProps>= ({isOpen, onclose, children}) =>  {
    const menuRef = useRef<HTMLDivElement>(null)

    useEffect(()=>{
        const handleClickOutSide = (event:MouseEvent)=>{
            if (menuRef.current && !menuRef.current.contains(event.target as Node)){
                onclose();
            }
        }
        if (isOpen){
            document.addEventListener('mousedown', handleClickOutSide);
        } else {
            document.removeEventListener('mousedown', handleClickOutSide)
        }

        return ()=>{
            document.removeEventListener('mousedown', handleClickOutSide)
        }

    }, [isOpen, onclose])

  return (
    <div className={`
            ${style.menu} bloco
        `}
        style={{
            bottom: isOpen ? '0' : '-100%',
        }}
        ref={menuRef}
    >
        <div className={`${style.areaBtn}`}>
            <button onClick={onclose} className={`btn-danger`}>
                Fechar
            </button>
        </div>
      {children}
    </div>
  )
}

export default OffCanvasMenu
