import style from "./HomePage.module.css"

function HomePage() {
  return (
    <main>
      
        <header className={`${style.cabecalho}`}>
            Imagem do cliente
        </header>
        <section className={`${style.listaFichas}`}>
            lista de fichas técnicas
        </section>
    </main>
  )
}

export default HomePage
