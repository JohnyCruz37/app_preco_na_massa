import {Routes, Route, useLocation} from "react-router-dom";
import './App.css'
import NavBar from './components/navBar/NavBar'
import HomePage from './pages/homePage/HomePage'
import ListaEmbalagens from './pages/listaEmbalagens/ListaEmbalagens'
import ListaIngrediente from './pages/listaIngrediente/ListaIngrediente'
import ListaInsumos from './pages/listaInsumos/ListaInsumos'
import Login from './pages/login/Login'
import CriarConta from './pages/criarConta/CriarConta'


function App() {
  const location = useLocation();

  const isInternalPage = !['/login', '/criar-conta'].includes(location.pathname);

  return (
    <div className='App'>
      {isInternalPage && <NavBar/>}
      <Routes>
        {/* Páginas internas */}
        <Route path='/' element={<HomePage />}/>
        <Route path='/lista-embalagens' element={<ListaEmbalagens />}/>
        <Route path='/lista-ingredientes' element={<ListaIngrediente />}/>
        <Route path='/lista-insumos' element={<ListaInsumos />}/>

        {/* Páginas externar */}
        <Route path='/login' element={<Login />}/>
        <Route path='/criar-conta' element={<CriarConta />}/>
      </Routes>
    </div>
  )
}

export default App
