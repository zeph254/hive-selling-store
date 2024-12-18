import { NavLink } from "react-router-dom"


export default function  NavBar (){

    return (
            
        <nav  className="navbar navbar-expand-lg navbar-light bg-light">
        <div  className="container-fluid">
          <button  className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
            <span  className="navbar-toggler-icon"></span>
          </button>
          <img  className="hive-logo"src="data:image/png;base64,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" alt="" />
          <div  className="collapse navbar-collapse" id="navbarTogglerDemo03">
            <ul  className="navbar-nav me-auto mb-2 mb-lg-0">
              
              <li  className="nav-item">
              <NavLink to="./" className="nav-link active" aria-current="page" href="#">Home</NavLink>
              </li>
              <li  className="nav-item">
              <NavLink to="shop" className="nav-link" href="#">Shop</NavLink>
              </li>
              <li  className="nav-item">
              <NavLink to="addproduct" className="nav-link" href="#">AddProduct</NavLink>
              </li>
              <li  className="nav-item">
              <NavLink to="help" className="nav-link" href="#">Help</NavLink>
              </li>
              <li  className="nav-item">
              <NavLink to="Profile" className="nav-link" href="#">Profle</NavLink>
              </li>
            </ul>
           
          </div>
        </div>
      </nav>
        )
    }