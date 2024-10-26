import style from "./CriarConta.module.css"

function CriarConta() {
  return (
    <main className={`mainPage`}>
      <section className={`bloco-sec-sombra ${style.blocoCriarConta}`}>         
          <article className={`bloco-sem-contorno`}>
            <h1>Faça seu Cadastro agora!</h1>

            <form className={``}>
              <fieldset className="mb-3 ">
                <label htmlFor="email">Nome:
                  <input type="text" name="nome" id="nome" placeholder="Digite seu nome" required />
                </label>
                <label htmlFor="email">Celular:
                  <input type="tel" name="celular" id="celular" placeholder="Digite seu celular" required />
                </label>
              </fieldset>

              <fieldset className="mb-3">
                <label htmlFor="email">E-mail:
                  <input type="email" name="email" id="email" placeholder="Digite seu e-mail" required />
                </label>
                <label htmlFor="email">Confirmar E-mail:
                  <input type="email" name="confirm-email" id="confirm-email" placeholder="Confirme seu e-mail" required />
                </label>
              </fieldset>

              <fieldset className="mb-5">
                <label htmlFor="senha">Senha:
                  <input type="password" name="senha" id="senha" placeholder="Digite sua senha" required />
                </label>
                <label htmlFor="senha">Confirmar Senha:
                  <input type="password" name="confirm-senha" id="confirm-senha" placeholder="Confirme sua senha" required />
                </label>
              </fieldset>
              <button type="submit" className={`btn-primary w-100`}>Cadastrar</button>
            </form>

            <div className={`text-center mt-3`}>
              <span>
                <a href="#">Login</a>
              </span>
            </div>
          </article>
      </section>
    </main>
  )
}

export default CriarConta
