import style from "./Login.module.css"
import logo from "../../assets/image/logo.png"
function Login() {
  return (
    <main className={`mainPage`}>
      <section className={`bloco-sec-sombra ${style.blocoLogin}`}>
          <article className={`${style.areaLogo}`}>
            <img src={logo} alt="logo" />
          </article>
          
          <article className={`bloco-sem-contorno ${style.areaFormLogin}`}>
            <h1>Faça seu login</h1>
            <form className={`${style.formLogin}`}>
              <label htmlFor="email">E-mail:
                <input type="email" id="email" placeholder="Digite seu e-mail" required />
              </label>
              <label htmlFor="senha">Senha:
                <input type="password" id="senha" placeholder="Digite sua senha" required />
              </label>
              <button type="submit" className={`btn-primary`}>Entrar</button>
            </form>
            <div className={`${style.links}`}>
              <span>
                <a href="#">Esqueceu a senha?</a>
              </span>
              <span>
                <a href="/cadastro">Cadastre-se</a>
              </span>
            </div>
          </article>
      </section>
    </main>
  )
}

export default Login
