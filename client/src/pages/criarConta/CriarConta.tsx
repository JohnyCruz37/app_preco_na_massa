import style from "./CriarConta.module.css"
import { useCriarConta } from "./useCriarConta"
function CriarConta() {
  const { formData, errors, handleChange, handleBlur,  handleSubmit } = useCriarConta();


  return (
    <main className={`mainPage`}>
      <section className={`bloco-sec-sombra ${style.blocoCriarConta}`}>         
          <article className={`bloco-sem-contorno`}>
            <h1>Faça seu Cadastro agora!</h1>

            <form className={``} onSubmit={handleSubmit}>
              <fieldset className="mb-3 ">
                <label htmlFor="name">Nome:
                  <input 
                    required 
                    type="text" 
                    name="name" 
                    id="name" 
                    placeholder="Digite seu nome" 
                    value={formData.name}
                    onChange={handleChange}
                    onBlur={handleBlur}
                  />
                  {errors.name && <p className="error">{errors.name}</p>}
                </label>
                <label htmlFor="lastname">sobrenome:
                  <input 
                    required 
                    type="text" 
                    name="lastName" 
                    id="lastname" 
                    placeholder="Digite seu sobrenome" 
                    value={formData.lastName}
                    onChange={handleChange}
                    onBlur={handleBlur}
                  />
                  {errors.lastName && <p className="error">{errors.lastName}</p>}
                </label>
                
                <label htmlFor="phone">Celular:
                  <input 
                    required 
                    type="tel" 
                    name="phone" 
                    id="phone" 
                    placeholder="Digite seu celular"
                    value={formData.phone}
                    onChange={handleChange} 
                    onBlur={handleBlur}
                  />
                  {errors.phone && <p className="error">{errors.phone}</p>}
                </label>
              </fieldset>

              <fieldset className="mb-3">
                <label htmlFor="email">E-mail:
                  <input 
                    required 
                    type="email" 
                    name="email" 
                    id="email" 
                    placeholder="Digite seu e-mail"
                    value={formData.email}
                    onChange={handleChange} 
                    onBlur={handleBlur}
                  />
                  {errors.email && <p className="error">{errors.email}</p>}
                </label>
                <label htmlFor="confirmEmail">Confirmar E-mail:
                  <input 
                    required 
                    type="email" 
                    name="confirmEmail" 
                    id="confirmEmail" 
                    placeholder="Confirme seu e-mail" 
                    value={formData.confirmEmail}
                    onChange={handleChange}
                    onBlur={handleBlur}

                  />
                  {errors.confirmEmail && <p className="error">{errors.confirmEmail}</p>}
                </label>
              </fieldset>

              <fieldset className="mb-5">
                <label htmlFor="password">Senha:
                  <input 
                    required 
                    type="password" 
                    name="password" 
                    id="password" 
                    placeholder="Digite sua senha" 
                    value={formData.password}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    
                  />
                  {errors.password && <p className="error">{errors.password}</p>}
                </label>
                <label htmlFor="confirmPassword">Confirmar Senha:
                  <input 
                    required 
                    type="password" 
                    name="confirmPassword" 
                    id="confirmPassword" 
                    placeholder="Confirme sua senha" 
                    value={formData.confirmPassword}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    
                  />
                  {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}
                </label>
              </fieldset>
              <button 
              type="submit" className={`btn-primary w-100`}>Cadastrar</button>
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
